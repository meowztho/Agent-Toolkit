# Multiple References and Extension Seams

Read when an authorized reference's extension surface matters, especially when an investigation must understand two or more systems for interoperability. A game mod or mashup is one example; the same method applies to applications, services and mixed runtimes. This is a conditional Reconstruction method, not a mod-design or implementation phase.

## Keep each reference independently grounded

Create a separate identity and coverage map for each product, build, platform, loader, content set and observed environment. Recover the requested functional slices in each system: behavior and state, engine/runtime or process boundaries, relevant code and data paths, asset loading, input/events, persistence, networking and error handling. Do not merge similarly named concepts or treat a feature observed in one reference as evidence about the other.

Use a concrete behavior, resource, event or failure as an anchor. Follow it from user-visible effect through runtime state to candidate code/data/resource producers, and back out to outputs and lifecycle. When source is unavailable, decompile or disassemble the relevant modules/functions, inspect callers, callees, xrefs, data flow, types and loader mappings, and descend to bytecode/assembly/bytes or live memory where pseudocode leaves a material question open. Keep original artifacts, provider settings, decompiler output and lower-level observations linked. Decompiled text is a derived view; it is useful for discovering hypotheses and reconstructing mechanisms, not proof that a function executes or that its inferred names/types are correct.

## Recover extension surfaces, not just symbol lists

Inventory observed or candidate seams in each reference: documented mod/plugin APIs, script callbacks, event dispatch, content/data override order, package/asset loaders, configuration, save formats, IPC or network messages, dynamic libraries, native imports/exports, engine object registries and update loops. Record observed loader, signing, integrity or update restrictions that affect a seam. If no declared seam answers the question, inspect candidate interception or patch locations as reference facts. For each candidate record:

```text
reference/build + module/package + stable semantic anchor
seam kind; lifecycle phase; thread/timing/context
caller/producer → boundary → callee/consumer → observable effect
arguments, return values, ABI/calling convention where relevant, memory/state ownership, data/resource format
load/override/precedence rules and failure/recovery behavior
evidence from declaration, decompilation, raw code/data and runtime probe
status: present | referenced | reachable | exercised | effective
address/version stability, ambiguity and unresolved indirect edges
```

Static exports, strings, a decompiled call site or a loaded library establish candidates within their coverage. Follow representative candidates with a normal runtime trace and, when needed, a controlled reversible probe that demonstrates whether the seam is reached and what it can change. Keep instrumented and unmodified observations separate. A hook that works in one session is not automatically a stable public mod API; record exact build, address mapping, initialization order and side effects.

## Correlate systems without inventing a combined design

When several references are involved, compare their relevant semantic boundaries only after each side has its own evidence graph: event/state timing, coordinate and unit systems, object/component identity, asset/material/audio formats, serialization, input, ownership, lifecycle, concurrency and network authority. Record exact or weaker correspondences, incompatible assumptions, required but unobserved transformations and candidate populations. Similar names, engines or file extensions do not establish a shared contract. Use `CROSS_LAYER_EVIDENCE_CORRELATION.md` for layer mappings and `GAME_ENGINE_ASSET_RECONSTRUCTION.md` when engine/asset semantics are present.

The handoff contains Reference Truth for each investigated system plus an evidence-linked seam map and, when several systems are involved, a correspondence map: where an extension could enter, which observed contract it reaches, which effects were actually exercised, version fragility, contradictions and unknowns. It does not choose the mashup architecture, write a mod, or claim two systems are compatible merely because a plausible adapter can be imagined. Preserve relevant raw code views and assets within their access/retention boundary; analysis access does not grant redistribution rights.
