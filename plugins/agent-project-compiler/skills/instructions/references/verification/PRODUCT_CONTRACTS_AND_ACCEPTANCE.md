# Delivery and Verification Guide

# Current Precedence — v2.29 Verification Truth, Representative Product Paths and Review Projections

Delivery is blocked when material interview answers are preserved only in the Ledger/chat but not materialized into canonical destinations, or when required source-ingest/reference mappings do not reconcile.

Evidence must prove the claim at the scope required by Acceptance/phase admission. When downstream conclusions depend on representative product inputs/pathways, explicitly distinguish synthetic fixtures/mocks/unit/contract exercises, partial/nonrepresentative integrations, and representative canonical product data/content/configuration + real user/external paths.

Synthetic evidence remains useful but keeps its true scope. It can prove technical execution/integration; it does **not automatically** prove representative product-path behavior or authorize downstream tuning/balance/performance/usability/release conclusions. Re-run or supplement at the stronger scope when required.


## Approval evidence keeps its own authority scope
Where a project requires human/project approval for an exact transition, technical evidence and approval evidence are different things. Build/test/runtime success may prove readiness for the transition; it does not prove permission to cross it. Approval evidence must identify the approving authority and be scoped/current enough for the transition/revision required by project truth.

Likewise, absence of approval does not invalidate evidence from authorized reversible preparation. Report the real state precisely: preparation/readiness may be verified while the gated transition remains pending. Do not promote `ready` to `approved/crossed`, and do not downgrade legitimate preparation to `blocked` merely because the later transition still awaits approval.

Core rules: `TECHNICALLY EXECUTABLE != ADMITTED FOR PRODUCT CONCLUSIONS`; `NEXT ATTRACTIVE TASK != NEXT ADMISSIBLE TASK`. For reusable architecture claims also distinguish `INTEGRATION PROVEN` from `REUSE/COMPOSITION PROVEN` and from `PRODUCT BREADTH`; consumer count alone never upgrades the architecture claim.

---


## Purpose

A detailed specification can still fail if the coding agent:
- builds subsystems before the user-facing path;
- never wires those subsystems into the normal UI;
- hard-codes setup that was meant to be selectable;
- marks acceptance criteria verified using weaker evidence than the criterion requires;
- forgets required screens/actions after context loss.

This guide converts product requirements into machine-readable execution and verification contracts.

---

## 1. Walking-Skeleton Rule

For interactive applications, games, and vertical slices:

**Establish the complete normal-user route early, using placeholders where necessary.**

Example:

```text
Boot
→ Main Menu
→ Setup
→ Selection
→ Rules
→ Match/Primary Experience
→ Pause
→ Results
→ Replay/Return
```

Before deep subsystem work is considered product progress, the agent should be able to traverse the intended top-level route in a running build.

Placeholder content is acceptable during the skeleton phase.
Missing required route nodes are not.

This prevents a technically rich backend from being mistaken for a usable vertical slice.

---

## 2. Machine-Readable Contracts

For nontrivial projects generate:

### `ACCEPTANCE_MATRIX.yaml`
Required unless the goal is trivially small.

Purpose:
Map each acceptance criterion to:
- authoritative sources;
- required user-visible capability;
- dependencies;
- required evidence types;
- forbidden insufficient evidence;
- current verification state.

### `contracts/SYSTEM_INTEGRATION.yaml`
Generate when important rules/state/configuration cross system boundaries.

Purpose:
Record authoritative rule/state ownership, producer-contract-consumer runtime paths, configuration traces and operational extension/data-driven boundaries. It prevents modular-looking files from hiding duplicate ownership or dead contracts.

### `contracts/APP_FLOW.yaml`
Generate for every nontrivial multi-screen, multi-state, lifecycle- or workflow-driven product unless an equivalent canonical workflow graph already exists.

Purpose:
Represent the **complete required product/user lifecycle**, not only the first runnable path. Nodes may be screens, modes, workflow states or externally observable lifecycle states. It must cover normal entry, setup/configuration, primary experience, interruption/recovery, completion/result, persistence/resume/progression and return/replay paths when applicable.

### `contracts/INPUT_ACTIONS.yaml`
Generate when keyboard/device/touch/shortcuts/remapping matter.

Purpose:
Define the complete semantic action registry and required defaults/contexts.

### `contracts/CONTENT_REGISTRY.yaml`
Generate when user-selectable or data-driven content matters.

Examples:
entities, stages, rulesets, products, document types, workflows, modules.

Purpose:
Prevent hard-coded test content from masquerading as a selectable/data-driven feature.

### `verification/AUTHORITY_REACHABILITY.yaml`
Generate for every nontrivial compiled package.

Purpose:
Prove that every active normative authority/required Blueprint is discoverable from the guaranteed bootstrap/JIT router graph. The report is generated evidence from `PROJECT_INDEX.yaml` + registries, never a second routing authority. Any unreachable normative node makes the package incomplete.

### `verification/FRESH_AGENT_RECONSTRUCTION.yaml`
Generate for nontrivial compiled packages before implementation task decomposition/final delivery.

