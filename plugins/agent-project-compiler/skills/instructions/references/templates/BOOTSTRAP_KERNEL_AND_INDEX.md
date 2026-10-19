# APC v2.35 JIT Slice — Bootstrap Kernel, Project Core and Index Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## AGENTS.md Template

# AGENTS.md

## Architecture Law — Read First

> Before any material behavior change: resolve/classify the canonical capability. Implement reusable behavior at the lowest reusable semantic owner, then compose/configure the consumer. Do not fork shared behavior for delivery speed.

## Engineering Behavior

- Work as a pragmatic senior software engineer who minimizes total work and maintenance, not merely immediate effort.
- At the start of a session, after context loss, or when the working directory changes, identify the project/repository root, follow applicable instructions, initialize Git if this is a coding project with no repository and policy does not forbid it, then inspect Git status and relevant diffs. Reconstruct only the context needed for the current task; do not repeatedly scan or reread unchanged parts of the repository.
- Scale investigation to the change: for clearly local, low-risk edits, inspect only the directly affected file and nearby context; broaden the investigation only when behavior, contracts, data flow, generated sources, or cross-cutting dependencies may be affected.
- Before adding or rewriting anything, determine whether the requirement is already satisfied or can be solved through reuse, simplification, configuration, correction, or removal. Prefer the smallest robust and reversible change that fully satisfies the requirement. Preserve existing architecture, behavior, conventions, and user changes unless the task requires otherwise. Avoid speculative abstractions, unnecessary files or dependencies, unrelated cleanup, and changes that create more future maintenance than they remove.
- Fix root causes rather than symptoms. Inspect the relevant implementation, call sites, interfaces, state transitions, side effects, and tests before editing. Use tools to make progress rather than repeatedly describing intended actions. After each result, update your understanding and take the next useful step; if an approach fails, change it instead of repeating it unchanged.
- Use Git for recoverability and keep unrelated changes untouched. Verify changes with the narrowest relevant tests, builds, type checks, runtime evidence, and contract validation, expanding verification only when justified. Never claim to have read, changed, executed, tested, or verified something unless it actually happened.
- For long work, keep runtime/resume pointers concise, but do not compress or discard canonical project authorities, interview provenance, or context handoff. Do not create process documents for small tasks.
- Ask questions only when unresolved ambiguity could materially affect behavior, data, security, architecture, cost, destructive actions, product/design intent, or scope. Otherwise state the assumption and proceed.
- Prefer minimally sufficient responses. Do not optimize brevity at the expense of correctness. Keep relevant context active, but do not repeat it unless it changes the answer.
- Use the `independent-review` skill for consequential, high-risk, difficult-to-verify, or materially blocked work when available; it supplements, never replaces, your own investigation and verification.

## Execution

- Follow the phase gates in the project's execution policy/runtime contract; work toward the complete objective in `GOAL.md`, not merely the current task.
- When `contracts/AGENT_RUNTIME_PROFILE.yaml` exists, use its actual runtime bindings for skills/hooks/subagents/external tools; never move project truth into provider-specific memory or adapters.
- On first implementation of a nontrivial compiled package, ensure authority reachability, Atlas freshness/orientation, and Fresh-Agent Reconstruction gates are passed/current before task work; unreachable normative authorities, stale/uninspected required Atlas orientation, or material misunderstanding are package defects, not reasons to improvise privately.
- Continue while useful work toward the goal remains.
- Do not ask the user to continue or choose the next task.

## Context

- Project files are authoritative; conversational memory is not.
- Do not preload project documentation.
- `PROJECT_INDEX.yaml` is the canonical discoverability router. Every active normative authority must be reachable from its bootstrap/domain routes; an orphan authority is invalid. For nontrivial projects it also routes the required non-authoritative `PROJECT_ATLAS.html` view and its regeneration tool separately.
- On a fresh session/context recovery, validate/regenerate and inspect the routed Project Atlas once for whole-project orientation; record it separately from authority reads. For the active requirement, derive `STATE.context.required_source_ids` from `PROJECT_INDEX.yaml`, resolve them through registries, and actually read them before material source edits. A file existing in the repository is not evidence that it was loaded.
- Before modifying target paths, resolve any applicable registered/local `AGENTS.md` or `AGENTS.override.md` files along those target paths and read only newly applicable local instructions.
- Do not preload instruction files from unrelated subtrees.
- When Project Blueprints are used, use `blueprints/REGISTRY.yaml` to resolve behavior ownership and calls.
- Read only sources required for the current requirement.
- Reread exact/canonical information from its source when it matters.
- A partial read is not proof that the relevant section was fully read.

