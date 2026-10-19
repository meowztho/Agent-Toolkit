# Coverage, Blueprint, Reference, and Asset Guide

# Current Precedence — Blueprint Role in Core-First Graph

Blueprints refine bounded behavior/implementation/data below the current Responsibility Owner/Capability/Integration model. They do not create a second owner hierarchy. When material, link Blueprint IDs to System/Capability/Trace/Acceptance IDs and stable implementation anchors. Modules/providers/extensions should use existing capability contracts and owner paths rather than encode producer/consumer-specific domain cores.

---


# Coverage and Blueprint Protocol

## Why this exists

A concise runtime package must not become a lossy project package.

`PROJECT_CORE.md` is intentionally short, but the compiler must preserve detailed intent in JIT-loaded authoritative blueprints under `docs/`.

## Pre-generation coverage map

Before generating files, internally map every material user statement to one of:

- `core`
- `goal`
- `design`
- `assets`
- `architecture`
- `content`
- `reference`
- `example_semantics`
- `negative_requirement`
- a domain/system spec
- `research_fact`
- `question`
- `excluded_with_reason`

Do not output this internal map unless it helps resolve ambiguity.

## Blueprint discovery

Determine which blueprint domains the project actually needs.

Common domains:

### Product / behavior
Feature behavior, workflows, states, rules, edge cases.

### Design / UX
Visual language, screen hierarchy, menu/navigation, layout, feedback, interaction patterns, accessibility, responsive behavior, information hierarchy.

### Technical architecture
Master systems, reusable capability hierarchy, composition boundaries, interfaces, persistence, data flow, extensibility, constraints.

### Content system
Repeatable content definitions, schemas, templates, progression/content expansion rules.

### Asset system
Iconsumers, sprites, icons, audio, 3D, animation, fonts, videos, datasets, external content, source/generation strategy.

### References
What was taken from external examples, what was adapted, what was rejected.

### Testing / validation
Observable acceptance and domain-specific verification.

Create only relevant domains.

## Derive implicit but necessary detail

The compiler may derive necessary structural consequences from confirmed intent.

Example:
If the user requires "new entities should mostly be content work", the package may specify a data-driven entity definition boundary and a entity-authoring blueprint as a recommendation/technical constraint, while preserving implementation-agent freedom over exact implementation.

Do NOT derive subjective choices the user has not made.

## Coverage audit before delivery

For nontrivial projects, first require `INTERVIEW_COVERAGE.yaml` to pass (or be explicitly partial) and verify every material Q/A in `INTERVIEW_LEDGER.md` has a canonical destination or documented unresolved status. Then check:

1. Can each material user statement be found in the generated package?
2. Could a capable implementation agent implement each user-visible behavior without rereading the original chat?
3. Are named references translated into concrete rules?
4. Are visual/design requirements concrete enough to build?
5. Are required assets identified with a source/generation path?
6. Are deferred/future requirements preserved where they affect today's architecture?
7. Are non-goals preserved?
8. Are contradictions resolved?
9. Are important exact/canonical values stored once in an authoritative source?
10. Does `PROJECT_INDEX.yaml` route every active normative authority (and every required Blueprint directly or through registered call reachability), with `verification/AUTHORITY_REACHABILITY.yaml` showing zero unreachable nodes?
11. Are illustrative/adversarial examples clearly distinguished from required content?
12. Are material negative requirements/forbidden interpretations captured as guardrails?
13. Can the Fresh-Agent Reconstruction gate explain the product model without the original chat and discover a non-bootstrap deep authority through `PROJECT_INDEX.yaml`?

If any answer is no, the package is not ready.

---

# Reference Compilation Protocol

## Reference ≠ requirement

Named games, apps, websites, screenshots, products, or workflows are communication shortcuts. The implementation agent should not be forced to infer later what the user liked about them.

## For each material reference

Record internally:
- reference;
- referenced domain;
- relevant observed traits;
- user-confirmed traits;
- compiler recommendations;
- deviations/exclusions;
- authoritative destination.

Example:

Reference: Product A
Domain: menu/navigation
Observed traits:
- persistent top-level tabs
- keyboard/device-first focus navigation
- large selected-item preview

User intent:
- controller-first navigation
- large preview

Excluded:
- persistent tabs

Destination:
- `docs/DESIGN.md#Menu Navigation`
- `docs/DESIGN.md#Selection Screens`

## Screenshots / iconsumers

If iconsumers are supplied or researched:
- extract layout, hierarchy, spacing, state, navigation, feedback, and style traits;
- do not describe only aesthetics;
- convert useful traits into buildable rules;
- preserve iconsumer/source references when the implementation agent may need to visually compare later.

