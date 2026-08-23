from __future__ import annotations

import ast
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from discovery_runtime.canonical import sha256_bytes, write_canonical_json
from discovery_runtime.manifest import recursive_manifest


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"
GOLD = ROOT / "qualification" / "gold"

LARGE_WORLD_REPO = Path(r"E:\large-world-source-navigation-2026-08-18")
SISTER_REPO = Path(r"E:\bounded-context-harness-effects")

D1_APPARATUS_COMMIT = "22d382063ffa71105b626e35b09c6051abe94f9e"
D1_SOURCE_COMMIT = "355df1826dc2f7cafd9db6122261cab4565ee356"
D2_FIXTURE_COMMIT = "73daddb69725a54e6bfe600fbc6577d2d3318b1c"
D2_REVIEW_COMMIT = "5229172cbd34143bc6ac84da2c4dbf0412960ff2"
SISTER_RESULT_COMMIT = "5fc4f050f3de176a023019df24cec4a5d5781e71"

TASK_SOURCES = {
    "d3_coverage_coalescing": {
        "commit": "96fc17270e1e780ac20f6253b1de8f645d20a2c8",
        "base": "studies/102_independent_action_batching/tasks/coverage-coalescing",
        "final_grader": "studies/102_independent_action_batching/grade-final-answer.mjs",
    },
    "d4_device_event_folding": {
        "commit": "c2b7678b3a5a30125175707ba0117820eff1f539",
        "base": "studies/103_mechanical_initial_formation/tasks/device-event-folding",
        "final_grader": "studies/103_mechanical_initial_formation/grade-final-answer.mjs",
    },
    "d5_deployment_wave_planning": {
        "commit": "ddb360625466dd7b59a9c3c3108c690b4b8323e5",
        "base": "studies/107_response_headroom_new_tasks/tasks/deployment-wave-planning",
        "final_grader": "studies/107_response_headroom_new_tasks/grade-final-answer.mjs",
    },
}