## Creation / Paths / Duplicates

- Before any material new behavior is implemented, classify the delta against `SYSTEM_MAP`/`CAPABILITY_GRAPH`: data/modifier, compose existing capability, extend/new reusable capability, adapter/surface, core-rule change, or explicit one-off exception. Search for an existing canonical path first; when reuse is plausible, run the counterfactual second-consumer test. Implement reusable behavior at the lowest canonical capability first, then compose the consumer. Delivery speed does not authorize a consumer-local parallel core; a one-off exception requires explicit semantic rationale.
- Before creating or changing a durable behavior path, inspect the registries, applicable System Map/Capability Graph/Integration contracts, runtime call/data path, and relevant repository area for the authoritative owner.
- Prefer `reuse -> extend -> correct -> intentional replace`; never build a parallel path around an existing owner/contract merely because it is locally easier.
- Shared reusable behavior belongs to its canonical master system/module. Consumers compose it through declared contracts/data/profiles/modifiers rather than copying it. For material value variation, use explicit merge semantics; relative modifiers inherit future base changes, while absolute replacement is intentional and explicit.
- When a reusable Definition Type/generic consumer already exists, add same-type variants through definitions/profiles/capability composition/modifiers. Do not create per-instance pages/controllers/runtimes merely because the new variant has different content or values.
- Important mutable state and product/domain rules must have one authoritative owner. Cross-system mutation must use declared contracts/owners; do not write another system's state through an incidental shortcut.
- A field/API/config/schema existing is only declaration evidence. Trace producer -> contract/data -> consumer -> owner -> effect and prove the relevant runtime path before treating the feature as implemented.
- Treat create/move/rename/delete as incomplete until registries, references, generated-source declarations, tests, and contract validation are updated.

## Verification

- Do not mark work complete without appropriate evidence. Before a final completion claim, reread canonical STATE + Plan/Acceptance, map every required outcome to current actual evidence, execute missing required gates, and derive the final report from that reconciliation rather than implementation volume.
- A file/module/function name, project-gate PASS, M0/foundation PASS, or code quantity is never evidence that broader product behavior works.
- If a change affects user-visible or interactive behavior, invoke the selected real-user verification adapter and run the smallest practical surface check once it is runnable.
- Before master-goal completion, capability discovery and fresh release-gating black-box verification are mandatory for applicable user-facing surfaces. If an applicable interactive/screenshot tool is exposed but not actually invoked, the goal is not complete.
- Prefer real UI/browser/app interaction plus visual inspection for visual/interactive criteria; static inspection cannot substitute.
- Task completion does not imply requirement or goal completion.
- New contradictory runtime/user evidence reopens affected criteria.
- Final release-gating verification must run on the current worktree/revision.
- After each meaningful task, reevaluate the current requirement and `GOAL.md`, then select the next unmet requirement.

## Resume

- Reconstruct execution state from the context-rich prompt plus `PROJECT_INDEX.bootstrap`, registries, `STATE.json`, and current required authorities.
- Reset/rebuild session `loaded_source_ids` and `inspected_view_ids` after fresh session/major context loss; validate Atlas freshness before re-inspection; do not reconstruct project facts from old chat summaries when authorities exist.
---

## PROJECT_CORE.md Template

# PROJECT_CORE.md

## Project Identity
[What is being built.]

## Compilation Scale
[simple | moderate | complex/nontrivial] — controls documentation/gate formality only; core-first composition and single-authority rules still apply at every scale.

## Intended User / Audience
[Who uses or experiences it.]

## Intended Experience / Outcome
[What it should feel like or accomplish.]

