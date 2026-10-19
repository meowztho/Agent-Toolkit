# Vision and Reference Preservation Guide

# Current Precedence — Reference Semantics

A named product, document, workflow, screenshot, site or researched source is not a specification. For each material reference preserve: stable reference ID; source identity/URL/date/version when available; provenance; `adopt | adapt | reject | inspiration-only`; exact traits/findings; rationale; explicit non-implied traits/exclusions; affected Responsibility/System/Capability/Acceptance IDs.

The compiler owns the abstraction used by the project. A later implementation agent should not need to reinterpret the same source and accidentally derive a different rule. START carries high-signal reference anchors; the Reference Register/Map remains canonical.

---


## Purpose

Autonomous projects can fail even when individual requirements are precise.

A common failure mode is:

```text
user describes a coherent product vision
→ compiler decomposes it into local requirements
→ local controls/components become more precise
→ global composition, tone, hierarchy, and intended experience are lost
→ implementation is technically plausible but no longer resembles the approved concept
```

The compiler must therefore preserve two things at the same time:

1. **holistic product intent** — what the user is trying to create and how the whole result should feel/work;
2. **engineering contracts** — the bounded rules required to implement and verify it.

Decomposition must add precision without replacing the original vision.

---

# 1. USER_VISION is a first-class authority

For projects with meaningful subjective/product/design intent, generate:

```text
docs/USER_VISION.md
```

This file is not a chat summary. It is the durable record of the user's actual intent.

It should preserve:
- the desired whole-product experience;
- important relationships between systems/screens/features;
- non-negotiable qualities;
- references and why the user cited them;
- accepted/rejected interpretations;
- high-signal verbatim user wording where exact phrasing carries meaning;
- approved visual concepts/mockups and their authority scope.

Do not fill it with every conversational sentence. Preserve only statements whose wording or relationship materially constrains the future result.

---

# 2. Verbatim Vision Anchors

When the user expresses a high-signal preference, preserve a short exact quote instead of replacing it only with compiler prose.

Example:

```markdown
## Vision Anchors

### VQ-001 — Home-screen role
Source: user
Status: confirmed
Original language: de

> "der slime mit idle animationen wie ein tamagichi"

Normalized interpretation:
The central creature is not decorative. It is the living focal point of the home screen and should idle/react like a virtual pet.

Derived authorities:
- DOC-DESIGN#Home
- CONTRACT-VISUAL#home
- BP-UI-HOME
```

Rules:
- Preserve the user's original language in the quote.
- Generated explanatory text may remain English.
- Do not silently "improve" a quote.
- Use stable quote IDs when downstream rules derive from it.
- Quote selectively; do not duplicate the full interview.
- If the user corrects the intent, supersede or mark the old anchor as rejected rather than leaving contradictory active anchors.

Exact user wording is provenance, not implementation syntax.

---

# 3. Holistic synthesis before decomposition

For products where design/experience matters, do not immediately turn the first description into atomized Blueprints.

Preferred sequence:

```text
raw user vision
→ understand references
→ holistic product/design synthesis
→ concept/mockup/proposed experience when useful
→ user correction/approval
→ vision lock
→ design/reference contracts
→ bounded Blueprints
→ implementation
```

The model may use its design judgment during the synthesis stage. The goal is to make the implicit whole visible before freezing local details.

Do not force the user to approve every implementation detail. The lock concerns product/design intent, not reversible engineering choices.

---

# 4. Approved Mockups are first-class references

If the user approves a generated or supplied mockup/concept, register it as an approved reference.

An approved mockup may be authoritative for:
- composition;
- visual hierarchy;
- persistent navigation;
- relative placement;
- density;
- grouping;
- style direction;
- visible content;
- interaction affordances shown in the reference.

It is not automatically authoritative for:
- exact source-code structure;
- hidden state architecture;
- implementation technology;
- interactions that cannot be inferred from the iconsumer.

Record an explicit authority scope.

Example:

```yaml
reference_id: REF-HOME-MOCKUP-03
status: user_approved
artifact: references/home_mockup_v3.png
authority_scope:
  - composition
  - hierarchy
  - persistent_navigation
  - relative_layout
  - visible_component_set
not_authority_for:
  - code_architecture
  - hidden_state
  - unspecified_transitions
```

