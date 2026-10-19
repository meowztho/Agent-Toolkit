# Capability Hierarchy and Core-First Change Gate Guide

# Current Precedence — v2.22 Core-First Extension + Reuse-Proof Boundary

Canonical chain:
`Requirement → Responsibility → canonical Responsibility Owner/Master System → Capability Contract → Module/Implementation/Provider → Consumer Composition → Data/Modifier/Substitution`.

Orthogonal producer path:
`manual/code/agent/builder/importer/API/external package → canonical semantic representation/interface → validation → Responsibility Owner path → domain behavior`.
Different adapters may execute different code; equivalent intent must not gain producer-specific business-rule ownership.

Role separations: `Project Authority Artifact != runtime/domain owner`; `Capability Contract != Module/Implementation/Provider`; `Definition/Profile != Runtime Instance/Scoped Mutable State`.

For material changes classify the smallest sufficient semantic delta using this canonical 15-class taxonomy: `DATA_OR_ASSET`, `VALUE_MODIFIER`, `CONFIG_OVERRIDE`, `SLOT_SUBSTITUTION`, `PROVIDER_SUBSTITUTION`, `COMPOSE_EXISTING_CAPABILITY`, `ADD_REUSABLE_MODULE`, `EXTEND_EXISTING_CAPABILITY`, `NEW_REUSABLE_CAPABILITY`, `NEW_ADAPTER_OR_PROVIDER`, `NEW_EXTENSION_POINT`, `EXTERNAL_CONTENT_PACKAGE`, `EXTERNAL_EXECUTABLE_EXTENSION`, `CORE_RULE_CHANGE`, `EXPLICIT_ONE_OFF_EXCEPTION`. Debug/discovery/review/migration are task types, not extra change classes. `CORE_OWNER_REPLACEMENT` is an architecture migration, not ordinary customization.

Public extension seams, when material, state owner/capability path, accepted module/provider/definition types, registration/validation, dependencies, allowed variation, forbidden writes/bypasses, runtime traces, version/schema/migration and evidence. Prefer data/content/modules/adapters to executable plugins when sufficient. External origin grants no extra authority.

Create advanced machinery only under material conditional profiles such as persistent/versioned definitions, distributed/async boundaries, dynamic external plugins, untrusted executable extensions, deterministic/reproducible execution, performance-critical runtime, multi-tenant/contextual configuration or polyglot/cross-runtime contracts. A normal configured external API provider is usually an adapter/provider, not automatically a plugin ecosystem.

Second-consumer proof must not create speculative shipping work. Prefer existing second consumer/provider → already-required planned case → adversarial scenario → isolated contract/test fixture → Fresh-Agent challenge. Architecture reuse proof scales with **semantic diversity, not consumer count**: use the smallest representative proof set that exercises materially different composition paths.

Use the same semantic graph forward for implementation and backward for debugging. Reuse/correct/extend canonical owners before creating parallel paths.

---


## Purpose

A modular project still drifts if a later user request is implemented directly on the most visible consumer because that is the fastest local edit.

The compiler must therefore preserve a stronger invariant across initial implementation, later conversations, context loss, handoffs and provider changes:

> **New behavior is implemented at the lowest reusable semantic capability that owns it, then composed into consumers. Consumer-specific differences are data/profiles/modifiers unless the behavior itself is a new reusable capability.**

The immediate user request is a product delta, not permission to bypass the architecture.

This applies to games, websites, APIs, desktop tools, bots, SaaS, data pipelines and other software.

---

# 1. Semantic hierarchy

Use a semantic hierarchy, not a mandatory class hierarchy.

```text
PRODUCT / APPLICATION
  ↓
DOMAIN / MASTER SYSTEM
  ↓
REUSABLE CAPABILITY
  ↓
REUSABLE MODULE / BEHAVIOR DEFINITION
  ↓
CONSUMER COMPOSITION / PROFILE
  ↓
INSTANCE DATA / MODIFIER
```

Not every project requires every level. Do not manufacture abstractions with no semantic responsibility.

Typical meanings:

- **Product/Application** — the complete user-facing product.
- **Master System** — canonical domain owner, e.g. Movement, Health, Pricing, Transactions, Notifications.
- **Capability** — reusable possibility/lifecycle inside or across a master system, e.g. Ground Locomotion, Flight Locomotion, Discount Evaluation, CSV Import Adapter contract.
- **Module/Behavior Definition** — reusable behavior/content module, e.g. ReusableAction, Compare Action, Retry Policy, Newsletter plugin.
- **Consumer Composition/Profile** — entity/page/service/workflow that attaches capabilities/modules and supplies identity/configuration.
- **Instance Data/Modifier** — values/assets/local deltas that do not introduce new reusable behavior.

