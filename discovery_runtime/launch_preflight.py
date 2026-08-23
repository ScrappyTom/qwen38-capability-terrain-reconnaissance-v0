from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Any

from .canonical import sha256_file


SAFE_RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


def validate_run_id(run_id: str) -> str:
    """Return a filesystem-safe literal run ID or raise before any writes."""

    if not SAFE_RUN_ID.fullmatch(run_id):
        raise ValueError(
            "run_id must be 1-128 characters, begin with an ASCII letter or "
            "digit, and contain only ASCII letters, digits, dot, underscore, or hyphen"
        )
    return run_id


def authorization_failures(
    value: dict[str, Any],
    *,
    expected_commit: str,
    run_id: str,
    contract: dict[str, Any],
) -> list[str]:
    """Mechanically compare an external authorization receipt to the freeze."""

    failures: list[str] = []
    if value.get("authorized") is not True:
        failures.append("not_authorized")
    if value.get("authorized_freeze_commit") != expected_commit:
        failures.append("commit")
    if value.get("authorized_run_id") != run_id:
        failures.append("run_id")
    if value.get("scope") != "qwen38-capability-terrain-reconnaissance-v0":
        failures.append("scope")
    maximum_calls = value.get("maximum_model_calls")
    if (
        isinstance(maximum_calls, bool)
        or not isinstance(maximum_calls, int)
        or maximum_calls != contract["max_total_actor_calls"]
    ):
        failures.append("calls")
    if value.get("one_attempt_per_call") is not True:
        failures.append("one_attempt_per_call")
    retries = value.get("retries")
    if isinstance(retries, bool) or not isinstance(retries, int) or retries != 0:
        failures.append("retries")
    if contract.get("one_attempt_per_call") is not True:
        failures.append("contract_one_attempt_per_call")
    if contract.get("retries") != 0:
        failures.append("contract_retries")
    return failures


def _file_gate(*, label: str, path_value: Any, expected_sha256: Any) -> dict[str, Any]:
    row: dict[str, Any] = {
        "label": label,
        "path": path_value,
        "expected_sha256": expected_sha256,
        "exists": False,
        "is_absolute": False,
        "bytes": None,
        "actual_sha256": None,
        "passed": False,
        "error": None,
    }
    try:
        if not isinstance(path_value, str) or not path_value:
            raise ValueError("locked path must be a non-empty string")
        path = Path(path_value)
        row["is_absolute"] = path.is_absolute()
        if not row["is_absolute"]:
            raise ValueError("locked path must be absolute")
        row["exists"] = path.is_file()
        if not row["exists"]:
            raise FileNotFoundError(path)
        row["bytes"] = path.stat().st_size
        row["actual_sha256"] = sha256_file(path)
        if not isinstance(expected_sha256, str) or row["actual_sha256"] != expected_sha256:
            raise ValueError("SHA-256 mismatch")
        row["passed"] = True
    except Exception as exc:
        row["error"] = f"{type(exc).__name__}: {exc}"
    return row


def _version_gate(*, label: str, path_value: Any, expected_version: Any) -> dict[str, Any]:
    row: dict[str, Any] = {
        "label": label,
        "path": path_value,
        "expected_version": expected_version,
        "actual_version": None,
        "exit_code": None,
        "passed": False,
        "error": None,
    }
    try:
        if not isinstance(path_value, str) or not Path(path_value).is_absolute():
            raise ValueError("locked executable path must be absolute")
        completed = subprocess.run(
            [path_value, "--version"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
        )
        row["exit_code"] = completed.returncode
        row["actual_version"] = completed.stdout.decode("utf-8", errors="replace").strip()
        if completed.returncode != 0:
            raise RuntimeError(f"version command exited {completed.returncode}")
        if row["actual_version"] != expected_version:
            raise ValueError("version mismatch")
        row["passed"] = True
    except Exception as exc:
        row["error"] = f"{type(exc).__name__}: {exc}"
    return row


def verify_external_locks(
    *,
    model_profile: dict[str, Any],
    evaluator_lock: dict[str, Any],
) -> dict[str, Any]:
    """Re-hash every external dependency and execute locked evaluator versions.

    The returned object is intentionally non-throwing so the caller can custody
    a failed gate before aborting the launch.
    """

    model_specs = (
        ("model", "model_path", "model_sha256"),
        ("tokenizer_projection", "tokenizer_projection_path", "tokenizer_projection_sha256"),
        ("server", "server_path", "server_sha256"),
        ("tokenizer", "tokenizer_path", "tokenizer_sha256"),
    )
    files = [
        _file_gate(
            label=label,
            path_value=model_profile.get(path_key),
            expected_sha256=model_profile.get(hash_key),
        )
        for label, path_key, hash_key in model_specs
    ]
    versions: list[dict[str, Any]] = []
    for label in ("python", "node", "npm"):
        locked = evaluator_lock.get(label)
        if not isinstance(locked, dict):
            files.append(
                _file_gate(label=f"evaluator_{label}", path_value=None, expected_sha256=None)
            )
            versions.append(
                _version_gate(label=label, path_value=None, expected_version=None)
            )
            continue
        files.append(
            _file_gate(
                label=f"evaluator_{label}",
                path_value=locked.get("path"),
                expected_sha256=locked.get("sha256"),
            )
        )
        versions.append(
            _version_gate(
                label=label,
                path_value=locked.get("path"),
                expected_version=locked.get("version"),
            )
        )
    failures = [f"file:{row['label']}" for row in files if not row["passed"]]
    failures.extend(f"version:{row['label']}" for row in versions if not row["passed"])
    return {
        "schema_version": "capability-terrain-launch-preflight-v0",
        "passed": not failures,
        "failures": failures,
        "files": files,
        "versions": versions,
        "locked_evaluator_paths": {
            label: evaluator_lock.get(label, {}).get("path")
            if isinstance(evaluator_lock.get(label), dict)
            else None
            for label in ("python", "node", "npm")
        },
    }
