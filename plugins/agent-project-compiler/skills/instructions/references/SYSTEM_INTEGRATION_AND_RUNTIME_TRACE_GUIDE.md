# System Integration, Ownership, and Runtime Trace Guide

# Current Precedence — Producer Convergence, Definitions and Implementation Anchors

Cross-system traces must respect the current role model: Project Authority Artifacts document; runtime Responsibility Owners decide/own state; Capability Contracts carry reusable semantics; Modules/Providers implement; Consumers compose.

Equivalent producer forms must converge at canonical semantic representation/interface + validation before domain behavior. Detect producer-specific bypasses as parallel implementation paths.

Review shared Definition/Profile objects separately from Runtime Instances/scoped mutable state; declarative shared definitions must not accidentally accumulate per-run/per-consumer mutation.


For approval-gated workflows, trace the boundary as `authorized preparation → exact gated transition → downstream state/effects`. The approval source/authority authorizes the transition; it does not become the runtime state owner. The canonical transition/state owner still performs the mutation through its declared contract. Record what is legal before approval and what exact mutation/effect remains forbidden until approval evidence exists.

For important traces maintain stable implementation anchors/breadcrumb IDs that point from System/Capability/Trace to actual code/data locations. Breadcrumbs are pointers, never duplicated rules. Reverse debugging follows visible failure/evidence → user/runtime flow → consumer/module/provider → capability contract → Responsibility Owner → implementation anchor → root-cause fix → forward re-test.

---


## Purpose

A project can look modular in files and still be incoherent at runtime. Services, configuration fields, APIs, Blueprints, and data definitions may exist while responsibilities are duplicated, state is written from several places, configuration is ignored, or the intended producer-to-consumer path is never connected.

This guide makes **semantic ownership and runtime integration** explicit without forcing premature class/framework design.

Core principle:

```text
Files/modules are not proof of architecture.
Architecture is ownership + state + decisions + contracts + dependency direction + runtime paths.
```

Use this layer for nontrivial projects where cross-system behavior, mutable state, configuration, extensibility, or important workflows can drift.

---

# 1. Single owner per material rule and state

For each important product/domain rule, identify one authoritative **decision owner**.
For each important mutable state, identify one authoritative **state owner**.

These may be different concepts from the producer of an event or the consumer of the result.

Example:

```text
Rule: Approval Required
Decision owner: Approval Policy System
Producer: Threshold/risk detection
Contract: ApprovalRequiredEvent
Consumer: Workflow Runtime
State owner(s): Workflow/approval lifecycle state
Effects: pause, notify reviewer, approve/reject/continue
```

Explicit exclusions:

```text
Threshold detector reports facts but does not decide approval consequences.
UI does not decide approval policy.
Persistence does not contain workflow-rule logic.
```

A material responsibility must not have multiple active authoritative owners unless the project explicitly defines coordinated/sharded ownership and its consistency rule.

---

# 2. Ownership matrix

Generate when material rules, mutable state, configuration, extensibility claims, or workflows cross system boundaries:

```text
contracts/SYSTEM_INTEGRATION.yaml
```

The contract should include an ownership matrix for important rules/state/capabilities.

Recommended semantic fields:

```yaml
ownership:
  RULE-APPROVAL-REQUIRED:
    kind: rule
    decision_owner: SYS-APPROVAL-POLICY
    state_owner: SYS-WORKFLOW-RUNTIME
    producers: [SYS-RISK-DETECTION]
    allowed_writers: [SYS-APPROVAL-POLICY]
    readers: [SYS-UI, SYS-NOTIFICATION]
    forbidden_owners: [SYS-UI, SYS-PERSISTENCE]
```

For state:

```yaml
  STATE-WORKFLOW-STATUS:
    kind: mutable_state
    state_owner: SYS-WORKFLOW-RUNTIME
    mutation_contracts: [CONTRACT-WORKFLOW-TRANSITION]
    allowed_writers: [SYS-WORKFLOW-RUNTIME]
    mutation_producers: [SYS-ACTION]
    readers: [SYS-ACTION, SYS-UI]
```