The hierarchy is about **semantic ownership and reuse**, not folder depth or inheritance.

---

# 2. Core-first change law

Before implementing any material new behavior requested for a concrete consumer, classify the request.

```text
USER REQUEST
  ↓
What consumer/surface appears to need the change?
  ↓
What reusable capability makes that behavior possible?
  ↓
Does that capability already exist?
  ├─ yes → compose/configure/extend through its contract
  └─ no  → create/extend the lowest reusable capability first
              ↓
           attach it to the consumer
```

Do not begin with "where can I patch this consumer?".
Begin with "which canonical capability owns this behavior?".

A consumer may directly change only:
- identity/content data;
- assets;
- declared profiles;
- explicit modifiers/replacements;
- consumer-local presentation/state that is genuinely not reusable domain behavior.

Reusable behavior must not first appear as an incidental method/branch in a consumer.

---

# 3. Change classification

Every material implementation request is classified before source edits.

Recommended classes:

```text
DATA_OR_ASSET
VALUE_MODIFIER
COMPOSE_EXISTING_CAPABILITY
EXTEND_EXISTING_CAPABILITY
NEW_REUSABLE_CAPABILITY
NEW_ADAPTER_OR_SURFACE
CORE_RULE_CHANGE
EXPLICIT_ONE_OFF_EXCEPTION
```

The last category requires rationale explaining why reuse is intentionally not appropriate. It must not become a shortcut for delivery speed.

For small local changes, classification may be one concise state record. For complex changes, create/update a scoped change/ExecPlan.

Suggested runtime state:

```yaml
current_change:
  id: CHG-...
  request: "..."
  classification: NEW_REUSABLE_CAPABILITY
  target_consumers: [CONSUMER-PLANE]
  master_system: SYS-MOVEMENT
  capability_path: [CAP-LOCOMOTION, CAP-FLIGHT]
  existing_owner: null
  new_owner: CAP-FLIGHT
  reuse_check:
    searched_existing_paths: true
    result: no_existing_flight_capability
  second_consumer_test:
    candidate_capability: CAP-FLIGHT
    plausible_consumers: [CONSUMER-BIRD, CONSUMER-DRONE]
    shared_semantics: airborne_flight_rules
    variation_axes: [speed_profile, control_source, stamina_or_fuel_profile]
    result: reusable_below_consumer
    rationale: "Shared flight semantics belong below Plane; consumer differences are profiles/modifiers."
  composition_after_change: [CAP-GROUND, CAP-FLIGHT]
  modifier_semantics: []
  one_off_exception_rationale: null
  required_contract_updates: [CONTRACT-CAPABILITY-GRAPH, CONTRACT-SYSTEM-INTEGRATION]
  status: classified
```

This is runtime/change state, not a second project truth.

---

# 4. How deep should decomposition go?

Descend until the requested behavior reaches the **lowest reusable semantic owner** with a stable contract.

Create or split a reusable capability when one or more are true:
- it owns distinct state, lifecycle, invariants or failure behavior;
- multiple current or plausible future consumers can use it;
- the user expects it to evolve independently;
- putting it in the requesting consumer would make that consumer own foreign domain logic;
- a second consumer would otherwise copy the behavior;
- testing it independently provides meaningful value;
- it represents a real extension point promised by the product.

Stop decomposing when:
- the difference is only a value/asset/label/profile/modifier;
- existing capabilities already express the behavior through composition;
- another layer would only rename a trivial helper without an independent contract;
- the abstraction would increase maintenance without protecting reuse/ownership.

The goal is **minimum reusable semantic depth**, not maximum number of systems.

---

# 5. Counterfactual second-consumer test

For a proposed new capability ask:

> Could a plausible second consumer use this behavior without copying or modifying the first consumer?

If yes, the capability should normally live below the consumers.

A second consumer does not always need to be implemented. The test can be architectural/adversarial.

If no plausible second consumer exists, still isolate the behavior when it has an independent lifecycle/contract or is expected to evolve. Otherwise keep it as local content/data rather than inventing a fake core.

---

# 5A. Representative Proof Set

