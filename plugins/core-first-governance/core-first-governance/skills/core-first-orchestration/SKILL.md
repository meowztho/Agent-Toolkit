---
name: core-first-orchestration
description: Route software work with minimal context using explicit material triggers and a defined local short path. The primary agent MUST apply Core-First itself when architecture/ownership/reuse is material. Load sibling Skills/procedures JIT only on material triggers; ground prerequisites, adapt execution, and route verification/review/completion without replacing canonical owners.
metadata:
  short-description: Minimal-context Core-First routing and execution
---

# Core-First Orchestration

## Kernel

The **primary agent is the user-facing orchestrator and final integrator**. It is not a dispatcher that outsources its own engineering responsibility.

Always preserve these invariants:

1. **Primary Core-First duty.** If architecture, ownership, authoritative state, reuse, composition, capability/module/provider boundaries, or extension semantics are material, the primary agent MUST load and apply `core-first-extension-architecture` itself before committing to the change boundary. Delegation never discharges this duty.
2. **Current truth beats cache.** Repository/project authorities and current external/runtime state outrank remembered chat, Skill memory, old plans, summaries, and stale evidence.
3. **Progressive disclosure.** Route from compact trigger knowledge; do not preload every sibling Skill or detailed orchestration procedure. Load the canonical owner JIT when its trigger becomes material.
4. **Ground before expensive action.** Material source/tool/prerequisite facts that can change the approach must be inspected and consumed before expensive implementation commits to them.
5. **Adaptive execution.** Use lightweight checkpoints when dependencies, prerequisites, state transitions, meaningful multi-step work, or invalidating evidence can change the path; otherwise use the local short path.
6. **Evidence matches the claim.** Static/log/tool evidence does not substitute for a material real user/external outcome. Route such claims to `observable-product-verification`.
7. **No parallel owners.** Plans, routing metadata, reviewers, verifiers, generated views, and host capabilities do not become project truth, architecture owners, or completion authorities.
8. **Exact gate boundary.** An approval/admission gate blocks the gated state transition, not authorized reversible preparation before it. A broader implementation request does not implicitly authorize crossing that transition.

## Skill routing capsule

`ROUTING KNOWLEDGE != PROCEDURAL KNOWLEDGE`.

| Material trigger | Canonical owner | Primary-agent duty |
| --- | --- | --- |
| architecture / ownership / authoritative state / reuse / composition / capability / provider / extension | `core-first-extension-architecture` | **MUST load + apply itself** before direct implementation or delegation |
| real user/external runtime, UI, visual, interaction, persistence, CLI/API side effect | `observable-product-verification` | ensure the real procedure actually occurs before claiming that outcome |
| material architecture/reuse/ownership conformance | `core-first-verifier` | route to separate fresh read-only verification when feasible; never substitute it for primary Core-First |
| consequential / high-risk / difficult-to-verify / materially blocked implementation | `independent-review` | route to anti-anchored independent review only when triggered |

Prefer host Skill metadata/discovery when available. It is an optimization/projection, not policy authority and not a replacement for the canonical Skill body. A native host capability may fulfill an invariant; it never erases it. **Reduce duplicate execution, not duplicate requirements.**

When a canonical Skill must be loaded fresh, prefer: (1) explicit host-native Skill attachment/injection; (2) a resolved installed `SKILL.md` path and fresh read; (3) another verifiable canonical-content mechanism. Never rely only on inherited conversational memory. If simultaneous multi-Skill activation is unreliable, sequence the procedures and pass raw evidence/findings between them instead.

## JIT orchestration procedures

Read only the detailed procedure whose trigger is material, **before** crossing that boundary:

- `references/GROUNDED_EXECUTION_PREFLIGHT.md` — multiple/opaque sources, research, migration/port/decompile, toolchain assumptions, or material user-surface/design/layout authority.
- `references/ADAPTIVE_EXECUTION_AND_CONTEXT.md` — meaningfully multi-step/dependent/expensive/restart-sensitive work; continuation/context loss; optional derived Working View/Atlas when useful.
- `references/EVIDENCE_DRIVEN_DEBUGGING.md` — active runtime/visual defect investigation where falsification, source identity, or effective runtime geometry is material.
- `references/DELEGATION_CONTEXT.md` — any delegated implementation/advice/investigation lane.
- `references/VERIFICATION_AND_COMPLETION_ROUTING.md` — observable product verification, Core-First verifier, Independent Review, finding reconciliation, or project-defined external completion authority.

Do not read all five merely because they exist.

## Operating sequence

### 1. Establish the active truth

