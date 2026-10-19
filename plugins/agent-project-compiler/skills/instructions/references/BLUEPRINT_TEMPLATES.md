# Prose Blueprint / Specification Template Library

# Current Precedence — Module/Provider and Anchor Fields

For nontrivial implementation/module/provider Blueprints, include when material: Responsibility Owner/System IDs, Capability Contract IDs, produced/consumed contracts, owned/scoped state, forbidden foreign writes/responsibilities, producer-convergence path, implementation anchor IDs, Acceptance/Evidence IDs and extension-point ID if this is a public seam. Definitions/Profile Blueprints must not model live mutable runtime instance state as shared declarative data.

---


These are detailed intent/specification templates. Implementation/Data Blueprints are defined separately in `RUNTIME_TEMPLATES.md` and `BLUEPRINT_REPOSITORY_GUIDE.md`. For nontrivial executable behavior, also generate separate `*.bp.yaml` Project Blueprints routed through `blueprints/REGISTRY.yaml`. Do not collapse unrelated systems/screens/flows into one large behavior file.

## Normative Authority Metadata Block

Every generated **normative prose authority** should begin with lightweight discoverability metadata. This is metadata/backlinking, not duplicated behavior truth.

```markdown
## Authority Metadata
- Artifact ID: `DOC-...`
- Authority for: [bounded responsibility]
- Routed by: `PROJECT_INDEX.yaml` domain(s): [...]
- Provenance: [VQ-/Q-/DEC- IDs when material]
- Integration refs: [CONTRACT-SYSTEM-INTEGRATION / CAPABILITY IDs when material]
- Blueprint refs: [BP-...]
- Acceptance refs: [AC-...]
```

The compiler must register the artifact in `PROJECT_REGISTRY.yaml` and route it from `PROJECT_INDEX.yaml`. A perfect system spec with no incoming bootstrap/JIT route is invalid.

---

## DESIGN.md Template

# DESIGN.md

## Authority Metadata
[Artifact ID, bounded authority responsibility, PROJECT_INDEX route domain(s), provenance/integration/Blueprint/Acceptance refs as applicable.]

## Design Goals
- [Observable design/UX goal]
- [...]

## Design Principles
- [Principle + practical consequence]
- [...]

## Reference-Derived Direction
[Only project-relevant traits. Link to REFERENCE_MAP when present.]

## Information Architecture
[Primary sections/modes/screens and relationships.]

## Navigation and Flows
### Primary Flow
1. [...]
2. [...]

### Back / Cancel / Recovery Behavior
[...]

## Screens and States

### [Screen / Menu / View]
Purpose:
[...]

Hierarchy:
1. [...]
2. [...]

Key components:
- [...]

Input / focus / interaction:
- [...]

States:
- default
- focused/hovered
- selected
- disabled
- loading/error/empty as applicable

Transitions:
- [...]

## Layout and Visual Hierarchy
[...]

## Visual Language
### Typography
[...]

### Color
[...]

### Iconography / Illustration
[...]

### Spacing / Shape / Density
[...]

## Interaction Feedback and Motion
[...]

## Input / Accessibility / Responsiveness
[...]

## Asset Dependencies
- [Asset group → ASSET_BLUEPRINT section]

## Validation
- [How the implementation agent should visually/functionally verify this design]

---

## ASSET_BLUEPRINT.md Template

# ASSET_BLUEPRINT.md

## Authority Metadata
[Artifact ID, bounded authority responsibility, PROJECT_INDEX route domain(s), provenance/integration/Blueprint/Acceptance refs as applicable.]

## Asset Strategy
[Overall strategy and quality target.]

## Source Priority
1. [user-provided / existing repo / generated / procedural / verified free / licensed / placeholder]
2. [...]
3. [...]

## Licensing / Attribution Rules
[...]

## Asset Inventory

### [Asset Group]
Purpose:
[...]

Required variants/states:
- [...]

Style / quality:
[...]

Technical requirements:
- format:
- dimensions/resolution:
- animation/frames:
- transparency/audio/etc.:

Source mode:
[...]

Fallback:
[...]

Destination / naming:
[...]

Replacement policy:
[...]

Validation:
- [...]

## Generation Rules
[When AI/code generation is allowed, expected consistency, prompt/reference handling, human decisions required.]

## Placeholder Rules
[What may be temporary and how replacement must avoid implementation churn.]

## Import / Integration
[...]

## Final Asset Validation
- consistency
- missing variants
- license status
- technical format
- runtime/render/audio validation

---

## ARCHITECTURE.md Template

# ARCHITECTURE.md

## Authority Metadata
[Artifact ID, bounded authority responsibility, PROJECT_INDEX route domain(s), provenance/integration/Blueprint/Acceptance refs as applicable.]

## Architectural Goals
- [...]

## Hard Constraints
- [...]

## Major Components / Modules
### [Component]
Responsibilities:
[...]

Owns:
[...]

Interfaces:
[...]

Must not own:
[...]

## Data / State Ownership
[...]

## Data Flow / Event Flow
[...]

## Extensibility
[What future additions must be possible without reconstruction.]

## Platform / Runtime Constraints
[...]

## Persistence / Networking / External Services
[As applicable.]

## Implementation Freedom
[Decisions intentionally delegated to the implementation agent.]

## Validation
- [...]

---

## CONTENT_BLUEPRINT.md Template

# CONTENT_BLUEPRINT.md

## Authority Metadata
[Artifact ID, bounded authority responsibility, PROJECT_INDEX route domain(s), provenance/integration/Blueprint/Acceptance refs as applicable.]

## Purpose
[What repeatable/project content this blueprint governs.]