def git_bytes(repo: Path, commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(repo), "show", f"{commit}:{path}"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def git_paths(repo: Path, commit: str, prefix: str) -> list[str]:
    completed = subprocess.run(
        ["git", "-C", str(repo), "ls-tree", "-r", "--name-only", commit, prefix],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    return [line for line in completed.stdout.splitlines() if line]


def write_exact(path: Path, data: bytes) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": len(data),
        "sha256": sha256_bytes(data),
    }


def require_clean_destination(path: Path) -> None:
    if path.exists() and any(path.iterdir()):
        raise RuntimeError(f"refusing to overwrite non-empty generated directory: {path}")
    path.mkdir(parents=True, exist_ok=True)


def extract_string_constant(source: bytes, name: str) -> str:
    module = ast.parse(source.decode("utf-8"))
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    value = ast.literal_eval(node.value)
                    if not isinstance(value, str):
                        raise TypeError(f"{name} is not a string")
                    return value
    raise KeyError(name)


def file_from_environment(environment: bytes, relative_path: str) -> bytes:
    payload = json.loads(environment)
    candidates = payload.get("final_workspace_files", payload.get("workspace_files"))
    if isinstance(candidates, dict):
        value = candidates.get(relative_path)
        if isinstance(value, str):
            return value.encode("utf-8")
        if isinstance(value, dict) and isinstance(value.get("content"), str):
            return value["content"].encode("utf-8")
    if isinstance(candidates, list):
        for row in candidates:
            if row.get("path") != relative_path:
                continue
            content = row.get("content", row.get("content_utf8"))
            if isinstance(content, str):
                return content.encode("utf-8")
    raise KeyError(f"{relative_path} not found in final_workspace_files")


def materialize_d1(lock_rows: list[dict[str, Any]]) -> None:
    target = FIXTURES / "d1_large_world_navigation"
    require_clean_destination(target)
    base = "experiments/large-world-source-navigation-v0"
    direct = {
        "task.md": "task.md",
        "candidate.md": "workspace/Q3XL_LARGE_WORLD_RUNTIME_MEMO.md",
        "FROZEN_ATLAS.json": "host/FROZEN_ATLAS.json",
        "SOURCE_LOCK.json": "host/UPSTREAM_SOURCE_LOCK.json",
        "acceptance.py": "host/acceptance.py",
        "SEMANTIC_RUBRIC.md": "host/SEMANTIC_RUBRIC.md",
    }
    for source_name, destination in direct.items():
        data = git_bytes(LARGE_WORLD_REPO, D1_APPARATUS_COMMIT, f"{base}/{source_name}")
        lock_rows.append(write_exact(target / destination, data))

    atlas_path = target / "host" / "FROZEN_ATLAS.json"
    atlas = json.loads(atlas_path.read_bytes())
    if atlas["source_commit"] != D1_SOURCE_COMMIT:
        raise RuntimeError("D1 source commit mismatch")
    for study in atlas["studies"]:
        for document in study["documents"]:
            relative = document["path"]
            data = git_bytes(LARGE_WORLD_REPO, D1_SOURCE_COMMIT, relative)
            if len(data) != document["size_bytes"] or sha256_bytes(data) != document["sha256"]:
                raise RuntimeError(f"D1 atlas/source mismatch: {relative}")
            lock_rows.append(write_exact(target / "source_documents" / relative, data))


def materialize_d2(lock_rows: list[dict[str, Any]]) -> None:
    target = FIXTURES / "d2_paper_revision"
    require_clean_destination(target)
    prefix = "fixtures/paper_revision_v1"
    for source_path in git_paths(LARGE_WORLD_REPO, D2_FIXTURE_COMMIT, prefix):
        relative = source_path.removeprefix(prefix + "/")
        lock_rows.append(
            write_exact(target / relative, git_bytes(LARGE_WORLD_REPO, D2_FIXTURE_COMMIT, source_path))
        )

    test_source = git_bytes(
        LARGE_WORLD_REPO,
        D2_FIXTURE_COMMIT,
        "tests/test_paper_revision_fixture_v1.py",
    )
    known_paper = extract_string_constant(test_source, "KNOWN_PAPER").encode("utf-8")
    lock_rows.append(write_exact(GOLD / "d2_paper_revision" / "paper.md", known_paper))


def materialize_sister_tasks(lock_rows: list[dict[str, Any]]) -> None:
    for task_id, spec in TASK_SOURCES.items():
        target = FIXTURES / task_id
        require_clean_destination(target)
        commit = spec["commit"]
        base = spec["base"]
        for source_path in git_paths(SISTER_REPO, commit, base):
            relative = source_path.removeprefix(base + "/")
            lock_rows.append(write_exact(target / relative, git_bytes(SISTER_REPO, commit, source_path)))
        final_data = git_bytes(SISTER_REPO, commit, spec["final_grader"])
        lock_rows.append(write_exact(target / "host" / "grade-final-answer.mjs", final_data))

    d3_env_path = (
        "runs/102_independent_action_batching_qwen36-27b_seeds3465-3467_pilot01/"
        "coverage-coalescing__v5__s3465/environment.json"
    )
    d3_environment = git_bytes(SISTER_REPO, SISTER_RESULT_COMMIT, d3_env_path)
    d3_source = file_from_environment(d3_environment, "src/coalesce-coverage.mjs")
    lock_rows.append(
        write_exact(GOLD / "d3_coverage_coalescing" / "src" / "coalesce-coverage.mjs", d3_source)
    )

    d5_env_path = (
        "runs/107_response_headroom_new_tasks_qwen36-27b_seeds3474-3476_pilot01/"
        "deployment-wave-planning__v5-generous-8192__s3476/environment.json"
    )
    d5_environment = git_bytes(SISTER_REPO, SISTER_RESULT_COMMIT, d5_env_path)
    d5_source = file_from_environment(d5_environment, "src/deployment-waves.mjs")
    lock_rows.append(
        write_exact(
            GOLD / "d5_deployment_wave_planning" / "src" / "deployment-waves.mjs",
            d5_source,
        )
    )


def main() -> None:
    require_clean_destination(FIXTURES)
    require_clean_destination(GOLD)
    lock_rows: list[dict[str, Any]] = []
    materialize_d1(lock_rows)
    materialize_d2(lock_rows)
    materialize_sister_tasks(lock_rows)

    source_lock = {
        "schema_version": "capability-terrain-source-lock-v0",
        "repositories": [
            {
                "path_at_materialization": str(LARGE_WORLD_REPO),
                "commits": {
                    "d1_apparatus": D1_APPARATUS_COMMIT,
                    "d1_corpus": D1_SOURCE_COMMIT,
                    "d2_fixture": D2_FIXTURE_COMMIT,
                    "d2_direct_review": D2_REVIEW_COMMIT,
                },
            },
            {
                "path_at_materialization": str(SISTER_REPO),
                "commits": {
                    "d3_fixture": TASK_SOURCES["d3_coverage_coalescing"]["commit"],
                    "d4_fixture": TASK_SOURCES["d4_device_event_folding"]["commit"],
                    "d5_fixture": TASK_SOURCES["d5_deployment_wave_planning"]["commit"],
                    "gold_evidence": SISTER_RESULT_COMMIT,
                },
            },
        ],
        "files": sorted(lock_rows, key=lambda row: row["path"]),
    }
    source_lock["file_count"] = len(source_lock["files"])
    source_lock["total_bytes"] = sum(row["bytes"] for row in source_lock["files"])
    write_canonical_json(ROOT / "SOURCE_LOCK.json", source_lock)
    write_canonical_json(ROOT / "FIXTURE_MANIFEST.json", recursive_manifest(FIXTURES))
    write_canonical_json(ROOT / "GOLD_MANIFEST.json", recursive_manifest(GOLD))


if __name__ == "__main__":
    main()
