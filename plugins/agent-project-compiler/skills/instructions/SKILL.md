---
name: instructions
description: Compile ideas, interviews, files, references and research into durable provider-neutral project authorities. Use whenever the Agent Project Compiler plugin is invoked. Keep the APC orchestrator kernel active and load only material JIT references and companion procedures.
metadata:
  short-description: APC orchestrator with Core-First JIT routing
---

# Agent Project Compiler (APC)

## Always-active orchestrator kernel

Compile user intent, interviews, files/references and grounded research into a durable provider-neutral project package usable without this chat. Compilation is distinct from implementation unless the user asks for both. Interview in the user's language; authorities are normally English unless the project requires otherwise. Preserve verbatim provenance unchanged.

`ALL INFORMATION MUST BE REACHABLE != ALL INFORMATION MUST BE LOADED`.

Project authorities are truth; chat/provider memory, plugin wrappers, Skills, plans, generated views and summaries are not. Preserve:
- **Product Truth** — what the product must be/feel/do;
- **Realization Truth** — outcomes, flows, responsibilities, contracts and stages needed to realize it;
- **Verification Truth** — what current evidence actually proves.

Always preserve these invariants:

1. One canonical owner per durable responsibility. Authority artifact != runtime owner; contract != implementation/provider; definition/profile != runtime state; equivalent producers converge before domain behavior.
2. Preserve the whole before decomposition. Material user answers keep stable Round/Q identity, exact question, verbatim answer in `INTERVIEW_LEDGER`, and materialization into their canonical authority. References become explicit `adopt | adapt | reject | inspiration-only` traits/exclusions; presence alone is never a requirement.
3. The compiler owns Product/Realization Truth, architecture intent, plan/admission and Acceptance. User-changing decisions are settled or explicit. Reversible implementation choices may remain delegated technical decisions. A build agent may not silently redesign Product Truth, remove required outcomes or weaken completion criteria.
4. `PROJECT_PLAN` owns dependency/admission rules; Product Realization owns required outcome scope; Acceptance/Evidence owns verification truth; `STATE` is only execution/admission pointer plus session routing state. `APP_FLOW` owns workflow/state topology, not all product scope.
5. Exact approval/admission gates block the gated transition, not authorized reversible preparation. `TECHNICALLY EXECUTABLE != ADMITTED FOR PRODUCT CONCLUSIONS`.
6. `PROJECT_INDEX.yaml` is the project JIT router. Required authorities must be reachable and actually read before dependent material edits. Visible/listed/mentioned != loaded.
7. Active context is disposable working memory. Current workspace/project authorities and current external/runtime evidence beat memory, old plans and stale load state. After context loss discover current state first, then reload the smallest active owner set; never hydrate the whole workspace/reference pack for reassurance.
8. Design is Product Realization, not late polish. Maturity is `Specified → Declared → Connected → Exercised → Verified`. Product Complete requires every required master-outcome node Verified by sufficient current evidence; Release Ready adds project-defined release gates. Runtime/user-surface claims require evidence at the relevant real boundary.
9. Structured projects use a project-native executable gate when material: derive admission/completion from authorities + current evidence, validate coverage/applicable runtime/content/persistence constraints, and self-test relevant known-bad mutants. `STATE`, code volume, file existence, skeleton success or test count cannot self-certify broader completion.
10. Skills are procedures, never project truth. Use the smallest material APC reference and companion procedure. If Core-First is available, load/apply it when architecture/ownership/reuse is material; otherwise use packaged owner/change rules. Provider bindings remain thin.
11. Rich START/CONTINUE/GOAL/Handoff/Atlas artifacts orient a fresh agent but do not replace canonical authorities. Generated views are disposable cache.
12. A production-shaped skeleton may use placeholders in declared slots, but production admission requires representative survivability evidence; ordinary completion should add/replace definitions/content/assets/config/bounded extensions rather than replace canonical owners/runtime architecture.
13. Classify workspace/package shape before choosing authority paths. Existing canonical project authorities may fulfill APC semantic roles directly; do not duplicate them. A durable package may be `PACKAGE_READY_PENDING_USER` with explicit bounded user gaps without claiming Product Complete.

## Plugin-native JIT routing capsule

The root Skill is the **single APC orchestrator**. Supporting references are detailed procedure owners. Do not preload all references and do not create another APC router merely to reduce file size.

When this table is insufficient, read `references/REFERENCE_INDEX.md` first.

