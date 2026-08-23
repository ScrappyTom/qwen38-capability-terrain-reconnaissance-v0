from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RECORD = (
    ROOT
    / "qualification"
    / "adjudications"
    / "D2_GOLD_PAPER_REVISION_081DF9DA88BF0235.json"
)
RUBRIC_PATH = ROOT / "qualification" / "D2_REQUIREMENT_RUBRIC.json"
PROTOCOL_PATH = ROOT / "ADJUDICATION_PROTOCOL.json"

ARTIFACT_PATHS = {
    "adjudication_protocol": PROTOCOL_PATH,
    "candidate_paper": ROOT / "qualification" / "gold" / "d2_paper_revision" / "paper.md",
    "editorial_memo": ROOT / "fixtures" / "d2_paper_revision" / "candidate" / "editorial_memo.md",
    "evidence_update": ROOT / "fixtures" / "d2_paper_revision" / "candidate" / "evidence_update.md",
    "gold_manifest": ROOT / "GOLD_MANIFEST.json",
    "rubric": RUBRIC_PATH,
    "task": ROOT / "fixtures" / "d2_paper_revision" / "task.md",
}

CHECK_SCRIPTS = {
    "hidden_grade": ROOT / "fixtures" / "d2_paper_revision" / "control" / "hidden_grade.py",
    "visible_check": ROOT / "fixtures" / "d2_paper_revision" / "control" / "visible_check.py",
}

ALLOWED_DISPOSITIONS = {"met", "partial", "not_met", "ambiguous"}


def canonical_json_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        + b"\n"
    )


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected one JSON object in {path}")
    return value


def file_binding(path: Path) -> dict[str, Any]:
    return {
        "bytes": path.stat().st_size,
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha256_path(path),
    }


def expected_candidate_manifest() -> dict[str, Any]:
    sources = {
        "editorial_memo.md": ARTIFACT_PATHS["editorial_memo"],
        "evidence_update.md": ARTIFACT_PATHS["evidence_update"],
        "paper.md": ARTIFACT_PATHS["candidate_paper"],
    }
    files = [
        {
            "bytes": path.stat().st_size,
            "path": relative,
            "sha256": sha256_path(path),
        }
        for relative, path in sorted(sources.items())
    ]
    identity_payload: dict[str, Any] = {"files": files, "schema_version": 1}
    manifest_sha256 = sha256_bytes(canonical_json_bytes(identity_payload))
    return {
        **identity_payload,
        "file_count": len(files),
        "manifest_sha256": manifest_sha256,
        "total_bytes": sum(row["bytes"] for row in files),
    }


