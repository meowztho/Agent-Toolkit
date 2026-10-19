# APC v2.35 JIT Slice — Vision, Decisions, Guardrails, Reconstruction and System-Map Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## `docs/USER_VISION.md` Template

```markdown
# User Vision

## Authority Metadata
- Artifact ID: `DOC-USER-VISION`
- Routed by: `PROJECT_INDEX.yaml` interview-provenance/bootstrap route(s)
- Provenance: `VQ-*` / `Q-*`

This file preserves high-signal user intent in the user's original wording. Normalized behavior remains authoritative in the routed system/design/contracts.

## VQ-001 — [Anchor title]

Source / context:
[where/when this wording occurred]

Verbatim user wording:
> [exact quote in original language]

Compiled intent:
- [...]

Authority scope:
- [product/design/system domains this anchor constrains]

Destination authorities:
- [stable artifact/system/contract IDs]

Status: active
```

Do not turn the complete interview into vision anchors; use `INTERVIEW_LEDGER.md` for full Q/A provenance.

---

## `docs/DECISION_COMPENDIUM.md` Template

```markdown
# Decision Compendium

## Authority Metadata
- Artifact ID: `DOC-DECISION-COMPENDIUM`
- Routed by: `PROJECT_INDEX.yaml` bootstrap/domain routes
- Provenance: `DEC-*` → `Q-*` / `VQ-*`

This is the readable normalized product model between verbatim interview provenance and exact system/contracts. Exact behavior stays authoritative in routed system/design/content/contracts.

## Product model in one page
[Concrete explanation of what is being built, how the major parts relate, and why the architecture is shaped this way.]

## DEC-001 — [Decision title]
- decision: [...]
- rationale: [...]
- authority_class: [USER|COMPILER|RESEARCHED_FACT|DELEGATED_TECHNICAL|DEFERRED]
- source_ids: [Q-..., VQ-..., REF-...]
- affected_systems: [SYS-...]
- rejected_alternatives: []
- example_ids: []
- canonical_destinations: [DOC-..., CONTRACT-...]

## Cross-system / capability mental model
[Readable master-system + reusable-capability hierarchy, composition relationships and why consumer behavior is implemented core-first. Do not duplicate exact contract fields.]

## Important guardrails / non-goals
- GR-... — [short statement + pointer]

## Example semantics
- EX-... — [required|illustrative|adversarial|reference-derived] — [what the example proves]

## Open / deferred
- [...]
```

Update after substantial interview rounds. Do not compress away the source Q/A and do not become a second exact system authority.

---

## `contracts/ARCHITECTURE_GUARDRAILS.yaml` Template

Generate when explicit negative requirements prevent plausible but wrong implementations.

```yaml
schema_version: 1

guardrails:
  GR-001:
    statement: "[what must not exist/become]"
    reason: "[why this would violate intent/architecture]"
    source_ids: [DEC-001]
    applies_to: [SYS-EXAMPLE]
    forbidden_patterns:
      - "[semantic pattern, not brittle filename regex]"
    verification:
      - "[architecture/integration audit check]"
```

Guardrails are product/compiler architecture constraints, not generic style rules. When reusable compositions are a core project principle, include semantic guardrails against consumer-local copies of shared systems and against copied resolved values that should remain relative to a canonical base.

---

## `verification/ABSTRACTION_TESTS.yaml` Template

Generate when modularity/data-driven/extensibility claims need representative or adversarial proof. Use the **smallest representative proof set that covers materially different composition paths**; architecture proof scales with semantic diversity, not consumer count.

```yaml
schema_version: 1

tests:
  ABS-001:
    title: "[reusable architecture challenge]"
    systems: [SYS-EXAMPLE]
    proof_claim: reuse_and_composition
    representative_proof_set:
      integration_case: CASE-BASELINE
      variation_axes_required:
        - "[material composition/modifier/provider/mapping axis]"
      stopping_rule: "all material variation axes covered; additional similar consumers are product/content breadth"
    cases:
      - id: CASE-BASELINE
        proof_role: canonical_walking_skeleton
        semantic_role: illustrative
        evidence_mode: real_or_required_case
        covers:
          - canonical_runtime_path
        description: "[...]"
      - id: CASE-A
        proof_role: representative_consumer
        semantic_role: illustrative
        evidence_mode: real_or_required_case
        covers:
          - "[variation axis A]"
        description: "[...]"
      - id: CASE-B
        proof_role: representative_consumer
        semantic_role: adversarial
        evidence_mode: "[real_required_case|adversarial_fixture|fresh_agent_challenge]"
        covers:
          - "[variation axis B]"
        description: "[...]"
    pass_conditions:
      - "baseline proves the canonical owner/contract/runtime integration path"
      - "representative cases use the same canonical master systems/capabilities"
      - "material differences are expressed through declared composition/data/modifier/provider seams unless a genuine new reusable capability is identified"
      - "no consumer-local duplicate rule owner, bypass or parallel runtime path is required"
      - "all required semantic variation axes are covered without speculative production-content count"
    architecture_proof_status: pending
```

