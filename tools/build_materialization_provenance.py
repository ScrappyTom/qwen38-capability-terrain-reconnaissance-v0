from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery_runtime.canonical import sha256_bytes, sha256_file, write_canonical_json
from tools.materialize_stage0 import (
    D1_APPARATUS_COMMIT,
    D1_SOURCE_COMMIT,
    D2_FIXTURE_COMMIT,
    LARGE_WORLD_REPO,
    SISTER_REPO,
    SISTER_RESULT_COMMIT,
    TASK_SOURCES,
    git_bytes,
    git_paths,
)


ROOT = Path(__file__).resolve().parents[1]


def blob_oid(repo: Path, commit: str, source_path: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), "rev-parse", f"{commit}:{source_path}"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    ).stdout.strip()


def direct_row(
    *,
    destination: str,
    repository: str,
    repo: Path,
    commit: str,
    source_path: str,
) -> dict[str, Any]:
    source = git_bytes(repo, commit, source_path)
    target = ROOT / destination
    return {
        "destination": destination,
        "repository": repository,
        "commit": commit,
        "source_path": source_path,
        "git_blob_oid": blob_oid(repo, commit, source_path),
        "derivation": "exact_git_blob_bytes",
        "source_bytes": len(source),
        "source_sha256": sha256_bytes(source),
        "materialized_bytes": target.stat().st_size,
        "materialized_sha256": sha256_file(target),
        "byte_equal": target.read_bytes() == source,
    }


