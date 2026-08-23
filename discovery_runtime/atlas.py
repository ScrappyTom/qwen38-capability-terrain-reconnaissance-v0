from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .canonical import sha256_bytes
from .worlds import WorldRejected


class SourceAtlas:
    EXPAND_PAGE_SIZE = 20
    SEARCH_PAGE_SIZE = 20
    MAX_EXACT_READ_BYTES = 16_384

    def __init__(self, atlas_path: Path, document_root: Path) -> None:
        self.payload = json.loads(atlas_path.read_bytes())
        self.document_root = document_root
        self.atlas_sha256 = self.payload["atlas_sha256"]
        self.source_commit = self.payload["source_commit"]
        self.studies = {row["node_id"]: row for row in self.payload["studies"]}
        self.documents: dict[str, dict[str, Any]] = {}
        self.sections: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
        for study in self.payload["studies"]:
            for document in study["documents"]:
                self.documents[document["node_id"]] = document
                for section in document["sections"]:
                    self.sections[section["node_id"]] = (document, section)

    def _document_bytes(self, document: dict[str, Any]) -> bytes:
        path = self.document_root / Path(document["path"])
        data = path.read_bytes()
        if len(data) != document["size_bytes"] or sha256_bytes(data) != document["sha256"]:
            raise RuntimeError(f"vendored atlas document mismatch: {document['path']}")
        return data

    def root(self) -> dict[str, Any]:
        return {"tool": "atlas_root", "accepted": True, "atlas_sha256": self.atlas_sha256, "source_commit": self.source_commit, "root": self.payload["root"]}

    def expand(self, node_id: str, cursor: int) -> dict[str, Any]:
        if node_id == "ROOT":
            children = [
                {"node_id": row["node_id"], "study": row["study"], "document_count": row["document_count"], "size_bytes": row["size_bytes"]}
                for row in self.payload["studies"]
            ]
        elif node_id in self.studies:
            children = [
                {"node_id": row["node_id"], "path": row["path"], "title": row["title"], "line_count": row["line_count"], "size_bytes": row["size_bytes"]}
                for row in self.studies[node_id]["documents"]
            ]
        elif node_id in self.documents:
            children = [
                {"node_id": row["node_id"], "title": row["title"], "start_line": row["start_line"], "end_line": row["end_line"], "size_bytes": row["size_bytes"]}
                for row in self.documents[node_id]["sections"]
            ]
        else:
            raise WorldRejected("atlas_node_not_expandable", f"unknown node: {node_id}")
        if cursor > len(children):
            raise WorldRejected("atlas_cursor_invalid", f"cursor {cursor} exceeds {len(children)}")
        end = min(len(children), cursor + self.EXPAND_PAGE_SIZE)
        return {"tool": "atlas_expand", "accepted": True, "node_id": node_id, "cursor": cursor, "returned": end - cursor, "total_children": len(children), "next_cursor": end if end < len(children) else None, "children": children, "atlas_sha256": self.atlas_sha256, "source_commit": self.source_commit}

    def search(self, query: str, cursor: int) -> dict[str, Any]:
        needle = query.casefold()
        matches: list[dict[str, Any]] = []
        for document in self.documents.values():
            if needle in document["path"].casefold() or needle in document["title"].casefold():
                matches.append({"kind": "document_metadata", "document_id": document["node_id"], "section_id": None, "path": document["path"], "line": None, "text": document["title"][:500]})
            for section in document["sections"]:
                if needle in section["title"].casefold():
                    matches.append({"kind": "section_heading", "document_id": document["node_id"], "section_id": section["node_id"], "path": document["path"], "line": section["start_line"], "text": section["title"][:500]})
            lines = self._document_bytes(document).decode("utf-8").splitlines()
            for line_number, line in enumerate(lines, start=1):
                if needle in line.casefold():
                    section_id = next((row["node_id"] for row in document["sections"] if row["start_line"] <= line_number <= row["end_line"]), None)
                    matches.append({"kind": "literal_line", "document_id": document["node_id"], "section_id": section_id, "path": document["path"], "line": line_number, "text": line[:500]})
        if cursor > len(matches):
            raise WorldRejected("atlas_cursor_invalid", f"cursor {cursor} exceeds {len(matches)}")
        end = min(len(matches), cursor + self.SEARCH_PAGE_SIZE)
        return {"tool": "atlas_search", "accepted": True, "query": query, "cursor": cursor, "returned": end - cursor, "total_matches": len(matches), "next_cursor": end if end < len(matches) else None, "matches": matches[cursor:end], "atlas_sha256": self.atlas_sha256, "source_commit": self.source_commit}

    def read(self, node_id: str) -> dict[str, Any]:
        if node_id in self.documents:
            document = self.documents[node_id]
            data = self._document_bytes(document)
            if len(data) > self.MAX_EXACT_READ_BYTES:
                raise WorldRejected("atlas_document_too_large", f"document is {len(data)} bytes; read bounded sections")
            start, end, title = 1, document["line_count"], document["title"]
        elif node_id in self.sections:
            document, section = self.sections[node_id]
            lines = self._document_bytes(document).decode("utf-8").splitlines(keepends=True)
            start, end, title = section["start_line"], section["end_line"], section["title"]
            data = "".join(lines[start - 1 : end]).encode("utf-8")
            if len(data) != section["size_bytes"] or sha256_bytes(data) != section["sha256"]:
                raise RuntimeError(f"atlas section mismatch: {node_id}")
        else:
            raise WorldRejected("atlas_node_not_readable", f"unknown node: {node_id}")
        return {"tool": "atlas_read", "accepted": True, "node_id": node_id, "atlas_sha256": self.atlas_sha256, "source_commit": self.source_commit, "path": document["path"], "file_sha256": document["sha256"], "title": title, "start_line": start, "end_line": end, "slice_size_bytes": len(data), "slice_sha256": sha256_bytes(data), "content": data.decode("utf-8")}
