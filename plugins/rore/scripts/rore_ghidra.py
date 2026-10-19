#!/usr/bin/env python3
"""Optional, target-copying Ghidra headless provider CLI for RORE Reconstruction."""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rore_runtime.ghidra_adapter import GhidraError, analyze, probe


def main(argv=None):
    parser = argparse.ArgumentParser(prog="rore-ghidra", description="Qualify or run an installed Ghidra headless provider")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("probe", "analyze"):
        command = sub.add_parser(name)
        command.add_argument("--install", required=True, help="Ghidra distribution root")
        command.add_argument("--jdk", required=True, help="compatible JDK root")
        if name == "analyze":
            command.add_argument("--source", required=True, help="authorized regular file")
            command.add_argument("--output", required=True, help="new run directory")
            command.add_argument("--address", help="optional Ghidra address to decompile")
            command.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args(argv)
    try:
        result = (probe(args.install, args.jdk) if args.command == "probe" else
                  analyze(args.install, args.jdk, args.source, args.output,
                          address=args.address, timeout_seconds=args.timeout))
    except (GhidraError, OSError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] in ("components-qualified-not-target-tested", "completed") else 1


if __name__ == "__main__":
    raise SystemExit(main())
