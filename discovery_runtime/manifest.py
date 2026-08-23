from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

from .canonical import canonical_json_bytes, sha256_bytes, sha256_file


DEFAULT_EXCLUDED_PARTS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
}


def recursive_manifest(
    root: Path,
    *,
    excluded_parts: Iterable[str] = DEFAULT_EXCLUDED_PARTS,
) -> dict[str, Any]:
    excluded = set(excluded_parts)
    files: list[dict[str, Any]] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        if any(part in excluded for part in Path(relative).parts):
            continue
        files.append(
            {
                "path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    payload = {"schema_version": 1, "files": files}
    payload["manifest_sha256"] = sha256_bytes(canonical_json_bytes(payload))
    payload["file_count"] = len(files)
    payload["total_bytes"] = sum(row["bytes"] for row in files)
    return payload
