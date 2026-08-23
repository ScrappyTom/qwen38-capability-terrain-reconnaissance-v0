from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery_runtime.canonical import canonical_json_bytes, sha256_bytes, sha256_file, write_canonical_json
from discovery_runtime.manifest import recursive_manifest


ROOT = Path(__file__).resolve().parents[1]
DERIVED_RUN_FILES = {
    "MECHANICAL_AUDIT.json",
    "RAW_RUN_MANIFEST.json",
    "RESULTS.md",
    "DIRECT_TRANSCRIPT_AUDIT.md",
    "D2_SEMANTIC_ADJUDICATION.json",
}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_bytes())
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def raw_manifest(run_root: Path) -> dict[str, Any]:
    files = []
    for path in sorted(item for item in run_root.rglob("*") if item.is_file()):
        relative = path.relative_to(run_root).as_posix()
        if relative in DERIVED_RUN_FILES:
            continue
        files.append({"path": relative, "bytes": path.stat().st_size, "sha256": sha256_file(path)})
    identity = {"files": files, "schema_version": "capability-terrain-raw-run-manifest-v0"}
    return {
        **identity,
        "file_count": len(files),
        "total_bytes": sum(row["bytes"] for row in files),
        "manifest_sha256": sha256_bytes(canonical_json_bytes(identity)),
    }


