from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery_runtime.canonical import sha256_file, write_canonical_json
from discovery_runtime.handoff import build_d6_message, select_d6_donor
from discovery_runtime.launch_preflight import (
    authorization_failures,
    validate_run_id,
    verify_external_locks,
)
from discovery_runtime.postflight import verify_cell_postflight
from discovery_runtime.runner import CellRunner
from discovery_runtime.server import BASE_URL, ServerProcess


ROOT = Path(__file__).resolve().parents[1]


def git_output(*arguments: str) -> str:
    return subprocess.run(["git", *arguments], cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8").stdout.strip()


def validate_authorization(path: Path, *, run_id: str, contract: dict[str, Any]) -> dict[str, Any]:
    resolved = path.resolve()
    try:
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        pass
    else:
        raise RuntimeError("authorization receipt must remain outside the repository")
    value = json.loads(resolved.read_bytes())
    failures = authorization_failures(
        value,
        expected_commit=git_output("rev-parse", "HEAD"),
        run_id=run_id,
        contract=contract,
    )
    if failures:
        raise RuntimeError(f"authorization receipt failed: {failures}")
    return value


def exact_receipts(run_root: Path) -> list[dict[str, Any]]:
    receipts = []
    for path in sorted((run_root / "results").glob("*/receipt.json")):
        row = json.loads(path.read_bytes())
        receipts.append(row)
    return receipts


def run_cell(
    *,
    cell_id: str,
    cell: dict[str, Any],
    profile: dict[str, Any],
    root: Path,
    d6_message: str | None = None,
    workspace_source: Path | None = None,
    task_text: str | None = None,
    inherited_result_root: Path | None = None,
) -> dict[str, Any]:
    cell_root = root / cell_id
    fixture = ROOT / cell["fixture"]
    effective_workspace_source = workspace_source or (fixture / cell["workspace"])
    server = ServerProcess(profile=profile, log_root=cell_root / "server")
    try:
        server.start()
        runner = CellRunner(
            repo_root=ROOT,
            cell_id=cell_id,
            cell=cell,
            profile=profile,
            run_root=cell_root / "run",
            base_url=BASE_URL,
            d6_initial_message=d6_message,
            workspace_source_override=workspace_source,
            task_text_override=task_text,
            inherited_result_root=inherited_result_root,
        )
        result = runner.run_initialized()
        postflight = verify_cell_postflight(
            run_root=cell_root / "run",
            workspace_source=effective_workspace_source,
            mutable_paths=set(cell["mutable_paths"]),
        )
        write_canonical_json(cell_root / "run" / "POSTFLIGHT.json", postflight)
        if not postflight["passed"]:
            raise RuntimeError(f"postflight failed for {cell_id}: {postflight['failures']}")
        if git_output("status", "--porcelain"):
            raise RuntimeError(f"repository changed during cell {cell_id}")
        return result
    finally:
        release = server.stop()
        if not release["released"]:
            raise RuntimeError(f"runtime release failed for {cell_id}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()

    validate_run_id(args.run_id)
    if git_output("status", "--porcelain"):
        raise RuntimeError("worktree must be clean")
    contract = json.loads((ROOT / "TRANCHE_CONTRACT.json").read_bytes())
    profile = json.loads((ROOT / "MODEL_PROFILE_LOCK.json").read_bytes())
    evaluator_lock = json.loads((ROOT / "EVALUATOR_RUNTIME_LOCK.json").read_bytes())
    qualification = json.loads((ROOT / "STAGE0_QUALIFICATION.json").read_bytes())
    if not qualification.get("passed"):
        raise RuntimeError("Stage 0 is not qualified")
    authorization = validate_authorization(args.authorization, run_id=args.run_id, contract=contract)
    run_root = ROOT / "runs" / args.run_id
    run_root.mkdir(parents=True, exist_ok=False)
    write_canonical_json(run_root / "AUTHORIZATION_RECEIPT.json", authorization)
    write_canonical_json(run_root / "FREEZE_BINDING.json", {"commit": git_output("rev-parse", "HEAD"), "contract_sha256": sha256_file(ROOT / "TRANCHE_CONTRACT.json"), "profile_sha256": sha256_file(ROOT / "MODEL_PROFILE_LOCK.json"), "qualification_sha256": sha256_file(ROOT / "STAGE0_QUALIFICATION.json")})
    launch_preflight = verify_external_locks(
        model_profile=profile,
        evaluator_lock=evaluator_lock,
    )
    write_canonical_json(run_root / "LAUNCH_PREFLIGHT.json", launch_preflight)
    if not launch_preflight["passed"]:
        raise RuntimeError(
            f"launch preflight failed: {launch_preflight['failures']}"
        )

    results = []
    try:
        for cell_id in ("D1", "D2", "D3", "D4", "D5"):
            result = run_cell(cell_id=cell_id, cell=contract["cells"][cell_id], profile=profile, root=run_root)
            results.append(result)

        donor = select_d6_donor(results)
        if donor is None:
            d6 = {"schema_version": "d6-null-result-v0", "cell_id": "D6", "donor": None, "model_calls": 0, "terminal": "prospective_null_no_changed_candidate", "slot_consumed": True, "candidates": [{"cell_id": row["cell_id"], "initial": row["initial_candidate_id"], "final": row["final_candidate_id"], "changed": row["candidate_changed"]} for row in results if row["cell_id"] in {"D2", "D3", "D4", "D5"}]}
            write_canonical_json(run_root / "D6_NULL.json", d6)
            results.append(d6)
        else:
            parent = next(row for row in results if row["cell_id"] == donor)
            parent_root = run_root / donor / "run"
            donor_cell = contract["cells"][donor]
            fixture = ROOT / donor_cell["fixture"]
            task_text = (fixture / donor_cell["task"]).read_text(encoding="utf-8")
            message = build_d6_message(
                donor_cell=donor,
                task_text=task_text,
                workspace=parent_root / "workspace",
                mutable_paths=set(donor_cell["mutable_paths"]),
                visible_check_id=donor_cell["visible_check"],
                candidate_id=parent["final_candidate_id"],
                latest_check=parent.get("latest_check"),
                observation_receipts=exact_receipts(parent_root),
            )
            d6_cell = {
                **donor_cell,
                "name": f"D6 exact fresh review from {donor}",
                "call_ceiling": contract["cells"]["D6"]["call_ceiling"],
                "donor_cell": donor,
            }
            d6_result = run_cell(cell_id="D6", cell=d6_cell, profile=profile, root=run_root, d6_message=message, workspace_source=parent_root / "workspace", task_text=task_text, inherited_result_root=parent_root)
            d6_result["donor_cell"] = donor
            write_canonical_json(run_root / "D6" / "run" / "RESULT.json", d6_result)
            results.append(d6_result)

        summary = {"schema_version": "capability-terrain-tranche-result-v0", "run_id": args.run_id, "freeze_commit": git_output("rev-parse", "HEAD"), "results": results}
        write_canonical_json(run_root / "TRANCHE_RESULT.json", summary)
    except Exception as exc:
        write_canonical_json(
            run_root / "TRANCHE_ABORTED.json",
            {
                "schema_version": "capability-terrain-tranche-aborted-v0",
                "run_id": args.run_id,
                "freeze_commit": git_output("rev-parse", "HEAD"),
                "completed_cells": [row.get("cell_id") for row in results],
                "error_type": type(exc).__name__,
                "error": str(exc),
                "retries": 0,
            },
        )
        raise


if __name__ == "__main__":
    main()
