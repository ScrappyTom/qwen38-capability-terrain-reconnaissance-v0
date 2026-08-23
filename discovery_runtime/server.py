from __future__ import annotations

import csv
import io
import json
import re
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

from .canonical import write_canonical_json


HOST = "127.0.0.1"
PORT = 8080
BASE_URL = f"http://{HOST}:{PORT}"


def port_open() -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.settimeout(0.25)
        return probe.connect_ex((HOST, PORT)) == 0


def active_server_pids() -> list[int]:
    if sys.platform != "win32":
        return []
    output = subprocess.run(
        ["tasklist", "/FI", "IMAGENAME eq llama-server.exe", "/FO", "CSV", "/NH"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    ).stdout
    result = []
    for row in csv.reader(io.StringIO(output)):
        if len(row) >= 2 and row[0].casefold() == "llama-server.exe":
            result.append(int(row[1]))
    return result


def gpu_processes() -> list[dict[str, Any]]:
    output = subprocess.run(
        ["nvidia-smi", "--query-compute-apps=pid,process_name,used_memory", "--format=csv,noheader,nounits"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    ).stdout
    rows = []
    for line in output.splitlines():
        parts = [part.strip() for part in line.split(",")]
        if len(parts) >= 3 and parts[0].isdigit():
            rows.append({"pid": int(parts[0]), "process": parts[1], "used_memory_mib": parts[2]})
    return rows


def get_json(path: str) -> dict[str, Any]:
    with urllib.request.urlopen(BASE_URL + path, timeout=15) as response:
        value = json.loads(response.read())
    if not isinstance(value, dict):
        raise RuntimeError(f"non-object response from {path}")
    return value


class ServerProcess:
    def __init__(self, *, profile: dict[str, Any], log_root: Path) -> None:
        self.profile = profile
        self.log_root = log_root
        self.process: subprocess.Popen[Any] | None = None
        self.stdout_handle: Any = None
        self.stderr_handle: Any = None

    def start(self) -> dict[str, Any]:
        if port_open():
            raise RuntimeError(f"port {PORT} is already open")
        existing = active_server_pids()
        if existing:
            raise RuntimeError(f"pre-existing llama-server processes: {existing}")
        self.log_root.mkdir(parents=True, exist_ok=False)
        stdout_path = self.log_root / "server.stdout.log"
        stderr_path = self.log_root / "server.stderr.log"
        self.stdout_handle = stdout_path.open("wb")
        self.stderr_handle = stderr_path.open("wb")
        arguments = [
            "-m", self.profile["model_path"],
            "--alias", self.profile["model_alias"],
            "--host", HOST,
            "--port", str(PORT),
            "--gpu-layers", "all",
            "--ctx-size", str(self.profile["server_ctx_size"]),
            "--parallel", "1",
            "--cache-type-k", self.profile["kv_cache"],
            "--cache-type-v", self.profile["kv_cache"],
            "--flash-attn", "on",
            "--no-context-shift",
            "--jinja",
            "--reasoning", "off",
            "--no-mmproj",
            "--verbose",
            "--metrics",
        ]
        creationflags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
        self.process = subprocess.Popen(
            [self.profile["server_path"], *arguments],
            cwd=self.log_root,
            stdout=self.stdout_handle,
            stderr=self.stderr_handle,
            creationflags=creationflags,
        )
        deadline = time.monotonic() + 300
        props = None
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(f"llama-server exited during startup: {self.process.returncode}")
            try:
                if get_json("/health").get("status") == "ok":
                    props = get_json("/props")
                    break
            except Exception:
                pass
            time.sleep(1)
        if props is None:
            raise TimeoutError("llama-server did not become ready")
        offload_deadline = time.monotonic() + 90
        offload = []
        while time.monotonic() < offload_deadline:
            self.stderr_handle.flush()
            text = stderr_path.read_text(encoding="utf-8", errors="replace")
            offload = [(int(a), int(b)) for a, b in re.findall(r"offloaded\s+(\d+)/(\d+)\s+layers\s+to\s+GPU", text, re.I)]
            if (66, 66) in offload:
                break
            time.sleep(0.5)
        gpu = gpu_processes()
        failures = []
        if props.get("model_alias") != self.profile["model_alias"]:
            failures.append("model_alias")
        if props.get("build_info") != "b10434-7e4c0a968":
            failures.append("runtime_build")
        if props.get("default_generation_settings", {}).get("n_ctx") != self.profile["context_tokens"]:
            failures.append("context")
        if (66, 66) not in offload:
            failures.append("gpu_offload")
        if not any(row["pid"] == self.process.pid for row in gpu):
            failures.append("pid_not_on_gpu")
        gate = {"schema_version": "capability-terrain-runtime-gate-v0", "passed": not failures, "failures": failures, "pid": self.process.pid, "props": props, "offload_matches": offload, "gpu_processes": gpu, "arguments": arguments}
        write_canonical_json(self.log_root / "RUNTIME_GATE.json", gate)
        if failures:
            raise RuntimeError(f"runtime gate failed: {failures}")
        return gate

    def stop(self) -> dict[str, Any]:
        errors = []
        pid = self.process.pid if self.process else None
        if self.process is not None and self.process.poll() is None:
            try:
                self.process.terminate()
                self.process.wait(timeout=30)
            except Exception as exc:
                errors.append(f"terminate:{type(exc).__name__}:{exc}")
                try:
                    self.process.kill()
                    self.process.wait(timeout=15)
                except Exception as kill_exc:
                    errors.append(f"kill:{type(kill_exc).__name__}:{kill_exc}")
        for handle in (self.stdout_handle, self.stderr_handle):
            if handle is not None:
                try:
                    handle.close()
                except Exception as exc:
                    errors.append(f"close:{type(exc).__name__}:{exc}")
        deadline = time.monotonic() + 20
        while port_open() and time.monotonic() < deadline:
            time.sleep(0.25)
        active = active_server_pids()
        gpu = gpu_processes()
        receipt = {"schema_version": "capability-terrain-runtime-release-v0", "pid": pid, "process_stopped": self.process is None or self.process.poll() is not None, "port_open_after": port_open(), "active_server_pids_after": active, "pid_on_gpu_after": any(row["pid"] == pid for row in gpu), "errors": errors}
        receipt["released"] = receipt["process_stopped"] and not receipt["port_open_after"] and pid not in active and not receipt["pid_on_gpu_after"] and not errors
        write_canonical_json(self.log_root / "RUNTIME_RELEASE.json", receipt)
        return receipt

    def __enter__(self) -> "ServerProcess":
        self.start()
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        release = self.stop()
        if exc is None and not release["released"]:
            raise RuntimeError("llama-server release failed")