These cases test expressiveness/reuse; they are not automatically shipping content. Once the representative proof set passes, additional similar consumers are product/content/scale work unless a new semantic variation axis appears.

---

## `verification/FRESH_AGENT_RECONSTRUCTION.yaml` Template

Generate for nontrivial compiled packages before implementation task decomposition/final delivery.

```yaml
schema_version: 1
criterion: AC-PACKAGE-RECONSTRUCTION
required: true
mode: "[independent_agent|self_isolated_reconstruction]"
status: pending

required_concepts:
  start_prompt_orientation: pending
  product_vision: pending
  major_workflows: pending
  system_model_and_rationale: pending
  ownership_and_integration: pending
  rejected_alternatives_and_guardrails: pending
  example_semantics: pending
  reference_traits: pending
  representative_flow_trace: pending
  representative_proof_set_reasoning: pending
  authoring_extension_model: pending
  open_decisions: pending
  authority_routing: pending
  deep_authority_discovery: pending
  authority_reachability_report: pending

material_misconceptions: []
missing_context: []
evidence: []
```

Pass only when a fresh agent with no original chat first forms the correct product/master-outcome model from the generated Start Prompt and then resolves exact rules from package authorities without material misconceptions. Prefer an independent agent/subagent when available; record fallback evidence honestly.

Add a required Acceptance Matrix entry, for example:

```yaml
AC-PACKAGE-RECONSTRUCTION:
  title: Fresh agent reconstructs the intended product model
  required: true
  status: unverified
  authority_ids:
    - DOC-USER-VISION
    - DOC-DECISION-COMPENDIUM
    - DOC-CONTEXT-HANDOFF
    - CONTRACT-SYSTEM-MAP
  evidence_required:
    - type: authority_reachability
    - type: fresh_agent_reconstruction
  evidence: []
```

---

## `contracts/SYSTEM_MAP.yaml` Template

```yaml
schema_version: 1

systems:
  SYS-EXAMPLE:
    responsibility_key: SYSTEM.EXAMPLE
    responsibility_scope:
      - "[durable responsibility]"
    must_not_own:
      - "[neighbor responsibility]"
    authority_ids: [DOC-SYSTEM-EXAMPLE]
    provides: [CONTRACT-EXAMPLE-OUTPUT]
    depends_on: []
    consumed_by: []
    configuration_inputs: []
    extension_points: []
    acceptance_ids: [AC-EXAMPLE]

composition_policy:
  values:
    default_resolution_order:
      - master_default
      - content_or_module_definition
      - reusable_profile
      - consumer_modifier
      - runtime_modifier
    merge_operator_must_be_explicit_when_material: true
    prefer_relative_modifier_when_base_should_propagate: true
    absolute_replace_requires_intent: true

compositions:
  COMPOSITION-EXAMPLE:
    consumer_shell: "[generic entity/page/bot/workflow host]"
    uses: [SYS-EXAMPLE]
    data_ids: []
    profile_ids: []
    modifiers:
      example_numeric_field:
        op: add
        value: 0
    explicit_replacements: []
    forbidden_local_ownership: []
```

`SYSTEM_MAP.yaml` owns topology/responsibility scope. Put material per-rule decision owners, mutable-state owners, allowed writers, and cross-system runtime edges in `SYSTEM_INTEGRATION.yaml` rather than duplicating them here.

---

## `verification/INTEGRATION_AUDIT.yaml` Template

Generate when `SYSTEM_INTEGRATION.yaml` is material to the current project/work.

```yaml
schema_version: 1
revision: "git:<revision-or-worktree-id>"
scope:
  changed_systems: [SYS-EXAMPLE]
  changed_requirement_ids: [REQ-EXAMPLE]

checks:
  single_decision_owner: pass
  single_state_owner: pass
  core_first_change_classification: pass
  requested_behavior_maps_to_canonical_capability: pass
  producer_contract_consumer_paths: pass
  no_parallel_or_bypass_paths: pass
  live_configuration_consumers: pass
  composition_value_resolution: pass
  base_change_propagation_for_relative_modifiers: pass
  explicit_cross_system_writes: pass
  composition_coherence_invariants: pass
  runtime_data_driven_claims: pass
  cross_domain_god_objects: pass
  dead_contracts: pass
  architecture_guardrails: pass

feature_maturity:
  FEATURE-EXAMPLE:
    specified: true
    declared: true
    connected: true
    exercised_evidence: [EV-EXAMPLE]
    verified_by: [AC-EXAMPLE]

findings: []
result: pass
```

This is revision-bound audit evidence, not a second ownership authority. Findings must point back to `SYSTEM_INTEGRATION`, implementation IDs, or Acceptance IDs.

---

