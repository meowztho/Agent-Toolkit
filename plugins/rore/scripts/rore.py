#!/usr/bin/env python3
"""RORE Evidence and read-only artifact CLI. External analyzers are not launched here."""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rore_runtime.bundle import (BundleError, capture_evidence, compare, export_bundle,
                                 import_bundle, init_bundle, inspect, validate)
from rore_runtime.rea_bridge import import_rea, inspect_rea_original, preview_rea
from rore_runtime.artifact_tools import (ArtifactError, capabilities, inspect_file,
                                         inventory_directory, inventory_zip, read_file_bytes, read_zip_member)
from rore_runtime.binary_layout import inspect_binary_layout, map_file_offset


def main(argv=None):
    parser = argparse.ArgumentParser(prog="rore", description="Inspect RORE Evidence bundles and local artifacts")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, arguments in {
        "validate": ("bundle",), "inspect": ("bundle", "record_id"),
        "compare": ("left", "right"), "export": ("bundle", "output"),
        "import": ("source", "destination"),
        "rea-preview": ("source",), "rea-import": ("source", "destination"),
        "rea-record": ("bundle", "record_id"),
    }.items():
        command = sub.add_parser(name)
        for argument in arguments:
            command.add_argument(argument)
    bundle_init = sub.add_parser("bundle-init", help="Create a new empty Evidence bundle")
    bundle_init.add_argument("destination")
    bundle_init.add_argument("identity")
    bundle_init.add_argument("--environment", default="")
    evidence_add = sub.add_parser("evidence-add", help="Append one Evidence record and retain complete raw files")
    evidence_add.add_argument("bundle")
    evidence_add.add_argument("record_id")
    evidence_add.add_argument("source")
    evidence_add.add_argument("method")
    evidence_add.add_argument("files", nargs="+")
    sub.add_parser("capabilities")
    file_inspect = sub.add_parser("file-inspect", help="Hash and identify one regular file without executing it")
    file_inspect.add_argument("path")
    file_bytes = sub.add_parser("file-bytes", help="Read an exact file-offset window")
    file_bytes.add_argument("path")
    file_bytes.add_argument("offset", type=int)
    file_bytes.add_argument("length", type=int)
    zip_inventory = sub.add_parser("zip-inventory", help="Page through ZIP metadata without extraction")
    zip_inventory.add_argument("path")
    zip_inventory.add_argument("--offset", type=int, default=0)
    zip_inventory.add_argument("--limit", type=int, default=200)
    zip_member = sub.add_parser("zip-member", help="Read exact decoded bytes from a ZIP member by index")
    zip_member.add_argument("path")
    zip_member.add_argument("index", type=int)
    zip_member.add_argument("offset", type=int)
    zip_member.add_argument("length", type=int)
    binary_layout = sub.add_parser("binary-layout", help="Inspect declared PE/ELF file layout")
    binary_layout.add_argument("path")
    file_map = sub.add_parser("map-file-offset", help="Map a file offset to candidate declared addresses")
    file_map.add_argument("path")
    file_map.add_argument("offset", type=int)
    directory_inventory = sub.add_parser("directory-inventory", help="Page through live directory metadata without following links")
    directory_inventory.add_argument("path")
    directory_inventory.add_argument("--offset", type=int, default=0)
    directory_inventory.add_argument("--limit", type=int, default=200)
    args = parser.parse_args(argv)
    try:
        result = {
            "bundle-init": lambda: init_bundle(args.destination, args.identity, args.environment),
            "evidence-add": lambda: capture_evidence(args.bundle, args.record_id, args.source, args.method, args.files),
            "validate": lambda: validate(args.bundle),
            "inspect": lambda: inspect(args.bundle, args.record_id),
            "compare": lambda: compare(args.left, args.right),
            "export": lambda: export_bundle(args.bundle, args.output),
            "import": lambda: import_bundle(args.source, args.destination),
            "rea-preview": lambda: preview_rea(args.source),
            "rea-import": lambda: import_rea(args.source, args.destination),
            "rea-record": lambda: inspect_rea_original(args.bundle, args.record_id),
            "capabilities": capabilities,
            "file-inspect": lambda: inspect_file(args.path),
            "file-bytes": lambda: read_file_bytes(args.path, args.offset, args.length),
            "zip-inventory": lambda: inventory_zip(args.path, args.offset, args.limit),
            "zip-member": lambda: read_zip_member(args.path, args.index, args.offset, args.length),
            "binary-layout": lambda: inspect_binary_layout(args.path),
            "map-file-offset": lambda: map_file_offset(args.path, args.offset),
            "directory-inventory": lambda: inventory_directory(args.path, args.offset, args.limit),
        }[args.command]()
    except (BundleError, ArtifactError, OSError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