If the user says "1:1", "exactly like this", or equivalent, increase fidelity requirements accordingly. Otherwise preserve the approved composition and intent without assuming pixel-perfect duplication.

---

# 5. Visual Design Contract

For visual applications with approved references or important layout intent, generate:

```text
contracts/VISUAL_DESIGN_CONTRACT.yaml
```

This contract is the machine-readable bridge between the holistic design and local implementation.

Recommended structure:

```yaml
screens:
  home:
    authority_ids:
      - DOC-USER-VISION
      - DOC-DESIGN
      - REF-HOME-MOCKUP-03

    gestalt:
      focal_point: central_creature
      visual_priority:
        - central_creature
        - primary_status
        - primary_actions
        - persistent_navigation

    persistent_shell:
      top_bar: true
      primary_navigation: true

    layout:
      top_bar_region: "0-10% height"
      content_region: "10-87% height"
      navigation_region: "87-100% height"
      central_creature: "centered; dominant visual mass"

    invariants:
      - navigation_position_consistent_across_primary_screens
      - content_must_not_visually_compete_with_primary_focal_point
      - no_debug_or_placeholder_layout_in_release_state
```

Use proportions/relationships rather than false pixel precision unless exact dimensions are genuinely required.

---

# 6. Gestalt Context Envelope

JIT context must not make a local task blind to the whole it belongs to.

For a design/UI/experience task, load the smallest **Gestalt Context Envelope** in addition to the local Blueprint:

```text
relevant USER_VISION anchors
+ approved reference/authority scope
+ parent screen/flow design contract
+ local Blueprint
+ relevant implementation/tests
```

Examples:

```text
implement one bottom-nav button
```

must still know:
- the navigation is persistent across five top-level screens;
- its visual position must remain constant;
- the home screen's focal point is the creature, not the navigation;
- the approved mockup defines the overall shell.

This is not permission to preload all project documentation. It is bounded parent-context routing.

---

# 7. Preserve relationships, not just components

Coverage is incomplete if all components are present but the user's relationships between them are missing.

The compiler must preserve statements such as:
- "X stays visible while Y changes";
- "A is the main focus and B is secondary";
- "all primary screens share the same navigation";
- "this feature should feel immediate and not interrupt flow";
- "new content should reuse the same system rather than create special-case code".

These often matter more to perceived fidelity than individual component descriptions.

Record them as invariants in the best authority: USER_VISION, DESIGN, APP_FLOW, VISUAL_DESIGN_CONTRACT, or a behavior Blueprint.

---

# 8. Reference compilation must remain traceable

A derived rule should be able to point back to its source.

Preferred chain:

```text
VQ-003 user quote
        ↓
REF-SSF2-MENU / REF-MOCKUP-04
        ↓
DOC-DESIGN#Navigation
        ↓
CONTRACT-VISUAL#primary_shell
        ↓
BP-UI-NAVIGATION
        ↓
AC-UI-07
        ↓
EV-UI-07 screenshot + interaction
```

Not every low-level rule requires the full chain, but important subjective decisions should remain auditable.

---

# 9. Design lock and controlled deviation

Once the user has approved a concept/reference and it has been compiled into authoritative design rules:

- do not casually redesign it during implementation;
- do not replace it with framework defaults because they are easier;
- do not simplify the visible composition merely to make a local task pass;
- do not interpret implementation freedom as product-design freedom.

A material deviation is allowed when:
- the user requested it;
- the approved design is technically impossible under a hard constraint;
- accessibility/platform constraints require adaptation;
- a stronger confirmed requirement conflicts with it.

Record the deviation and reason.

---

# 10. Runtime fidelity loop

For approved visual references, verification should explicitly compare **Soll vs Ist**:

```text
approved reference / visual contract
→ running final/current build
→ screenshot/render at same meaningful state
→ inspect composition + hierarchy + required visible elements
→ inspect interaction separately
→ fix mismatch
→ record evidence
```

Do not reduce visual verification to:
- "all nodes exist";
- "all buttons are present";
- "the screen opens";
- "the build passes".

A screen can contain every required component and still fail the intended design.

---

# 11. Screen-level acceptance is mandatory when Gestalt matters

Component-level criteria are insufficient for a composed interface.