Distinguish:
- decision owner — decides a rule/outcome;
- state owner — owns the canonical mutable value/lifecycle;
- producer — emits information/request/result;
- allowed writer — is permitted to mutate the canonical state;
- reader/consumer — reads or reacts;
- side-effect owner — performs an external effect when separate.

Do not solve this by allowing every producer to write shared state directly.

---

# 3. Producer → Contract → Consumer runtime paths

Every material cross-system feature should have an intentional path:

```text
Producer
→ Contract / Data
→ Consumer
→ State owner / decision owner
→ Side effects / observable result
```

Example:

```text
External/UI Input
→ Input Adapter
→ CanonicalCommand
→ Workflow Controller
→ ActionRequest
→ Action Runtime
```

The compiler should capture semantics, not necessarily implementation classes.

Recommended trace fields:

```yaml
runtime_paths:
  TRACE-COMMAND:
    requirement_ids: [REQ-INPUT-01]
    producer: SYS-INPUT-ADAPTER
    contract: DATA-CANONICAL-COMMAND
    consumer: SYS-WORKFLOW-CONTROLLER
    decision_owner: SYS-ACTION-POLICY
    state_owner: SYS-WORKFLOW-RUNTIME
    side_effects:
      - presentation_request
      - external_effect_when_applicable
    invalid_path:
      - unsupported_command_is_rejected_or_ignored_by_defined_policy
    verification: [AC-INPUT-RUNTIME]
```

If producer, contract, consumer, owner, side effects, or invalid/failure behavior is materially unknown, the system/integration definition is not complete. Ask the user only when the missing choice is product-owned; otherwise delegate the implementation detail while preserving the required semantic relationship.

---

# 4. No parallel implementation

Before implementing or changing a responsibility:

```text
Find owner/contract/current path
→ Reuse
→ Extend
→ Correct
→ Intentionally replace/supersede
→ Create only if no authoritative path exists
```

Never create an independent second path merely because it is locally easier.

Examples of forbidden drift:
- a workflow/policy service exists but a page also advances the same canonical state independently;
- a canonical authorization service exists but individual pages reimplement permission logic;
- a pricing engine exists but PDF/report code recalculates totals independently;
- Input/Command service owns semantic commands but a consumer bypasses it and reads a provider-specific raw signal directly.

The duplicate-creation gate must inspect **behavioral ownership and call/data paths**, not only filenames or registry entries.

---

# 5. Feature maturity: Specified → Declared → Connected → Exercised → Verified

A declared API/config/schema is not an implemented feature.

Use these stages where useful:

```text
specified  = requirement/contract exists

declared   = code/config/API/schema field exists

connected  = runtime path actually consumes/uses it

exercised  = the intended path has executed

verified   = observed outcome matches the requirement with qualifying evidence
```

Only `verified` can satisfy a completion criterion that requires actual behavior.

Example:

```yaml
feature_trace:
  CPU-SELECTION:
    specified: true
    declared:
      - config_field_isCpu
      - StartMatch_parameter_isCpu
    connected:
      - creates_cpu_input_source: false
      - routes_to_selected_entity: false
    exercised: false
    verified: false
    status: not_implemented
```

This model supplements, not replaces, the Acceptance Matrix and Evidence Index.

---

# 6. Dead contract detection

An integration audit should actively look for **declared-but-dead contracts**:

- parameters never read;
- config/settings values never consumed;
- data-definition fields with no runtime path;
- services/modules with no callers/consumers;
- return values/results ignored when they carry required behavior;
- mutable state written from multiple unapproved locations;
- configuration overridden by constants/hard-coded branches;
- event/message types produced but never handled;
- feature flags that do not gate the claimed behavior;
- generated/UI options not connected to runtime state;
- consumer values copied from a canonical base when they were intended to remain relative/delta-based;
- declared modifiers whose merge operator/order is ambiguous or never executed.

A field existing is evidence only for `declared`, not `connected` or `verified`.

Use static analysis/search/AST/call-site inspection where practical, then runtime evidence for the behavior claim.

---

# 7. Contract-to-runtime / requirement trace

