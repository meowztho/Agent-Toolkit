"""Retained local jobs for RORE-owned optional provider operations."""

from __future__ import annotations

import ctypes
import hashlib
import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .ghidra_adapter import MAX_RUN_SECONDS, analyze, probe
from .provider_setup import GHIDRA, JDK, default_root, install_ghidra, windows_x64

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
JOB_ID = re.compile(r"[0-9a-f]{32}\Z")
ADDRESS = re.compile(r"[A-Za-z0-9_:.]+\Z")


class ProviderJobError(ValueError):
    """A requested provider job or retained result is invalid."""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _jobs_root(path: str | Path | None) -> Path:
    return Path(path).expanduser().resolve(strict=False) if path else default_root().parent / "jobs"


def _write(path: Path, value: dict) -> None:
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)


def _start(request: dict, jobs_root: str | Path | None) -> dict:
    root = _jobs_root(jobs_root)
    root.mkdir(parents=True, exist_ok=True)
    job_id = uuid.uuid4().hex
    job_dir = root / job_id
    job_dir.mkdir(exist_ok=False)
    _write(job_dir / "request.json", request)
    _write(job_dir / "state.json", {"job_id": job_id, "kind": request["kind"],
                                    "status": "queued", "updated_at": _now()})
    command = [sys.executable, "-m", "rore_runtime.provider_jobs", "run", str(job_dir)]
    with (job_dir / "stdout.log").open("wb") as stdout, (job_dir / "stderr.log").open("wb") as stderr:
        try:
            process = subprocess.Popen(command, cwd=PACKAGE_ROOT, stdin=subprocess.DEVNULL,
                                       stdout=stdout, stderr=stderr,
                                       creationflags=(subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW)
                                       if os.name == "nt" else 0,
                                       start_new_session=os.name != "nt")
        except OSError as exc:
            _write(job_dir / "state.json", {"job_id": job_id, "kind": request["kind"],
                                            "status": "failed", "error": str(exc),
                                            "updated_at": _now()})
            raise ProviderJobError(f"provider job could not start: {exc}") from exc
    (job_dir / "pid.txt").write_text(str(process.pid), encoding="ascii")
    return {"job_id": job_id, "status": "started", "job_dir": str(job_dir),
            "pid": process.pid, "kind": request["kind"],
            "output": request.get("output")}


def start_install(*, root: str | Path | None = None, archives: str | Path | None = None,
                  jobs_root: str | Path | None = None) -> dict:
    """Start the existing verified Windows setup without blocking an MCP call."""
    if not windows_x64():
        raise ProviderJobError("automatic Ghidra setup is qualified only for Windows x64")
    provider_root = Path(root).expanduser().resolve(strict=False) if root else default_root()
    request = {"kind": "ghidra-install", "root": str(provider_root),
               "archives": str(Path(archives).resolve(strict=True)) if archives else None,
               "created_at": _now()}
    return _start(request, jobs_root)


def start_analysis(source: str | Path, output: str | Path, *, address: str | None = None,
                   timeout_seconds: int = 900, root: str | Path | None = None,
                   archives: str | Path | None = None, auto_install: bool = True,
                   jobs_root: str | Path | None = None) -> dict:
    """Start an isolated Ghidra import, installing the pinned provider if needed."""
    if type(timeout_seconds) is not int or not 30 <= timeout_seconds <= MAX_RUN_SECONDS:
        raise ProviderJobError(f"timeout must be 30..{MAX_RUN_SECONDS} seconds")
    if address is not None and (address.lower() == "none" or not ADDRESS.fullmatch(address)):
        raise ProviderJobError("address must be a Ghidra address token without whitespace or paths")
    target = Path(source).expanduser().resolve(strict=True)
    if not target.is_file():
        raise ProviderJobError("target must be a regular file")
    destination = Path(output).expanduser().resolve(strict=False)
    if destination.exists() or not destination.parent.is_dir():
        raise ProviderJobError("output must be a new directory inside an existing parent")
    provider_root = Path(root).expanduser().resolve(strict=False) if root else default_root()
    request = {"kind": "ghidra-analysis", "source": str(target), "output": str(destination),
               "address": address, "timeout_seconds": timeout_seconds,
               "root": str(provider_root), "archives": str(Path(archives).resolve(strict=True)) if archives else None,
               "auto_install": auto_install, "created_at": _now()}
    return _start(request, jobs_root)


