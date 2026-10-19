# System Composition and Project Atlas Guide

# Current Precedence — v2.22 Product Capability Envelope, Responsibility Discovery and Atlas

Before freezing `SYSTEM_MAP` in greenfield/unclear projects, discover durable Responsibilities from outcomes, authoritative state/decisions, workflows/events, external/I-O boundaries, data/lifecycle/persistence boundaries and, for existing repositories, APIs/call graphs/tests. Do not convert every feature noun into a system.

Terminology: Project Authority Artifact documents truth; it is not the runtime/domain Responsibility Owner. A Responsibility Owner/Master System owns a durable policy/state responsibility. Capability Contracts expose reusable semantics beneath owners. Modules/Providers realize contracts; Consumers compose them.

For nontrivial projects Atlas remains mandatory generated orientation, never normative truth. Its generator/fingerprint/freshness lifecycle must reflect roadmap/build-order and phase-admission status from canonical `PROJECT_PLAN`/Acceptance authorities. On fresh session/context recovery inspect a fresh Atlas for whole-project orientation, then load exact normative sources; Atlas inspection never replaces source reads.

---


## Purpose

A project can be accurately described and still drift if the coding agent is repeatedly allowed to invent the same responsibility in several places.

The compiler must therefore turn the product into a **coherent set of canonical master systems** and make higher-level product objects compose those systems instead of rebuilding them.

Examples:

```text
Interactive consumer
= Input/Command System
+ Runtime State/Policy System
+ Action/Workflow System
+ Presentation System
+ Consumer Data/Profiles/Modifiers
```

```text
Website page
= Site Shell
+ Navigation System
+ Typography/Theme System
+ Layout System
+ Motion/Effects System
+ Data/API System
+ Page Content
```


```text
Discord-as-UI automation
= Discord Interaction Core (post/edit/stop/enable/disable lifecycle)
+ Scheduler/State System
+ Desktop GUI consumer
+ Feature modules
+ per-consumer configuration/modifiers
```

The desktop GUI or a new feature should call/compose the same posting/lifecycle core rather than recreating when/how Discord messages are posted. One central rule change then propagates to every consumer unless a declared local modifier/replacement intentionally differs.

The exact system set is project-specific. The compiler discovers it from the user's vision, references, product surface, and future extension requirements.

---

# 1. System-first decomposition

Apply the single-owner/reuse principle to every coding project. Scale the number/formality of systems to complexity: a tiny program may need only a few clear responsibility boundaries, while a large application needs explicit contracts and many system authorities. Modularity means shared reusable behavior is not copied per consumer; it does **not** mean manufacturing unnecessary services/classes.

Before creating task-sized Blueprints, identify the durable responsibilities that should exist once and be reused. `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` is the canonical authority for how far to decompose below master systems and for classifying later user-request deltas.

Generate for nontrivial projects:

```text
contracts/SYSTEM_MAP.yaml
```

A master system should have:
- stable `system_id`;
- one clear responsibility scope;
- what responsibility domain belongs to it;
- what it explicitly must not own;
- public semantic interface/capabilities;
- dependencies;
- configuration/data inputs;
- extension/modifier/explicit-replacement points;
- systems/objects that consume it;
- authoritative docs/Blueprint IDs;
- acceptance/verification links.

Do not use arbitrary folder names as systems. A system exists because it owns a durable responsibility.

---

# 2. Example system maps

## Interactive realtime application (illustrative)

Possible responsibility candidates, adapted to the actual product:

```text
SYS-INPUT-COMMAND       semantic inputs/commands and source routing
SYS-RUNTIME-STATE       canonical actor/session state where applicable
SYS-MOVEMENT-STATE      spatial/state-transition rules when movement exists
SYS-ACTION              action availability, validation and execution semantics
SYS-ENVIRONMENT         shared environment/boundary/world rules when applicable
SYS-PRESENTATION        presentation requests/bindings
SYS-CONTENT             definitions/profiles/configuration and selection
SYS-SESSION-FLOW        lifecycle, setup, active flow, result/exit state
SYS-UI-SHELL            persistent shell/navigation surfaces
SYS-SETTINGS            configuration/accessibility/persistence where applicable
SYS-AUTHORING           builder/content-authoring path when it proves modularity
```