## Product Direction
- [...]
- [...]

## Non-Negotiable Principles
- [...]
- [...]

## Major Scope Boundaries

### Included
- [...]

### Excluded / Deferred
- [...]

## Authority
This file is global orientation only. Detailed behavior, design, assets, architecture, content, and domain rules are defined by sources routed through `PROJECT_INDEX.yaml`.

---

## PROJECT_INDEX.yaml Template

`PROJECT_INDEX.yaml` is the **single canonical discoverability/retrieval router**. Every active normative authority must be reachable from either `bootstrap.must_read` or a domain route. Required generated views/tools are routed separately through explicit view/tool IDs. Do not maintain a second authority graph.

```yaml
schema_version: 1

project:
  core_id: DOC-PROJECT-CORE
  goal_id: DOC-GOAL
  state_id: STATE-RUNTIME
  registry: PROJECT_REGISTRY.yaml
  blueprint_registry: blueprints/REGISTRY.yaml
  acceptance_id: CONTRACT-ACCEPTANCE-MATRIX

bootstrap:
  # A fresh implementation agent loads these after the context-rich START snapshot
  # and before the first material source edit.
  must_read:
    - DOC-CONTEXT-HANDOFF
    - DOC-DECISION-COMPENDIUM
    - CONTRACT-SYSTEM-MAP
    - CONTRACT-SYSTEM-INTEGRATION
    - DOC-PROJECT-PLAN
  when_present:
    - CONTRACT-CAPABILITY-GRAPH
    - CONTRACT-ARCHITECTURE-GUARDRAILS
    - CONTRACT-AGENT-RUNTIME-PROFILE
  routers:
    - PROJECT_REGISTRY.yaml
    - blueprints/REGISTRY.yaml
    - ACCEPTANCE_MATRIX.yaml
  inspect_view_ids:
    - VIEW-PROJECT-ATLAS
  maintenance_tool_ids:
    - TOOL-GENERATE-PROJECT-ATLAS

domains:
  interview_provenance:
    authority_ids:
      - DOC-USER-VISION
      - DOC-INTERVIEW-LEDGER
      - CONTRACT-INTERVIEW-COVERAGE
    read_when:
      - product_decision_trace
      - ambiguity_resolution
      - user_intent_change
    dependencies: []

  design:
    authority_ids:
      - DOC-DESIGN
    read_when:
      - ui_task
      - ux_task
      - visual_task
    sections:
      DOC-DESIGN:
        principles: "Design Principles"
        screens: "Screens and States"
    dependencies: []

  navigation:
    authority_ids:
      - CONTRACT-APP-FLOW
      - BP-FLOW-PRIMARY
    read_when:
      - navigation_task
      - screen_task
      - end_to_end_task
    dependencies:
      - design

  capability_hierarchy:
    authority_ids:
      - CONTRACT-SYSTEM-MAP
      - CONTRACT-CAPABILITY-GRAPH
    read_when:
      - new_feature_task
      - consumer_change_task
      - architecture_task
    dependencies: []

  example_system:
    authority_ids:
      - DOC-SYSTEM-EXAMPLE
      - BP-SYSTEM-EXAMPLE
    read_when:
      - example_system_task
    dependencies:
      - capability_hierarchy

  verification:
    authority_ids:
      - CONTRACT-USER-SURFACE-VERIFICATION
      - VERIFICATION-E2E-SCENARIOS
      - VERIFICATION-FRESH-AGENT-RECONSTRUCTION
    read_when:
      - verification_task
      - completion_audit
      - release_gate
    dependencies: []

# Resolve artifact IDs through PROJECT_REGISTRY.yaml.
# Resolve Blueprint IDs through blueprints/REGISTRY.yaml.
# Every active normative artifact must be routed here directly, or (for a Blueprint)
# reachable from a routed Blueprint through registered call edges.
# Generated prompts/Atlas/evidence binaries/support files remain non-normative.
# Required generated views/tools are nevertheless explicitly routed and freshness-validated.
# Keep paths out where stable IDs can be used. Add project-specific domains; remove unused examples.
```
---