| Material trigger | Read JIT |
| --- | --- |
| classify compiler task, research unknowns, broad build-order/admission | `references/COMPILER_GUIDE.md` |
| interview/completeness/provenance/handoff | `references/INTERVIEW_COMPLETENESS_AND_HANDOFF_GUIDE.md` |
| vision/reference/design intent | `references/VISION_AND_REFERENCE_PRESERVATION_GUIDE.md` |
| system decomposition / composition / System Map | `references/composition/SYSTEM_MODEL_AND_COMPOSITION.md` |
| capability envelope / responsibility ownership | `references/composition/CAPABILITY_ENVELOPE_AND_OWNERSHIP.md` |
| Project Atlas / coverage / presentation composition | `references/composition/ATLAS_AND_COVERAGE.md` |
| definition-driven reusable product engine | `references/composition/DEFINITION_DRIVEN_COMPOSITION.md` |
| capability/change class/reuse/extension | `references/CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` |
| cross-system owner/state/producer/runtime/coherence | `references/SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md` |
| Product/Flow/Input/Content/Acceptance contracts | `references/verification/PRODUCT_CONTRACTS_AND_ACCEPTANCE.md` |
| evidence/completion | `references/verification/EVIDENCE_AND_COMPLETION.md` |
| surface + heartbeat/review/fidelity/coherence/survivability verification | `references/verification/SURFACE_AND_ADVANCED_VERIFICATION.md` |
| execution bootstrap/context/read gates | `references/execution/BOOTSTRAP_AND_CONTEXT.md` |
| implementation/integration loop | `references/execution/IMPLEMENTATION_AND_INTEGRATION.md` |
| finalization/claim reconciliation | `references/execution/FINALIZATION_AND_COMPLETION.md` |
| continuity/repair/derived admission/survivability | `references/execution/CONTINUITY_REPAIR_AND_SURVIVABILITY.md` |
| context/runtime/output/source-load rules | `references/RUNTIME_GUIDE.md` |
| actual UI/runtime/external outcome verification | `references/USER_SURFACE_VERIFICATION_GUIDE.md` |
| START/CONTINUE/GOAL | `references/BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md` |
| Fresh-Agent Reconstruction | `references/FRESH_AGENT_RECONSTRUCTION_GUIDE.md` |
| Blueprint/detail/assets | `references/BLUEPRINT_GUIDE.md` |
| Blueprint↔code/repository/Git | `references/BLUEPRINT_REPOSITORY_GUIDE.md` |
| project/external skill lifecycle | `references/SKILL_LIFECYCLE_GUIDE.md` |
| APC plugin packaging/JIT/context cost | `references/PLUGIN_NATIVE_JIT_ARCHITECTURE.md` |
| provider/hooks/subagents/memory/tools | `references/AGENT_RUNTIME_PORTABILITY_GUIDE.md` |
| non-repo/package root, existing authority binding, minimal package, unresolved user decisions | `references/compilation/PACKAGE_SHAPE_AUTHORITY_BINDING_AND_OPEN_DECISIONS.md` |
| concrete artifact template | route via `references/REFERENCE_INDEX.md` to the single needed `references/templates/*` group |

If several triggers apply, sequence only the owners needed for the **next material decision**. Loading a reference is a whole-file context operation in this host; choose a true JIT slice rather than a legacy monolith.

## Companion Core-First governance

When `core-first-governance` is available, keep it a separate procedural owner:
- architecture / ownership / authoritative state / reuse / composition / capability / provider / extension material → primary agent loads + applies `core-first-extension-architecture` before freezing the owner/change boundary;
- routing/freshness/delegation/verification semantics material → use `core-first-orchestration` JIT;
- real user/external runtime claim material → `observable-product-verification` when available;
- material architecture/reuse/ownership conformance → fresh read-only `core-first-verifier` when feasible;
- consequential/high-risk/difficult-to-verify implementation → `independent-review` when triggered.

Never claim an external Skill was loaded from memory. If absent, use APC/project-native owners/gates and state the actual limitation.

## Context freshness and recovery

Invalidate remembered procedures/plans/load markers after a fresh session, major compaction/context loss, workspace/project switch, relevant Skill/authority revision, major workstream switch, material workspace/external-state change, or uncertainty that a required source was loaded.

Then:
1. cheaply discover current workspace/control-plane/target roots, instructions, VCS state when present, current-change state, routing/index, compact `STATE` and relevant evidence;
2. use `PROJECT_INDEX.yaml` instead of guessing filenames;
3. reset/rebuild session source-load evidence;
4. load only authorities and APC/companion procedures required by the active decision;
5. reconcile completed/remaining outcomes, blockers, assumptions, admission and evidence;
6. replan if the next admissible/best action changed.

## Compilation sequence

1. Establish active truth from current workspace/project/package sources; classify workspace shape and control-plane vs runnable/shippable root before asking the user to repeat known information.
2. Classify: new compile, decision update, package audit/reconstruction, continuation/rehydration, or compiler-distribution maintenance.
3. Route JIT to the smallest procedure owner set.
4. Research material factual unknowns where appropriate; close user-owned gaps or keep them explicit. Use `PACKAGE_READY_PENDING_USER` only as a derived handoff status when open user decisions are impact-bounded; never promote a provisional interpretation to Product Truth.
5. Infer provisional Product Capability/Responsibility Envelope as compiler hypothesis; challenge ordinary missing responsibilities; resolve `Requirement → Responsibility → canonical Owner/System → Capability Contract → Module/Implementation/Provider → Consumer Composition → Data/Modifier/Substitution`.
6. Compile complete Product Realization flows/lifecycles/surfaces/states/workflows/cross-cutting outcomes and a production-shaped representative skeleton without mistaking it for whole-product completion.
7. Compile dependency/admission and Acceptance; downstream synthetic work cannot support stronger product conclusions than its evidence class.
8. Bind provider/runtime/skills through thin adapters and explicit degradation paths.
9. Verify criterion-specific claims with current evidence; gates reject status claims that outrun Plan + Product Realization + Acceptance + evidence.
10. COMPLETE only when Fresh-Agent Reconstruction, authority reachability, outcome planning/coverage, ownership/producer convergence and the project-native executable gate all satisfy their declared scope.

## Output invariants

Reuse/bind existing canonical project authorities first; generate only applicable missing authorities: Vision/Ledger/Coverage/Decisions/Handoff, `PRODUCT_REALIZATION`, Plan, System/Capability/Integration, domain contracts, Blueprints, Acceptance/evidence, registries/index/state and START/CONTINUE/GOAL. When material, include representative product-path heartbeats, deterministic review projections, reproducible source→generator→artifact pipelines and finish/fidelity outcomes.

After each milestone: update evidence → derive admission → continue with the next admissible stage. Stop only at COMPLETE, `PACKAGE_READY_PENDING_USER` when remaining material compilation is blocked only by explicit user-owned decisions, a genuine external dependency, the exact approval boundary actually reached, or explicit user stop.
