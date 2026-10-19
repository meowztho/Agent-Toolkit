# RORE — Replication-Oriented Reverse Engineering

RORE is a provider-neutral Agent Plugin for **deep reconstruction of authorized reference systems**. Its purpose is to recover how a reference actually behaves and is structured — not to decide what a new product should be, not to redesign the reference for a builder, and not to implement or release a replica.

The word *replication-oriented* describes the required depth: RORE should produce an auditable, replication-ready model of the authorized reference. An independent implementation agent should be able to recover its observable behavior, structure, data semantics, mechanics, interface and asset semantics, runtime behavior, protocols, constraints and relevant edge cases from that model without rediscovering the reference. Each material claim retains its evidence, provenance, confidence and unknowns. RORE preserves the reference's own architecture rather than translating it into a proposed target design.

The current package keeps that boundary unchanged. It covers evidence freshness, reviewer independence, justified descent to lower-level binary/memory facts, source trust, API projection across distinct system layers, failure-guided investigation and conservative cross-layer correlation.

## Boundary

```text
REFERENCE TARGET
→ observe / acquire / inventory
→ extract / decode / decompile / inspect
→ dynamic + runtime + memory analysis when useful
→ controlled perturbation to expose hidden causality
→ qualify Evidence
→ Findings
→ Paths
→ reference-native Models + reference comparison cases
→ coverage / contradictions / unknowns
= REFERENCE TRUTH
STOP RORE
```

RORE does **not** own target requirements, target architecture, product planning, implementation, replica acceptance, branding, launch or release. It has no APC dependency and does not compile a downstream project package.

Reference comparison cases describe repeatable observations of the **original** system, with preconditions, inputs, outcomes, tolerances and evidence. They help a later agent compare an implementation with the reference; they are not target-product acceptance or release decisions.

The portable handoff keeps raw Evidence and its index separate from revisable Findings, Models and narrative. A later project compiler can consume that source material and decide what the new project should require; RORE does not depend on that compiler. Tool output is calibrated before it supports a material claim where practical, and every target-touching action is checked against the current authorized scope.

A request to investigate a named or supplied target is the default broad analysis scope for that target. RORE uses the request and session context without asking for a generic ownership statement or repeated permission for ordinary extraction, decompilation, observation, bounded reversible local probes and needed contained user-scoped analysis tools. It asks about a genuinely new target, account, access, cost, privilege or external effect when that boundary is unclear. Analysis permission is separate from sharing or redistribution.

For broad investigations, `rore-orchestration` routes through the JIT [coverage campaign](skills/rore-orchestration/references/BROAD_COVERAGE_CAMPAIGN.md): retain the target's population and evidence map across surfaces, APIs, assets, data, architecture and runtime, then follow material leads toward observed effects. The [Evidence CLI](docs/EVIDENCE_BUNDLE_V1.md) can create a new bundle and append complete raw files; larger collections remain in indexed companion storage.

For several references, the [extension-seam method](skills/rore-reconstruction/references/MULTI_REFERENCE_EXTENSION_SEAMS.md) keeps each product's truth separate while tracing decompiled mechanisms, runtime effects and evidenced interoperability surfaces. A later project can use this map to design a mod or mashup.

For comparable PNG captures of two reference states or versions, the optional standard-library [image difference locator](scripts/rore_imgdiff.py) marks candidate visual changes. Its indicator is not a UI parity or functional-equivalence verdict; keep each capture's build, environment, state, viewport and time with the Evidence record.

## Plugin identity since v0.15.0

The technical manifest name is `rore`. Earlier RORE releases used `corereplica`, which the host treats as a different installation identity. Installing v0.15.0 may leave the old `corereplica` plugin present alongside RORE; select `rore` for new work and retire the old installation only after its configuration and handoffs are accounted for. This package does not uninstall or overwrite it. CoreReplica v0.4.0 uses its separate `corereplica-skills` identity. Historical Evidence bundles and target findings keep their own IDs and are not rewritten by this plugin rename.

## Active skills

| Skill | Responsibility |
| --- | --- |
| `rore-orchestration` | Choose the next analysis method from target/surface, current knowledge gap, required evidence boundary and available capabilities. |
| `rore-reconstruction` | Acquire, interpret and connect evidence into Findings, Paths and reference-native models while preserving the original system's structure and uncertainty. |
| `rore-evidence-review` | Read-only audit of evidence sufficiency, fixity, traceability, contradictions, coverage and claim overreach. |

These are canonical responsibilities, not a mandatory three-stage pipeline. Narrow work may use only reconstruction; evidence review is triggered when a claim, handoff, broad completeness statement or high-consequence interpretation needs an independent check.

## Core evidence model

```text
Evidence = directly observed/acquired fact or bounded derived artifact
Finding  = evidence-backed interpretation
Path     = grounded relationship/flow/cause connecting evidence/findings
Model    = a reference-native synthesis: surface, state, component, data,
           protocol, causal, asset, mechanics, architecture, etc.
```

RORE preserves several distinctions:

```text
parseable output != correct object identity
correct subset != population completeness
two tools agree != independent corroboration
present != referenced != reachable != exercised != effective
model-generated annotation != grounded Reference Truth
```