def status(job_id: str, *, jobs_root: str | Path | None = None) -> dict:
    if not JOB_ID.fullmatch(job_id):
        raise ProviderJobError("job_id must be a RORE job identifier")
    job_dir = _jobs_root(jobs_root) / job_id
    state = json.loads((job_dir / "state.json").read_text(encoding="utf-8"))
    if state.get("job_id") != job_id:
        raise ProviderJobError("job state identity mismatch")
    state["job_dir"] = str(job_dir)
    state["pid"] = int((job_dir / "pid.txt").read_text(encoding="ascii")) if (job_dir / "pid.txt").is_file() else None
    if state["status"] in {"queued", "running"} and state["pid"] is not None and not _process_alive(state["pid"]):
        latest = json.loads((job_dir / "state.json").read_text(encoding="utf-8"))
        if latest.get("status") in {"queued", "running"}:
            state["retained_status"] = state["status"]
            state["status"] = "interrupted"
            state["error"] = "worker exited without a terminal result; inspect job logs and retained output"
        else:
            latest["job_dir"] = str(job_dir)
            latest["pid"] = state["pid"]
            state = latest
    return state


def _process_alive(pid: int) -> bool:
    if os.name == "nt":
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.OpenProcess.argtypes = (ctypes.c_ulong, ctypes.c_int, ctypes.c_ulong)
        kernel32.OpenProcess.restype = ctypes.c_void_p
        kernel32.GetExitCodeProcess.argtypes = (ctypes.c_void_p, ctypes.POINTER(ctypes.c_ulong))
        kernel32.GetExitCodeProcess.restype = ctypes.c_int
        kernel32.CloseHandle.argtypes = (ctypes.c_void_p,)
        handle = kernel32.OpenProcess(0x1000, 0, pid)
        if not handle:
            return False
        try:
            code = ctypes.c_ulong()
            return bool(kernel32.GetExitCodeProcess(handle, ctypes.byref(code)) and code.value == 259)
        finally:
            kernel32.CloseHandle(handle)
    try:
        os.kill(pid, 0)
        return True
    except PermissionError:
        return True
    except ProcessLookupError:
        return False


def _run(job_dir: Path) -> None:
    job_id = job_dir.name
    base = {"job_id": job_id, "kind": None}
    try:
        request = json.loads((job_dir / "request.json").read_text(encoding="utf-8"))
        base["kind"] = request["kind"]
        _write(job_dir / "state.json", {**base, "status": "running", "updated_at": _now()})
        if request["kind"] == "ghidra-install":
            result = install_ghidra(request["root"], request["archives"])
            _write(job_dir / "setup.json", result)
            final = {"status": result["status"], "result_path": str(job_dir / "setup.json")}
        elif request["kind"] == "ghidra-analysis":
            root = Path(request["root"])
            install = root / GHIDRA.directory
            jdk = root / JDK.directory
            try:
                probe(install, jdk)
            except (OSError, ValueError):
                if not request["auto_install"]:
                    raise
                install_ghidra(root, request["archives"])
            result = analyze(install, jdk, request["source"], request["output"],
                             address=request["address"], timeout_seconds=request["timeout_seconds"])
            final = {"status": result["status"], "result_path": str(Path(request["output"]) / "run.json"),
                     "output": request["output"]}
        else:
            raise ProviderJobError("unsupported provider job kind")
        _write(job_dir / "state.json", {**base, **final, "updated_at": _now()})
    except Exception as exc:
        _write(job_dir / "state.json", {**base, "status": "failed", "error": str(exc),
                                        "updated_at": _now()})


