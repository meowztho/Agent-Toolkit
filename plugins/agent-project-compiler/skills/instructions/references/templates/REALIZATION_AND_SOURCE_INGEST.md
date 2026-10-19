# Runtime Template Library

# Current Precedence — v2.27 Product / Realization / Verification Truth Templates

The following shapes supersede conflicting earlier template examples. Scale them to project complexity; do not create unused files merely to satisfy a template.

## `contracts/PRODUCT_REALIZATION.yaml` Template

Canonical scope/outcome inventory; do not store mutable verification truth here.

```yaml
product_realization:
  PR-001:
    title: "[required observable/cross-cutting product outcome]"
    disposition: required            # required|optional|deferred|out_of_scope
    provenance:
      authority_class: USER          # USER|COMPILER|RESEARCHED|DELEGATED
      source_ids: [DEC-..., Q-...]
    flow_node_ids: [FLOW-...]         # empty for non-flow outcomes
    system_ids: [SYS-...]
    capability_ids: [CAP-...]
    contract_ids: [CONTRACT-...]
    producer_ids: []
    consumer_ids: []
    surface_ids: []
    content_ids: []
    plan_stage: M...
    acceptance_ids: [AC-...]
```

Rules:
- every required master-outcome property appears in exactly one canonical PR entry or is explicitly represented by a referenced grouped authority with a unique mapping;
- APP_FLOW owns transitions and may be referenced from PR outcomes;
- current verification state is derived from Acceptance/Evidence, not written here as an independent truth;
- cross-cutting outcomes such as persistence/performance/authoring/compatibility belong here even when they are not a screen/flow node.

## `verification/PRODUCT_REALIZATION_COVERAGE.yaml` Template

Generated/derived evidence view:

```yaml
source_fingerprints:
  product_realization: "..."
  project_plan: "..."
  acceptance: "..."
coverage:
  PR-001:
    plan_stage_resolves: true
    owners_resolve: true
    acceptance_ids_resolve: true
    derived_maturity: Verified
    evidence_ids: [EVID-...]
    evidence_sufficient: true
summary:
  required_total: 1
  verified: 1
  unverified: 0
  verdict: PASS
```

This file never owns product scope, stage rules or verification status.

## Whole-product realization coverage before `PROJECT_PLAN`

Before writing milestone order, enumerate the required product lifecycle/flow using the project's actual domain language.

```markdown
## Whole-product realization coverage
| Node / Outcome ID | User-visible purpose | Owner/System/Capability | Flow predecessors | Plan stage | Acceptance IDs | Surface/reference IDs | Disposition |
|---|---|---|---|---|---|---|---|
| FLOW-... | ... | ... | ... | M... | AC-... | REF-... | required |
```

This table is a readable view. Machine-checkable mappings belong in `APP_FLOW`/workflow contracts and Acceptance.

No required node may be left with an empty plan stage or Acceptance mapping.

## `docs/PROJECT_PLAN.md` material dependency-bound stage
```markdown
## Phase / Milestone — [Name]
- Outcome: [...]
- Product-realization node/outcome IDs: [...]
- System/Capability/Blueprint IDs: [...]
- depends_on:
  - id: [SYS/CAP/AC/...]
    required_maturity: [existing project maturity/acceptance state]
- entry_evidence: [...]
- admission_condition: [...]
- why_now: [...]
- implementation_objective: [...]
- integration_objective: [...]
- exploratory_before_admission:
    allowed: [...]
    may_support: [...]
    must_not_authorize: [...]
- completion_condition: [...]
- unlocks: [...]
- reuse_obligations: [...]
- deferred_not_now: [...]
- replan_triggers: [...]
- approval_boundary: # optional; only when project truth defines a human/project gate
    reversible_preparation_allowed: [...]
    gated_transition: [...]
    approval_authority: [...]
    approval_evidence: [...]
    downstream_requires_transition: [...]
    broad_request_counts_as_approval: false
```
Not every trivial stage needs every field. Use the richer shape where downstream validity materially depends on upstream maturity/evidence. An approval boundary blocks its exact transition, not authorized reversible preparation before it.

## `provenance/SOURCE_INGEST_MANIFEST.yaml`
```yaml
sources:
  SRC-001:
    identity: "..."
    hash: "..."
    extracted_question_ids: []
    material_reference_ids: []
reconciliation:
  expected: 0
  materialized: 0
  unresolved: []
```

## `verification/INTERVIEW_MATERIALIZATION.yaml`
```yaml
questions:
  Q-001:
    ledger_present: true
    verbatim_present: true
    material: true
    canonical_destinations: [DEC-001, SYS-001, AC-001]
    materialized: true
unresolved_material: []
```

## `docs/REFERENCE_REGISTER.md` / reference map
For each material reference record stable ID, source identity/URL/date/version, provenance, adopt|adapt|reject|inspiration-only traits, rationale, non-implied traits/exclusions and affected System/Capability/Acceptance IDs.

## `contracts/EXTENSION_POINTS.yaml` (conditional only)
Record public seam ID, owner System/Capability, accepted definition/module/provider types, registration/validation, dependencies, allowed variation/substitution, forbidden writes/bypasses, runtime trace IDs, version/schema/migration behavior and acceptance evidence.

## Runtime/read state additions
`STATE.context` supports `required_source_ids`, current-session `loaded_source_ids`, Atlas `inspected_view_ids`, current change classification and admission status/pointers where material. Generated evidence records prove reachability/freshness/read behavior but never become a second architecture truth.

---


