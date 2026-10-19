#!/usr/bin/env python3
"""Inspect or explicitly provision optional RORE analysis capabilities."""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rore_runtime.provider_setup import SetupError, doctor, install_ghidra, plan


def main(argv=None):
    parser = argparse.ArgumentParser(prog="rore-setup", description="On-demand provider setup; never runs a target")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("doctor", "plan-ghidra", "install-ghidra"):
        command = sub.add_parser(name)
        command.add_argument("--root", help="user-scoped provider directory")
        if name != "doctor":
            command.add_argument("--archives", help="directory containing the exact pinned ZIPs; avoids downloads")
    args = parser.parse_args(argv)
    try:
        if args.command == "doctor":
            result = doctor(args.root)
        elif args.command == "plan-ghidra":
            result = plan(args.root, args.archives)
        else:
            result = install_ghidra(args.root, args.archives)
    except (SetupError, OSError, ValueError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
