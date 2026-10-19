#!/usr/bin/env python3
"""Optional RORE-owned provider MCP; setup and analysis are explicit jobs."""

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mcp.server import MCPServer
from mcp.types import ToolAnnotations

from rore_runtime.provider_jobs import analysis_page, decompilation_page, start_analysis, start_install, status
from rore_runtime.provider_setup import doctor, plan

mcp = MCPServer("RORE Providers", version="0.16.1")
READ_ONLY = ToolAnnotations(readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)
START_JOB = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True)
MAX_RESPONSE_BYTES = 256 * 1024


def _bounded(result: dict[str, Any]) -> dict[str, Any]:
    if len(json.dumps(result, ensure_ascii=False).encode("utf-8")) > MAX_RESPONSE_BYTES:
        raise ValueError("Result exceeds MCP response budget; use a smaller page or retained files. No data was truncated.")
    return result


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_provider_doctor(root: str | None = None) -> dict[str, Any]:
    """Inspect local provider candidates and the exact Ghidra/JDK qualification state."""
    return _bounded(doctor(root))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_provider_plan_ghidra(root: str | None = None, archives: str | None = None) -> dict[str, Any]:
    """Show the verified Windows x64 Ghidra/JDK acquisition inputs and effects."""
    return _bounded(plan(root, archives))


@mcp.tool(annotations=START_JOB, structured_output=True)
def rore_provider_start_ghidra_install(root: str | None = None, archives: str | None = None) -> dict[str, Any]:
    """Start optional user-scoped Ghidra/JDK installation; poll the returned job ID."""
    return _bounded(start_install(root=root, archives=archives))


@mcp.tool(annotations=START_JOB, structured_output=True)
def rore_provider_start_ghidra_analysis(source: str, output: str, address: str | None = None,
                                       timeout_seconds: int = 900, root: str | None = None,
                                       archives: str | None = None, auto_install: bool = True) -> dict[str, Any]:
    """Analyze an exact target copy in a new directory; install Ghidra on demand if absent."""
    return _bounded(start_analysis(source, output, address=address, timeout_seconds=timeout_seconds,
                                   root=root, archives=archives, auto_install=auto_install))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_provider_job_status(job_id: str) -> dict[str, Any]:
    """Read a provider job's retained status, setup result or analysis run path."""
    return _bounded(status(job_id))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_provider_ghidra_page(output: str, section: str, offset: int = 0, limit: int = 25) -> dict[str, Any]:
    """Page a hash-checked Ghidra run summary, program, inventory or selected references."""
    return _bounded(analysis_page(output, section, offset=offset, limit=limit))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_provider_decompilation_page(output: str, offset: int = 0, characters: int = 12000) -> dict[str, Any]:
    """Page hash-checked pseudocode from a selected function, without hiding truncation."""
    return _bounded(decompilation_page(output, offset=offset, characters=characters))


if __name__ == "__main__":
    mcp.run()