def analysis_page(output: str | Path, section: str, *, offset: int = 0, limit: int = 25) -> dict:
    """Page verified retained Ghidra export without truncating MCP responses."""
    if type(offset) is not int or type(limit) is not int or offset < 0 or not 1 <= limit <= 25:
        raise ProviderJobError("offset must be nonnegative and limit 1..25")
    run_dir = Path(output).expanduser().resolve(strict=True)
    run = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    if run.get("status") not in {"completed", "partial"} or not run.get("copy_integrity", {}).get("unchanged"):
        raise ProviderJobError("Ghidra run has no qualified retained analysis")
    analysis_file = run_dir / "analysis.json"
    expected = run.get("output_files", {}).get("analysis.json", {}).get("sha256")
    if not expected or hashlib.sha256(analysis_file.read_bytes()).hexdigest() != expected:
        raise ProviderJobError("retained analysis hash differs from run manifest")
    analysis = json.loads(analysis_file.read_text(encoding="utf-8"))
    if analysis.get("schema_version") != 1 or analysis.get("provider") != "ghidra-headless":
        raise ProviderJobError("retained analysis schema/provider mismatch")
    base = {"status": run["status"], "output": str(run_dir), "section": section,
            "import_verified": run.get("import_identity", {}).get("verified", False),
            "auto_analysis_timed_out": run.get("auto_analysis_timed_out")}
    if section == "run":
        return {**base, "value": {key: run.get(key) for key in (
            "schema_version", "provider", "source", "copied_input", "requested_address",
            "timeout_seconds", "status", "exit_code", "output_files", "import_identity",
            "coverage", "copy_integrity", "auto_analysis_timed_out", "warnings")}}
    if section == "program":
        return {**base, "value": analysis["program"]}
    if section == "selected_function":
        selected = dict(analysis.get("selected_function") or {})
        for key in ("instructions", "references", "calling_functions", "called_functions"):
            if key in selected:
                value = selected.pop(key)
                selected[f"{key}_count"] = value.get("total") if isinstance(value, dict) else len(value)
        return {**base, "value": selected}
    if section in {"references", "instructions", "calling_functions", "called_functions"}:
        inventory = (analysis.get("selected_function") or {}).get(section)
    elif section in {"functions", "strings", "external_symbols", "external_entry_points", "memory_blocks"}:
        inventory = analysis.get(section)
    else:
        raise ProviderJobError("unknown Ghidra result section")
    if inventory is None:
        raise ProviderJobError("requested section was not exported")
    items = inventory if isinstance(inventory, list) else inventory["items"]
    total = len(items) if isinstance(inventory, list) else inventory["total"]
    emitted = len(items) if isinstance(inventory, list) else inventory["emitted"]
    complete = True if isinstance(inventory, list) else inventory["complete"]
    end = min(offset + limit, len(items))
    return {**base, "total": total, "emitted": emitted, "complete": complete,
            "offset": offset, "next_offset": end if end < len(items) else None,
            "items": items[offset:end]}


def decompilation_page(output: str | Path, *, offset: int = 0, characters: int = 12000) -> dict:
    """Read a hash-checked slice of the selected function's retained pseudocode."""
    if type(offset) is not int or type(characters) is not int or offset < 0 or not 1 <= characters <= 12000:
        raise ProviderJobError("offset must be nonnegative and characters 1..12000")
    run_dir = Path(output).expanduser().resolve(strict=True)
    run = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    if run.get("status") not in {"completed", "partial"} or not run.get("copy_integrity", {}).get("unchanged"):
        raise ProviderJobError("Ghidra run has no qualified retained decompilation")
    expected = run.get("output_files", {}).get("decompile.c", {}).get("sha256")
    if not expected:
        raise ProviderJobError("selected function has no retained decompilation")
    path = run_dir / "decompile.c"
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ProviderJobError("retained decompilation hash differs from run manifest")
    content = raw.decode("utf-8")
    end = min(offset + characters, len(content))
    return {"status": run["status"], "output": str(run_dir), "sha256": expected,
            "import_verified": run.get("import_identity", {}).get("verified", False),
            "total_characters": len(content), "offset": offset,
            "next_offset": end if end < len(content) else None, "text": content[offset:end]}


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "run" or not JOB_ID.fullmatch(Path(sys.argv[2]).name):
        raise SystemExit("usage: python -m rore_runtime.provider_jobs run JOB_DIRECTORY")
    _run(Path(sys.argv[2]))
