from __future__ import annotations

import unittest

from discovery_runtime.actions import ActionRejected, parse_action, validate_final_response


class ActionTests(unittest.TestCase):
    def test_accepts_one_declared_action(self) -> None:
        value = parse_action(b'{"action":"atlas_root"}\n', atlas=True)
        self.assertEqual(value, {"action": "atlas_root"})

    def test_rejects_duplicate_keys(self) -> None:
        with self.assertRaises(ActionRejected) as raised:
            parse_action(b'{"action":"tree","action":"read","path":"x"}', atlas=False)
        self.assertEqual(raised.exception.code, "duplicate_json_key")

    def test_rejects_extra_fields(self) -> None:
        with self.assertRaises(ActionRejected) as raised:
            parse_action(b'{"action":"tree","path":".","comment":"x"}', atlas=False)
        self.assertEqual(raised.exception.code, "undeclared_fields")

    def test_final_response_labels(self) -> None:
        good = "Root cause: x\nFiles changed: x\nVerification: x\nRemaining limitations: x"
        self.assertTrue(validate_final_response(good, require_labels=True)["passed"])
        self.assertFalse(validate_final_response("done", require_labels=True)["passed"])


if __name__ == "__main__":
    unittest.main()
