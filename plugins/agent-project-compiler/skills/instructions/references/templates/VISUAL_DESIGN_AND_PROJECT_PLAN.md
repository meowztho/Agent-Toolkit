# APC v2.35 JIT Slice — Visual Design and Project Plan Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## `contracts/VISUAL_DESIGN_CONTRACT.yaml` Template

Generate for design-heavy products when whole-screen/page composition must remain stable across local implementation work.

```yaml
schema_version: 1

surfaces:
  SURFACE-EXAMPLE:
    authority_ids: [DOC-DESIGN]
    vision_anchor_ids: [VQ-001]
    approved_reference_ids: []
    focal_priority: []
    persistent_regions: []
    layout_relationships: []
    invariants: []
    allowed_deviations: []
    acceptance_ids: [AC-UI-EXAMPLE]
```

Use visual checkpoint/runtime evidence to verify it; do not infer fidelity from component existence.

---

## `docs/PROJECT_PLAN.md` Template

```markdown
# Project Plan

## Authority Metadata
- Artifact ID: `DOC-PROJECT-PLAN`
- Routed by: `PROJECT_INDEX.yaml` bootstrap/planning routes
- System/Acceptance refs: [SYS-... / AC-...]

Status: `[draft_before_reconstruction|final_after_reconstruction]`

## Planning Basis
- User vision: DOC-USER-VISION
- Decision model: DOC-DECISION-COMPENDIUM
- Context handoff: DOC-CONTEXT-HANDOFF
- System topology: CONTRACT-SYSTEM-MAP
- Reconstruction gate: VERIFY-FRESH-AGENT-RECONSTRUCTION
- Acceptance: DOC/CONTRACT-ACCEPTANCE

## Delivery Strategy
[How the complete product will be assembled without losing the walking skeleton.]

## Phase 0 — Walking Skeleton
- systems/flows involved: [...]
- observable outcome: [...]
- placeholders allowed: [...]
- skeleton_classification: [exploratory|production_candidate|production_admitted]
- required_survivability_acceptance_ids: [AC-...]
- gate: [...]

## Phase / Milestone — [Name]
- System IDs: [...]
- Blueprint IDs: [...]
- depends_on: [...]
- implementation objective: [...]
- integration objective: [...]
- skills/capabilities: [...]
- acceptance/evidence: [...]

## Integration Order
[Dependency-aware order and why.]

## Independent Work Units
[Systems/components that can be implemented and tested independently.]

## Deferred / Future
[Future work preserved without pretending it is current scope.]
```

---