## Content Model
### [Content Type]
Required fields:
- [...]

Optional fields:
- [...]

Relationships:
- [...]

## Authoring / Creation Workflow
[...]

## Reuse and Variation
- reusable Definition Type ID: [...]
- generic runtime/surface consumer: [...]
- composed Capability IDs: [...]
- reusable profiles/presets: [...]
- allowed modifiers/replacements + merge semantics: [...]
- state ownership boundary: [...]
- cross-system invariant IDs: [...]
- authoring/registration path: [...]
- rule for adding another same-type definition without core-code duplication: [...]

## Definition / Instance Separation
[What is declarative definition/profile data vs mutable runtime/session instance state.]

## Presentation / Output Slots
[Stable semantic slots/hooks used by generic consumers; placeholders and production assets/outputs use the same slots.]

## Progression / Catalog / Discovery
[As applicable.]

## Expansion Rules
[How new content is added without changing core systems.]

## Asset / Design Dependencies
[...]

## Validation
- schema/config validation
- missing content checks
- runtime/content preview checks

---

## REFERENCE_MAP.md Template

# REFERENCE_MAP.md

## Authority Metadata
[Artifact ID, bounded authority responsibility, PROJECT_INDEX route domain(s), provenance/integration/Blueprint/Acceptance refs as applicable.]

## Purpose
Translate external references into explicit project rules. References are evidence/inspiration, not executable requirements by themselves.

## [Reference Name]

Referenced domain:
[...]

Why the user cited it:
[...]

Relevant observed traits:
- [...]

Adopted:
- [Trait → concrete project rule → authoritative destination]

Adapted:
- [Trait → modification → destination]

Rejected / Out of Scope:
- [...]

Live reread required?
- [No / condition when yes]

Source/version note:
[When relevant.]

---

## Detailed System Authority Template

Use for `docs/systems/<SYSTEM>.md` when a core system is nontrivial. This is the canonical prose-template owner for detailed system authorities.

```markdown
# [System Name]

## Authority Metadata
[Artifact ID, bounded authority responsibility, PROJECT_INDEX route domain(s), provenance/integration/Blueprint/Acceptance refs as applicable.]

System ID: `SYS-...`

## Purpose / User-visible role
[...]

## User intent and provenance
- VQ-...
- Q-...

## Owned responsibilities
- [...]

## Must not own
- [...]

## States / Rules / Lifecycle
[...]

## Inputs / Triggers
[...]

## Outputs / Feedback
[...]

## Semantic ownership references
- mutable state ownership refs: [entries in `CONTRACT-SYSTEM-INTEGRATION`]
- rule/decision ownership refs: [entries in `CONTRACT-SYSTEM-INTEGRATION`]

Do not duplicate the full ownership matrix here. Explain only system-local semantics that are needed to understand those references.

## Producers / Contracts / Consumers
[Material cross-system Runtime Trace IDs and system-local explanation.]

## Cross-system writes / side effects
[Reference canonical mutation/side-effect paths in `SYSTEM_INTEGRATION`; describe local handling only.]

## Dependencies / Consumers
[...]

## Configuration / Content
[...]

For inherited/composed values, define the canonical source and deterministic value-resolution semantics when material. Do not leave `override` ambiguous.

## Composition / Consumer Binding
- canonical systems/modules consumed: [...]
- consumer-owned identity/content state: [...]
- forbidden copied/shared logic: [...]
- reusable profiles/presets: [...]

## Value Resolution / Modifiers
For each material configurable field or field family:
- base source: [...]
- resolution order: [...]
- merge operator: [add|multiply|replace|min|max|append|remove|project-specific]
- consumer modifier semantics: [...]
- runtime/context modifier semantics: [...]
- propagation expectation when base changes: [...]

## Variants / Overrides / Exceptions
Use explicit replacement only when independence from the base is intentional; otherwise prefer declared relative modifiers/deltas so canonical base changes propagate.
[...]

## Guardrails / Negative Requirements
[Reference applicable `ARCHITECTURE_GUARDRAILS` IDs; do not duplicate global guardrail truth.]

## Representative / Adversarial Examples
- EX/CASE-... — [required|illustrative|adversarial|reference-derived] — [what this example proves]

## Authoring / Creation Path
[When this system participates in data-driven/modular content creation, explain the canonical authoring path and how it reaches the same runtime contracts.]

## Extension points / Future constraints
[...]

## Design / Asset implications
[...]

## Skills / Capabilities
[...]

## Blueprint / Contract ownership
- behavior: [...]
- implementation/data: [...]
- contracts: [...]

## Acceptance / Evidence
- AC-... → [...]

## Open / Deferred
- [...]
```

For a nontrivial core system, a shallow `SYSTEM_MAP` row is insufficient; generate a detailed system authority.


## MODIFIER_BLUEPRINT.md Template

Use when a reusable modifier/policy/upgrade/transformation is itself a material authored object.

```markdown
# [Modifier Name]

## Authority Metadata
[...]

Modifier ID: `MOD-...`

## Target seam
- owner System/Capability: [...]
- target field/behavior/output slot: [...]

## Operation
- operator/module: [add|multiply|replace|min|max|append|remove|bounded behavior module|project-specific]
- value/configuration: [...]
- preconditions/eligibility: [...]
- priority/order/conflict semantics: [...]

## Must not own
- canonical target state/rule owner;
- copied target implementation;
- unrelated consumer-specific behavior.

## Composition
- compatible Definition Types/definitions: [...]
- dependencies/exclusions: [...]
- resolution order: [...]

## Verification
- base behavior without modifier;
- effective behavior with modifier;
- base-change propagation when relative;
- no foreign write/parallel owner.
```
