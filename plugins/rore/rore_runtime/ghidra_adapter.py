"""Optional Ghidra headless provider. Its output is derived evidence, not Reference Truth."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from .artifact_tools import ArtifactError, _with_file

SCRIPT = Path(__file__).resolve().parents[1] / "providers" / "ghidra" / "ROREExport.java"
MAX_RUN_SECONDS = 3600


class GhidraError(ValueError):
    """The selected provider or its run did not meet the declared boundary."""


def _hash(path: Path, algorithm: str = "sha256") -> str:
    digest = hashlib.new(algorithm)
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _properties(path: Path) -> dict[str, str]:
    result = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            result[key.strip()] = value.strip()
    return result


def probe(install: str | Path, jdk: str | Path) -> dict:
    """Qualify a specific local installation without touching a target."""
    install_path = Path(install).resolve(strict=True)
    jdk_path = Path(jdk).resolve(strict=True)
    if not install_path.is_dir() or not jdk_path.is_dir():
        raise GhidraError("Ghidra installation and JDK must be directories")
    headless = install_path / "support" / ("analyzeHeadless.bat" if os.name == "nt" else "analyzeHeadless")
    java = jdk_path / "bin" / ("java.exe" if os.name == "nt" else "java")
    properties_file = install_path / "Ghidra" / "application.properties"
    for path in (headless, java, properties_file, SCRIPT):
        if not path.is_file():
            raise GhidraError(f"required provider component missing: {path}")
    properties = _properties(properties_file)
    minimum = properties.get("application.java.min")
    try:
        java_run = subprocess.run([str(java), "-version"], capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GhidraError(f"JDK version check failed: {exc}") from exc
    version_output = (java_run.stderr + java_run.stdout).strip()
    match = re.search(r'\bversion\s+"(\d+)(?:\.|\")', version_output)
    if java_run.returncode or not match:
        raise GhidraError(f"JDK version could not be established: {version_output[:300]}")
    java_major = int(match.group(1))
    if minimum is None or not minimum.isdigit() or java_major < int(minimum):
        raise GhidraError(f"Ghidra requires JDK {minimum or 'unknown'}; selected JDK is {java_major}")
    return {"provider": "ghidra-headless", "status": "components-qualified-not-target-tested",
            "install": str(install_path), "headless": str(headless),
            "headless_sha256": _hash(headless), "application_properties_sha256": _hash(properties_file),
            "ghidra_version": properties.get("application.version"),
            "ghidra_release": properties.get("application.release.name"),
            "minimum_java": int(minimum), "jdk": str(jdk_path), "java_sha256": _hash(java),
            "java_version": version_output.splitlines()[0],
            "script": str(SCRIPT), "script_sha256": _hash(SCRIPT)}


def _snapshot(source: Path, destination: Path) -> dict:
    def copy(stream, identity):
        with destination.open("xb") as output:
            shutil.copyfileobj(stream, output, length=1024 * 1024)
        if _hash(destination) != identity["sha256"]:
            raise ArtifactError("copied target bytes differ from inspected source")
        return identity
    return _with_file(source, copy)


def _stop_tree(process: subprocess.Popen) -> None:
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                       capture_output=True, timeout=15)
    else:
        os.killpg(process.pid, signal.SIGKILL)


def analyze(install: str | Path, jdk: str | Path, source: str | Path,
            output: str | Path, *, address: str | None = None,
            timeout_seconds: int = 900) -> dict:
    """Import an immutable target copy into a new isolated project and retain raw outputs."""
    if type(timeout_seconds) is not int or not 30 <= timeout_seconds <= MAX_RUN_SECONDS:
        raise GhidraError(f"timeout must be 30..{MAX_RUN_SECONDS} seconds")
    if address is not None and (address.lower() == "none" or not re.fullmatch(r"[A-Za-z0-9_:.]+", address)):
        raise GhidraError("address must be a Ghidra address token without whitespace or paths")
    selected = probe(install, jdk)
    target = Path(source).absolute()
    if not target.is_file():
        raise GhidraError("target must be a regular file")
    out = Path(output).resolve(strict=False)
    out.mkdir(parents=False, exist_ok=False)
    (out / "input").mkdir()
    (out / "project").mkdir()
    (out / "config").mkdir()
    (out / "cache").mkdir()
    copied = out / "input" / target.name
    started_at = datetime.now(timezone.utc).isoformat()
    run = {"schema_version": 1, "provider": selected, "started_at": started_at,
           "requested_address": address, "timeout_seconds": timeout_seconds,
           "status": "preparing", "source": None, "copied_input": str(copied),
           "command": None, "exit_code": None, "output_files": {}}
    try:
        run["source"] = _snapshot(target, copied)
        command = [selected["headless"], str(out / "project"), "ROREAnalysis",
                   "-import", str(copied), "-scriptPath", str(SCRIPT.parent),
                   "-postScript", SCRIPT.name, str(out / "analysis.json"), address or "none",
                   "-analysisTimeoutPerFile", str(min(timeout_seconds - 10, 600)),
                   "-librarySearchPaths", str(out / "input"),
                   "-log", str(out / "ghidra.log"), "-scriptlog", str(out / "script.log")]
        run["command"] = command
        env = os.environ.copy()
        env["JAVA_HOME"] = selected["jdk"]
        env["PATH"] = str(Path(selected["jdk"]) / "bin") + os.pathsep + env.get("PATH", "")
        env["XDG_CONFIG_HOME"] = str(out / "config")
        env["XDG_CACHE_HOME"] = str(out / "cache")
        run["status"] = "running"
        with (out / "stdout.log").open("wb") as stdout, (out / "stderr.log").open("wb") as stderr:
            process = subprocess.Popen(command, cwd=out, env=env, stdin=subprocess.DEVNULL,
                                       stdout=stdout, stderr=stderr,
                                       creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
                                       start_new_session=os.name != "nt")
            try:
                run["exit_code"] = process.wait(timeout=timeout_seconds)
            except subprocess.TimeoutExpired:
                _stop_tree(process)
                process.wait(timeout=15)
                run["status"] = "timeout"
        if run["status"] != "timeout":
            if run["exit_code"] == 0 and (out / "analysis.json").is_file():
                analysis = json.loads((out / "analysis.json").read_text(encoding="utf-8"))
                if (not isinstance(analysis, dict) or analysis.get("schema_version") != 1
                        or analysis.get("provider") != "ghidra-headless"):
                    raise GhidraError("Ghidra export schema/provider identity mismatch")
                if type(analysis.get("auto_analysis_timed_out")) is not bool:
                    raise GhidraError("Ghidra export has no auto-analysis timeout status")
                imported_md5 = analysis.get("program", {}).get("executable_md5")
                copied_md5 = _hash(copied, "md5")
                run["import_identity"] = {"copied_input_md5": copied_md5,
                                          "provider_executable_md5": imported_md5,
                                          "verified": imported_md5 == copied_md5}
                if imported_md5 and imported_md5 != copied_md5:
                    raise GhidraError("provider imported bytes do not match the copied target")
                run["status"] = "completed" if imported_md5 and not analysis.get("auto_analysis_timed_out") else "partial"
                run["coverage"] = {key: {"total": analysis[key]["total"],
                                          "emitted": analysis[key]["emitted"],
                                          "complete": analysis[key]["complete"]}
                                   for key in ("functions", "strings", "external_symbols", "external_entry_points")}
                run["auto_analysis_timed_out"] = analysis.get("auto_analysis_timed_out")
                if address is not None and "selected_function" not in analysis:
                    raise GhidraError("Ghidra export omitted the requested function selection")
                if "selected_function" in analysis:
                    run["selected_function"] = analysis["selected_function"]
                    if address is not None and analysis["selected_function"].get("requested_address") != address:
                        raise GhidraError("Ghidra export returned a different requested address")
                    if "function_entry" in analysis["selected_function"]:
                        refs = analysis["selected_function"].get("references")
                        if (not isinstance(refs, dict) or type(refs.get("total")) is not int
                                or type(refs.get("emitted")) is not int
                                or type(refs.get("complete")) is not bool
                                or not isinstance(refs.get("items"), list)
                                or not 0 <= refs["emitted"] <= refs["total"]
                                or refs["emitted"] != len(refs["items"])
                                or refs["complete"] != (refs["total"] == refs["emitted"])):
                            raise GhidraError("Ghidra selected function has no valid reference inventory")
                        if not refs["complete"]:
                            run["status"] = "partial"
                    if analysis["selected_function"].get("status") != "decompiled":
                        run["status"] = "partial"
                    elif (analysis["selected_function"].get("output_file") != "decompile.c"
                          or not (out / "decompile.c").is_file()):
                        raise GhidraError("Ghidra reported decompilation without its output file")
                    if (analysis["selected_function"].get("status") == "decompiled"
                            and "instructions" not in analysis["selected_function"]):
                        raise GhidraError("Ghidra reported decompilation without an instruction inventory")
                    if ("instructions" in analysis["selected_function"]
                            and not analysis["selected_function"]["instructions"].get("complete")):
                        run["status"] = "partial"
            else:
                run["status"] = "provider_failed"
    except (ArtifactError, OSError, ValueError, KeyError, TypeError, AttributeError,
            subprocess.SubprocessError) as exc:
        run["status"] = "failed"
        run["error"] = str(exc)
    finally:
        run["finished_at"] = datetime.now(timezone.utc).isoformat()
        if run["source"] is not None:
            try:
                copied_sha256 = _hash(copied)
                unchanged = copied_sha256 == run["source"]["sha256"]
                run["copy_integrity"] = {"sha256_after": copied_sha256, "unchanged": unchanged}
                if not unchanged:
                    run["status"] = "failed"
                    run["error"] = "copied target bytes changed during provider run"
            except OSError as exc:
                run["status"] = "failed"
                run["error"] = f"copied target could not be verified after provider run: {exc}"
        for name in ("analysis.json", "decompile.c", "stdout.log", "stderr.log", "ghidra.log", "script.log"):
            path = out / name
            if path.is_file():
                run["output_files"][name] = {"sha256": _hash(path), "size": path.stat().st_size}
        (out / "run.json").write_text(json.dumps(run, indent=2, ensure_ascii=False), encoding="utf-8")
    return run