For each important option/rule/configuration, the implementation agent should be able to trace:

```text
Requirement / Rule / Setting
→ authority
→ base/profile/consumer/runtime value resolution when applicable
→ runtime reader/consumer
→ decision/state owner
→ observable effect
→ evidence
```

Example:

```text
Policy.AutoApprove = false
→ approval-policy contract
→ Approval Resolver reads setting
→ qualifying request does not auto-approve
→ run representative request
→ workflow remains pending approval
```

If a configuration claim has no runtime consumer or the consumer's behavior contradicts the contract, the criterion remains unverified.

Generate important traces in `contracts/SYSTEM_INTEGRATION.yaml` and bind them to Acceptance IDs.

---

# 8. Runtime graph over folder structure

Do not infer modularity from:

```text
InteractionService.cs
InputService.cs
FormService.cs
MatchService.cs
```

Instead reconstruct or inspect the relevant runtime graph:

- who owns state;
- who makes decisions;
- who may mutate state;
- producer → contract → consumer edges;
- dependency direction;
- cycles/backchannels;
- duplicate rule implementations;
- bypasses around canonical services/contracts.

Repository topology remains useful for navigation, but runtime responsibility topology is the architectural truth being checked.

---

# 9. God-object / God-service detection by domain ownership

Do not use line count as the main signal.

Warn when one implementation unit owns state or decisions belonging to several unrelated domains, for example one implementation unit owning:

```text
input normalization
workflow policy
persistence
authorization
pricing/calculation
external notifications
visual presentation
```


The audit should compare code-unit ownership against `SYSTEM_MAP` / `SYSTEM_INTEGRATION` responsibilities.

A large cohesive unit can be valid. A smaller unit crossing six authoritative domains can still be a God object.

---

# 10. Runtime-data-driven test

`Data exists` is not the same as `runtime is data-driven`.

For any requirement that claims configurable/data-driven/plugin/template behavior, define an operational extension test:

```text
What should be addable/changeable without changing which core code?
```

Examples:
- new entity with different moves/values without modifying EntityBrain/core interaction code;
- new report through schema/template/configuration without editing report engine code;
- new theme without editing application logic;
- new provider through the documented integration boundary without modifying consumers.

A system is data-driven only when runtime actually consumes the data through the canonical path.

When data layers use base values plus consumer-specific variation, also test **propagation semantics**: changing the canonical base should update consumers that use relative modifiers, while explicit `replace` consumers remain intentionally fixed. A copied resolved value is not a valid relative override.

---

# 11. Integration Audit

For nontrivial/cross-system work, add a distinct execution gate:

```text
System Decomposition
→ Ownership + Runtime Flow
→ Contracts / Blueprints
→ Implementation
→ Integration Audit
→ User-surface / black-box verification
```

The Integration Audit checks applicable items:

1. one authoritative decision owner per material rule;
2. one authoritative state owner per material mutable state;
3. producer → contract → consumer path is complete;
4. no unapproved parallel implementation/bypass exists;
5. declared fields/config/contracts have real consumers;
6. configuration actually controls the required runtime behavior;
7. no core rule is hidden in an unrelated system;
8. data definitions actually drive runtime where claimed;
9. cross-system writes occur only through declared mutation contracts/owners;
10. implementation units do not accidentally accumulate unrelated domain ownership;
11. feature maturity reaches the evidence level required by Acceptance;
12. runtime traces for changed material requirements still resolve on the current revision;
13. applicable `ARCHITECTURE_GUARDRAILS` are not violated by a plausible alternate/shortcut implementation.

Run the narrow affected audit after material cross-system changes and a broader audit before final completion. When `CAPABILITY_GRAPH.yaml`/current-change classification applies, also verify that reusable behavior was implemented at the classified canonical capability rather than first appearing inside the requesting consumer. Record the result in `verification/INTEGRATION_AUDIT.yaml` when the audit is release-relevant or needs to survive context loss. This evidence file is revision-bound and must not become a second ownership authority.

Use **Runtime Trace** as the canonical term for requirement/configuration-to-runtime tracing; "Requirement Trace" is an acceptable explanatory alias, not a separate contract type.