def audit(run_root: Path) -> dict[str, Any]:
    failures: list[str] = []
    contract = load(ROOT / "TRANCHE_CONTRACT.json")
    freeze = load(run_root / "FREEZE_BINDING.json")
    authorization = load(run_root / "AUTHORIZATION_RECEIPT.json")
    preflight = load(run_root / "LAUNCH_PREFLIGHT.json")
    tranche = load(run_root / "TRANCHE_RESULT.json")

    if (run_root / "TRANCHE_ABORTED.json").exists():
        failures.append("tranche_aborted_present")
    expected_freeze = {
        "commit": authorization.get("authorized_freeze_commit"),
        "contract_sha256": sha256_file(ROOT / "TRANCHE_CONTRACT.json"),
        "profile_sha256": sha256_file(ROOT / "MODEL_PROFILE_LOCK.json"),
        "qualification_sha256": sha256_file(ROOT / "STAGE0_QUALIFICATION.json"),
    }
    if freeze != expected_freeze:
        failures.append("freeze_binding")
    if authorization.get("authorized_run_id") != run_root.name:
        failures.append("authorization_run_id")
    if authorization.get("maximum_model_calls") != contract["max_total_actor_calls"]:
        failures.append("authorization_calls")
    if authorization.get("one_attempt_per_call") is not True or authorization.get("retries") != 0:
        failures.append("authorization_attempt_policy")
    if preflight.get("passed") is not True or preflight.get("failures") != []:
        failures.append("launch_preflight")
    if tranche.get("freeze_commit") != freeze["commit"] or tranche.get("run_id") != run_root.name:
        failures.append("tranche_binding")

    results = tranche.get("results", [])
    if [row.get("cell_id") for row in results] != ["D1", "D2", "D3", "D4", "D5", "D6"]:
        failures.append("cell_order")

    total_prompt = 0
    total_completion = 0
    total_cached = 0
    total_calls = 0
    total_attempts = 0
    accepted = 0
    rejected = 0
    action_counts: Counter[str] = Counter()
    pressure_events: list[dict[str, Any]] = []
    cell_rows: list[dict[str, Any]] = []

    for result in results:
        cell_id = result["cell_id"]
        cell_root = run_root / cell_id
        measured = load(cell_root / "run" / "RESULT.json")
        if measured != result:
            failures.append(f"{cell_id}:tranche_result_mismatch")
        calls = measured.get("calls", [])
        call_dirs = sorted((cell_root / "run" / "calls").glob("call-*"))
        if len(call_dirs) != len(calls):
            failures.append(f"{cell_id}:call_directory_count")
        postflight = load(cell_root / "run" / "POSTFLIGHT.json")
        release = load(cell_root / "server" / "RUNTIME_RELEASE.json")
        if postflight.get("passed") is not True or postflight.get("failures") != []:
            failures.append(f"{cell_id}:postflight")
        if postflight.get("calls_checked") != len(calls):
            failures.append(f"{cell_id}:postflight_call_count")
        if release.get("released") is not True or release.get("errors") != []:
            failures.append(f"{cell_id}:runtime_release")
        if release.get("port_open_after") is not False or release.get("pid_on_gpu_after") is not False:
            failures.append(f"{cell_id}:runtime_residue")

        cell_prompt = 0
        cell_completion = 0
        cell_cached = 0
        cell_actions: list[str] = []
        for call, call_dir in zip(calls, call_dirs, strict=True):
            call_number = call["call"]
            if call_dir.name != f"call-{call_number:03d}":
                failures.append(f"{cell_id}:call_order:{call_number}")
            capacity = load(call_dir / "capacity.json")
            if capacity.get("fit") is not True or capacity.get("after_tokens") != call.get("prompt_tokens"):
                failures.append(f"{cell_id}:capacity:{call_number}")
            if capacity.get("after_tokens", contract["prompt_ceiling_tokens"] + 1) > contract["prompt_ceiling_tokens"]:
                failures.append(f"{cell_id}:prompt_ceiling:{call_number}")
            if capacity.get("substitutions"):
                pressure_events.append({"cell_id": cell_id, **capacity})

            attempt_dirs = sorted(call_dir.glob("provider-attempt-*"))
            if [path.name for path in attempt_dirs] != ["provider-attempt-1"]:
                failures.append(f"{cell_id}:attempt_count:{call_number}")
            total_attempts += len(attempt_dirs)
            transport = call.get("transport", {})
            if transport.get("response_status") != 200 or transport.get("error") is not None:
                failures.append(f"{cell_id}:provider_transport:{call_number}")

            usage = call.get("usage", {})
            prompt = usage.get("prompt_tokens", 0)
            completion = usage.get("completion_tokens", 0)
            cached = usage.get("prompt_tokens_details", {}).get("cached_tokens", 0)
            cell_prompt += prompt
            cell_completion += completion
            cell_cached += cached
            if prompt != call.get("prompt_tokens"):
                failures.append(f"{cell_id}:prompt_accounting:{call_number}")

            result_id = call["result_id"]
            exact_path = cell_root / "run" / "results" / result_id / "result.json"
            receipt = load(cell_root / "run" / "results" / result_id / "receipt.json")
            if receipt.get("exact_body_bytes") != exact_path.stat().st_size or receipt.get("exact_body_sha256") != sha256_file(exact_path):
                failures.append(f"{cell_id}:result_receipt:{result_id}")
            if call.get("accepted") is True:
                accepted += 1
            else:
                rejected += 1
            action_name = call.get("action", {}).get("action") if isinstance(call.get("action"), dict) else "INVALID"
            cell_actions.append(action_name)
            action_counts[action_name] += 1

        final_manifest = recursive_manifest(cell_root / "run" / "workspace")
        if final_manifest != measured.get("final_manifest"):
            failures.append(f"{cell_id}:final_manifest")
        total_calls += len(calls)
        total_prompt += cell_prompt
        total_completion += cell_completion
        total_cached += cell_cached
        cell_rows.append(
            {
                "cell_id": cell_id,
                "calls": len(calls),
                "terminal": measured.get("terminal"),
                "candidate_changed": measured.get("candidate_changed"),
                "submitted": measured.get("submitted"),
                "accepted_actions": sum(call.get("accepted") is True for call in calls),
                "rejected_actions": sum(call.get("accepted") is not True for call in calls),
                "actions": cell_actions,
                "prompt_tokens": cell_prompt,
                "completion_tokens": cell_completion,
                "cached_prompt_tokens": cell_cached,
                "external_evaluation_exit_code": measured.get("external_evaluation_exit_code"),
                "initial_candidate_id": measured.get("initial_candidate_id"),
                "final_candidate_id": measured.get("final_candidate_id"),
            }
        )

    if total_calls != total_attempts:
        failures.append("one_attempt_per_call")
    if total_calls > contract["max_total_actor_calls"]:
        failures.append("total_call_ceiling")
    if total_prompt + total_completion > contract["max_total_serialized_tokens"]:
        failures.append("serialized_token_ceiling")
    if pressure_events:
        # Pressure is legal, but it must be reported rather than silently folded.
        pass

    changed_order = [row["cell_id"] for row in cell_rows if row["cell_id"] in {"D2", "D3", "D4", "D5"} and row["candidate_changed"]]
    d6 = next((row for row in results if row.get("cell_id") == "D6"), None)
    if changed_order and (d6 is None or d6.get("donor_cell") != changed_order[0]):
        failures.append("d6_donor_selection")

    return {
        "schema_version": "capability-terrain-mechanical-audit-v0",
        "run_id": run_root.name,
        "freeze_commit": freeze["commit"],
        "passed": not failures,
        "failures": failures,
        "cells": cell_rows,
        "totals": {
            "actor_calls": total_calls,
            "provider_attempts": total_attempts,
            "retries": 0,
            "prompt_tokens": total_prompt,
            "completion_tokens": total_completion,
            "serialized_tokens": total_prompt + total_completion,
            "cached_prompt_tokens": total_cached,
            "cache_reuse_rate": total_cached / total_prompt if total_prompt else 0,
            "accepted_actions": accepted,
            "rejected_actions": rejected,
            "action_counts": dict(sorted(action_counts.items())),
            "pressure_events": len(pressure_events),
            "pressure_substitutions": sum(len(row.get("substitutions", [])) for row in pressure_events),
        },
        "pressure_event_details": pressure_events,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("run_id")
    args = parser.parse_args()
    run_root = ROOT / "runs" / args.run_id
    if not run_root.is_dir():
        raise SystemExit(f"missing run: {run_root}")
    manifest = raw_manifest(run_root)
    audit_result = audit(run_root)
    write_canonical_json(run_root / "RAW_RUN_MANIFEST.json", manifest)
    write_canonical_json(run_root / "MECHANICAL_AUDIT.json", audit_result)
    print(canonical_json_bytes(audit_result).decode("utf-8"), end="")
    return 0 if audit_result["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