def run_machine_check(script: Path) -> tuple[dict[str, Any], str, int]:
    with tempfile.TemporaryDirectory(prefix="d2-adjudication-validation-") as temporary:
        candidate_dir = Path(temporary)
        (candidate_dir / "paper.md").write_bytes(
            ARTIFACT_PATHS["candidate_paper"].read_bytes()
        )
        (candidate_dir / "evidence_update.md").write_bytes(
            ARTIFACT_PATHS["evidence_update"].read_bytes()
        )
        (candidate_dir / "editorial_memo.md").write_bytes(
            ARTIFACT_PATHS["editorial_memo"].read_bytes()
        )
        completed = subprocess.run(
            [sys.executable, str(script), str(candidate_dir)],
            cwd=script.parent,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        result = {"parse_error": str(exc), "stdout": completed.stdout}
    return result, sha256_bytes(canonical_json_bytes(result)), completed.returncode


def validate(record_path: Path = DEFAULT_RECORD) -> dict[str, Any]:
    failures: list[str] = []
    try:
        raw_record = record_path.read_bytes()
        record = load_object(record_path)
        rubric = load_object(RUBRIC_PATH)
        protocol = load_object(PROTOCOL_PATH)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        return {
            "schema_version": "d2-adjudication-validation-v1",
            "passed": False,
            "failures": [f"input_error: {type(exc).__name__}: {exc}"],
        }

    if raw_record != canonical_json_bytes(record):
        failures.append("record: bytes are not canonical JSON")

    required_keys = {
        "adjudication_id",
        "bindings",
        "blocking_unsupported_claims",
        "candidate_id",
        "candidate_manifest",
        "closure_readiness",
        "criterion_dispositions",
        "evaluator_id",
        "evidence_sha256",
        "machine_evidence",
        "rationale",
        "rubric_sha256",
        "schema_version",
        "task_sha256",
    }
    if set(record) != required_keys:
        failures.append("record: top-level key set mismatch")
    if record.get("schema_version") != "d2-paper-revision-adjudication-v1":
        failures.append("record.schema_version: mismatch")
    if not isinstance(record.get("adjudication_id"), str) or not record.get(
        "adjudication_id"
    ):
        failures.append("record.adjudication_id: required non-empty string")

    expected_manifest = expected_candidate_manifest()
    if record.get("candidate_manifest") != expected_manifest:
        failures.append("candidate_manifest: does not match exact candidate workspace")
    if record.get("candidate_id") != expected_manifest["manifest_sha256"]:
        failures.append("candidate_id: does not match candidate manifest")

    expected_bindings = {
        name: file_binding(path) for name, path in ARTIFACT_PATHS.items()
    }
    gold_manifest = load_object(ARTIFACT_PATHS["gold_manifest"])
    expected_bindings["gold_manifest"]["declared_manifest_sha256"] = gold_manifest.get(
        "manifest_sha256"
    )
    if record.get("bindings") != expected_bindings:
        failures.append("bindings: exact path/length/SHA-256 set mismatch")

    task_sha256 = sha256_path(ARTIFACT_PATHS["task"])
    rubric_sha256 = sha256_path(RUBRIC_PATH)
    if record.get("task_sha256") != task_sha256:
        failures.append("task_sha256: mismatch")
    if rubric.get("task_sha256") != task_sha256:
        failures.append("rubric.task_sha256: does not bind exact task")
    if record.get("rubric_sha256") != rubric_sha256:
        failures.append("rubric_sha256: mismatch")
    expected_evidence_hashes = {
        "editorial_memo.md": sha256_path(ARTIFACT_PATHS["editorial_memo"]),
        "evidence_update.md": sha256_path(ARTIFACT_PATHS["evidence_update"]),
    }
    if record.get("evidence_sha256") != expected_evidence_hashes:
        failures.append("evidence_sha256: mismatch")

    expected_evaluator_id = protocol["applies_to"]["D2"]["evaluator_id"]
    if record.get("evaluator_id") != expected_evaluator_id:
        failures.append("evaluator_id: mismatch")

    machine_evidence = record.get("machine_evidence")
    if not isinstance(machine_evidence, dict) or set(machine_evidence) != set(
        CHECK_SCRIPTS
    ):
        failures.append("machine_evidence: expected visible_check and hidden_grade")
        machine_evidence = {}
    for name, script in CHECK_SCRIPTS.items():
        result, result_sha256, returncode = run_machine_check(script)
        expected = {
            "result": result,
            "result_sha256": result_sha256,
            "script": file_binding(script),
        }
        if machine_evidence.get(name) != expected:
            failures.append(f"machine_evidence.{name}: fresh result or binding mismatch")
        if returncode != 0 or result.get("passed") is not True:
            failures.append(f"machine_evidence.{name}: fresh check did not pass")

    expected_criteria = [item["id"] for item in rubric["criteria"]]
    dispositions = record.get("criterion_dispositions")
    statuses: dict[str, str] = {}
    if not isinstance(dispositions, list) or len(dispositions) != 13:
        failures.append("criterion_dispositions: expected exactly 13 entries")
        dispositions = []
    observed_order: list[str] = []
    for index, item in enumerate(dispositions):
        field = f"criterion_dispositions[{index}]"
        if not isinstance(item, dict) or set(item) != {
            "criterion_id",
            "disposition",
            "evidence",
        }:
            failures.append(f"{field}: key set mismatch")
            continue
        criterion_id = item.get("criterion_id")
        disposition = item.get("disposition")
        evidence = item.get("evidence")
        observed_order.append(criterion_id)
        if criterion_id in statuses:
            failures.append(f"{field}.criterion_id: duplicate")
        elif criterion_id not in expected_criteria:
            failures.append(f"{field}.criterion_id: unknown")
        else:
            statuses[criterion_id] = disposition
        if disposition not in ALLOWED_DISPOSITIONS:
            failures.append(f"{field}.disposition: invalid")
        if not isinstance(evidence, list) or not evidence or any(
            not isinstance(entry, str) or not entry.strip() for entry in evidence
        ):
            failures.append(f"{field}.evidence: required non-empty string list")
    if observed_order != expected_criteria:
        failures.append("criterion_dispositions: identity/order differs from frozen rubric")

    blockers = record.get("blocking_unsupported_claims")
    if not isinstance(blockers, list) or any(
        not isinstance(item, str) or not item.strip() for item in blockers
    ):
        failures.append("blocking_unsupported_claims: invalid list")
        blockers = ["invalid blocker representation"]
    derived_readiness = (
        "ready"
        if len(statuses) == 13
        and all(value == "met" for value in statuses.values())
        and not blockers
        else "not_ready"
    )
    if record.get("closure_readiness") != derived_readiness:
        failures.append(
            f"closure_readiness: expected {derived_readiness} under frozen rule"
        )
    if not isinstance(record.get("rationale"), str) or not record.get("rationale"):
        failures.append("rationale: required non-empty string")

    return {
        "adjudication_id": record.get("adjudication_id"),
        "candidate_id": expected_manifest["manifest_sha256"],
        "criterion_statuses": {
            criterion_id: statuses.get(criterion_id, "missing")
            for criterion_id in expected_criteria
        },
        "derived_closure_readiness": derived_readiness,
        "failures": failures,
        "passed": not failures,
        "record_sha256": sha256_bytes(raw_record),
        "recorded_closure_readiness": record.get("closure_readiness"),
        "schema_version": "d2-adjudication-validation-v1",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", nargs="?", type=Path, default=DEFAULT_RECORD)
    args = parser.parse_args()
    result = validate(args.record.resolve())
    print(canonical_json_bytes(result).decode("utf-8"), end="")
    return 0 if result["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
