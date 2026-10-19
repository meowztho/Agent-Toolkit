# APC v2.35 JIT Slice — Execution, Runtime, Capability, Integration and Skill Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## `contracts/EXECUTION_POLICY.yaml` Template

```yaml
schema_version: 1

phases:
  - BOOTSTRAP_REPOSITORY
  - DISCOVER_CAPABILITIES
  - BIND_AGENT_RUNTIME
  - LOAD_BOOTSTRAP_CONTEXT
  - VERIFY_AUTHORITY_REACHABILITY
  - VALIDATE_PROJECT_RECONSTRUCTION   # once for fresh compiled projects when required
  - SELECT_REQUIREMENT
  - RESOLVE_REQUIRED_AUTHORITIES
  - LOAD_JIT_CONTEXT
  - VERIFY_CONTEXT_LOAD_GATE
  - CLASSIFY_CHANGE_ARCHITECTURE
  - RESOLVE_SKILLS_FOR_REQUIREMENT
  - BLUEPRINT_OR_REUSE
  - IMPLEMENT_UNIT
  - VERIFY_UNIT
  - INTEGRATE
  - VERIFY_INTEGRATION
  - AUDIT_SYSTEM_INTEGRATION      # when material cross-system behavior changed
  - VERIFY_USER_SURFACE
  - HYGIENE
  - RECORD_MILESTONE

finalization:
  - FINAL_CONTRACT_AUDIT
  - FINAL_BUILD_TEST
  - FINAL_USER_SURFACE_GATE
  - INDEPENDENT_REVIEW_IF_TRIGGERED
  - FINAL_GIT_CHECK

rules:
  walking_skeleton_priority: true
  user_surface_after_observable_change: true
  user_surface_tool_invocation_required_when_available: true
  final_black_box_required_for_user_facing_product: true
  scoped_hygiene_after_green_requirement: true
  authority_reachability_gate: true
  required_authority_load_gate_before_source_edit: true
  reconstruction_gate_before_first_implementation: true
  core_first_change_classification_before_source_edit: true
```


---

## `contracts/AGENT_RUNTIME_PROFILE.yaml` Template

Generate for nontrivial autonomous projects when the execution harness offers customizable agent primitives. Populate from actual discovery, not model-name assumptions.

```yaml
schema_version: 1

runtime:
  provider: null
  client_or_harness: null
  version: null

capabilities:
  hierarchical_instructions:
    available: false
    mechanism: null
  agent_skills:
    available: false
    standard_compatible: null
    project_path: null
    supports_multi_skill_composition: null
  lifecycle_hooks:
    available: false
    session_start_context: null
    user_prompt_context: null
    pre_tool_gate: null
    post_tool_observer: null
    pre_compact: null
    post_compact: null
    stop_or_finish_gate: null
  subagents:
    available: false
    isolated_context: null
    parallel: null
  mcp_or_external_tools:
    available: false
    mechanism: null
    permission_model: null
    read_only_mode_available: null
    trust_reviewed: false
  persistent_memory:
    available: false
    canonical_project_truth_allowed: false
  workflows_or_commands:
    available: false
  worktrees_or_sandboxes:
    available: false

bindings:
  instruction_kernel: AGENTS.md
  provider_adapter: null
  skill_router: null
  architecture_law_context_hook: null
  authority_reachability_validator: null
  required_source_load_observer: null
  required_source_gate_hook: null
  change_classification_gate_hook: null
  context_rehydration_hook: null
  completion_gate_hook: null
  integration_audit_hook: null
  reconstruction_executor: null
  independent_review_executor: null
  external_tool_adapter: null

fallbacks: []
```

Rules:
- product truth never lives only in this profile or a provider customization;
- provider-specific instruction files are thin generated adapters;
- semantic lifecycle events map to provider-specific hook names here;
- if hooks are unavailable, deterministic validators remain explicit runtime gates;
- memory is non-canonical and must not be required for reconstruction.

---

## `verification/TOOL_CAPABILITIES.yaml` Template

```yaml
schema_version: 1

capabilities:
  interactive_desktop:
    available: false
    adapter: null
    verified_by: null

  browser_interaction:
    available: false
    adapter: null
    verified_by: null

  screenshot_capture:
    available: false
    adapter: null
    verified_by: null

  engine_runtime:
    available: false
    adapter: null
    verified_by: null

selected:
  user_surface_adapter: null
  screenshot_adapter: null
  fallback_adapter: null

surface_gate:
  required: false
  final_scenario: null
  require_interactive_invocation: false
  require_visual_artifacts: false
  status: not_evaluated
```

