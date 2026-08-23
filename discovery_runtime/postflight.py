from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

from .canonical import sha256_bytes
from .manifest import recursive_manifest
from .worlds import FileWorld


def verify_cell_postflight(
    *,
    run_root: Path,
    workspace_source: Path,
    mutable_paths: set[str],
) -> dict[str, Any]:
    """Replay admitted mutations and verify exact result/attempt custody."""

    failures: list[str] = []
    summary = json.loads((run_root / "RESULT.json").read_bytes())
    calls = summary.get("calls", [])
    result_dirs = sorted((run_root / "results").glob("RESULT-*"))
    if len(result_dirs) != len(calls):
        failures.append("result_count")

    for index, row in enumerate(calls, start=1):
        call_dir = run_root / "calls" / f"call-{index:03d}"
        attempts = sorted(call_dir.glob("provider-attempt-*"))
        if [path.name for path in attempts] != ["provider-attempt-1"]:
            failures.append(f"attempt_count:{index}")
        result_id = row.get("result_id")
        result_path = run_root / "results" / str(result_id) / "result.json"
        receipt_path = run_root / "results" / str(result_id) / "receipt.json"
        if not result_path.is_file() or not receipt_path.is_file():
            failures.append(f"missing_result:{index}")
            continue
        body = result_path.read_bytes()
        value = json.loads(body)
        receipt = json.loads(receipt_path.read_bytes())
        if value.get("result_id") != result_id or receipt.get("result_id") != result_id:
            failures.append(f"result_identity:{index}")
        if receipt.get("exact_body_bytes") != len(body) or receipt.get("exact_body_sha256") != sha256_bytes(body):
            failures.append(f"result_receipt:{index}")

    with tempfile.TemporaryDirectory(prefix="capability-terrain-postflight-") as temporary:
        replay = FileWorld(
            source=workspace_source,
            runtime_root=Path(temporary) / "workspace",
            mutable_paths=mutable_paths,
        )
        if replay.candidate_id != summary.get("initial_candidate_id"):
            failures.append("initial_candidate")
        for index, row in enumerate(calls, start=1):
            action = row.get("action")
            if not isinstance(action, dict):
                continue
            result_id = row.get("result_id")
            result_path = run_root / "results" / str(result_id) / "result.json"
            if not result_path.is_file():
                continue
            result = json.loads(result_path.read_bytes())
            if result.get("accepted") is not True:
                continue
            try:
                if action.get("action") == "patch":
                    replayed = replay.patch(
                        action["path"], action["old"], action["new"], action["expected_file_sha256"]
                    )
                    if any(replayed.get(key) != result.get(key) for key in ("candidate_before", "candidate_after", "file_sha256_before", "file_sha256_after")):
                        failures.append(f"mutation_replay:{index}")
                elif action.get("action") == "replace_file":
                    replayed = replay.replace_file(
                        action["path"], action["content"], action["expected_file_sha256"]
                    )
                    if any(replayed.get(key) != result.get(key) for key in ("candidate_before", "candidate_after", "file_sha256_before", "file_sha256_after")):
                        failures.append(f"mutation_replay:{index}")
                elif action.get("action") == "run_check":
                    if result.get("evaluated_candidate_id") != replay.candidate_id:
                        failures.append(f"check_candidate_binding:{index}")
            except Exception as exc:
                failures.append(f"mutation_replay_exception:{index}:{type(exc).__name__}")
        if replay.candidate_id != summary.get("final_candidate_id"):
            failures.append("final_candidate")
        if recursive_manifest(run_root / "workspace")["manifest_sha256"] != summary.get("final_candidate_id"):
            failures.append("final_workspace_manifest")

    return {
        "schema_version": "capability-terrain-cell-postflight-v0",
        "passed": not failures,
        "failures": failures,
        "calls_checked": len(calls),
        "results_checked": len(result_dirs),
        "one_provider_attempt_per_completed_call": not any(item.startswith("attempt_count:") for item in failures),
        "mutation_replay": "exact for admitted patch and replace_file actions; nonmutating observations remain under raw custody",
        "initial_candidate_id": summary.get("initial_candidate_id"),
        "final_candidate_id": summary.get("final_candidate_id"),
    }
