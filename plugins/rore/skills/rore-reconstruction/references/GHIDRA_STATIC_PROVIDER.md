# Ghidra as a conditional native-code provider

Read this only when the active question needs loader-aware disassembly, symbols, references, function graphs, decompilation or program-memory inspection and an actual Ghidra installation is available or being evaluated. Ghidra is a provider beneath RORE Reconstruction, never a required owner or proof source by itself. For byte windows and declared PE/ELF layout, use RORE's native artifact operations first when they answer the question.

RORE's optional, executable headless adapter is specified in `docs/GHIDRA_PROVIDER_ADAPTER.md`. Qualify the installed provider with `scripts/rore_ghidra.py probe`; `analyze` retains the copied input, isolated project, raw export and logs. The adapter is a bounded acquisition path, not an automatic Reference Truth verdict.

If Ghidra is needed but absent on Windows x64, the user-requested acquisition route is `docs/PROVIDER_SETUP.md` and `PROVIDER_PROVISIONING.md`; installation never follows from reading this method alone.

## Qualify the provider and target

1. Bind the exact target copy/build to a full hash. Record Ghidra version/build, host, loader, language/processor, compiler specification, image base, analysis options and timeout. A source archive or script name is not an installed runnable provider.
2. Start in an isolated local project/scratch directory. `analyzeHeadless` imports or processes programs and may write its project; `-readOnly` and `-deleteProject` affect project persistence, not the original target's broader runtime effects. Avoid a shared server project or broad recursive import unless explicitly intended. Preserve stdout, stderr, log, script log, exit/cancellation and project/output artifacts before cleanup.
3. Confirm what was imported: original file identity, selected loader, loaded program names/count, memory blocks, file-backed ranges, overlays and import warnings. Container imports may expand into several programs. A successful import or auto-analysis is not a complete or correct interpretation.
4. Calibrate a material export/query on a known-answer sample for the same format/architecture when practical. On the target, challenge one critical function/xref/address interpretation against original bytes, format metadata, runtime trace or another independent boundary.

## Recover the mechanism

- Begin from the discriminating anchor: entry point, export/import, message/API name, string/resource reference, crash address or observed behavior. Record the search population and ambiguity; an absent hit within one search is bounded negative evidence.
- Follow callers, callees, data references, control flow, types and relevant memory/data blocks. The packaged selected-function export now includes bounded instruction-origin references with exact Ghidra address spaces, type and operand; use them to locate candidate call/data sites before a narrower query or runtime check. It is not a whole-program dataflow graph. Distinguish Ghidra-created functions, imported symbols, user labels and model-generated names. Indirect calls, thunks, dynamic loading, self-modifying code and unresolved references remain open edges.
- Preserve the listing/bytes/addresses beside selected decompiler output. Pseudocode, recovered types and variable names are derived interpretations. For a material rule, trace the condition, state/data source, effect and alternate path to original bytes or independent runtime evidence.
- Record address spaces explicitly: source file offset, file-backed program address, RVA or link-time address, Ghidra image base and observed runtime module base. A program address can lack an original file offset; multiple addresses can map to one offset. Relocations, loader transformations, patches and overlays may change bytes. Never convert file offset to runtime VA by a bare addition without a verified mapping.
- If packed, encrypted, obfuscated or generated code prevents static recovery, separate the visible wrapper, unpacked/runtime observation and unknown internals. Use controlled authorized dynamic capture when it has higher information value; do not label a failed decompile as semantic absence.

## Output to RORE

Retain raw Ghidra project/export/logs as derived artifacts with provider/build/settings and target hash. Convert only supported observations into Evidence, then Findings and Paths. Include function/edge coverage, unresolved indirect edges, analysis warnings and contradictions. Reconnect any dynamic observation to stable source/program anchors where possible; session-local addresses stay session-local.

The supplied `ghidra-master.zip` is a 12.3 DEV source snapshot, not an installed distribution. Its headless and PyGhidra documentation informed this method. No Ghidra implementation or GPL-subtree code is included in RORE; see `SOURCE_PROVENANCE.md`.
