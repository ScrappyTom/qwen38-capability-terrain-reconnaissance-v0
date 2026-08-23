from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from .canonical import canonical_json_bytes


class ActionRejected(ValueError):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ActionRejected("duplicate_json_key", f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_one_object(raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise ActionRejected("response_not_utf8", str(exc)) from exc
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=lambda token: (_ for _ in ()).throw(
                ActionRejected("nonfinite_number", f"non-finite number: {token}")
            ),
        )
    except ActionRejected:
        raise
    except json.JSONDecodeError as exc:
        raise ActionRejected("invalid_json", str(exc)) from exc
    if not isinstance(value, dict):
        raise ActionRejected("response_not_object", "response must be one JSON object")
    return value


@dataclass(frozen=True)
class Field:
    kind: str
    required: bool = True
    minimum: int | None = None
    maximum: int | None = None
    enum: tuple[str, ...] = ()
    nullable: bool = False


@dataclass(frozen=True)
class ActionDefinition:
    name: str
    description: str
    fields: dict[str, Field]


COMMON_ACTIONS = (
    ActionDefinition("tree", "List files below one workspace-relative path.", {"path": Field("str", minimum=1, maximum=512)}),
    ActionDefinition(
        "search",
        "Find literal UTF-8 text below one workspace-relative path.",
        {"path": Field("str", minimum=1, maximum=512), "query": Field("str", minimum=1, maximum=500)},
    ),
    ActionDefinition("read", "Read one complete UTF-8 workspace file.", {"path": Field("str", minimum=1, maximum=512)}),
    ActionDefinition(
        "patch",
        "Replace one exact string in one mutable file. The old text must occur exactly once and the expected hash must be current.",
        {
            "path": Field("str", minimum=1, maximum=512),
            "old": Field("str", minimum=1, maximum=32768),
            "new": Field("str", maximum=32768),
            "expected_file_sha256": Field("sha256"),
        },
    ),
    ActionDefinition(
        "replace_file",
        "Replace one complete mutable UTF-8 file using its current file hash.",
        {
            "path": Field("str", minimum=1, maximum=512),
            "content": Field("str", maximum=32768),
            "expected_file_sha256": Field("sha256"),
        },
    ),
    ActionDefinition(
        "run_check",
        "Run one declared visible check against the exact current candidate.",
        {"check_id": Field("str", minimum=1, maximum=100)},
    ),
    ActionDefinition(
        "reopen_exact",
        "Reopen one exact externally custodied result by its receipt ID.",
        {"result_id": Field("str", minimum=1, maximum=100)},
    ),
    ActionDefinition(
        "submit",
        "Submit the exact current candidate and a bounded final response.",
        {"final_response": Field("str", minimum=1, maximum=12000)},
    ),
)

ATLAS_ACTIONS = (
    ActionDefinition("atlas_root", "Return the frozen atlas root.", {}),
    ActionDefinition(
        "atlas_expand",
        "Expand one atlas hierarchy node with deterministic pagination.",
        {"node_id": Field("str", minimum=1, maximum=100), "cursor": Field("int", minimum=0)},
    ),
    ActionDefinition(
        "atlas_search",
        "Search frozen atlas metadata, headings, and literal source lines.",
        {"query": Field("str", minimum=1, maximum=200), "cursor": Field("int", minimum=0)},
    ),
    ActionDefinition("atlas_read", "Read one exact atlas document or bounded section.", {"node_id": Field("str", minimum=1, maximum=100)}),
)


def action_definitions(*, atlas: bool) -> tuple[ActionDefinition, ...]:
    return COMMON_ACTIONS + (ATLAS_ACTIONS if atlas else ())


def _validate_field(name: str, value: Any, field: Field) -> None:
    if value is None and field.nullable:
        return
    if field.kind == "str":
        if not isinstance(value, str):
            raise ActionRejected("field_type", f"{name} must be a string")
        length = len(value)
        if field.minimum is not None and length < field.minimum:
            raise ActionRejected("field_length", f"{name} is too short")
        if field.maximum is not None and length > field.maximum:
            raise ActionRejected("field_length", f"{name} is too long")
        if field.enum and value not in field.enum:
            raise ActionRejected("field_enum", f"{name} is not an allowed value")
    elif field.kind == "int":
        if isinstance(value, bool) or not isinstance(value, int):
            raise ActionRejected("field_type", f"{name} must be an integer")
        if field.minimum is not None and value < field.minimum:
            raise ActionRejected("field_range", f"{name} is below minimum")
        if field.maximum is not None and value > field.maximum:
            raise ActionRejected("field_range", f"{name} exceeds maximum")
    elif field.kind == "sha256":
        if not isinstance(value, str) or len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
            raise ActionRejected("field_sha256", f"{name} must be a lowercase SHA-256")
    else:
        raise RuntimeError(f"unknown field kind: {field.kind}")


def validate_action(value: dict[str, Any], *, atlas: bool) -> dict[str, Any]:
    action = value.get("action")
    if not isinstance(action, str):
        raise ActionRejected("missing_action", "action must be a string")
    definitions = {row.name: row for row in action_definitions(atlas=atlas)}
    definition = definitions.get(action)
    if definition is None:
        raise ActionRejected("unknown_action", f"unknown action: {action}")
    expected = {"action", *definition.fields}
    extras = sorted(set(value) - expected)
    missing = sorted(name for name, field in definition.fields.items() if field.required and name not in value)
    if extras:
        raise ActionRejected("undeclared_fields", f"undeclared fields: {extras}")
    if missing:
        raise ActionRejected("missing_fields", f"missing fields: {missing}")
    for name, field in definition.fields.items():
        if name in value:
            _validate_field(name, value[name], field)
    return value


def parse_action(raw: bytes, *, atlas: bool) -> dict[str, Any]:
    return validate_action(parse_one_object(raw), atlas=atlas)


def _field_schema(field: Field) -> dict[str, Any]:
    if field.kind in {"str", "sha256"}:
        schema: dict[str, Any] = {"type": "string"}
        if field.kind == "sha256":
            schema["pattern"] = "^[0-9a-f]{64}$"
        if field.minimum is not None:
            schema["minLength"] = field.minimum
        if field.maximum is not None:
            schema["maxLength"] = field.maximum
        if field.enum:
            schema["enum"] = list(field.enum)
        return schema
    schema = {"type": "integer"}
    if field.minimum is not None:
        schema["minimum"] = field.minimum
    if field.maximum is not None:
        schema["maximum"] = field.maximum
    return schema


def action_catalog(*, atlas: bool) -> list[dict[str, Any]]:
    rows = []
    for definition in action_definitions(atlas=atlas):
        rows.append(
            {
                "action": definition.name,
                "description": definition.description,
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {name: _field_schema(field) for name, field in definition.fields.items()},
                    "required": [name for name, field in definition.fields.items() if field.required],
                },
            }
        )
    return rows


def system_prompt(*, atlas: bool, max_calls: int) -> str:
    catalog = canonical_json_bytes(action_catalog(atlas=atlas)).decode("utf-8").strip()
    return (
        "You are operating a bounded exact experimental workbench. Return exactly one bare JSON action "
        "per assistant turn, with no Markdown or text outside the object. The action catalog is authoritative; "
        "undeclared fields and invalid actions are rejected without repair. Read governing files before changing "
        "the candidate. A mutation result must cross into a later decision before you may treat it as observed. "
        "A check is bound to the exact candidate it evaluated; after any later mutation it is stale. Submit only "
        "when you choose to finish. "
        f"The trajectory permits at most {max_calls} model calls. Action catalog: {catalog}"
    )


def validate_final_response(text: str, *, require_labels: bool) -> dict[str, Any]:
    labels = ["Root cause:", "Files changed:", "Verification:", "Remaining limitations:"]
    positions = [text.find(label) for label in labels]
    ordered = all(value >= 0 for value in positions) and positions == sorted(positions)
    return {"required": require_labels, "labels": labels, "positions": positions, "passed": (not require_labels) or ordered}