When material, identify the project/repository root, applicable instructions, relevant current Git/repository state, and exact project authorities for the active requirement. Use existing routing/index artifacts before broad rediscovery; validate stale/ambiguous routes against current code/runtime state.

### 2. Decide Core-First materiality

Core-First is material when the task can affect or discover ownership/authoritative state, reuse/duplication, capability/module/provider boundaries, consumer composition, producer convergence, extension seams, cross-boundary contracts, architecture repair/refactor, or a reusable feature whose correct owner/path is not settled.

If material, load `core-first-extension-architecture` fresh when required by context invalidation and apply it **in the primary context** before choosing the ownership/change boundary. Then direct execution and delegation are only execution modes beneath that decision.

Use the **local short path** only when: owner/edit location + semantics are clear; no material architecture/contract/producer/persistence/gate/authority/dependency decision remains; shared behavior/authoritative transitions are unchanged; and a direct bounded check proves correctness. File count/difficulty alone do not decide materiality. If a material architecture question appears, stop, load/apply Core-First, then continue.

### 3. Ground material prerequisites

If the grounded-preflight trigger is material, read `references/GROUNDED_EXECUTION_PREFLIGHT.md` and satisfy it before expensive execution. Listing a file, search result, library, tool, or log is not the same as understanding or consuming what it proves.

### 4. Frame, reconcile, and debug from evidence

If work is meaningfully multi-step/dependent/ambiguous/expensive/restart-sensitive, or current state must be recovered after continuation/compaction/new evidence, read `references/ADAPTIVE_EXECUTION_AND_CONTEXT.md`. Use a suitable native plan/task mechanism when available; otherwise the simplest equivalent state. Do not duplicate a native planner with a second Governance artifact.

For active runtime/visual defect investigation where negative evidence can change the causal model, read `references/EVIDENCE_DRIVEN_DEBUGGING.md` before continuing material diagnosis.

### 5. Choose direct execution or delegation

Prefer direct work when small/tightly coupled/cheaper to verify. If delegation materially improves parallelism, specialist depth, context isolation, or independent evidence, read `references/DELEGATION_CONTEXT.md` first. Delegated results remain evidence/input; the primary agent inspects and reconciles them before integration.

### 6. Route verification and completion

When any verification/review/completion trigger is material, read `references/VERIFICATION_AND_COMPLETION_ROUTING.md` and load the relevant sibling Skill JIT. Do not infer a user-facing outcome from logs, tests, tool success, or implementation state when the claim requires the real surface.

### 7. Report only what evidence proves

Before completion, the primary agent must be able to identify, as applicable: the canonical owner/change boundary; grounded material prerequisites; execution/replan state; delegation boundaries; actual automated/static checks; real-surface verification status; architecture-verifier status; Independent Review resolution; project-defined external completion result; and material host limitations.

## Freshness / context invalidation

Treat remembered Skill content and execution plans as cache. Re-read the required canonical Skill/authorities after a fresh context/session, major compaction/context loss, project/repository switch, relevant Skill/authority revision, major domain/workstream switch, material current-state change, or uncertainty that the required content was actually loaded.

Do not rebuild confidence by loading all Skills/history. Reload only what the active decision requires, inspect current state, reconcile assumptions/progress, and replan if the next best action changed.

## Host-neutral degradation

- no Skill metadata/discovery → use the routing capsule, then JIT-load the required canonical Skill;
- no native planner/task tracker → use the simplest lightweight execution state;
- no delegated agents → primary agent performs the lane; Core-First still applies in the primary context whenever material;
- no persistent delegated context → use fresh bounded delegated tasks instead;
- no explicit Skill injection → resolve/read the canonical Skill through an available file/context mechanism;
- no read-only/fresh isolation → use the strongest available isolation and disclose the limitation; do not falsely claim it;
- no suitable executable product-surface capability → affected observable claim remains `INCONCLUSIVE`/unverified rather than being replaced by logs/static evidence.

Do not build a custom orchestration, QA, planning, or computer-control platform merely to emulate a missing host feature unless the product itself requires one.

## Anti-patterns

Do not:
- turn the primary agent into a router that delegates Core-First away;
- preload every Skill or all project history "just in case";
- treat routing metadata, a plan, log output, a verifier PASS, or reviewer prose as project truth;
- continue a stale plan after material evidence changed owner/constraints/dependencies/feasibility/acceptance;
- treat discovered/listed sources or tools as consumed knowledge;
- let targeted workers invent architecture;
- reuse an implementation/advisor context as its own independent verifier;
- duplicate sibling procedure rules here when a JIT owner/reference already exists;
- bypass a project-defined external completion authority;
- encode provider-specific agent/planner/browser/computer-use APIs as portable law.