## Live reference vs compiled reference

Prefer compiling stable traits into project docs.

Require live rereading/research only when:
- the external reference is version-sensitive;
- exact current API/product behavior matters;
- implementation needs an exact asset/source/license check.

## Avoid imitation ambiguity

If a reference could imply copying protected branding/assets, translate inspiration into original project rules and asset direction rather than instructing the implementation agent to copy protected material.

---

# Asset Strategy Reference

## Purpose

Projects often fail because code is specified but the assets needed to make the result coherent are not.

Create `docs/ASSET_BLUEPRINT.md` whenever the project materially depends on external or generated assets.

## Asset categories

Consider as applicable:
- UI icons and illustrations;
- sprites / sprite sheets;
- textures/materials;
- 3D models;
- rigging/animation;
- VFX;
- audio/music/voice;
- fonts;
- video;
- logos/branding;
- datasets/content packs;
- templates/sample data.

## Source modes

For each asset group choose or define a fallback chain:

1. user-provided;
2. generated by available AI/tooling;
3. created procedurally or programmatically;
4. existing repository/reusable asset;
5. verified free/open asset;
6. purchased/licensed asset;
7. temporary placeholder.

Do not assume AI generation is always best. Prefer the source that minimizes maintenance and licensing risk while meeting quality/style needs.

## Blueprint fields

For each important asset group specify:
- purpose;
- required variants/states;
- visual/audio/content direction;
- technical format/dimensions/resolution/frames where known;
- source strategy;
- fallback;
- license/attribution constraints;
- import/integration destination;
- naming convention;
- replacement/migration expectations for placeholders;
- validation criteria.

## Ask the user when
- spending money is expected;
- a particular art/style identity matters and references are insufficient;
- use of AI-generated assets is a meaningful preference;
- commercial licensing restrictions materially affect choices;
- user-owned assets must be used.

## Implementation-agent autonomy
The implementation agent may normally choose exact tools, conversion steps, compression, atlas packing, import settings, and placeholder implementations if product intent and quality constraints are preserved.


# Blueprint/code modularity invariant

For material reusable/stateful responsibilities, the compiler should describe enough of the Blueprint boundary that a coding agent can implement it as an independent cohesive unit without rediscovering system ownership.

A Blueprint should answer, as applicable:

```text
What responsibility does this unit own?
What does it explicitly not own?
What can callers ask it to do?
What state/data may it own or write?
What other contracts may it call/read?
What observable result proves it works?
Where is its implementation boundary anchored?
```

Do not force trivial helper functions/local value transformations into separate Blueprints. The goal is clean semantic building blocks, not maximum file/interface count.

When a user asks for a modular or extensible product, prefer a composition model where screens/entities/workflows/features assemble canonical Blueprint-backed capabilities/modules rather than embedding copies of system behavior.


# v2.30 Blueprint-as-composable product block

Blueprints should make product variants composable in the same sense that a mature engine/editor exposes reusable object types: the Blueprint describes the stable semantic slots, not a copy of all implementation code.

For a repeatable product type, a Blueprint may define:

- stable identity/type;
- required/optional data fields;
- capabilities/modules it can compose;
- conditions/preconditions;
- lifecycle hooks/events;
- presentation/output slots;
- allowed modifier/replacement seams;
- state ownership boundary;
- generic runtime/surface consumer binding;
- authoring/registration path;
- Acceptance requirements.

Keep separate:

```text
Behavior/Reusable-Type Blueprint
Implementation Blueprint
Data/Definition Blueprint
Modifier/Policy Blueprint
```

Only create the layers the project needs.

A Definition Blueprint should be duplicable/adaptable for another same-type variant without copying owner logic. A Modifier Blueprint should reference the canonical capability/field seam it changes rather than copy the full target definition.

## Placeholder replacement

Placeholder presentation/content is valid only when attached through the same production contract/slot intended for final material. Replacing it with production content should not require moving state/rule ownership or bypassing the canonical consumer/runtime.


# v2.31 Coherence-aware Blueprints

A Blueprint that participates in a material cross-system relationship should reference the applicable `SYSTEM_INTEGRATION` invariant/trace IDs rather than copying the relationship locally.

Blueprints may declare:
- canonical source/owner IDs they depend on;
- invariant IDs that must remain true;
- invalidation/recompute/regeneration hooks where applicable;
- Acceptance IDs that prove the relationship.

A Blueprint must not repair a violated shared invariant by embedding a consumer-local corrective offset/value/rule unless the project explicitly defines that local override as intended product semantics.