The counterfactual second-consumer test asks whether reuse **should exist**. A Representative Proof Set proves that the implemented architecture **actually supports reuse**.

**Owner/capability existence is resolved before reuse proof.** A canonical Responsibility Owner does not require multiple consumers/implementations, and a coherent reusable capability may be valid with one implementation. Representative Proof challenges the maturity of an already reasoned reusable seam; it must not be used as an admission test for whether the owner exists. If ownership is unclear, resolve the Responsibility/Owner path first.

For every materially reusable system/capability, prefer the **smallest representative set that exercises materially different composition paths**. Do not measure architecture maturity by the number of production consumers created.

Use three semantic roles when applicable:

```text
CANONICAL WALKING SKELETON / REFERENCE CONSUMER
= proves the canonical end-to-end integration path: owners connect, definitions/config reach runtime, and the normal contract can execute.

REPRESENTATIVE CONSUMERS
= meaningfully different cases that challenge composition, modifiers, mappings, providers, lifecycle/failure behavior or other material variation seams while reusing the same canonical owners/capabilities.

PRODUCTION BREADTH
= additional similar consumers/content after reuse is proven; useful for product coverage/scale, not additional architecture acceptance.
```

Some domains may call the first role a universal dummy, template, baseline provider or reference implementation. The role is optional and domain-specific; the semantic purpose is the canonical walking skeleton.

## Choose by variation axes, not count

1. Identify the material variation seams the architecture promises to support.
2. Select one canonical skeleton/reference case that proves the normal owner/contract/runtime path.
3. Add the fewest heterogeneous cases needed to exercise materially different seams.
4. Prove every case uses the same canonical owners/capabilities and declared extension/variation contracts without consumer-local rule duplication or hidden bypasses.
5. Stop when every material variation axis is covered. Additional similar cases become content/scale testing unless they introduce a genuinely new semantic axis.

Typical variation axes include:
- different module/capability composition;
- relative modifiers versus defaults;
- different action/input/mapping profiles;
- provider substitution;
- synchronous versus asynchronous/failure behavior;
- optional capability presence/absence;
- version/schema variation;
- different producer/authoring paths converging on the same runtime owner.

A representative case does **not** have to become speculative shipping content. Evidence priority remains:

```text
real existing consumer/provider
→ already-required planned consumer/provider
→ adversarial or isolated fixture
→ Fresh-Agent architecture challenge
```

## Acceptance distinction

```text
Walking skeleton alone
→ integration may be proven

Walking skeleton + heterogeneous representative cases
→ reuse/composition may be proven

More similar consumers
→ product breadth/scale evidence
```

Architecture reuse proof passes only when the heterogeneous cases reuse the same canonical semantic owners/capabilities, variations stay within declared contracts/data/modifiers/providers, and no consumer-local duplicate rule owner/path is required. If a representative case forces an undeclared core patch, either the capability boundary is incomplete or the test has exposed a genuinely new reusable capability; classify that change before continuing.

Core invariant:

> **REUSE PROOF SCALES WITH SEMANTIC DIVERSITY, NOT CONSUMER COUNT.**

---

# 6. Universal examples

## Vehicle movement

Initial project:

```text
SYS-MOVEMENT
  CAP-LOCOMOTION
    CAP-GROUND

Car = CAP-GROUND + CarProfile
```

Later request:

> Add an airplane that can fly.

Wrong:

```text
Plane
  drive()
  fly()   # plane-specific flight implementation
```

Correct semantic change:

```text
SYS-MOVEMENT
  CAP-LOCOMOTION
    CAP-GROUND
    CAP-FLIGHT     # new reusable capability

Car   = CAP-GROUND + CarProfile
Plane = CAP-GROUND + CAP-FLIGHT + PlaneProfile
Bird  = CAP-FLIGHT + BirdProfile
Drone = CAP-FLIGHT + DroneProfile
```

Plane and Bird may configure Flight differently. They do not own different flight cores.

## Quota / limit

```text
SYS-QUOTA
  owns current quota lifecycle and validation
  base limit = 100

Consumer A profile: limit add +50
Effective limit = 150
```

Changing the core base to 120 produces 170 when the modifier is relative. The consumer does not gain a second quota implementation. Producers request changes through the Quota contract instead of writing canonical quota state directly.

## Movement speed

```text
SYS-MOVEMENT
  CAP-GROUND.speed base = 5

Consumer A: speed multiply 1.2
Consumer B: speed add +2
```