Populate from tools actually exposed by the current harness/session, not from assumptions about the model/provider.


---

## Implementation Blueprint `*.impl.bp.yaml` Template

```yaml
blueprint:
  id: BP-IMPL-EXAMPLE
  responsibility_key: IMPL.EXAMPLE
  type: implementation_boundary
  version: 1
  implements: []
  artifact_ids:
    - IMPL-EXAMPLE-FACADE
  internal_artifact_ids: []

boundary:
  kind: module_or_component
  public_entry_artifact_id: IMPL-EXAMPLE-FACADE
  consumers_must_not_import_internal_artifacts: true

interface:
  public_operations: []
  inputs: []
  outputs: []

state:
  owns: []
  must_not_own: []

dependencies:
  reads: []
  calls_public_boundaries: []
  forbidden_internal_dependencies: []

operations:
  example_operation:
    preconditions: []
    postconditions: []
    failure_behavior: []

invariants: []

verification:
  unit: []
  integration: []
  debug_probes: []
```

Use for a nontrivial module/service/component/controller/adapter or cohesive code boundary with an independently meaningful responsibility. One Blueprint may anchor multiple internal source files; do not force one Blueprint per class/function.


---

## Data Blueprint `*.data.bp.yaml` Template

```yaml
blueprint:
  id: BP-DATA-EXAMPLE
  responsibility_key: DATA.EXAMPLE
  type: data_structure
  version: 1
  artifact_id: DATA-EXAMPLE

schema:
  fields: []

collection_invariants: []

operations:
  - create
  - lookup
  - update

serialization:
  required: false

verification:
  tests: []
  debug_probes: []
```

Use for shared/stateful/invariant-rich schemas, registries, stores, queues, catalogs, or collections. Do not Blueprint trivial local arrays/lists.

---

## `contracts/CAPABILITY_GRAPH.yaml` Template

Generate when reusable semantic hierarchy below/among master systems matters.

```yaml
schema_version: 1

capabilities:
  CAP-EXAMPLE:
    parent_system: SYS-EXAMPLE
    parent_capability: null
    kind: reusable_capability
    responsibility: "[semantic reusable behavior]"
    owns: []
    parameters: []
    consumers: []
    authority_ids: []
    acceptance: []
```

Rules:
- top-level domain ownership remains in `SYSTEM_MAP.yaml`;
- hierarchy is semantic, not a class/folder tree;
- consumer values/modifiers do not become capability ownership;
- runtime edges must agree with `SYSTEM_INTEGRATION.yaml`;
- new behavior requested for a consumer is classified before implementation and descends to the lowest reusable capability that should own it.

---

## `contracts/SYSTEM_INTEGRATION.yaml` Template

Generate for nontrivial projects when material rules/state/configuration cross system boundaries. Keep detailed behavior in system authorities; this contract records semantic ownership and cross-system runtime edges.

