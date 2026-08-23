from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from .canonical import contained_path, sha256_bytes, sha256_file
from .manifest import recursive_manifest


class WorldRejected(ValueError):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


class FileWorld:
    def __init__(
        self,
        *,
        source: Path,
        runtime_root: Path,
        mutable_paths: set[str],
        max_file_bytes: int = 32_768,
    ) -> None:
        if runtime_root.exists():
            raise RuntimeError(f"runtime root already exists: {runtime_root}")
        shutil.copytree(source, runtime_root)
        self.root = runtime_root.resolve()
        self.mutable_paths = set(mutable_paths)
        self.max_file_bytes = max_file_bytes
        self.initial_manifest = recursive_manifest(self.root)

    @property
    def candidate_id(self) -> str:
        return recursive_manifest(self.root)["manifest_sha256"]

    def snapshot(self) -> dict[str, Any]:
        return recursive_manifest(self.root)

    def _path(self, relative: str) -> Path:
        try:
            return contained_path(self.root, relative)
        except ValueError as exc:
            raise WorldRejected("invalid_path", str(exc)) from exc

    def _require_file(self, relative: str) -> Path:
        path = self._path(relative)
        if not path.is_file():
            raise WorldRejected("file_not_found", f"not a file: {relative}")
        return path

    def tree(self, relative: str) -> dict[str, Any]:
        path = self._path(relative)
        if not path.exists() or not path.is_dir():
            raise WorldRejected("directory_not_found", f"not a directory: {relative}")
        entries = []
        for item in sorted(path.rglob("*")):
            if any(part in {".git", "node_modules", "__pycache__"} for part in item.parts):
                continue
            row = {"path": item.relative_to(self.root).as_posix(), "type": "directory" if item.is_dir() else "file"}
            if item.is_file():
                row.update({"bytes": item.stat().st_size, "sha256": sha256_file(item)})
            entries.append(row)
        return {"tool": "tree", "accepted": True, "path": relative, "candidate_id": self.candidate_id, "entries": entries}

    def read(self, relative: str) -> dict[str, Any]:
        path = self._require_file(relative)
        data = path.read_bytes()
        if len(data) > self.max_file_bytes:
            raise WorldRejected("file_too_large", f"file exceeds {self.max_file_bytes} bytes")
        try:
            content = data.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            raise WorldRejected("file_not_utf8", str(exc)) from exc
        return {
            "tool": "read",
            "accepted": True,
            "path": relative,
            "content": content,
            "bytes": len(data),
            "file_sha256": sha256_bytes(data),
            "candidate_id": self.candidate_id,
        }

    def search(self, relative: str, query: str) -> dict[str, Any]:
        path = self._path(relative)
        if not path.exists():
            raise WorldRejected("path_not_found", f"path not found: {relative}")
        files = [path] if path.is_file() else sorted(item for item in path.rglob("*") if item.is_file())
        matches: list[dict[str, Any]] = []
        for file in files:
            if any(part in {".git", "node_modules", "__pycache__"} for part in file.parts):
                continue
            try:
                lines = file.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                continue
            for number, line in enumerate(lines, start=1):
                if query in line:
                    matches.append({"path": file.relative_to(self.root).as_posix(), "line": number, "text": line[:500]})
                    if len(matches) == 100:
                        return {"tool": "search", "accepted": True, "query": query, "truncated": True, "matches": matches, "candidate_id": self.candidate_id}
        return {"tool": "search", "accepted": True, "query": query, "truncated": False, "matches": matches, "candidate_id": self.candidate_id}

    def _mutation_path(self, relative: str, expected_file_sha256: str) -> Path:
        if relative not in self.mutable_paths:
            raise WorldRejected("path_not_mutable", f"path is not mutable: {relative}")
        path = self._require_file(relative)
        actual = sha256_file(path)
        if actual != expected_file_sha256:
            raise WorldRejected("stale_file_hash", f"expected {expected_file_sha256}; current {actual}")
        return path

    def patch(self, relative: str, old: str, new: str, expected_file_sha256: str) -> dict[str, Any]:
        before_candidate = self.candidate_id
        path = self._mutation_path(relative, expected_file_sha256)
        content = path.read_text(encoding="utf-8")
        occurrences = content.count(old)
        if occurrences != 1:
            raise WorldRejected("patch_match_count", f"old text occurs {occurrences} times")
        updated = content.replace(old, new, 1)
        data = updated.encode("utf-8")
        if len(data) > self.max_file_bytes:
            raise WorldRejected("replacement_too_large", f"file would exceed {self.max_file_bytes} bytes")
        path.write_bytes(data)
        return {
            "tool": "patch",
            "accepted": True,
            "accepted": True,
            "path": relative,
            "candidate_before": before_candidate,
            "candidate_after": self.candidate_id,
            "file_sha256_before": expected_file_sha256,
            "file_sha256_after": sha256_bytes(data),
            "bytes_after": len(data),
        }

    def replace_file(self, relative: str, content: str, expected_file_sha256: str) -> dict[str, Any]:
        before_candidate = self.candidate_id
        path = self._mutation_path(relative, expected_file_sha256)
        data = content.encode("utf-8")
        if len(data) > self.max_file_bytes:
            raise WorldRejected("replacement_too_large", f"file would exceed {self.max_file_bytes} bytes")
        path.write_bytes(data)
        return {
            "tool": "replace_file",
            "accepted": True,
            "accepted": True,
            "path": relative,
            "candidate_before": before_candidate,
            "candidate_after": self.candidate_id,
            "file_sha256_before": expected_file_sha256,
            "file_sha256_after": sha256_bytes(data),
            "bytes_after": len(data),
        }