Speed differences are modifiers, not separate Movement systems.

## Ability / reusable_action

```text
CAP-PROJECTILE / Ability runtime
  Action_Base.daconsumer = 5

Consumer A: reusable_action daconsumer add +8
```

If the base becomes 7, Consumer A becomes 15. `13` is not copied into the consumer unless an explicit replacement is intended.

## Generic product page

```text
ProductPage = generic rendering consumer
ProductDefinition = title/iconsumer/price/options/badges/actions

SYS-PRICING   → price
SYS-DISCOUNT  → discount result
SYS-INVENTORY → availability
SYS-REVIEWS   → review data
```

A laptop and a shirt use the same ProductPage. ProductPage does not implement discount or inventory rules.

If a new reusable `Compare` action is required, define it as an action/capability/module and attach it to eligible products instead of adding laptop-only comparison logic to ProductPage.

## Personal finance

```text
Manual Entry ─┐
CSV Import ────┼→ canonical Transaction Pipeline → Transaction Store
Bank Sync ─────┘

Transaction Store → Budget / Analytics / Search / Reports
```

A later PayPal importer is another adapter/producer. It does not create `PayPalTransaction` business logic inside Budget or Analytics.

## Discord-as-UI bot

Posting/edit/stop/enable/disable lifecycle belongs to a canonical Discord interaction core. Desktop GUI, schedulers and feature modules compose that core. A later feature does not recreate Discord lifecycle behavior locally.

---

# 7. Capability Graph contract

For projects where capability depth/reuse is material, generate:

```text
contracts/CAPABILITY_GRAPH.yaml
```

Example:

```yaml
schema_version: 1

capabilities:
  CAP-LOCOMOTION:
    parent_system: SYS-MOVEMENT
    parent_capability: null
    kind: capability_group
    responsibility: "Reusable movement modes"

  CAP-GROUND:
    parent_system: SYS-MOVEMENT
    parent_capability: CAP-LOCOMOTION
    kind: reusable_capability
    owns:
      - grounded_movement_rules
    parameters:
      - speed
      - acceleration

  CAP-FLIGHT:
    parent_system: SYS-MOVEMENT
    parent_capability: CAP-LOCOMOTION
    kind: reusable_capability
    owns:
      - airborne_flight_rules
    consumers:
      - CONSUMER-PLANE
      - CONSUMER-BIRD
```

Rules:
- stable capability IDs;
- exactly one semantic parent/owner where applicable;
- capability nodes describe reusable semantics, not code files;
- consumer references do not make the consumer an owner;
- values/profile overrides remain outside the capability definition unless they are canonical defaults;
- paths must resolve to `SYSTEM_MAP` and `SYSTEM_INTEGRATION` owners.

`SYSTEM_MAP` remains the authority for top-level master systems. `CAPABILITY_GRAPH` owns the reusable semantic hierarchy beneath/among those systems. `SYSTEM_INTEGRATION` owns runtime producer/writer/consumer flow.

---

# 8. Architecture law must survive later conversation

A later user message is treated as a **delta against the existing capability graph**, not a fresh greenfield implementation request.

Always-on project instructions must include a short version of this law:

> Before implementing new behavior on a consumer, resolve the canonical system/capability. If the behavior is reusable and missing, add/extend the reusable capability first, then compose the consumer. Use data/profiles/modifiers for variation. Delivery speed is not permission to create a parallel consumer-local core.

This belongs in the root agent instruction layer because provider conversations, summaries and compaction are not reliable long-term enforcement.

The full rationale remains in project authorities; do not bloat always-loaded instructions with every example.

---

# 9. Provider-neutral enforcement

When the runtime supports lifecycle hooks, enforce the law as process, not only prose.

Recommended lifecycle:

```text
UserPromptSubmit / session steer
  → inject architecture-law reminder + current master outcome

Before first source write for a material change
  → require current_change.classification
  → require canonical owner/capability path
  → require reuse check and, when applicable, second-consumer test
  → reject EXPLICIT_ONE_OFF_EXCEPTION without recorded semantic rationale

Post edit / milestone
  → integration/dead-contract/duplicate-owner audit

PreCompact / PostCompact or equivalent
  → rehydrate architecture kernel / capability graph pointer

Stop / TaskCompleted
  → block completion if current change is not audited/verified
```

A deterministic hook can validate that the classification/required records exist and schemas resolve. Semantic correctness may require the agent/independent reviewer, but the agent must not be able to skip the gate silently.