This is not a checklist. The Product Capability Envelope decides what is applicable; responsibility discovery decides what deserves a canonical owner.

## Website / web application

Possible candidates:

```text
SYS-WEB-SHELL          app/site shell and global regions
SYS-NAVIGATION         routes, navigation state, breadcrumbs/history
SYS-THEME              colors, design tokens, light/dark variants
SYS-TYPOGRAPHY         font roles, scale, text rhythm
SYS-LAYOUT             responsive layout primitives/grid/spacing
SYS-MOTION             transitions, effects, reduced-motion behavior
SYS-COMPONENTS         reusable UI primitives
SYS-PAGE-COMPOSITION   page-specific composition using shared systems
SYS-FORMS              form behavior, validation, submission feedback
SYS-DATA               fetching/cache/state/API integration
SYS-AUTH               identity/session/authorization when applicable
SYS-ACCESSIBILITY      focus, keyboard, semantics, contrast policy
SYS-SEO-METADATA       when applicable
SYS-AUTHORING          CMS/template/admin authoring when it is a core extension path
```

Again, derive the actual map from the project rather than forcing a template.

---

# 3. Master once, reference many

The most important invariant:

> A reusable responsibility is defined once at its canonical owner. Consumers reference/configure it; they do not rebuild local copies.

Example for a configurable consumer:

```yaml
composition:
  consumer_priority:
    type: configurable_consumer
    uses:
      - SYS-INPUT-COMMAND
      - SYS-RUNTIME-STATE
      - SYS-ACTION
      - SYS-PRESENTATION
    data:
      definition: DATA-CONSUMER-PRIORITY
    profiles:
      behavior: priority_default
    modifiers:
      timeout:
        op: add
        value: 8
```

The consumer does **not** own another command parser, state engine, action-policy engine, or presentation architecture.

Local variation belongs in data/config/profiles/declared modifiers or intentional explicit replacements.

## Defaults, profiles, modifiers, and replacement policy

Each reusable system should define, where applicable:
- canonical defaults and their provenance;
- reusable profiles/presets;
- allowed local modifiers and explicit replacements;
- forbidden per-object duplication/bypass;
- what kind of change requires editing the master system contract instead of adding a modifier/replacement.

Prefer:

```text
master default
+ reusable profile
+ small explicit modifier (preferred when base changes should propagate)
```

over copying the system and customizing the copy. Defaults may be user-confirmed, reference-derived, researched, or compiler-selected; record the provenance when it materially affects later decisions.

## Consumer shell + layered value resolution

For reusable architectures, prefer a thin **consumer shell** (entity/page/bot/workflow/component host) that composes canonical systems/modules plus data instead of embedding copies of those systems. The consumer may own identity/content-specific state and declared local modifiers, but shared reusable behavior remains at its master owner.

Do not use the word `override` without defining its merge semantics. A local value can mean very different things:

- `add` / delta;
- `multiply`;
- `replace` (absolute value);
- `min` / `max`;
- collection `append` / `remove`;
- another project-specific deterministic merge operator.

Prefer **relative modifiers** when the user expects global/base changes to propagate. Example:

```text
ReusableAction base timeout = 5
Consumer modifier = add +8
Effective timeout = 13

Later ReusableAction base = 7
Same consumer modifier = +8
Effective timeout = 15
```

Do not store `13` as a copied consumer value in this case; that would sever propagation from the canonical ReusableAction definition. Use explicit `replace: 13` only when the consumer is intentionally fixed independently of future base changes.

For important configurable values, define the resolution pipeline, for example:

```text
master/system default
→ content/module definition
→ reusable profile/preset
→ consumer-specific modifier
→ contextual/runtime modifier
→ effective value
```

Each field/system may use a different valid subset/order, but it must be deterministic and traceable when material. Core changes should propagate automatically through non-replacing layers.

This principle applies beyond games: shared bot scheduling + channel-specific timing deltas, site theme tokens + page-specific modifiers, API retry defaults + endpoint modifiers, workflow defaults + customer-specific policy deltas, etc.

---

# 4. Input/Command vs Action/Workflow

Avoid coupling input-source mechanics to consumer-specific behavior.

## Input/Command System
Owns, as applicable:
- semantic commands/actions;
- device/API/UI source mappings;
- source ownership/context;
- buffering/debouncing where globally applicable;
- remapping/configuration/persistence;
- normalized command events.

It should not own one consumer's action catalog or domain policy.

## Action/Workflow System
Owns, as applicable:
- actions available to a consumer/profile;
- sequencing/timing/preconditions;
- transitions/chains;
- action state/validity;
- resource/rate/policy requirements;
- consumer-specific variation through definitions/profiles.

The Action/Workflow system consumes semantic commands from the Input/Command system. A new consumer normally adds data/profile/action definitions, not another input stack. If a project intentionally combines these responsibilities, define one canonical combined owner rather than recreating it per consumer.

---

# 5. Composition objects

Many user-facing things are not standalone systems. They are **compositions**.

Examples:
- configurable actor/consumer;
- page/page template;
- dashboard;
- product workflow;
- provider-backed integration;
- report/export definition;
- editor/authoring tool.

Generate composition definitions when reuse matters, either in `contracts/SYSTEM_MAP.yaml`, `contracts/CONTENT_REGISTRY.yaml`, or dedicated data Blueprints.

Each composition should state:
- systems it uses;
- data/profile IDs;
- allowed profiles/modifiers/explicit replacements;
- forbidden local duplicate ownership;
- verification that the shared systems are actually reused.

## Authoring as architecture proof

When the user's modular/data-driven goal depends on creating new content without core-code changes, model the authoring/builder path as a first-class system/domain instead of a late convenience UI. It must produce data/content consumed by the same canonical runtime systems. Use `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` for the operational authoring proof and adversarial examples.

---

# 6. System Map contract

Recommended shape:

```yaml
schema_version: 1

systems:
  SYS-INPUT-COMMAND:
    responsibility: semantic command normalization and source routing
    authority_ids: [DOC-INPUT, BP-SYS-INPUT, DATA-ACTIONS]
    responsibility_scope:
      - semantic_command_registry
      - source_assignment
      - input_context
    must_not_own:
      - consumer_action_catalog
      - domain_outcome_policy
    provides:
      - semantic_command_stream
      - mapping_api
    depends_on: []
    consumed_by:
      - SYS-ACTION
      - SYS-NAVIGATION
    verification:
      - AC-INPUT-CANONICAL

compositions:
  configurable_consumer:
    required_systems:
      - SYS-INPUT-COMMAND
      - SYS-RUNTIME-STATE
      - SYS-ACTION
      - SYS-PRESENTATION
    local_duplicate_ownership_forbidden: true
```

`SYSTEM_MAP.yaml` is authoritative for **top-level system topology and responsibility scope**. When reusable capability depth is material, `CAPABILITY_GRAPH.yaml` owns the semantic hierarchy below/among master systems. `SYSTEM_INTEGRATION.yaml` owns material per-rule decision ownership, mutable-state ownership, allowed writers and cross-system runtime edges. Do not maintain competing detailed ownership matrices across them.

`SYSTEM_MAP.yaml` should be compact **as a routing/topology contract**, but the project package itself is not compactness-limited. Every nontrivial core system should have a detailed canonical authority plus bounded Blueprints/contracts where applicable. Detailed rules must never be dropped merely to keep the file count small.

---

