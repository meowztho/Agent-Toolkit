# Static Code / Binary Reconstruction

Recover likely structure from source, bytecode, native code, metadata and related artifacts.

Useful semantic capabilities include:
- function/class/module identity;
- callers/callees and xrefs;
- control/data flow;
- imports/exports/symbols/types;
- strings/constants/resources;
- state machines/validation/transforms;
- vtables/RTTI/object layouts where evidenced;
- producer/consumer and enforcement-site mapping.

A decompiler is an important acquisition and interpretation surface, especially when source is unavailable and a hidden call/data path or extension point is the active question. Use it to select and follow relevant functions, callers, callees and state transitions rather than stopping at import/export or string inventories. Preserve access to lower-level facts when an important conclusion depends on it; decompiled text alone cannot establish runtime reachability, actual types/names or full behavior.

When loader-aware native-code analysis is needed and Ghidra is the selected available provider, read `GHIDRA_STATIC_PROVIDER.md`. Its project, loader, address-space and output boundaries apply to that provider only; the same evidence contract applies to other disassemblers.

Use the highest useful semantic level first, but descend only as far as unresolved information requires:

```text
source / metadata
→ decompiler / IR
→ bytecode / assembly
→ raw bytes / hex
→ live memory / machine state
```

Do not descend for ceremony. Descend when the lower layer can discriminate a material hypothesis that the higher layer cannot, then reconnect the low-level fact to stable semantic anchors before promoting a Finding.

## Optional rebuild comparison

When a reconstructed source candidate, the corresponding reference bytes and a suitable build path are available, rebuilding the candidate and comparing corresponding functions, objects, data or linked ranges can test a specific static hypothesis. This is a bounded reference-analysis experiment, not a target-product build or a required stage. Select an existing comparator or a focused script by capability and exact format fit; no named service or tool is a prerequisite.

Record the reference and candidate identities, compiler/linker versions and options, build inputs, compared unit and address/relocation mapping, commands, raw outputs and unmatched ranges. Separate exact byte matches from heuristic similarity, untested units and unknown coverage. A copied original assembly/byte stub may match without reconstructing source; a mismatch may arise from build settings or layout rather than different logic. Neither a match percentage nor exact bytes prove original source form, runtime reachability, complete behavior or whole-reference coverage. Carry only the conclusion supported by the compared range into Findings and Paths; use runtime evidence for runtime-sensitive claims.

## Byte / hex evidence

When bytes matter, preserve the original artifact identity and the exact byte range. Inspect headers, section/segment layout, signatures, encodings, compact tables, embedded resources and version differences as the question requires. Record the relevant file offset, section/segment-relative position, virtual/runtime address and module base only where each mapping is established; file bytes and mapped process memory may differ because of loading, relocation, decoding or patching. Record architecture, width, endianness and encoding assumptions before interpreting multi-byte values or strings. Link the raw bytes or hash, parser/disassembler view, xrefs and the Finding they support. If an offset/address translation or decoded meaning is uncertain, keep it a hypothesis rather than presenting a plausible hex pattern as a recovered rule.

Language/runtime clues matter: Go, Rust, C++ RTTI/EH, ObjC/Swift, .NET/AOT, WASM or heavy obfuscation may require different semantics. Do not force a C-like interpretation when the runtime model contradicts it.

For a broad mechanism, search for material enforcement-site fan-out. One check found does not prove the mechanism is fully mapped.

## Managed and mixed native boundaries

For PE/CLI or another managed format, classify the actual component bytes before choosing a decompiler. Preserve original metadata, signatures, method tokens and CIL/bytecode separately from reconstructed source-like text; a method token and its name are build-local. Inspect native imports/exports, declarations and packaging separately. A managed declaration matching a native export is a candidate handoff, not proof of the body executed or its effect. ReadyToRun, NativeAOT, IL2CPP, embedded assemblies and ordinary CIL may coexist in one product; classify each component rather than assigning one label to the whole package. Missing CIL in a native image does not prove managed semantics were recovered.

For an offline crash/core, use a format-aware reader to preserve raw note/exception ranges, historical threads, registers and mapped segment candidates before any debugger enrichment. Historical PID and mapping display names are not live-process or current-file identities. Match an executable/library to the exact dump and build before mapping a fault address into a function. Missing or unsupported notes limit the conclusion; they do not prove that the corresponding runtime state did not exist.
