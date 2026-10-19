# RORE Decision Compendium

## D-001 — Product identity
The user-facing plugin is **RORE — Replication-Oriented Reverse Engineering**. From v0.15.0 its technical manifest name is `rore`, separate from CoreReplica's `corereplica-skills`. Releases through v0.14.0 used `corereplica`; host installation/update identity therefore changes. The old installation remains a separate plugin until explicitly retired. This rename does not change the Evidence bundle schema or rewrite historical findings.

## D-002 — Scope boundary
RORE owns reference reverse engineering and reconstruction only. It stops at qualified Reference Truth and does not own downstream target-product decisions, project compilation, target architecture, implementation, replica acceptance, branding, launch or release.

## D-003 — Reference-native reconstruction
The reference is allowed to reveal its own architecture, logic, state model, data model, protocols, flows, timing and failure behavior. RORE preserves those structures and uncertainties rather than converting them into a cleaner or implementation-oriented target design.

## D-004 — Owner topology
RORE has three durable responsibilities: orchestration, reconstruction and read-only evidence review. Surface, static, runtime, memory, protocol, web, mobile, engine/asset and other analysis modes or conditional profiles are JIT methods beneath reconstruction unless future evidence proves a distinct canonical responsibility.

## D-005 — Evidence discipline
`CLAIM STRENGTH <= PROVEN EVIDENCE BOUNDARY`. Object identity, parser correctness, source precedence, population coverage, methodological independence, target identity and runtime status remain explicit where material.

## D-006 — Analysis decision quality
RORE admits hypothesis-driven stage exits, negative evidence, deadlock→replan, stage/tool-bias detection, runtime back-annotation and context-pollution detection from the reviewed reverse-skill methodology. These improve epistemic quality and do not create a security-product owner.

## D-007 — Perturbation and causal probing
Controlled mutation, boundary tests, replay/sequence variation, timing/concurrency probes, failure/recovery injection, DOM/client-state changes, memory edits and similar authorized interventions are valid when they materially expose mechanism or causality. Their purpose is understanding, not exploit maximization.

## D-008 — Provider-neutral tooling
RORE routes `question → required evidence boundary → analysis capability → provider`. IDA, Ghidra, Binary Ninja, radare2, x64dbg, Frida, browser/CDP tools, packet analyzers and helper scripts are providers, not responsibility owners.

## D-009 — Stable reference identities
When useful, stable reference IDs such as `SUR`, `FLOW`, `STATE`, `COMP`, `ENT`, `PROTO`, `E`, `FIND`, `PATH` and `PROBE` preserve cross-artifact relationships. They are not a mandatory schema imposed on every target.

## D-010 — Cross-version semantics
Cross-version work re-resolves semantic anchors — call relationships, strings, constants, types, schemas, patterns, behavior and data references — rather than transplanting raw addresses or offsets.

## D-011 — LLM/decompiler annotations
Function names, summaries, source-identification guesses and other model-assisted annotations are reversible derived hypotheses until grounded by target evidence.

## D-012 — External research
Public docs, source/history, reviews, changelogs, community reports and research can discover mechanisms and new local evidence paths. Target-specific claims remain externally documented until target corroboration is sufficient for the claimed boundary.

## D-013 — Upstream replica-skill admission
RORE retains useful recon ideas from `Jakeschincariol/replica-skill`: stable screen/flow identities, state inventories, component mapping, inferred data models with evidence/confidence, measured visual semantics and systematic edge-state thinking. Clone priorities, sizing, target architecture/design/build and ship/parity semantics are not admitted.

## D-014 — Upstream reverse-skill admission
RORE retains provider-neutral reverse-engineering methods from `zhaoxuya520/reverse-skill`, including protocol/mobile/web/binary-diff patterns, Evidence→Finding→Path, analysis-decision quality and selected adversarial/pwn/patch-diff reasoning where it serves mechanism discovery. Offensive impact, persistence, lateral movement, credential theft and exploit stabilization are not RORE goals.

## D-015 — Evidence review boundary
Evidence Review audits an existing reconstruction package read-only. It may report unsupported claims, stale hashes, contradictions, unlinked evidence or overclaimed coverage, but the correction is performed later by Reconstruction so the reviewer does not silently repair its own judgment target.