If hooks are unavailable, the same sequence is a mandatory phase gate in the execution runtime.

Provider adapters map this invariant to their actual primitives; the invariant itself stays provider-neutral.

---

# 10. Context loss and handoff

`CONTEXT_HANDOFF.md`, context-rich START/CONTINUE/GOAL prompts and reconstruction artifacts must include the **architecture law and current capability model**, not only current tasks.

After major context loss:

```text
rehydrate product model
→ rehydrate master systems + capability graph + guardrails
→ rehydrate current change classification
→ only then resume JIT task work
```

Do not resume from a summary that says only "currently adding plane flight". A sufficient handoff says that Flight is a reusable capability under Movement and Plane is a consumer composition.

When a user correction intentionally changes the architecture, update the canonical graph/guardrails first. Conversation text alone must not silently supersede the stored architecture.

---

# 11. Fresh-agent and adversarial change tests

Fresh-Agent Reconstruction must include at least one **future-change test** for modular/extensible projects.

Examples:

- "The project currently has cars. Add a flying plane. Where does Flight belong?"
- "A consumer needs +50 quota. Do you copy the quota logic or apply a declared modifier through the canonical owner?"
- "Add PayPal import. Which systems should change?"
- "A product gains Compare. Does ProductPage gain laptop-specific logic?"

PASS requires the agent to:
1. identify the correct existing consumer/system;
2. classify the change;
3. descend to the lowest reusable semantic owner;
4. create/extend a capability only when necessary;
5. compose/configure the consumer afterward;
6. preserve single ownership/runtime flow;
7. state what core code must **not** be duplicated.

A package that explains the current architecture but causes a fresh agent to violate it on the first new feature is not reconstructable enough.

---

# 12. Completion / integration audit additions

For material changes, Integration Audit should verify:

- change classification was recorded before implementation;
- requested consumer behavior maps to an existing/new canonical capability;
- no reusable behavior first appeared only inside the consumer;
- new capability has one owner and stable contract;
- consumer variation uses declared data/profile/modifier semantics;
- second-consumer/adversarial reuse test passes when applicable;
- no parallel implementation path was added;
- canonical base changes propagate through relative modifiers;
- handoff/start/continue snapshots are regenerated when architecture materially changes;
- final runtime evidence exercises the actual canonical path.

Core invariant:

> **Implement the capability first, then the consumer. Configure differences; do not fork the shared behavior.**


# v2.30 Definition-driven composition gate

When repeated variants share semantics, distinguish **capability ownership** from **variant definition**.

Preferred chain:

```text
canonical Capability
→ Blueprint/reusable Definition Type seam
→ Definition/Profile/Composition
→ generic consumer/runtime
→ instance
```

Before adding variant-specific code, classify the request:

1. **data/profile change** — same capabilities, different values/content;
2. **modifier composition** — same owner, declared delta/module/merge semantics;
3. **capability composition** — existing reusable capabilities combined differently;
4. **new reusable capability** — missing semantic behavior belongs at canonical owner;
5. **new consumer/reusable Definition Type** — genuinely different realization contract;
6. **explicit one-off exception** — only when semantic reuse is not intended and rationale is recorded.

A repeated instance is not evidence for another owner.

## Product-engine test

Where repeatability is a material product claim, acceptance should prove at least one of:

- a second materially different definition reaches the same generic runtime/surface without copied core logic;
- a base-definition change propagates through declared relative modifiers;
- adding/removing a composed capability changes behavior through the public seam;
- the authoring/producer path can create a new definition that appears in the normal product without source-code edits outside declared registration/generation.

This proves the project acts like a reusable domain engine rather than a collection of individually hardcoded examples.


# v2.31 Composition-coherence change classification

Before a local fix to a consumer/projection, ask whether the defect is actually a violated cross-system relationship.

Classify:

```text
LOCAL_DEFECT
  one owner/implementation is wrong; no shared relation changed

COHERENCE_DEFECT
  two or more owners/projections disagree about one canonical relation/source

MISSING_INVARIANT
  the product requires a cross-system relation but the package never modeled it

DERIVATION_BYPASS
  a consumer copied/overrode data that should derive from the canonical source
```

For `COHERENCE_DEFECT` or `DERIVATION_BYPASS`, repair the canonical source/derivation/contract first and rerun all affected consumers. Do not normalize drift by teaching every consumer its own exception.
