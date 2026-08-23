from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .canonical import sha256_bytes
from .manifest import recursive_manifest


UUID_PATTERN = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b")
WINDOWS_PATH_PATTERN = re.compile(r"\b[A-Za-z]:\\[^\s\"'<>|]+")
POSIX_TEMP_PATH_PATTERN = re.compile(r"/(?:tmp|var/tmp)/[^\s\"'<>|]+")
ISO_TIMESTAMP_PATTERN = re.compile(r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z\b")
DURATION_PATTERN = re.compile(r"\b\d+(?:\.\d+)?\s*(?:ms|milliseconds?|seconds?)\b", re.IGNORECASE)


def normalize_volatile_text(value: str) -> str:
    value = UUID_PATTERN.sub("<UUID>", value)
    value = WINDOWS_PATH_PATTERN.sub("<ABSOLUTE_PATH>", value)
    value = POSIX_TEMP_PATH_PATTERN.sub("<TEMP_PATH>", value)
    value = ISO_TIMESTAMP_PATTERN.sub("<TIMESTAMP>", value)
    value = DURATION_PATTERN.sub("<DURATION>", value)
    return value


def locked_executable(repo_root: Path, name: str) -> str:
    lock = json.loads((repo_root / "EVALUATOR_RUNTIME_LOCK.json").read_bytes())
    row = lock.get(name)
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise RuntimeError(f"missing locked evaluator executable: {name}")
    path = Path(row["path"])
    if not path.is_absolute():
        raise RuntimeError(f"locked evaluator path is not absolute: {name}")
    return str(path)


def run_process(command: list[str], *, cwd: Path, timeout: int = 120) -> dict[str, Any]:
    environment = dict(os.environ)
    environment.pop("NODE_TEST_CONTEXT", None)
    creationflags = subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0
    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
        creationflags=creationflags,
        start_new_session=os.name != "nt",
    )
    timeout_cleanup: dict[str, Any] | None = None
    try:
        stdout, stderr = process.communicate(timeout=timeout)
        exit_code = process.returncode
        timed_out = False
    except subprocess.TimeoutExpired:
        if os.name == "nt":
            cleanup = subprocess.run(
                ["taskkill", "/PID", str(process.pid), "/T", "/F"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=30,
            )
            timeout_cleanup = {
                "method": "taskkill_process_tree",
                "root_pid": process.pid,
                "exit_code": cleanup.returncode,
                "stdout": cleanup.stdout.decode("utf-8", errors="replace"),
                "stderr": cleanup.stderr.decode("utf-8", errors="replace"),
            }
        else:
            import signal

            os.killpg(process.pid, signal.SIGKILL)
            timeout_cleanup = {"method": "kill_process_group", "root_pid": process.pid, "exit_code": 0}
        stdout, stderr = process.communicate(timeout=30)
        exit_code = 124
        timed_out = True
    return {
        "command": command,
        "exit_code": exit_code,
        "timed_out": timed_out,
        "timeout_seconds": timeout,
        "timeout_cleanup": timeout_cleanup,
        "stdout": stdout.decode("utf-8", errors="replace"),
        "stderr": stderr.decode("utf-8", errors="replace"),
        "stdout_sha256": sha256_bytes(stdout),
        "stderr_sha256": sha256_bytes(stderr),
    }


def run_against_disposable_workspace(
    workspace: Path,
    operation,
) -> dict[str, Any]:
    """Evaluate exact bytes in a copy and make evaluator side effects visible.

    This guards candidate/world integrity. It is not an operating-system
    security sandbox; the frozen GPU authorization remains the authority for
    executing model-authored task code.
    """

    live_before = recursive_manifest(workspace)
    with tempfile.TemporaryDirectory(prefix="capability-terrain-eval-") as temporary:
        copied = Path(temporary) / "workspace"
        shutil.copytree(workspace, copied)
        copy_before = recursive_manifest(copied)
        raw = operation(copied)
        copy_after = recursive_manifest(copied)
    live_after = recursive_manifest(workspace)
    integrity = {
        "live_workspace_unchanged": live_before == live_after,
        "evaluation_copy_unchanged": copy_before == copy_after,
        "live_candidate_before": live_before["manifest_sha256"],
        "live_candidate_after": live_after["manifest_sha256"],
        "evaluation_candidate_before": copy_before["manifest_sha256"],
        "evaluation_candidate_after": copy_after["manifest_sha256"],
    }
    integrity["passed"] = integrity["live_workspace_unchanged"] and integrity["evaluation_copy_unchanged"]
    raw["process_exit_code"] = raw["exit_code"]
    raw["integrity"] = integrity
    if not integrity["passed"]:
        raw["exit_code"] = 1
    return raw


def bounded_projection_value(value: Any, *, depth: int = 0) -> Any:
    """Bound volatile diagnostics without changing the exact external raw result."""

    if isinstance(value, str):
        value = normalize_volatile_text(value)
        if len(value) <= 500:
            return value
        return value[:500] + f"…<truncated {len(value) - 500} characters; exact raw externally custodied>"
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if depth >= 4:
        return "<nested diagnostic omitted; exact raw externally custodied>"
    if isinstance(value, list):
        bounded = [bounded_projection_value(item, depth=depth + 1) for item in value[:50]]
        if len(value) > 50:
            bounded.append(f"<truncated {len(value) - 50} list items; exact raw externally custodied>")
        return bounded
    if isinstance(value, dict):
        items = list(value.items())
        bounded = {
            str(key): bounded_projection_value(item, depth=depth + 1)
            for key, item in items[:50]
        }
        if len(items) > 50:
            bounded["<truncated>"] = f"{len(items) - 50} keys; exact raw externally custodied"
        return bounded
    return bounded_projection_value(str(value), depth=depth + 1)


def stable_projection(raw: dict[str, Any], *, check_id: str, candidate_id: str) -> dict[str, Any]:
    stdout = raw["stdout"]
    tests: list[dict[str, Any]] = []
    for line in stdout.splitlines():
        match = re.match(r"^(not ok|ok)\s+\d+\s+-\s+(.+)$", line.strip())
        if match:
            tests.append({"name": match.group(2), "passed": match.group(1) == "ok"})
    parsed: Any = None
    stripped = stdout.strip()
    if stripped.startswith("{"):
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            parsed = None
    if isinstance(parsed, dict):
        failures = []
        for row in parsed.get("failures", []):
            if not isinstance(row, dict):
                continue
            failures.append(
                {
                    key: bounded_projection_value(value)
                    for key, value in row.items()
                    if key in {"case", "expected", "actual", "name", "error"}
                }
            )
        tests = [
            {"name": bounded_projection_value(row.get("name", row.get("case", "unnamed"))), "passed": bool(row.get("passed"))}
            for row in parsed.get("checks", [])
            if isinstance(row, dict)
        ] or tests
        passed = bool(parsed.get("passed", raw["exit_code"] == 0))
    else:
        failures = []
        passed = raw["exit_code"] == 0
    return {
        "tool": "run_check",
        "accepted": True,
        "check_id": check_id,
        "evaluated_candidate_id": candidate_id,
        "current_candidate_id": candidate_id,
        "currency": "current",
        "passed": passed,
        "tests": tests,
        "failures": failures,
        "raw_output": "externally_custodied",
        "projection_limits": {"maximum_string_characters": 500, "maximum_list_items": 50, "maximum_depth": 4, "volatile_normalization": ["UUID", "absolute Windows path", "POSIX temp path", "ISO-8601 UTC timestamp", "duration"]},
    }


def run_visible(cell_id: str, *, repo_root: Path, workspace: Path, candidate_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    if cell_id == "D1":
        command_for = lambda copied: [locked_executable(repo_root, "python"), str(repo_root / "tools" / "check_d1_candidate.py"), str(copied)]
        check_id = "memo_visible"
        cwd = repo_root
    elif cell_id == "D2":
        control = repo_root / "fixtures" / "d2_paper_revision" / "control"
        command_for = lambda copied: [locked_executable(repo_root, "python"), str(control / "visible_check.py"), str(copied)]
        check_id = "visible"
        cwd = control
    elif cell_id in {"D3", "D4", "D5"}:
        command_for = lambda copied: [locked_executable(repo_root, "npm"), "test"]
        check_id = "npm_test"
        cwd = workspace
    else:
        raise KeyError(cell_id)
    raw = run_against_disposable_workspace(
        workspace,
        lambda copied: run_process(
            command_for(copied),
            cwd=(copied if cell_id in {"D3", "D4", "D5"} else cwd),
        ),
    )
    projection = stable_projection(raw, check_id=check_id, candidate_id=candidate_id)
    if not raw["integrity"]["passed"]:
        projection["passed"] = False
        projection["failures"].append(
            {"case": "evaluator_workspace_integrity", "expected": True, "actual": raw["integrity"]}
        )
    return raw, projection


def run_external(cell_id: str, *, repo_root: Path, workspace: Path) -> dict[str, Any]:
    if cell_id == "D1":
        return run_against_disposable_workspace(
            workspace,
            lambda copied: run_process([locked_executable(repo_root, "python"), str(repo_root / "tools" / "check_d1_candidate.py"), str(copied)], cwd=repo_root),
        )
    if cell_id == "D2":
        control = repo_root / "fixtures" / "d2_paper_revision" / "control"
        return run_against_disposable_workspace(
            workspace,
            lambda copied: run_process([locked_executable(repo_root, "python"), str(control / "hidden_grade.py"), str(copied)], cwd=control),
        )
    task_dirs = {
        "D3": "d3_coverage_coalescing",
        "D4": "d4_device_event_folding",
        "D5": "d5_deployment_wave_planning",
    }
    task = repo_root / "fixtures" / task_dirs[cell_id]
    def grade(copied: Path) -> dict[str, Any]:
        evaluator = copied.parent / "evaluator"
        evaluator.mkdir()
        copied_grader = evaluator / "grade-artifact.mjs"
        copied_manifest = evaluator / "starting-world-manifest.json"
        shutil.copyfile(task / "grade-artifact.mjs", copied_grader)
        shutil.copyfile(task / "starting-world-manifest.json", copied_manifest)
        primary = run_process([locked_executable(repo_root, "node"), str(copied_grader), str(copied)], cwd=copied)
        if cell_id != "D4":
            return primary
        supplement_path = repo_root / "qualification" / "evaluators" / "d4_plain_object_grade.mjs"
        copied_supplement = evaluator / "d4_plain_object_grade.mjs"
        shutil.copyfile(supplement_path, copied_supplement)
        supplement = run_process(
            [locked_executable(repo_root, "node"), str(copied_supplement), str(copied)],
            cwd=copied,
        )
        primary_parsed = parsed_json_result(primary)
        supplement_parsed = parsed_json_result(supplement)
        combined = {
            "schema_version": "capability-terrain-d4-combined-external-grade-v0",
            "passed": primary["exit_code"] == 0 and supplement["exit_code"] == 0,
            "primary": {"raw": primary, "parsed": primary_parsed},
            "plain_object_supplement": {"raw": supplement, "parsed": supplement_parsed},
        }
        stdout = (json.dumps(combined, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
        return {
            "command": [primary["command"], supplement["command"]],
            "exit_code": 0 if combined["passed"] else 1,
            "stdout": stdout.decode("utf-8"),
            "stderr": "",
            "stdout_sha256": sha256_bytes(stdout),
            "stderr_sha256": sha256_bytes(b""),
        }
    return run_against_disposable_workspace(workspace, grade)


def run_final_response_external(
    cell_id: str,
    *,
    repo_root: Path,
    final_response_path: Path,
) -> dict[str, Any]:
    if cell_id in {"D1", "D2"}:
        return {
            "schema_version": "final-response-external-result-v0",
            "applicable": False,
            "cell_id": cell_id,
            "reason": "no vendored final-response grader for this cell",
        }
    task_dirs = {
        "D3": "d3_coverage_coalescing",
        "D4": "d4_device_event_folding",
        "D5": "d5_deployment_wave_planning",
    }
    if cell_id not in task_dirs:
        raise KeyError(cell_id)
    task = repo_root / "fixtures" / task_dirs[cell_id]
    return run_process(
        [
            locked_executable(repo_root, "node"),
            str(task / "host" / "grade-final-answer.mjs"),
            str(final_response_path),
        ],
        cwd=task,
    )


def parsed_json_result(raw: dict[str, Any]) -> dict[str, Any] | None:
    try:
        value = json.loads(raw["stdout"])
    except (json.JSONDecodeError, TypeError):
        return None
    return value if isinstance(value, dict) else None