In addition to local checks, define one or more screen-level criteria such as:

```yaml
AC-UI-HOME-GESTALT:
  title: Home screen matches approved composition and hierarchy
  evidence_required:
    - interactive_runtime
    - screenshot_review
  sources:
    - DOC-USER-VISION
    - CONTRACT-VISUAL
    - REF-HOME-MOCKUP-03
```

This prevents:

```text
button A PASS
button B PASS
panel PASS
navigation PASS
```

from being mistaken for:

```text
whole screen PASS
```

---

# 12. Compiler behavior after a successful concept/mockup

When a concept generated from the user's description is accepted as "this is basically my vision":

1. treat that as valuable product evidence;
2. register the iconsumer/reference;
3. extract its hierarchy, layout, shell, grouping, states, and visible content;
4. link those traits to exact USER_VISION anchors where possible;
5. ask only about materially ambiguous interactions/content;
6. compile a visual contract;
7. then decompose implementation responsibilities.

Do not throw away the successful holistic synthesis and start again from abstract requirements.

---

# 13. Coverage Gate additions

Before delivering a compiled project, verify:

- Is the original desired experience still recognizable from the package?
- Are high-signal user phrases preserved where paraphrase could lose meaning?
- Are approved mockups/references registered with authority scope?
- Are global visual/layout relationships preserved outside local component Blueprints?
- Will a local UI task receive enough parent/Gestalt context to avoid design drift?
- Is there a screen-level acceptance criterion in addition to component checks where appropriate?
- Can visual runtime evidence be compared against the approved reference?
- Can a future agent distinguish the user's words from compiler interpretation/recommendation?

If not, the package is not loss-resistant.

---

# 14. Core principle

```text
The compiler must not replace a coherent user vision with a bag of correct parts.

Preserve the whole.
Then add precision.
Then verify the whole again in the running product.
```

# Reference ingestion and project-specific visual baseline gate

A visual file placed in the repository is not consumed merely because its filename is discoverable.

For every material user-supplied screenshot/mockup/design image:
1. preserve/copy the actual artifact into the generated project when licensing/privacy permits;
2. assign a stable reference ID and register its path/provenance;
3. route it from the applicable surface/design domain in `PROJECT_INDEX`;
4. extract `adopt/adapt/reject/inspiration-only` traits and explicit exclusions;
5. mark it as `required_reference_id` for implementation/verification tasks whose fidelity depends on it;
6. require actual visual inspection with a capable tool before such work; if no such capability exists, visual fidelity remains unresolved/inconclusive rather than silently delegated to generic model taste.

## Consolidated mockup / visual baseline

When visual direction is material but supplied references are fragmented, cross-surface, or too ambiguous to drive implementation, create a project-specific **derived visual baseline** before broad UI implementation:
- use the user's supplied references and compiled traits as inputs;
- generate a coherent mockup/storyboard/HTML prototype with an available image/design/UI capability;
- record which source traits it preserves and where it intentionally adapts them;
- if the choice is materially subjective and not already delegated, obtain user approval before Design Lock;
- if design judgment was delegated, label the mockup `COMPILER_RECOMMENDATION` and keep user references higher in precedence.

Do not generate a new mockup merely to overwrite a clear supplied mockup. The derived baseline is a bridge from several references to one implementation target, not a license for generic redesign.

START/Atlas should expose reference thumbnails/links where practical, but exact visual work still requires inspection of the underlying registered reference artifacts.


# v2.24 Visual target stays active during realization

A correct `DESIGN.md` or registered reference is insufficient if later execution never places its meaning into active context.

For design-heavy projects compile a compact, generated **Visual/User-Surface Target capsule** for START and for any continuation whose admitted work affects the surface. It should include:

- product-specific visual identity/gestalt in a few high-signal lines;
- applicable registered reference IDs;
- approved/delegated derived baseline ID when one exists;
- essential composition/hierarchy/placement constraints;
- explicit anti-default traits where generic framework/model styling would violate the vision.

This capsule is not authoritative and cannot replace the underlying visual authorities. Its purpose is to prevent JIT routing from making visual intent invisible until late polish.

Design realization should begin on a representative normal-user surface early enough that screenshot-to-authority feedback can still change shared primitives/layout before many consumers are built.
