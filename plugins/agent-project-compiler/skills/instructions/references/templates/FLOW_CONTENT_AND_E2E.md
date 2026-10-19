# APC v2.35 JIT Slice — Acceptance, Flow, Content and E2E Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## ACCEPTANCE_MATRIX.yaml Template

```yaml
goal: GOAL.md

criteria:
  AC-01:
    title: "[Criterion title]"
    required: true
    status: unverified
    authority_ids:
      - "DOC-..."
      - "BP-..."
    depends_on: []
    evidence_required:
      - type: "[unit_test|runtime_flow|e2e_scenario|visual_review|build|artifact_inspection]"
    insufficient_evidence:
      - code_inspection
    evidence: []
```

Rules:
- `verified` requires evidence matching `evidence_required`.
- New contradictory evidence changes status to `needs_recheck` or `unverified`.
- Dependent completion criteria must not remain verified after a dependency is invalidated.


---

## contracts/APP_FLOW.yaml Template

Use the project's actual nodes. They may represent user surfaces, workflow states, lifecycle states, processing stages or other externally meaningful states; do not impose a domain-specific taxonomy.

```yaml
entry: FLOW-ENTRY
workflow_owner: SYS-APPLICATION-FLOW

nodes:
  FLOW-ENTRY:
    kind: surface_or_state
    required: true
    purpose: "[normal product entry]"
    system_ids: [SYS-...]
    capability_ids: [CAP-...]
    authority_ids: [DOC-..., REF-...]
    design_authority_ids: []
    plan_stage: M1
    acceptance_ids: [AC-...]
    actions:
      primary:
        to: FLOW-SETUP

  FLOW-SETUP:
    kind: surface_or_state
    required: true
    purpose: "[required setup/configuration before primary experience]"
    system_ids: [SYS-...]
    authority_ids: [DOC-...]
    design_authority_ids: [DOC-DESIGN]
    plan_stage: M2
    acceptance_ids: [AC-...]
    actions:
      continue:
        to: FLOW-PRIMARY
      back:
        to: FLOW-ENTRY

  FLOW-PRIMARY:
    kind: primary_experience
    required: true
    purpose: "[core normal-user experience]"
    system_ids: [SYS-...]
    plan_stage: M3
    acceptance_ids: [AC-...]
    actions:
      interrupt:
        to: FLOW-INTERRUPT
      complete:
        to: FLOW-RESULT

  FLOW-INTERRUPT:
    kind: interruption_recovery
    required: true
    purpose: "[pause/cancel/recovery state when applicable]"
    plan_stage: M3
    acceptance_ids: [AC-...]
    actions:
      resume:
        to: FLOW-PRIMARY
      exit:
        to: FLOW-ENTRY

  FLOW-RESULT:
    kind: completion_result
    required: true
    purpose: "[result/completion state]"
    plan_stage: M4
    acceptance_ids: [AC-...]
    actions:
      continue:
        to: FLOW-PROGRESSION
      replay:
        to: FLOW-PRIMARY
      home:
        to: FLOW-ENTRY

  FLOW-PROGRESSION:
    kind: persistence_progression
    required: "[true when product requires it]"
    purpose: "[save/unlock/progression/resume behavior]"
    plan_stage: M4
    acceptance_ids: [AC-...]
    actions:
      home:
        to: FLOW-ENTRY
      next:
        to: FLOW-SETUP

terminal_states: []
global_rules:
  one_canonical_flow_owner: true
  required_nodes_must_have_plan_stage: true
  required_nodes_must_have_acceptance: true
  derived_surfaces_do_not_own_global_flow_state: true
```

Required checks:
- every required node is reachable from `entry` or explicitly marked as an intentional independent entry;
- every required node maps to a plan stage and Acceptance;
- every material user surface maps to its design/reference authority;
- normal user completion has a coherent return/replay/resume path where the product requires one.

Do not stop the flow graph at the first runnable primary-experience node.

---

## contracts/INPUT_ACTIONS.yaml Template

```yaml
actions:
  ui_confirm:
    label: Confirm
    contexts: [ui]
    required: true
    remappable: true
    defaults:
      keyboard: Enter
      device: primary_action

  ui_back:
    label: Back
    contexts: [ui]
    required: true
    remappable: true
    defaults:
      keyboard: Escape
      device: secondary_action

  example_gameplay_action:
    label: "[Display label]"
    contexts: [primary_flow]
    required: true
    remappable: true
    defaults:
      keyboard: null
      device: null

conflict_policy: "[project rule]"
persistence_required: true
```

Enumerate the complete required semantic action set. Do not use a couple of example bindings as a substitute for the registry.


---

## contracts/CONTENT_REGISTRY.yaml Template

Every content definition that can enter runtime should declare a shipping disposition when material:

```yaml
content:
  CONTENT-EXAMPLE:
    disposition: production   # production|prototype|test_fixture|debug_only|deprecated
```

Rules:
- `test_fixture` / `debug_only` must be unreachable from normal shipping compositions/defaults/progression/user flows;
- `prototype` is not silently promoted to production; promotion is an explicit authority change;
- project_gate may traverse default compositions/registries/APP_FLOW load paths to reject leakage.


```yaml
content_types:
  example_type:
    entries:
      example_id:
        required_for_current_goal: true
        definition_artifact_id: "DATA-..."
        selectable_through_normal_ui: true
        acceptance:
          - AC-XX
```

Use for entities, stages, rulesets, templates, modes, products, modules, or other data-driven/selectable content.


---

## verification/E2E_SCENARIOS.yaml Template

```yaml
scenarios:
  primary_flow:
    release_gate: true
    environment: exported_or_production_like_build
    steps:
      - launch_application
      - assert_state: entry
      - perform_normal_user_setup
      - enter_primary_experience
      - assert_required_runtime_entities_visible
      - complete_primary_experience
      - assert_state: results_or_success
      - exercise_replay_or_return
    proves:
      - AC-XX
```

For visual/interactive applications add concrete layout/viewport/stability checks where relevant.

---