## D-016 — Domain neutrality
RORE is domain-neutral. Product categories such as web, API, ERP, CRM, desktop, mobile, protocol, game or simulation do not become responsibility owners and none is a primary target. Domain/surface labels may select conditional JIT profiles, but routing remains `knowledge gap → evidence boundary → analysis method/capability → provider`. Games are retained as a useful high-complexity stress-test domain, not as a privileged architecture focus.

## D-017 — REA methodology admission
The user-supplied REA 6.2.0 snapshot contributes provider-neutral acquisition recipes, failure-guided investigation, conservative cross-layer matching, explicit capture/readiness limits, imported Evidence integrity checks and continuing-unknown discipline. These extend Reconstruction and its existing Orchestration/Review interfaces; they create no fourth owner, mandatory REA runtime, tool installer, REA-format database or downstream reconstruction-verification gate. The source ZIP remains an audited influence rather than an executable dependency.

## D-018 — Optional Evidence transport
RORE's versioned Evidence bundle is a companion index over complete source files. Its CLI and read-only MCP interface share one implementation and belong beneath Reconstruction; neither validates the semantics of a Finding or becomes an analysis provider. The MCP SDK is a transport dependency, not an REA/APC/Core First dependency. Tool-master entries remain inert provider seeds until exact-host capability and effects are verified.

REA Evidence JSON enters through a structural adapter beneath the same Reconstruction owner: retain the original bytes, identify the source bundle separately from any subjects, project stable REA record/revision IDs, and expose original records through read-only queries. REA's semantic validation and live analysis commands remain with REA; this import does not attest their outcomes or create a second evidence authority.

## D-019 — Native artifact observations and conditional deep analyzers

RORE's Reconstruction owner now provides its own bounded regular-file, ZIP, directory and declared PE/ELF layout observations. CLI and read-only MCP are two transports over one Python core. Exact bytes, hashes and coordinate spaces are evidence candidates, not a decompiler or runtime claim. For deeper native control/data flow, a selected installed Ghidra or equivalent analyzer remains a qualified external provider. The supplied Ghidra source snapshot contributes a conditional headless-analysis method and address/loader cautions, not a bundled executable or new owner.

## D-020 — Optional deep static provider adapter

An explicit CLI may invoke a separately installed Ghidra distribution on a verified target copy when loader-aware static analysis is material. RORE owns the narrow adapter and export script beneath Reconstruction; Ghidra remains a provider, and the existing read-only MCP remains read-only. A new isolated project retains input, raw export, logs and status. Imported-file identity, analysis timeout, inventory caps and selected decompilation status bound claims. Provider output becomes qualified Evidence only after interpretation; it does not become a second truth owner or require the Ghidra source snapshot at runtime.

## D-021 — Requested provider acquisition

When a needed evidence capability is absent, Orchestration selects the capability and Reconstruction owns bounded provider setup/qualification within the user's investigation scope. The tested Windows x64 Ghidra/JDK recipe pins official ZIPs and checks their hashes before contained extraction; other providers use a JIT, official-source acquisition method at execution time. A broad analysis request covers a needed freely available, contained user-scoped provider unless restricted, while paid, privileged or system-wide acquisition needs a separate basis. Setup is a provider prerequisite, not a new owner, automatic plugin activation, installation of a whole catalog, or proof that an arbitrary target can be reconstructed. The read-only MCP remains unchanged.

## D-022 — Broad extraction depth and unresolved facts

For a broad authorized investigation, RORE seeks all technically accessible reference information, including low-level details, rather than stopping when one mechanism or a plausible implementation outline is understood. A bounded question can close on sufficient mechanism evidence; broad completion requires visible coverage and disposition of remaining avenues. A failed or inaccessible avenue records the exact attempts, evidence limit, alternative methods and possible later user input. `currently unresolved/blocked` does not mean the reference fact is intrinsically unrecoverable. The implementation agent normally relies on RORE's handoff even when the finished original remains accessible; APC may combine it with later user knowledge without becoming a RORE dependency.

## D-023 — Provider independence and recoverable target changes

RORE may obtain tools or source material online, but no named repository, download endpoint or analyzer is mandatory. The packaged Ghidra recipe is one optional tested route. If it fails, the agent returns to the required capability and tries an alternate qualified provider, host tool or bounded helper before declaring the evidence boundary unavailable. For authorized perturbation, use a representative copy when practical; in-place experiments remain possible when their baseline, exact writes, external effects and verified recovery are recorded. Git is one recording method for suitable files, not a substitute for snapshots of registry, process, database or other state.

