from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

from discovery_runtime.evaluation import locked_executable, run_final_response_external
from discovery_runtime.launch_preflight import (
    authorization_failures,
    validate_run_id,
    verify_external_locks,
)


ROOT = Path(__file__).resolve().parents[1]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class LaunchPreflightTests(unittest.TestCase):
    def test_run_id_is_a_safe_literal(self) -> None:
        self.assertEqual(validate_run_id("2026-08-23-scout_v0.1"), "2026-08-23-scout_v0.1")
        for invalid in ("", ".", "../escape", "a/b", r"a\b", " space"):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                validate_run_id(invalid)

    def test_authorization_requires_one_attempt_and_integer_zero_retries(self) -> None:
        contract = {"max_total_actor_calls": 42, "one_attempt_per_call": True, "retries": 0}
        base = {
            "authorized": True,
            "authorized_freeze_commit": "abc",
            "authorized_run_id": "run-1",
            "scope": "qwen38-capability-terrain-reconnaissance-v0",
            "maximum_model_calls": 42,
            "one_attempt_per_call": True,
            "retries": 0,
        }
        self.assertEqual(
            authorization_failures(base, expected_commit="abc", run_id="run-1", contract=contract),
            [],
        )
        missing_attempt = {key: value for key, value in base.items() if key != "one_attempt_per_call"}
        self.assertIn(
            "one_attempt_per_call",
            authorization_failures(missing_attempt, expected_commit="abc", run_id="run-1", contract=contract),
        )
        boolean_retries = {**base, "retries": False}
        self.assertIn(
            "retries",
            authorization_failures(boolean_retries, expected_commit="abc", run_id="run-1", contract=contract),
        )

    def test_external_gate_hashes_and_versions_exact_paths(self) -> None:
        executable = Path(sys.executable).resolve()
        version = sys.version.split()[0]
        expected_version = f"Python {version}"
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            files = {}
            for name in ("model", "projection", "server", "tokenizer"):
                path = root / f"{name}.bin"
                path.write_bytes(name.encode("ascii"))
                files[name] = path
            profile = {
                "model_path": str(files["model"]),
                "model_sha256": file_sha256(files["model"]),
                "tokenizer_projection_path": str(files["projection"]),
                "tokenizer_projection_sha256": file_sha256(files["projection"]),
                "server_path": str(files["server"]),
                "server_sha256": file_sha256(files["server"]),
                "tokenizer_path": str(files["tokenizer"]),
                "tokenizer_sha256": file_sha256(files["tokenizer"]),
            }
            evaluator = {
                name: {
                    "path": str(executable),
                    "sha256": file_sha256(executable),
                    "version": expected_version,
                }
                for name in ("python", "node", "npm")
            }
            passed = verify_external_locks(model_profile=profile, evaluator_lock=evaluator)
            self.assertTrue(passed["passed"], passed)
            files["model"].write_bytes(b"changed")
            failed = verify_external_locks(model_profile=profile, evaluator_lock=evaluator)
            self.assertFalse(failed["passed"])
            self.assertIn("file:model", failed["failures"])

    def test_runtime_uses_locked_evaluator_paths_and_final_grader(self) -> None:
        lock = json.loads((ROOT / "EVALUATOR_RUNTIME_LOCK.json").read_bytes())
        self.assertEqual(locked_executable(ROOT, "node"), lock["node"]["path"])
        with tempfile.TemporaryDirectory() as temp:
            response = Path(temp) / "response.txt"
            response.write_text(
                "Root cause: The implementation omitted contract logic.\n"
                "Files changed: The declared implementation target was updated.\n"
                "Verification: The exact visible test suite passed after the change.\n"
                "Remaining limitations: No known limitations remain within the frozen task.\n",
                encoding="utf-8",
            )
            result = run_final_response_external(
                "D3", repo_root=ROOT, final_response_path=response
            )
            self.assertEqual(result["exit_code"], 0, result)
            not_applicable = run_final_response_external(
                "D2", repo_root=ROOT, final_response_path=response
            )
            self.assertFalse(not_applicable["applicable"])


if __name__ == "__main__":
    unittest.main()
