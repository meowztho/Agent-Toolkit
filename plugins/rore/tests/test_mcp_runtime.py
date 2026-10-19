import asyncio
import importlib.util
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from test_evidence_bundle_runtime import make_bundle
from rore_runtime.rea_bridge import import_rea


@unittest.skipUnless(importlib.util.find_spec("mcp"), "optional MCP SDK is not installed")
class McpRuntimeTests(unittest.TestCase):
    def test_provider_stdio_discovery_and_read_only_plan(self):
        from mcp import Client, StdioServerParameters

        async def exercise(root: Path):
            project = Path(__file__).resolve().parents[1]
            config = json.loads((project / "mcp.json").read_text(encoding="utf-8"))["mcpServers"]["rore-providers"]
            params = StdioServerParameters(
                command=config["command"],
                args=[argument.replace("${PLUGIN_ROOT}", str(project)) for argument in config["args"]],
                cwd=str(project),
            )
            async with Client(params, raise_exceptions=True) as client:
                listed = await client.list_tools()
                names = {tool.name for tool in listed.tools}
                self.assertEqual(names, {"rore_provider_doctor", "rore_provider_plan_ghidra",
                                         "rore_provider_start_ghidra_install",
                                         "rore_provider_start_ghidra_analysis",
                                         "rore_provider_job_status", "rore_provider_ghidra_page",
                                         "rore_provider_decompilation_page"})
                planned = await client.call_tool("rore_provider_plan_ghidra", {"root": str(root)})
                self.assertFalse(planned.is_error)
                self.assertEqual(len(planned.structured_content["artifacts"]), 2)
                self.assertFalse(root.exists())

        with tempfile.TemporaryDirectory() as temp:
            asyncio.run(exercise(Path(temp) / "providers"))

    def test_stdio_tool_discovery_and_read_only_call(self):
        from mcp import Client, StdioServerParameters

        async def exercise(bundle: Path, rea_source: Path, imported_rea: Path, archive: Path):
            root = Path(__file__).resolve().parents[1]
            config = json.loads((root / "mcp.json").read_text(encoding="utf-8"))["mcpServers"]["rore-evidence"]
            params = StdioServerParameters(
                command=config["command"],
                args=[argument.replace("${PLUGIN_ROOT}", str(root)) for argument in config["args"]],
                cwd=str(root),
            )
            async with Client(params, raise_exceptions=True) as client:
                listed = await client.list_tools()
                names = {tool.name for tool in listed.tools}
                self.assertEqual(names, {"rore_validate_bundle", "rore_inspect_record", "rore_compare_bundles",
                                         "rore_preview_rea_export", "rore_inspect_rea_original", "rore_capabilities",
                                         "rore_file_inspect", "rore_file_bytes", "rore_zip_inventory", "rore_zip_member",
                                         "rore_binary_layout", "rore_map_file_offset", "rore_directory_inventory"})
                result = await client.call_tool("rore_validate_bundle", {"bundle": str(bundle)})
                self.assertFalse(result.is_error)
                self.assertEqual(result.structured_content["counts"]["evidence"], 1)
                found = await client.call_tool("rore_inspect_record", {"bundle": str(bundle), "record_id": "E-001"})
                self.assertEqual(found.structured_content["record"]["id"], "E-001")
                preview = await client.call_tool("rore_preview_rea_export", {"source": str(rea_source)})
                self.assertEqual(preview.structured_content["counts"]["records"], 1)
                original = await client.call_tool("rore_inspect_rea_original", {"bundle": str(imported_rea), "record_id": "ev_test"})
                self.assertEqual(original.structured_content["record"]["normalized_result"], {"value": 42})
                file_bytes = await client.call_tool("rore_file_bytes", {"path": str(bundle / "raw/sample.bin"), "offset": 0, "length": 2})
                self.assertEqual(file_bytes.structured_content["bytes"]["hex"], "00ff")
                inventory = await client.call_tool("rore_zip_inventory", {"path": str(archive)})
                self.assertEqual(inventory.structured_content["total_members"], 1)
                member = await client.call_tool("rore_zip_member", {"path": str(archive), "index": 0, "offset": 0, "length": 3})
                self.assertEqual(member.structured_content["bytes"]["ascii"], "abc")
                directory = await client.call_tool("rore_directory_inventory", {"path": str(bundle), "limit": 2})
                self.assertGreaterEqual(directory.structured_content["total_entries"], 2)

        with tempfile.TemporaryDirectory() as temp:
            bundle = Path(temp) / "bundle"
            make_bundle(bundle)
            rea_source = Path(temp) / "rea.json"
            rea_source.write_text(json.dumps({
                **{key: [] for key in ("artifacts", "providers", "environments", "scenarios", "captures", "unknowns")},
                "records": [{"evidence_id": "ev_test", "operation": "observe", "normalized_result": {"value": 42}}],
            }), encoding="utf-8")
            imported_rea = Path(temp) / "rea-imported"
            import_rea(rea_source, imported_rea)
            archive = Path(temp) / "sample.zip"
            with zipfile.ZipFile(archive, "w") as output:
                output.writestr("asset.bin", b"abc")
            asyncio.run(exercise(bundle, rea_source, imported_rea, archive))


if __name__ == "__main__":
    unittest.main()