## D-024 — Broad coverage as an investigation route

A broad reference investigation maintains a live population and coverage map across the reference's own surfaces, assets, data, APIs, processes, network and internals. Orchestration selects the next material evidence boundary from that map; Reconstruction acquires and links raw Evidence, Findings, Paths and reference-native Models. Static presence is a lead to reachability, exercise, effect and causality, not a reason to close a whole-system mission. The map does not filter facts through later product or project decisions. Large raw collections stay complete in indexed companion storage when the optional Evidence bundle transport limit is reached.

## D-025 — Bounded Evidence authoring and layout diagnostics

The existing Reconstruction-owned bundle core may initialize a new Evidence index and append complete raw files as one Evidence record through the CLI. This is an authoring aid, not an analysis provider, semantic validator or second evidence owner; existing records remain intact, and MCP stays read-only. PE layout inspection reports overlapping declared raw ranges, zero-sized raw sections and ranges beyond the file as diagnostics while preserving ambiguous mapping results and avoiding loader claims.

## D-026 — Multiple references and extension seams

RORE may investigate several authorized references for a later mashup, mod or interoperability project. It maintains separate identities and evidence graphs, uses decompilation/disassembly as an active route to hidden mechanisms and candidate entry points, and tests reachability/effects against runtime evidence where material. Reconstruction owns the reference-native seam and correspondence map beneath existing Orchestration routing; this adds no mod-builder, combined-product architecture owner or mandatory analyzer. A candidate hook or similarly named object across products is not an established compatible contract.

## D-027 — Context-derived analysis scope

A user's request to investigate a named or unambiguously supplied reference is itself the broad analysis scope for that target unless narrowed. Orchestration applies the request, project context and prior session permissions without a generic legal-proof question or repeated per-method approval. Static extraction, decompilation, local runtime observation and bounded reversible local probes are ordinary methods within that scope. An internal action check distinguishes components of the named reference from a newly discovered account, remote service, unrelated host or material external effect; only the latter unresolved boundary merits a focused question. Analysis scope does not automatically grant sharing, product inclusion or redistribution.

## D-028 — Native tool integration from supplemental research

Extend the existing Ghidra headless provider first: selected functions now export bounded instruction-origin references with Ghidra addresses and spaces, type, operand, source and flow/read/write flags. This closes a concrete traceability gap left by function-level caller/callee sets. The Python adapter marks capped reference output partial; it does not treat a missing analyzed edge as semantic absence.

For live analysis, prefer a qualified tool's official interface over a new bridge: GDB's version-pinned Machine Interface, LLDB's Python API, x64dbg's native commands/scripts, or Frida's Python/JavaScript APIs according to the exact host and target. The current RORE methods already specify baseline, process/thread/module identity, breakpoint/watchpoint/instrumentation effects, raw trace and recovery. A custom x64dbg C++ plugin with local transport remains conditional on a demonstrated operation that commands/scripts cannot reliably provide; third-party MCP/bridge repositories are not dependencies. Rizin/radare2, angr, Binary Ninja, IDA and engine asset/runtime tools remain optional providers selected by a concrete unresolved capability, version/license and target-format fit, not a package-wide tool catalog or fixed pipeline. N64Recomp and XenonRecomp are platform-specific examples of reconstructing code, jump targets and runtime contracts; they do not imply universal recompilation or create a RORE recompiler owner.

## D-029 — Explicit provider jobs through RORE-owned MCP

The existing Ghidra/JDK Windows setup recipe and copied-target Ghidra adapter remain the only automatic provider path. A separate `rore-providers` MCP offers read-only doctor/plan/status/result queries and explicit retained install/analysis jobs. A selected analysis may install its missing pinned provider on demand; plugin activation and tool discovery do not install anything. Job requests and status are retained outside the plugin, interrupted workers are reported rather than left pending indefinitely, and bounded result pages check the adapter's output hashes. The existing `rore-evidence` MCP remains read-only. This is one Reconstruction-owned capability with two transports, not a foreign MCP bridge, general command runner, second analysis truth owner or claim that every reverse-engineering tool can be installed automatically.
