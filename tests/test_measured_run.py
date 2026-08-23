from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.audit_tranche_run import audit, raw_manifest
from tools.validate_measured_d2_adjudication import validate


ROOT = Path(__file__).resolve().parents[1]
RUN_ROOT = ROOT / "runs" / "2026-08-23-capability-terrain-v0"


class MeasuredRunTests(unittest.TestCase):
    def test_mechanical_audit_recomputes(self) -> None:
        result = audit(RUN_ROOT)
        self.assertTrue(result["passed"], result["failures"])
        self.assertEqual(39, result["totals"]["actor_calls"])
        self.assertEqual(39, result["totals"]["provider_attempts"])
        self.assertEqual(0, result["totals"]["retries"])
        self.assertEqual(101657, result["totals"]["serialized_tokens"])
        self.assertEqual(19, result["totals"]["rejected_actions"])
        self.assertEqual(0, result["totals"]["pressure_events"])

    def test_raw_manifest_recomputes(self) -> None:
        expected = json.loads((RUN_ROOT / "RAW_RUN_MANIFEST.json").read_bytes())
        self.assertEqual(expected, raw_manifest(RUN_ROOT))

    def test_measured_d2_adjudication_recomputes(self) -> None:
        result = validate(RUN_ROOT / "D2_SEMANTIC_ADJUDICATION.json")
        self.assertTrue(result["passed"], result["failures"])
        self.assertEqual("not_ready", result["derived_closure_readiness"])
        self.assertEqual(
            {"met": 12, "partial": 1, "not_met": 0, "ambiguous": 0, "total": 13},
            result["derived_score"],
        )


if __name__ == "__main__":
    unittest.main()
