from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .actions import ActionRejected, parse_action, system_prompt, validate_final_response
from .atlas import SourceAtlas
from .canonical import canonical_json_bytes, sha256_bytes, write_canonical_json
from .evaluation import parsed_json_result, run_external, run_final_response_external, run_visible
from .model_io import LiveTokenizer, completion_payload, extract_completion, post_json_custodied
from .worlds import FileWorld, WorldRejected


@dataclass
class StoredResult:
    result_id: str
    value: dict[str, Any]
    body: bytes
    message_index: int
    delivered_at_call: int | None = None
    demoted: bool = False

    def receipt(self) -> dict[str, Any]:
        identity_keys = ("tool", "path", "node_id", "query", "check_id", "source_result_id")
        return {
            "result_id": self.result_id,
            "exact_body_bytes": len(self.body),
            "exact_body_sha256": sha256_bytes(self.body),
            "mechanical_identity": {
                key: self.value[key]
                for key in identity_keys
                if key in self.value
            },
            "exact_reopen": {"action": "reopen_exact", "result_id": self.result_id},
        }


class CellRunner:
    def __init__(
        self,
        *,
        repo_root: Path,
        cell_id: str,
        cell: dict[str, Any],
        profile: dict[str, Any],
        run_root: Path,
        base_url: str = "http://127.0.0.1:8080",
        d6_initial_message: str | None = None,
        workspace_source_override: Path | None = None,
        task_text_override: str | None = None,
        inherited_result_root: Path | None = None,
    ) -> None:
        self.repo_root = repo_root
        self.cell_id = cell_id
        self.cell = cell
        self.profile = profile
        self.run_root = run_root
        self.base_url = base_url.rstrip("/")
        self.d6_initial_message = d6_initial_message
        self.tokenizer = LiveTokenizer(self.base_url)
        self.run_root.mkdir(parents=True, exist_ok=False)
        fixture = repo_root / cell["fixture"]
        workspace_source = workspace_source_override or (fixture / cell["workspace"])
        self.world = FileWorld(
            source=workspace_source,
            runtime_root=run_root / "workspace",
            mutable_paths=set(cell["mutable_paths"]),
        )
        self.atlas = (
            SourceAtlas(fixture / "host" / "FROZEN_ATLAS.json", fixture / "source_documents")
            if cell.get("atlas")
            else None
        )
        self.task_text = task_text_override or (fixture / cell["task"]).read_text(encoding="utf-8")
        self.messages: list[dict[str, str]] = []
        self.results: dict[str, StoredResult] = {}
        self.reopen_store: dict[str, StoredResult] = {}
        self.next_result = 1
        if inherited_result_root is not None:
            self._load_inherited_results(inherited_result_root)
        self.latest_check: dict[str, Any] | None = None
        self.submitted = False
        self.final_response: str | None = None

    def _load_inherited_results(self, parent_run_root: Path) -> None:
        maximum = 0
        for result_path in sorted((parent_run_root / "results").glob("RESULT-*/result.json")):
            result_id = result_path.parent.name
            try:
                number = int(result_id.removeprefix("RESULT-"))
            except ValueError as exc:
                raise RuntimeError(f"invalid inherited result ID: {result_id}") from exc
            receipt_path = result_path.parent / "receipt.json"
            value = json.loads(result_path.read_bytes())
            receipt = json.loads(receipt_path.read_bytes())
            body = result_path.read_bytes()
            if (
                value.get("result_id") != result_id
                or receipt.get("result_id") != result_id
                or receipt.get("exact_body_bytes") != len(body)
                or receipt.get("exact_body_sha256") != sha256_bytes(body)
            ):
                raise RuntimeError(f"inherited result custody mismatch: {result_id}")
            self.reopen_store[result_id] = StoredResult(
                result_id=result_id,
                value=value,
                body=body,
                message_index=-1,
                delivered_at_call=0,
                demoted=True,
            )
            maximum = max(maximum, number)
        self.next_result = maximum + 1

    def initial_messages(self) -> list[dict[str, str]]:
        initial = {
            "schema_version": "capability-terrain-initial-surface-v0",
            "cell_id": self.cell_id,
            "candidate_id": self.world.candidate_id,
            "mutable_paths": sorted(self.world.mutable_paths),
            "visible_check_id": self.cell.get("visible_check"),
            "exact_external_history": True,
            "exact_results_reopenable_after_demotion": True,
        }
        if self.atlas is not None:
            initial["atlas_orientation"] = {
                "root_id": "ROOT",
                "atlas_sha256": self.atlas.atlas_sha256,
                "source_commit": self.atlas.source_commit,
                **self.atlas.payload["root"],
            }
        content = self.d6_initial_message or (
            "AUTHORITATIVE TASK\n"
            + self.task_text
            + "\n\nINITIAL EXACT WORK SURFACE\n"
            + canonical_json_bytes(initial).decode("utf-8")
        )
        return [
            {"role": "system", "content": system_prompt(atlas=self.atlas is not None, max_calls=self.cell["call_ceiling"])},
            {"role": "user", "content": content},
        ]

    def _save_result(self, value: dict[str, Any], *, message_index: int) -> StoredResult:
        result_id = f"RESULT-{self.next_result:03d}"
        self.next_result += 1
        value = {**value, "schema_version": "exact-action-result-v0", "result_id": result_id}
        body = canonical_json_bytes(value)
        stored = StoredResult(result_id=result_id, value=value, body=body, message_index=message_index)
        self.results[result_id] = stored
        self.reopen_store[result_id] = stored
        result_dir = self.run_root / "results" / result_id
        result_dir.mkdir(parents=True, exist_ok=False)
        (result_dir / "result.json").write_bytes(body)
        write_canonical_json(result_dir / "receipt.json", stored.receipt())
        return stored

    def _result_message(self, stored: StoredResult) -> str:
        return "EXACT ACTION RESULT\n" + stored.body.decode("utf-8")

    def _receipt_message(self, stored: StoredResult) -> str:
        return "EXACT RESULT RECEIPT\n" + canonical_json_bytes(stored.receipt()).decode("utf-8")

    def _count(self) -> tuple[int, str]:
        return self.tokenizer.count_messages(self.messages)

    def _relieve_if_needed(self, call_number: int) -> dict[str, Any]:
        before, rendered = self._count()
        receipt: dict[str, Any] = {"call": call_number, "before_tokens": before, "substitutions": [], "skipped_nonpositive": [], "prompt_ceiling": self.profile["prompt_ceiling_tokens"]}
        if before <= self.profile["prompt_ceiling_tokens"]:
            receipt.update({"after_tokens": before, "fit": True})
            (self.run_root / "calls" / f"call-{call_number:03d}" / "rendered-prompt.txt").write_text(rendered, encoding="utf-8")
            return receipt
        for stored in self.results.values():
            if stored.delivered_at_call is None or stored.demoted:
                continue
            current_tokens = self._count()[0]
            old = self.messages[stored.message_index]["content"]
            self.messages[stored.message_index]["content"] = self._receipt_message(stored)
            after, rendered = self._count()
            savings = current_tokens - after
            if savings <= 0:
                self.messages[stored.message_index]["content"] = old
                receipt["skipped_nonpositive"].append(
                    {
                        "result_id": stored.result_id,
                        "before_tokens": current_tokens,
                        "prospective_after_tokens": after,
                        "prospective_savings_tokens": savings,
                    }
                )
                continue
            stored.demoted = True
            receipt["substitutions"].append({"result_id": stored.result_id, "before_message_bytes": len(old.encode("utf-8")), "before_tokens": current_tokens, "after_tokens": after, "savings_tokens": savings})
            if after <= self.profile["prompt_ceiling_tokens"]:
                receipt.update({"after_tokens": after, "fit": True})
                (self.run_root / "calls" / f"call-{call_number:03d}" / "rendered-prompt.txt").write_text(rendered, encoding="utf-8")
                return receipt
        final_tokens, final_rendered = self._count()
        (self.run_root / "calls" / f"call-{call_number:03d}" / "rendered-prompt.txt").write_text(final_rendered, encoding="utf-8")
        receipt.update({"after_tokens": final_tokens, "fit": False})
        return receipt

    def _reconcile_latest_check(self) -> None:
        if self.latest_check is None:
            return
        current = self.world.candidate_id
        self.latest_check["current_candidate_id"] = current
        self.latest_check["currency"] = (
            "current"
            if self.latest_check.get("evaluated_candidate_id") == current
            else "stale"
        )

    def _reject(self, *, action: str | None, code: str, message: str) -> dict[str, Any]:
        return {"tool": action or "response", "accepted": False, "error": {"code": code, "message": message}, "candidate_id": self.world.candidate_id}

    def execute(self, action: dict[str, Any], call_dir: Path) -> tuple[dict[str, Any], bool]:
        name = action["action"]
        if name == "tree":
            return self.world.tree(action["path"]), False
        if name == "search":
            return self.world.search(action["path"], action["query"]), False
        if name == "read":
            return self.world.read(action["path"]), False
        if name == "patch":
            result = self.world.patch(action["path"], action["old"], action["new"], action["expected_file_sha256"])
            self._reconcile_latest_check()
            return result, False
        if name == "replace_file":
            result = self.world.replace_file(action["path"], action["content"], action["expected_file_sha256"])
            self._reconcile_latest_check()
            return result, False
        if name == "run_check":
            expected = self.cell.get("visible_check")
            if action["check_id"] != expected:
                raise WorldRejected("unknown_check", f"declared check is {expected}")
            raw, projection = run_visible(self.cell_id if self.cell_id != "D6" else self.cell["donor_cell"], repo_root=self.repo_root, workspace=self.world.root, candidate_id=self.world.candidate_id)
            write_canonical_json(call_dir / "check.raw.json", raw)
            self.latest_check = projection
            return projection, False
        if name == "reopen_exact":
            stored = self.reopen_store.get(action["result_id"])
            if stored is None:
                raise WorldRejected("unknown_result", f"unknown result ID: {action['result_id']}")
            return {
                "tool": "reopen_exact",
                "accepted": True,
                "source_result_id": stored.result_id,
                "reopened": True,
                "reopened_exact_body_bytes": len(stored.body),
                "reopened_exact_body_sha256": sha256_bytes(stored.body),
                "reopened_exact_result": stored.value,
                "current_candidate_id": self.world.candidate_id,
            }, False
        if name == "submit":
            final_contract = validate_final_response(action["final_response"], require_labels=bool(self.cell.get("requires_labeled_final_response")))
            self.submitted = True
            self.final_response = action["final_response"]
            return {"tool": "submit", "accepted": True, "candidate_id": self.world.candidate_id, "inline_label_screen": final_contract, "external_final_response_grade_pending": True}, True
        if self.atlas is not None:
            if name == "atlas_root":
                return {**self.atlas.root(), "candidate_id": self.world.candidate_id}, False
            if name == "atlas_expand":
                return {**self.atlas.expand(action["node_id"], action["cursor"]), "candidate_id": self.world.candidate_id}, False
            if name == "atlas_search":
                return {**self.atlas.search(action["query"], action["cursor"]), "candidate_id": self.world.candidate_id}, False
            if name == "atlas_read":
                return {**self.atlas.read(action["node_id"]), "candidate_id": self.world.candidate_id}, False
        raise WorldRejected("unknown_action", name)

    def run_initialized(self) -> dict[str, Any]:
        self.messages = self.initial_messages()
        initial_candidate = self.world.candidate_id
        calls: list[dict[str, Any]] = []
        terminal = "actor_call_budget_exhausted"
        for call_number in range(1, self.cell["call_ceiling"] + 1):
            call_dir = self.run_root / "calls" / f"call-{call_number:03d}"
            call_dir.mkdir(parents=True, exist_ok=False)
            relief = self._relieve_if_needed(call_number)
            write_canonical_json(call_dir / "capacity.json", relief)
            if not relief["fit"]:
                terminal = "context_capacity_exhausted"
                break
            prompt_tokens = relief["after_tokens"]
            payload = completion_payload(self.messages, profile=self.profile)
            _, response, transport = post_json_custodied(self.base_url, "/v1/chat/completions", payload, call_dir / "provider-attempt-1")
            content, usage, finish_reason = extract_completion(response)
            for stored in self.results.values():
                if stored.delivered_at_call is None and stored.message_index < len(self.messages):
                    stored.delivered_at_call = call_number
            (call_dir / "assistant-content.txt").write_text(content, encoding="utf-8")
            self.messages.append({"role": "assistant", "content": content})
            action: dict[str, Any] | None = None
            try:
                action = parse_action(content.encode("utf-8"), atlas=self.atlas is not None)
                write_canonical_json(call_dir / "action.json", action)
                result, is_terminal = self.execute(action, call_dir)
            except (ActionRejected, WorldRejected) as exc:
                result = self._reject(action=action.get("action") if action else None, code=exc.code, message=exc.message)
                is_terminal = False
            message_index = len(self.messages)
            stored = self._save_result(result, message_index=message_index)
            self.messages.append({"role": "user", "content": self._result_message(stored)})
            call_record = {"call": call_number, "prompt_tokens": prompt_tokens, "usage": usage, "finish_reason": finish_reason, "transport": transport, "action": action, "result_id": stored.result_id, "accepted": result.get("accepted"), "candidate_id": self.world.candidate_id}
            calls.append(call_record)
            write_canonical_json(call_dir / "call.json", call_record)
            if is_terminal:
                terminal = "submitted"
                break
        external = run_external(self.cell_id if self.cell_id != "D6" else self.cell["donor_cell"], repo_root=self.repo_root, workspace=self.world.root)
        write_canonical_json(self.run_root / "external-evaluation.raw.json", external)
        final_response_evaluation: dict[str, Any] | None = None
        if self.final_response is not None:
            final_response_path = self.run_root / "final-response.txt"
            final_response_path.write_text(self.final_response, encoding="utf-8")
            final_response_raw = run_final_response_external(
                self.cell_id if self.cell_id != "D6" else self.cell["donor_cell"],
                repo_root=self.repo_root,
                final_response_path=final_response_path,
            )
            write_canonical_json(self.run_root / "final-response-evaluation.raw.json", final_response_raw)
            final_response_evaluation = {
                "applicable": final_response_raw.get("applicable", True),
                "exit_code": final_response_raw.get("exit_code"),
                "parsed": parsed_json_result(final_response_raw) if "stdout" in final_response_raw else None,
            }
        donor_for_evaluation = self.cell_id if self.cell_id != "D6" else self.cell["donor_cell"]
        summary = {
            "schema_version": "capability-terrain-cell-result-v0",
            "cell_id": self.cell_id,
            "initial_candidate_id": initial_candidate,
            "final_candidate_id": self.world.candidate_id,
            "candidate_changed": initial_candidate != self.world.candidate_id,
            "terminal": terminal,
            "submitted": self.submitted,
            "calls": calls,
            "result_count": len(self.results),
            "delivery_ledger": [
                {
                    "result_id": stored.result_id,
                    "delivered_at_call": stored.delivered_at_call,
                    "demoted": stored.demoted,
                    **stored.receipt(),
                }
                for stored in self.results.values()
            ],
            "external_evaluation_exit_code": external["exit_code"],
            "final_response_evaluation": final_response_evaluation,
            "D2_requirement_readiness": (
                {
                    "status": "not_adjudicated",
                    "evaluator_id": "paper-revision-requirement-review-v0",
                    "protocol": "ADJUDICATION_PROTOCOL.json",
                }
                if donor_for_evaluation == "D2"
                else None
            ),
            "final_manifest": self.world.snapshot(),
            "latest_check": self.latest_check,
        }
        write_canonical_json(self.run_root / "RESULT.json", summary)
        write_canonical_json(self.run_root / "messages.final.json", self.messages)
        return summary