```yaml
schema_version: 1

ownership:
  RULE-EXAMPLE:
    kind: rule
    decision_owner: SYS-EXAMPLE-A
    state_owner: SYS-EXAMPLE-B
    producers: [SYS-EXAMPLE-C]
    allowed_writers: [SYS-EXAMPLE-B]
    readers: [SYS-EXAMPLE-D]
    forbidden_owners: []

  STATE-EXAMPLE:
    kind: mutable_state
    state_owner: SYS-EXAMPLE-B
    mutation_contracts: [DATA-EXAMPLE-RESULT]
    mutation_producers: [SYS-EXAMPLE-A]
    allowed_writers: [SYS-EXAMPLE-B]
    readers: [SYS-EXAMPLE-A, SYS-EXAMPLE-D]

runtime_paths:
  TRACE-EXAMPLE:
    requirement_ids: [REQ-EXAMPLE]
    producer: SYS-EXAMPLE-C
    contract: DATA-EXAMPLE-COMMAND
    consumer: SYS-EXAMPLE-A
    decision_owner: SYS-EXAMPLE-A
    state_owner: SYS-EXAMPLE-B
    side_effects:
      - effect: EFFECT-EXAMPLE
        owner: SYS-EXAMPLE-B
    failure_or_invalid_path: []
    acceptance_ids: [AC-EXAMPLE]

composition_invariants:
  INV-EXAMPLE:
    statement: "[relationship that must remain coherent]"
    canonical_source_owner: SYS-EXAMPLE-A
    source_ids: [STATE-EXAMPLE]
    dependent_projections:
      - consumer: SYS-EXAMPLE-B
        relation: "[derived/read/propagated relationship]"
        update_semantics: deterministic_derivation
      - consumer: SYS-EXAMPLE-D
        relation: "[second required projection]"
        update_semantics: live_read
    forbidden_local_overrides: []
    acceptance_ids: [AC-EXAMPLE]

configuration_traces:
  CFG-EXAMPLE:
    source: SETTING-EXAMPLE
    consumed_by: SYS-EXAMPLE-A
    affects: RULE-EXAMPLE
    observable_effect: "[required runtime effect]"
    acceptance_ids: [AC-EXAMPLE]

value_resolution_traces:
  VALUE-EXAMPLE:
    base_source: DATA-MASTER-DEFINITION
    layers:
      - source: DATA-MASTER-DEFINITION
        op: replace_base
      - source: PROFILE-EXAMPLE
        op: add
      - source: CONSUMER-EXAMPLE
        op: add
    consumer: SYS-EXAMPLE-A
    base_change_should_propagate: true
    acceptance_ids: [AC-EXAMPLE]

extension_tests:
  EXT-EXAMPLE:
    claim: data_driven
    operation: "[add/change content/config]"
    must_not_require_changes_to: [IMPL-CORE-EXAMPLE]
    acceptance_ids: [AC-EXAMPLE]
```

Rules:
- one active decision owner per material rule and one active state owner per material mutable state unless an explicit coordinated-ownership model exists;
- producers do not gain write authority merely because they detect/emit a condition;
- a declared setting/field/API is not connected until a runtime consumer/path is identified;
- important traces bind to Acceptance/evidence;
- relative modifier traces must prove that canonical base changes propagate; explicit replacement is used only when intentional independence is required;
- local implementation may vary, but bypass/parallel paths that duplicate the authoritative semantic responsibility are forbidden.
- Composition Invariants own no state; they reference existing owners and required relationships;
- when a canonical source changes, every affected required projection must remain coherent through its declared update semantics;
- consumer-local compensating values/rules are forbidden when they merely mask a broken shared invariant.

---

## `contracts/SKILL_REQUIREMENTS.yaml` v2 Template

```yaml
schema_version: 2

policy:
  installed_does_not_mean_active: true
  minimal_jit_routing: true
  inspect_installed_before_external_search: true
  review_external_source_before_install: true
  global_install_requires_policy_or_user_permission: true
  project_local_skills_may_be_generated_when_justified: true

requirements:
  SKILLREQ-EXAMPLE:
    capability: "[vendor-neutral capability]"
    needed_by: [SYS-EXAMPLE]
    load_when: ["[task/requirement class]"]
    priority: medium
    discovery_terms: ["..."]
    resolution:
      status: unresolved
      skill: null
      source: null
      scope: null                 # global | project | harness
      version_or_commit: null
      content_hash: null
      license: null
      reviewed: false
      rejection_reason: null
```

Rules:
- requirements describe capabilities first, not preferred vendor names;
- concrete resolution is recorded after discovery/review;
- do not repeatedly rediscover a recorded rejected candidate unless relevant facts changed;
- route only skills needed by the current requirement/system context;
- skills never replace project authorities;
- correctness must not require simultaneous multi-skill activation.

---

## Project-local `.agents/skills/<name>/SKILL.md` Template

Generate only for a repeated repository procedure not adequately covered by an existing skill.

```markdown
---
name: [project-workflow-name]
description: [Narrow trigger, repository scope, and useful boundary/negative trigger.]
---

# Purpose
[Repeated project workflow.]

## Required authorities
- [SYSTEM/CONTRACT/ARTIFACT IDs to resolve/read before work]

## Procedure
1. Inspect an existing representative implementation/content item.
2. Use the canonical master systems and declared extension points.
3. [Workflow-specific steps.]
4. Run the mapped validation/evidence checks.

## Must not
- Do not duplicate canonical behavior or data into this skill.
- Do not create a parallel owner for an existing master-system responsibility.
- [Workflow-specific guardrail.]

## Verification
- [Deterministic/interactive evidence expected.]
```

The description is a routing surface. Make it concrete enough to trigger for the intended workflow and narrow enough to avoid unrelated tasks.


---


---