---

# 12. Generated project contract

Recommended project artifact:

```text
contracts/SYSTEM_INTEGRATION.yaml
```

Suggested shape:

```yaml
schema_version: 1

ownership:
  RULE-EXAMPLE:
    kind: rule
    decision_owner: SYS-A
    state_owner: SYS-B
    producers: [SYS-C]
    allowed_writers: [SYS-B]
    readers: [SYS-D]
    forbidden_owners: []

runtime_paths:
  TRACE-EXAMPLE:
    requirement_ids: [REQ-01]
    producer: SYS-C
    contract: DATA-EVENT-X
    consumer: SYS-A
    decision_owner: SYS-A
    state_owner: SYS-B
    side_effects:
      - effect: EFFECT-EXAMPLE
        owner: SYS-B
    failure_or_invalid_path: []
    acceptance_ids: [AC-01]

configuration_traces:
  CFG-EXAMPLE:
    source: SETTING-X
    consumed_by: SYS-A
    affects: RULE-EXAMPLE
    observable_effect: "..."
    acceptance_ids: [AC-02]

value_resolution_traces:
  VALUE-EXAMPLE:
    base_source: DATA-MASTER-X
    layers:
      - {source: DATA-MASTER-X, op: replace_base}
      - {source: CONSUMER-Y, op: add}
    effective_consumer: SYS-A
    base_change_should_propagate: true
    acceptance_ids: [AC-02]

extension_tests:
  EXT-EXAMPLE:
    claim: data_driven
    operation: "Add ..."
    must_not_require_changes_to:
      - IMPL-CORE-X
    acceptance_ids: [AC-03]
```

Scale the contract. A tiny static site may need none of this; a stateful application/service may need many entries.

---

# 13. Blueprint and implementation mapping

Behavior Blueprints describe intended bounded behavior. Implementation/Data Blueprints describe code/data responsibilities. `SYSTEM_INTEGRATION.yaml` describes **cross-system semantic edges and ownership**.

Do not duplicate complete system specs into the integration contract. Use stable IDs.

Implementation Blueprints for nontrivial units should declare:
- systems/responsibilities implemented;
- owned state;
- allowed mutation contracts;
- consumed/produced contracts;
- forbidden responsibilities where useful;
- verification hooks.

Contract validation should flag unresolved IDs and duplicate active owners where deterministically possible.

---

# 14. Compiler discovery questions

During planning/interview, ask only material user-owned questions but ensure the package can answer, where relevant:

- Who/what decides this rule?
- What is the authoritative state/source of truth?
- What produces the triggering information?
- What consumes it?
- What observable effects follow?
- What important failure/invalid path exists?
- What should be configurable/data-driven, and what must be possible without core-code changes?
- Could two systems reasonably believe they own the same decision/state?

The compiler should not invent classes/patterns unnecessarily. It establishes semantic contracts and leaves reversible implementation choices to the coding agent.

---

# 15. Coverage / completion invariant

Before package delivery for a nontrivial integrated system, ask:

> Could two future implementation units reasonably implement the same material rule, write the same state, or consume the same configuration differently because this package does not define ownership/runtime relationships?

If yes, clarify or record the intended relationship.

Before implementation completion, ask:

> Is every claimed feature merely declared, or can its actual runtime path and observable effect be traced and evidenced on the current revision?

Core invariant:

```text
Single authoritative ownership.
Intentional producer → contract → consumer paths.
No parallel behavior paths.
Declared != connected != verified.
Runtime graph outranks folder appearance.
Data-driven claims require runtime consumption.
Integration evidence is required before completion.
```

# Canonical definition/store/authoring convergence

When reusable domain definitions/content feed more than one consumer, treat the definition path as a first-class runtime/integration trace rather than allowing each surface to own its own representation.

Recommended semantic trace:

```text
Producer/editor/importer
→ Draft/Definition Contract
→ canonical validation
→ versioned publish/store/repository owner
→ canonical query/read model
→ Consumer A / Consumer B / ...
→ optional runtime snapshot/instance
→ scoped runtime modifiers/state
```

