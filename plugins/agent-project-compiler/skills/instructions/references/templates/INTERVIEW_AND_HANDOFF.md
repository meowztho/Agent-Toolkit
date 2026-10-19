# APC v2.35 JIT Slice — Interview, Coverage and Handoff Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## `docs/INTERVIEW_LEDGER.md` Template

```markdown
# Interview Ledger

## Authority Metadata
- Artifact ID: `DOC-INTERVIEW-LEDGER`
- Routed by: `PROJECT_INDEX.yaml` interview-provenance route
- Purpose: verbatim material Q/A provenance

This is the durable provenance record for material compiler questions and user answers. Exact behavior remains authoritative in routed project contracts/specs.

## Q-001 — [Topic]

Question:
> [exact question as asked]

User answer:
> [verbatim answer in original language]

Compiled meaning:
- [...]

Classification:
- confirmed_user_decision

Example semantics (when applicable):
- null # required | illustrative | adversarial | reference-derived

Affected systems/domains:
- SYS-...

Canonical destinations:
- DOC-...#...
- CONTRACT-...

Status:
- active

Supersedes / clarified by:
- null
```

Do not omit material Q/A merely because its conclusion also exists in a system spec.

---

## `contracts/INTERVIEW_COVERAGE.yaml` Template

```yaml
schema_version: 1
project: PROJECT-ID

product_capability_envelope:
  inference_basis:
    product_archetype: "[compiler hypothesis, not USER authority]"
    sources: [VQ-..., REF-...]
  expected_responsibilities:
    - key: RESPONSIBILITY-EXAMPLE
      rationale: "ordinary responsibility implied by the requested product"
      provenance: compiler_inference
      disposition: modeled # modeled|covered_by_existing_owner|not_applicable|intentionally_deferred|delegated_technical|needs_user_decision
      owner_or_destination: SYS-EXAMPLE
      notes: []
  unconsidered_material: 0

status_values:
  - confirmed
  - research_resolved
  - delegated_technical
  - intentionally_deferred
  - not_applicable
  - unresolved_user
  - contradiction

systems:
  SYS-EXAMPLE:
    fields:
      purpose: confirmed
      user_visible_behavior: confirmed
      states_rules: confirmed
      inputs_triggers: delegated_technical
      outputs_feedback: confirmed
      content_configuration: confirmed
      dependencies: confirmed
      variants_overrides: not_applicable
      value_resolution_propagation: not_applicable
      failure_recovery: not_applicable
      design_ux: confirmed
      future_constraints: confirmed
      acceptance: confirmed
    question_ids: []
    notes: []

completion_gate:
  unresolved_user: 0
  contradictions: 0
  unconsidered_material_responsibilities: 0
  status: passed
```

Add/remove fields per domain. The gate concerns user-owned material decisions, not implementation trivia.

---

## `CONTEXT_HANDOFF.md` Template

```markdown
# Project Context Handoff

## Authority Metadata
- Artifact ID: `DOC-CONTEXT-HANDOFF`
- Routed by: `PROJECT_INDEX.yaml` bootstrap
- Purpose: rich fresh-agent/context-loss onboarding; exact rules remain in canonical authorities

## What the user is trying to create
[Rich product description, not a one-line summary.]

## Intended experience / gestalt
[What it should feel like and what must remain recognizable.]

## Important original wording
- VQ-... — "..."

## References and why they matter
### [Reference]
- cited for: [...]
- adopted traits: [...]
- explicitly not implied: [...]

## How the concept evolved
[Chronological/thematic narrative of important discussions and clarifications.]

## Major decisions and rationale
### [Decision]
- decision: [...]
- why: [...]
- source: Q-... / VQ-...
- canonical authority: [...]

## Rejected / changed alternatives
- [...]

## Product archetype / expected capability envelope
[Compiler-inferred coverage hypothesis plus dispositions: modeled / covered elsewhere / not applicable / deferred / delegated / user decision. This is not USER authority.]

## Master systems, capability hierarchy and composition model
[Readable overview + pointers to SYSTEM_MAP/CAPABILITY_GRAPH. Include the core-first law and examples that prevent later consumer-local bypasses.]

## How later user requests must extend the architecture
[Explain that follow-up requests are deltas: classify data/modifier vs composition vs existing/new reusable capability before source edits. Record known extension examples.]

## Future constraints that matter now
- [...]

## Open / deferred decisions
- [...]

## Prior drift/failure lessons
[Only project-relevant lessons that a new agent must not repeat.]

## Canonical source map
- discoverability/JIT router: `PROJECT_INDEX.yaml`
- artifact path/identity resolution: `PROJECT_REGISTRY.yaml`
- authority reachability evidence: `verification/AUTHORITY_REACHABILITY.yaml`
- exact vision: `docs/USER_VISION.md`
- interview provenance: `docs/INTERVIEW_LEDGER.md`
- readable decision model: `docs/DECISION_COMPENDIUM.md`
- completeness state: `contracts/INTERVIEW_COVERAGE.yaml`
- package reconstruction: `verification/FRESH_AGENT_RECONSTRUCTION.yaml`
- systems: `contracts/SYSTEM_MAP.yaml`
- reusable capability hierarchy: `contracts/CAPABILITY_GRAPH.yaml` when present
- negative architecture constraints: `contracts/ARCHITECTURE_GUARDRAILS.yaml` when present
- abstraction/reconstruction evidence: `verification/ABSTRACTION_TESTS.yaml`, `verification/FRESH_AGENT_RECONSTRUCTION.yaml`
- [...]
```

Keep this detailed enough to onboard an agent after context loss. Do not replace precise contracts with the handoff.

# Template — project-native executable gate

For nontrivial projects with structured project truth, emit an **actual executable** `tools/project_gate.<ext>` in an available runtime. The filename/runtime may differ; keep one canonical gate entry point.

Do not ship the following as uninstantiated pseudocode. The compiler must specialize it to the concrete generated contracts and dependency environment.