For broad investigations, material coverage is explicit: `covered | partial | unresolved | not_applicable | out_of_scope`.

## Reconstruction methods

`rore-reconstruction` JIT-loads only the methods that fit the current gap:

- surface / flow / state reconstruction;
- visual / interaction measurement;
- artifact extraction and nested container recovery;
- static code / binary reconstruction;
- runtime / dynamic observation;
- memory / state / reader-writer causality;
- web / JavaScript / API reconstruction;
- protocol reconstruction;
- data / schema / format reconstruction;
- mobile/platform reconstruction;
- conditional engine / asset / runtime profiling when those semantics exist;
- cross-version / differential reconstruction;
- mechanics / rules / balancing reconstruction;
- external/version/review research;
- controlled perturbation and causal probing;
- failure-guided reconstruction from an observed crash, error, wrong result or recovery defect;
- cross-layer Evidence correlation between shipped, derived and runtime objects;
- provider-independent acquisition recipes when an integrated analysis suite is absent.

A named tool is a **provider**, not an owner. RORE first identifies the required analysis capability, then discovers an available provider or uses the smallest auditable helper that can supply it.

## RORE CLI and MCP

RORE includes a small, independent [Evidence bundle format](docs/EVIDENCE_BUNDLE_V1.md) and [native artifact tools](docs/NATIVE_ARTIFACT_TOOLS.md). `python scripts/rore.py --help` runs with the Python standard library. It can validate/inspect/compare Evidence bundles, import/export byte-preserving archives, hash and inspect local files, inventory ZIPs/directories, read exact byte windows and inspect declared PE/ELF file mappings. A REA Evidence JSON export can be previewed and imported without requiring REA; its original bytes and IDs are retained, while REA's semantic validation remains outside this structural intake. The packaged `mcp.json` exposes thirteen read-only Evidence/artifact queries and a separate RORE-owned provider server for explicit setup and analysis jobs. Both local servers need `uv` and the pinned Python MCP SDK dependency. [Provider seeds](skills/rore-reconstruction/references/PROVIDER_SEEDS.md) from tool-master are inert leads. For deeper native analysis, the [optional Ghidra adapter](docs/GHIDRA_PROVIDER_ADAPTER.md) analyzes a verified file copy and retains its project, raw export and logs. When that provider is needed but absent, [on-demand setup](docs/PROVIDER_SETUP.md) can obtain pinned Ghidra/JDK archives on Windows x64 through CLI or MCP; other providers follow the conditional JIT acquisition method. Plugin startup does not install a provider. The supplied third-party source archives are not runtime dependencies.

## Perturbation as an epistemic instrument

RORE may deliberately vary inputs, state, memory, DOM/client state, files/configuration, timing, sequence or other authorized boundaries when normal observation cannot reveal the mechanism. The purpose is causal understanding, not exploit maximization.

Controlled malformed inputs, local faults and temporary patches/hooks can reveal validation, enforcement and recovery behavior. Record the broken-state observation beside the unmodified baseline and continue while material reconstruction gaps remain.

```text
baseline
→ hypothesis
→ vary one material dimension
→ observe differential
→ trace cause
→ corroborate against stable anchors
→ restore / record residue
→ Evidence + Finding + Path
```

Stop when the mechanism is sufficiently understood for the requested reconstruction scope.

## Reference identities

Use stable IDs where the target contains the corresponding class, for example:

```text
SUR-###    surface/screen/view
FLOW-###   user/system flow
STATE-###  material state
COMP-###   component/subsystem
ENT-###    data/domain entity
PROTO-###  protocol/message identity
E-###      evidence
FIND-###   finding
PATH-###   user/call/data/runtime/causal path
PROBE-###  reproducible probe
ORACLE-### reference comparison case
ASSET-###  material asset/resource when useful
```

Do not force unused classes onto a target. Stable IDs exist to preserve relationships across evidence and versions, not to impose a foreign architecture.

## Provenance

RORE evolves from CoreReplica and retains methodology provenance from the MIT-licensed `Jakeschincariol/replica-skill` and `zhaoxuya520/reverse-skill`. v0.4.3 reviewed `tool-master.zip` for tool-discovery concepts; v0.5.0 adapted selected methods from `rea-main.zip`; v0.8.0 added RORE-owned artifact operations and a conditional Ghidra method; v0.9.0 added a RORE-owned optional Ghidra adapter; v0.10.0 added on-demand provider setup; v0.11.0 clarified broad extraction depth and recoverable interventions; v0.12.0 added broad coverage, Evidence authoring and PE raw-layout diagnostics; v0.13.0 added multi-reference extension seams; v0.14.0 derives target-scoped analysis and tool-acquisition scope from the user's request; v0.15.0 separates the technical plugin identity and admits selected CoreReplica v0.4.0 workspace, probing, runtime and PNG-difference methods; v0.16.0 adds explicit provider jobs through RORE's own MCP; v0.16.1 adds optional, range-scoped rebuild comparison guidance. See `SOURCE_PROVENANCE.md`.
