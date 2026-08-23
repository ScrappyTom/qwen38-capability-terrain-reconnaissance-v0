from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery_runtime.canonical import canonical_json_bytes, sha256_file
from discovery_runtime.manifest import recursive_manifest


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUN_ID = "2026-08-23-capability-terrain-v0"
ALLOWED = {"met", "partial", "not_met", "ambiguous"}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_bytes())
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def validate(record_path: Path) -> dict[str, Any]:
    failures: list[str] = []
    record = load(record_path)
    rubric_path = ROOT / record["rubric"]["path"]
    rubric = load(rubric_path)
    task_path = ROOT / "fixtures" / "d2_paper_revision" / "task.md"
    d2_workspace = ROOT / "runs" / record["run_id"] / "D2" / "run" / "workspace"
    d6_workspace = ROOT / "runs" / record["run_id"] / "D6" / "run" / "workspace"

    if record.get("freeze_commit") != "f3092c73065353d5fbdb4c3646632b6586c7e50b":
        failures.append("freeze_commit")
    if record.get("applies_to_cells") != ["D2", "D6"]:
        failures.append("applies_to_cells")
    if sha256_file(task_path) != record.get("task_sha256") or rubric.get("task_sha256") != record.get("task_sha256"):
        failures.append("task_binding")
    if sha256_file(rubric_path) != record.get("rubric", {}).get("sha256"):
        failures.append("rubric_binding")

    d2_manifest = recursive_manifest(d2_workspace)
    d6_manifest = recursive_manifest(d6_workspace)
    candidate = record.get("candidate", {})
    if d2_manifest != d6_manifest or d2_manifest.get("manifest_sha256") != candidate.get("manifest_sha256"):
        failures.append("candidate_manifest")
    for label, workspace in (("d2", d2_workspace), ("d6", d6_workspace)):
        paper = workspace / "paper.md"
        if sha256_file(paper) != candidate.get("paper_sha256") or paper.stat().st_size != candidate.get("paper_bytes"):
            failures.append(f"{label}_paper_binding")

    expected_evidence = {
        "editorial_memo.md": sha256_file(d2_workspace / "editorial_memo.md"),
        "evidence_update.md": sha256_file(d2_workspace / "evidence_update.md"),
    }
    if record.get("evidence_sha256") != expected_evidence:
        failures.append("evidence_binding")

    visible = record.get("machine_evidence", {}).get("visible_check", {})
    visible_raw_path = ROOT / visible.get("raw_path", "missing")
    visible_result_path = ROOT / "runs" / record["run_id"] / "D2" / "run" / "results" / "RESULT-006" / "result.json"
    visible_result = load(visible_result_path)
    if (
        not visible_raw_path.is_file()
        or sha256_file(visible_raw_path) != visible.get("raw_sha256")
        or sha256_file(visible_result_path) != visible.get("model_visible_result_sha256")
        or visible_result.get("passed") is not True
        or visible_result.get("currency") != "current"
    ):
        failures.append("visible_machine_evidence")

    hidden = record.get("machine_evidence", {}).get("hidden_grade", {})
    hidden_path = ROOT / hidden.get("raw_path", "missing")
    hidden_raw = load(hidden_path) if hidden_path.is_file() else {}
    try:
        hidden_payload = json.loads(hidden_raw.get("stdout", "{}"))
    except json.JSONDecodeError:
        hidden_payload = {}
    hidden_cases = [row.get("case") for row in hidden_payload.get("failures", [])]
    if (
        not hidden_path.is_file()
        or sha256_file(hidden_path) != hidden.get("raw_sha256")
        or hidden_payload.get("passed") is not False
        or hidden_payload.get("case_count") != hidden.get("case_count")
        or hidden_cases != hidden.get("failed_cases")
    ):
        failures.append("hidden_machine_evidence")

    criteria = [row["id"] for row in rubric.get("criteria", [])]
    dispositions = record.get("criterion_dispositions", [])
    if [row.get("criterion_id") for row in dispositions] != criteria:
        failures.append("criterion_identity_order")
    status_counts = Counter(row.get("disposition") for row in dispositions)
    if not set(status_counts).issubset(ALLOWED):
        failures.append("criterion_status")
    expected_score = {key: status_counts.get(key, 0) for key in ("met", "partial", "not_met", "ambiguous")}
    expected_score["total"] = len(dispositions)
    if record.get("score") != expected_score:
        failures.append("score")
    derived_readiness = "ready" if len(dispositions) == 13 and status_counts == Counter({"met": 13}) and not record.get("blocking_requirements") else "not_ready"
    if record.get("closure_readiness") != derived_readiness:
        failures.append("closure_readiness")
    if record.get("closure_readiness") == "not_ready" and not record.get("blocking_requirements"):
        failures.append("blocking_requirements")

    return {
        "schema_version": "d2-measured-adjudication-validation-v0",
        "record_path": record_path.relative_to(ROOT).as_posix(),
        "record_sha256": sha256_file(record_path),
        "candidate_id": d2_manifest.get("manifest_sha256"),
        "derived_score": expected_score,
        "derived_closure_readiness": derived_readiness,
        "passed": not failures,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "record",
        nargs="?",
        type=Path,
        default=ROOT / "runs" / DEFAULT_RUN_ID / "D2_SEMANTIC_ADJUDICATION.json",
    )
    args = parser.parse_args()
    result = validate(args.record.resolve())
    print(canonical_json_bytes(result).decode("utf-8"), end="")
    return 0 if result["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