Rules:
- one canonical owner for definition identity/version/publish validity;
- all equivalent producers converge before domain behavior;
- builders/admin/AI authoring do not write around canonical validation;
- consumers do not cache/copy semantic fields as a second truth merely for convenience;
- Definition/Profile is distinct from Runtime Instance/scoped mutable state;
- when a running process must be stable against later content edits, snapshot/pin the exact definition version at the boundary;
- runtime effects/modifiers change runtime state/effective values, not the canonical published definition unless the user explicitly requests authoring.

Operational data-driven proof:
1. publish/change a definition once;
2. two representative consumers receive the same new canonical definition through their normal paths;
3. an already-created pinned runtime instance remains stable when required;
4. invalid/unpublished draft data cannot bypass validation into the representative runtime.

This is the general form of card/item/template/workflow/configuration/catalog definitions; do not hardcode any one domain's vocabulary into generated architecture.


# v2.27 Consumer access rights

When consumer/adapter boundaries are material, `SYSTEM_INTEGRATION.yaml` should state rights explicitly:

```yaml
consumer_access:
  CONSUMER-EXAMPLE:
    role: consumer_adapter
    allowed_reads: [STATE-A, QUERY-B]
    allowed_commands: [CMD-X]
    owned_writes: [STATE-LOCAL]
    forbidden_foreign_writes: [STATE-FOREIGN]
```

`allowed_commands` means the consumer may request a canonical owner transition through the declared contract; it does **not** grant direct ownership of the target state.

Core invariant:

```text
Consumer Composition != Domain Ownership
```

UI/renderers/input/persistence/importers/debug surfaces/agent interfaces must not acquire foreign-state ownership merely because they are convenient mutation entry points.


# Blueprint-boundary runtime conformance

Where implementation Blueprints/public module boundaries exist, runtime traces should cross systems through declared public contracts rather than internal implementation anchors.

Audit material edges for:

```text
producer/consumer
→ declared public contract
→ canonical system/capability owner
→ implementation boundary
→ owned state/effect
```

Direct calls into a foreign owner's known internal helper/store/state path are boundary bypasses unless explicitly admitted as part of the public contract.


# v2.30 Definition-to-instance trace

For materially data-driven/repeatable types, a runtime trace may include:

```text
authoring/producer
→ validated Definition/Profile
→ Definition-Type/capability resolution
→ generic runtime/surface consumer
→ owned runtime instance state
→ observable effect/output
```

This trace proves that a definition is actually consumed by the canonical engine path rather than existing as unused registry data.

Modifiers should trace:

```text
Modifier Definition
→ declared target seam
→ deterministic resolution/composition
→ canonical owner behavior/state
→ observable effective result
```

A modifier or generic consumer may not become a foreign writer of another owner's state merely because it participates in composition.


# v2.31 Composition Coherence Invariants

This guide owns the **cross-system relationship contract**, not the underlying system state.

Use a Composition Invariant when correctness depends on multiple systems/projections agreeing about one canonical relation.

Required semantics:

```text
Invariant ID
canonical source/owner
source contract/data/state IDs
dependent consumers/projections
derivation/update semantics
invalidation/recompute/regeneration rule
forbidden local ownership/override
Acceptance/evidence
```

Common update semantics may include:
- live read;
- command/event propagation;
- deterministic derivation;
- recompute;
- regenerate;
- transactional synchronization;
- explicitly versioned snapshot.

Choose project-native semantics; do not invent synchronization machinery when a simple canonical read suffices.

## Repair trace

For a reported defect:

```text
observable symptom
→ affected Acceptance
→ invariant
→ canonical source/owner
→ dependent projections
→ actual drift/bypass
→ canonical repair
→ affected evidence rerun
```

If the symptom is truly local, stop at the local owner. If several consumers independently need the same corrective knowledge, treat that as evidence of missing canonical derivation or missing invariant rather than copying the fix.

## Invariant evidence

A material invariant is not Verified because its IDs resolve.

Evidence should exercise a representative change or state and observe all required projections after settling. Where deterministic projection is possible, compare derived outputs to the same canonical input/source revision.
