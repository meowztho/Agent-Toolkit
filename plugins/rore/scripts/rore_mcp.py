#!/usr/bin/env python3
"""Read-only MCP adapter over RORE Evidence and artifact operations."""

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mcp.server import MCPServer
from mcp.types import ToolAnnotations

from rore_runtime.bundle import compare, inspect, validate
from rore_runtime.rea_bridge import inspect_rea_original, preview_rea
from rore_runtime.artifact_tools import capabilities, inspect_file, inventory_directory, inventory_zip, read_file_bytes, read_zip_member
from rore_runtime.binary_layout import inspect_binary_layout, map_file_offset

mcp = MCPServer("RORE Analysis", version="0.16.1")
READ_ONLY = ToolAnnotations(readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)
MAX_RESPONSE_BYTES = 256 * 1024


def _bounded(result: dict[str, Any]) -> dict[str, Any]:
    if len(json.dumps(result, ensure_ascii=False).encode("utf-8")) > MAX_RESPONSE_BYTES:
        raise ValueError("Complete result exceeds the MCP response budget; use the CLI on the same bundle. No data was truncated.")
    return result


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_validate_bundle(bundle: str) -> dict[str, Any]:
    """Validate a local RORE bundle's links and raw-file hashes without changing it."""
    return _bounded(validate(bundle))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_inspect_record(bundle: str, record_id: str) -> dict[str, Any]:
    """Read one Evidence, Finding, Path, Model or Unknown record from a valid bundle."""
    return _bounded(inspect(bundle, record_id))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_compare_bundles(left: str, right: str) -> dict[str, Any]:
    """Compare two valid bundles by target, record IDs and every file hash."""
    return _bounded(compare(left, right))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_preview_rea_export(source: str) -> dict[str, Any]:
    """Inspect a REA Evidence JSON export's shape, hash and subject identities without importing it."""
    return _bounded(preview_rea(source))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_inspect_rea_original(bundle: str, record_id: str) -> dict[str, Any]:
    """Read one original REA record from a validated, imported RORE bundle."""
    return _bounded(inspect_rea_original(bundle, record_id))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_capabilities() -> dict[str, Any]:
    """List implemented RORE artifact operations and their evidence boundaries."""
    return _bounded(capabilities())


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_file_inspect(path: str) -> dict[str, Any]:
    """Hash a local regular file and identify only observed leading signatures."""
    return _bounded(inspect_file(path))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_file_bytes(path: str, offset: int, length: int) -> dict[str, Any]:
    """Read exact file-offset bytes with a full source hash; no VA mapping is inferred."""
    return _bounded(read_file_bytes(path, offset, length))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_zip_inventory(path: str, offset: int = 0, limit: int = 200) -> dict[str, Any]:
    """Read a page of ZIP central-directory metadata without extraction."""
    return _bounded(inventory_zip(path, offset, limit))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_zip_member(path: str, index: int, offset: int, length: int) -> dict[str, Any]:
    """Hash and read exact decoded bytes of one ZIP member by central-directory index."""
    return _bounded(read_zip_member(path, index, offset, length))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_binary_layout(path: str) -> dict[str, Any]:
    """Inspect PE sections or ELF load segments as declared file layout."""
    return _bounded(inspect_binary_layout(path))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_map_file_offset(path: str, offset: int) -> dict[str, Any]:
    """Map a file offset to candidate declared addresses, never live runtime VAs."""
    return _bounded(map_file_offset(path, offset))


@mcp.tool(annotations=READ_ONLY, structured_output=True)
def rore_directory_inventory(path: str, offset: int = 0, limit: int = 200) -> dict[str, Any]:
    """Page through live directory metadata without following symlinks or junctions."""
    return _bounded(inventory_directory(path, offset, limit))


if __name__ == "__main__":
    mcp.run()
