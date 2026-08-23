from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Stage0Tests(unittest.TestCase):
    def test_canonical_stage0_checker(self) -> None:
        completed = subprocess.run([sys.executable, str(ROOT / "tools/check_stage0.py"), "--skip-external-hashes"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