Purpose:
Prove that an agent without the original chat can reconstruct the intended product model, system rationale, guardrails, example/reference semantics, representative flow and authority routing. Detailed policy lives in `FRESH_AGENT_RECONSTRUCTION_GUIDE.md`. Include `AC-PACKAGE-RECONSTRUCTION` (or equivalent stable ID) as a required package-quality criterion.

### `verification/ABSTRACTION_TESTS.yaml`
Generate when modularity/data-driven/extensibility claims require representative/adversarial architecture-expression tests. These examples are not automatically shipping content.

When reuse is an acceptance claim, record the **Representative Proof Set**: the canonical walking-skeleton/reference case that proves integration, the minimum heterogeneous cases that cover material variation axes, and why additional similar consumers are not required for architecture acceptance. Reuse proof is complete when those cases exercise the same canonical owners/capabilities without consumer-local rule duplication/bypass. More similar consumers then provide product/content breadth or scale evidence unless they introduce a new semantic variation axis.

### `verification/INTEGRATION_AUDIT.yaml`
Generate when material cross-system ownership/runtime traces are implemented or changed and the audit result must be durable/release-gating.

Purpose:
Record revision-bound results for ownership conflicts, producer-contract-consumer closure, parallel/bypass paths, dead contracts/configuration, data-driven runtime consumption and feature maturity. It is evidence only; `SYSTEM_INTEGRATION.yaml` remains the semantic authority.

### `verification/E2E_SCENARIOS.yaml`
Generate when completion requires multi-step runtime behavior.

Purpose:
Define exact end-to-end scenarios that prove user/external-visible success.

These files are compact contracts. Detailed explanations remain in `docs/`.

---

## 3. APP_FLOW Contract

Each required screen/state should have a stable ID.

Recommended fields:

```yaml
screens:
  main_menu:
    required: true
    purpose: Entry point
    authority_ids: [DOC-DESIGN]
    authority_section: Main Menu
    implementation_ref: null
    reads: []
    writes: []
    actions:
      play:
        to: player_setup
      options:
        to: options
      quit:
        to: exit

  player_setup:
    required: true
    actions:
      continue:
        to: character_select
      back:
        to: main_menu
```

Also define:
- entry state;
- terminal/completion states;
- normal-user setup/configuration path;
- primary experience states;
- interruption/pause/cancel/back semantics;
- result/completion and replay/return routes;
- persistence/resume/progression transitions where applicable;
- error/recovery routes;
- persistent navigation/workflow owner;
- which state/data survives each transition;
- `plan_stage` for every required node;
- `acceptance_ids` for every required node;
- governing design/reference authority IDs for material user surfaces;
- owning System/Capability IDs where applicable.

### Navigation invariant

Individual screens must not own independent hidden copies of global navigation/setup state.

The implementation must have one coherent navigation/state owner or equivalent architecture.

Every required APP_FLOW transition must be exercised in runtime verification.

---

## 4. INPUT_ACTIONS Contract

Do not represent a complete remapping system with two example bindings.

Define the semantic registry:

```yaml
actions:
  ui_confirm:
    contexts: [ui]
    required: true
    remappable: true
    defaults:
      keyboard: Enter
      device: primary_action

  light_attack:
    contexts: [primary_flow]
    required: true
    remappable: true
    defaults:
      keyboard: J
      device: secondary_action
```

Recommended fields:
- stable action ID;
- display label;
- contexts;
- required/optional;
- default keyboard/device/touch bindings where applicable;
- remappable;
- conflict policy;
- persistence requirement;
- acceptance criteria.

UI should be generated from or validated against the registry where practical.

A remapping feature is incomplete if required semantic actions are missing from the user-facing configuration path.

---

## 5. CONTENT_REGISTRY Contract

When the product claims selectable/data-driven content, define it explicitly:

```yaml
items:
  standard:
    required_for_slice: true
    source: data/items/standard
  alternate:
    required_for_slice: true
    source: data/items/alternate

providers:
  primary:
    required_for_slice: true
    source: config/providers/primary

profiles:
  default:
    required_for_slice: true
```

The normal UI must consume the registry/data source.

A hard-coded runtime choice does not satisfy "selectable" or "data-driven".

---

## 6. ACCEPTANCE_MATRIX Contract

Example:

```yaml
criteria:
  AC-15:
    title: User-facing shell and navigation
    status: unverified
    sources:
      - docs/GAME_FLOW.md
      - docs/UI_AND_MENUS.md
      - contracts/APP_FLOW.yaml
    depends_on: []
    evidence_required:
      - type: runtime_flow
        environment: exported_build
        input: keyboard
      - type: runtime_flow
        environment: exported_build
        input: primary_input_device
      - type: visual_review
    insufficient_evidence:
      - code_inspection
      - scene_exists
      - build_compiles

  AC-22:
    title: Shareable build
    status: unverified
    depends_on: [AC-14, AC-15, AC-16, AC-18]
    evidence_required:
      - type: e2e_scenario
        scenario: primary_full_match
        environment: exported_build
```

Statuses:
- `unverified`
- `in_progress`
- `verified`
- `needs_recheck`
- `blocked`

Do not use `verified` without recorded qualifying evidence.

---