def main() -> None:
    rows: list[dict[str, Any]] = []
    d1_base = "experiments/large-world-source-navigation-v0"
    for source_name, destination in {
        "task.md": "fixtures/d1_large_world_navigation/task.md",
        "candidate.md": "fixtures/d1_large_world_navigation/workspace/Q3XL_LARGE_WORLD_RUNTIME_MEMO.md",
        "FROZEN_ATLAS.json": "fixtures/d1_large_world_navigation/host/FROZEN_ATLAS.json",
        "SOURCE_LOCK.json": "fixtures/d1_large_world_navigation/host/UPSTREAM_SOURCE_LOCK.json",
        "acceptance.py": "fixtures/d1_large_world_navigation/host/acceptance.py",
        "SEMANTIC_RUBRIC.md": "fixtures/d1_large_world_navigation/host/SEMANTIC_RUBRIC.md",
    }.items():
        rows.append(direct_row(destination=destination, repository="large-world-source-navigation-2026-08-18", repo=LARGE_WORLD_REPO, commit=D1_APPARATUS_COMMIT, source_path=f"{d1_base}/{source_name}"))
    atlas = json.loads((ROOT / "fixtures/d1_large_world_navigation/host/FROZEN_ATLAS.json").read_bytes())
    for study in atlas["studies"]:
        for document in study["documents"]:
            rows.append(direct_row(destination=f"fixtures/d1_large_world_navigation/source_documents/{document['path']}", repository="large-world-source-navigation-2026-08-18", repo=LARGE_WORLD_REPO, commit=D1_SOURCE_COMMIT, source_path=document["path"]))

    d2_prefix = "fixtures/paper_revision_v1"
    for source_path in git_paths(LARGE_WORLD_REPO, D2_FIXTURE_COMMIT, d2_prefix):
        relative = source_path.removeprefix(d2_prefix + "/")
        rows.append(direct_row(destination=f"fixtures/d2_paper_revision/{relative}", repository="large-world-source-navigation-2026-08-18", repo=LARGE_WORLD_REPO, commit=D2_FIXTURE_COMMIT, source_path=source_path))

    for task_id, spec in TASK_SOURCES.items():
        for source_path in git_paths(SISTER_REPO, spec["commit"], spec["base"]):
            relative = source_path.removeprefix(spec["base"] + "/")
            rows.append(direct_row(destination=f"fixtures/{task_id}/{relative}", repository="bounded-context-harness-effects", repo=SISTER_REPO, commit=spec["commit"], source_path=source_path))
        rows.append(direct_row(destination=f"fixtures/{task_id}/host/grade-final-answer.mjs", repository="bounded-context-harness-effects", repo=SISTER_REPO, commit=spec["commit"], source_path=spec["final_grader"]))

    derived = [
        {
            "destination": "qualification/gold/d2_paper_revision/paper.md",
            "repository": "large-world-source-navigation-2026-08-18",
            "commit": D2_FIXTURE_COMMIT,
            "source_path": "tests/test_paper_revision_fixture_v1.py",
            "derivation": "Python AST literal KNOWN_PAPER encoded as UTF-8",
        },
        {
            "destination": "qualification/gold/d3_coverage_coalescing/src/coalesce-coverage.mjs",
            "repository": "bounded-context-harness-effects",
            "commit": SISTER_RESULT_COMMIT,
            "source_path": "runs/102_independent_action_batching_qwen36-27b_seeds3465-3467_pilot01/coverage-coalescing__v5__s3465/environment.json",
            "derivation": "workspace_files[path=src/coalesce-coverage.mjs].content_utf8 encoded as UTF-8",
        },
        {
            "destination": "qualification/gold/d5_deployment_wave_planning/src/deployment-waves.mjs",
            "repository": "bounded-context-harness-effects",
            "commit": SISTER_RESULT_COMMIT,
            "source_path": "runs/107_response_headroom_new_tasks_qwen36-27b_seeds3474-3476_pilot01/deployment-wave-planning__v5-generous-8192__s3476/environment.json",
            "derivation": "workspace_files[path=src/deployment-waves.mjs].content_utf8 encoded as UTF-8",
        },
    ]
    repo_map = {"large-world-source-navigation-2026-08-18": LARGE_WORLD_REPO, "bounded-context-harness-effects": SISTER_REPO}
    for row in derived:
        repo = repo_map[row["repository"]]
        source = git_bytes(repo, row["commit"], row["source_path"])
        target = ROOT / row["destination"]
        row.update({"git_blob_oid": blob_oid(repo, row["commit"], row["source_path"]), "source_bytes": len(source), "source_sha256": sha256_bytes(source), "materialized_bytes": target.stat().st_size, "materialized_sha256": sha256_file(target), "byte_equal": None})
        rows.append(row)
    d4 = ROOT / "qualification/gold/d4_device_event_folding/src/fold-device-events.mjs"
    rows.append({"destination": d4.relative_to(ROOT).as_posix(), "repository": None, "commit": None, "source_path": None, "git_blob_oid": None, "derivation": "new host-authored Stage-0 reference; qualified against the inherited 8-case grader plus the frozen plain-object supplement", "source_bytes": None, "source_sha256": None, "materialized_bytes": d4.stat().st_size, "materialized_sha256": sha256_file(d4), "byte_equal": None})
    d4_evaluator = ROOT / "qualification/evaluators/d4_plain_object_grade.mjs"
    rows.append({"destination": d4_evaluator.relative_to(ROOT).as_posix(), "repository": None, "commit": None, "source_path": None, "git_blob_oid": None, "derivation": "new host-authored Stage-0 evaluator supplement for the task-declared plain-object distinction", "source_bytes": None, "source_sha256": None, "materialized_bytes": d4_evaluator.stat().st_size, "materialized_sha256": sha256_file(d4_evaluator), "byte_equal": None})

    payload = {"schema_version": "capability-terrain-materialization-provenance-v0", "rows": sorted(rows, key=lambda row: row["destination"])}
    payload["row_count"] = len(payload["rows"])
    payload["all_direct_rows_byte_equal"] = all(row["byte_equal"] is True for row in payload["rows"] if row["derivation"] == "exact_git_blob_bytes")
    write_canonical_json(ROOT / "MATERIALIZATION_PROVENANCE.json", payload)


if __name__ == "__main__":
    main()
