# RORE native artifact acquisition

The Python standard-library core in `rore_runtime/artifact_tools.py` and `binary_layout.py` implements bounded, read-only observations. CLI and MCP call the same functions. These operations supply Evidence candidates; they do not decompile, execute, unlock, validate a complete file format or prove runtime behavior. No REA, tool-master or Ghidra source package is required.

Run `python scripts/rore.py capabilities` for the implemented operation list and current limits. The `mcp.json` server exposes read-only equivalents with `rore_` prefixes. Use the CLI when the MCP response budget is exceeded; neither path silently truncates a result.

| CLI operation | Observation and boundary |
| --- | --- |
| `file-inspect PATH` | Full SHA-256, size, and a leading-signature format candidate for one regular file. |
| `file-bytes PATH OFFSET LENGTH` | Exact file-offset hex/ASCII window and source hash. No address inference. |
| `zip-inventory PATH [--offset N --limit N]` | Indexed central-directory metadata pages, including duplicate names and path/symlink flags. No payload validation or extraction. |
| `zip-member PATH INDEX OFFSET LENGTH` | Exact decoded member window, full member/source hashes and CRC check. Member offset is independent of archive file offset. |
| `directory-inventory PATH [--offset N --limit N]` | Paged live metadata for a bounded tree without traversing symlinks/reparse points. This is not an atomic snapshot or file-byte identity. |
| `binary-layout PATH` | Declared PE sections or ELF `PT_LOAD` segments, backed-range flags and format properties. PE output also lists overlapping declared raw ranges, zero-raw sections and unbacked ranges; these are header observations, not loader decisions. |
| `map-file-offset PATH OFFSET` | All candidate declared PE RVAs/preferred VAs or ELF link-time addresses for a source file offset. These are not live process addresses. |

Limits currently are a 1 GiB source, a 4 KiB byte window, 64 MiB decoded ZIP member, 100,000 ZIP or directory entries and a 200-entry page. Over-limit, unsupported, incomplete or changed sources fail explicitly. Each file observation hashes the opened source before and after the projection and checks metadata; a mutable live tree has a weaker coverage claim. An adversarial writer with an exact ABA mutation can evade this observational check; take a controlled immutable copy when fixity is critical.

Record the returned source hash and coordinate space in an Evidence record before interpreting bytes. For section-relative or runtime addresses, add a proven loader/module mapping. A declared layout does not establish that a loader selected the file, how it relocated it, or whether a byte was executed. For xrefs, control flow, disassembly, decompilation, assets inside non-ZIP containers, process memory, network and live causality, route by the missing capability through `rore-orchestration`; use `GHIDRA_STATIC_PROVIDER.md` only when Ghidra is the selected available native-code provider.
