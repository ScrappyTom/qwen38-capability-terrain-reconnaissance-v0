from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from discovery_runtime.atlas import SourceAtlas
from discovery_runtime.canonical import sha256_file
from discovery_runtime.worlds import FileWorld, WorldRejected


ROOT = Path(__file__).resolve().parents[1]


class WorldTests(unittest.TestCase):
    def test_patch_is_hash_bound_and_contained(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source"
            source.mkdir()
            (source / "candidate.txt").write_text("old\n", encoding="utf-8")
            world = FileWorld(source=source, runtime_root=Path(temp) / "runtime", mutable_paths={"candidate.txt"})
            before = world.candidate_id
            result = world.patch("candidate.txt", "old", "new", sha256_file(world.root / "candidate.txt"))
            self.assertNotEqual(before, result["candidate_after"])
            with self.assertRaises(WorldRejected):
                world.read("../outside.txt")

    def test_atlas_vendoring_matches_freeze(self) -> None:
        fixture = ROOT / "fixtures/d1_large_world_navigation"
        atlas = SourceAtlas(fixture / "host/FROZEN_ATLAS.json", fixture / "source_documents")
        self.assertEqual(len(atlas.documents), 103)
        self.assertEqual(len(atlas.sections), 971)
        root = atlas.root()
        self.assertEqual(root["root"]["total_exact_bytes"], 766_502)
        first = next(iter(atlas.sections))
        self.assertTrue(atlas.read(first)["content"])


if __name__ == "__main__":
    unittest.main()
