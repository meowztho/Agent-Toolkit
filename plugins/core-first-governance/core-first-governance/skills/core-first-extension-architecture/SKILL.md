---
name: core-first-extension-architecture
description: Design, extend, review, refactor, or debug modular software by discovering durable responsibilities, challenging broad responsibility coverage, resolving canonical owners, distinguishing owners from implementation roles, classifying the smallest semantic change, reusing before extending, composing consumers instead of duplicating core behavior, and converging producers onto one canonical owner path. Use for reusable features, ownership ambiguity/conflicts/gaps, provider/adapter additions, import/build paths, configurable variants, repeated local implementations, extension points, plugin/mod systems, architecture repair, or Greenfield system decomposition. Do not use for isolated edits where the owner/path and intended semantics are already clear and reuse, ownership, authoritative state, contracts, producers/gates, or system boundaries are not material.
---

# Core-First Extension Architecture

Use the repository's own authorities as project truth. This Skill teaches a provider- and domain-neutral decision procedure; it does not replace project architecture.

## Core principle

Do not start from "what new class/plugin should I add?"

Start from:

```text
Requirement
→ Responsibility
→ Canonical Responsibility Owner / Master System
→ Capability Contract
→ Module / Implementation / Provider
→ Consumer Composition
→ Data / Modifier / Substitution
```

The hierarchy is semantic, not a required class tree or folder layout.

A universal rule or authoritative state transition has one canonical owner. Extensions may add capabilities, implementations, providers, data, or composition through declared seams; they do not gain permission to create parallel owners or mutate foreign authoritative state directly.

## Phase 0 — Responsibility discovery

For Greenfield, broad product/subsystem work, or unclear architecture, first discover durable responsibility boundaries.

Inspect only what is needed: user/business outcomes, authoritative state/decisions, workflows/events, external/I/O and persistence boundaries, data/lifecycle flows, and relevant APIs/tests.

**Responsibility coverage challenge:** before accepting a broad responsibility set, ask whether a competent domain expert could immediately identify an important ordinary responsibility implied by the requested product that is neither modeled/covered by an existing owner nor explicitly excluded, deferred, or left unresolved. Surface such a gap before owner resolution. Domain expectations are discovery hypotheses, not project authority: do not invent optional features or override explicit user/project decisions.

Group responsibilities only where they genuinely belong to one durable owner. Do not manufacture subsystems merely to fit this method. Do not run a whole-product sweep for a narrow local task.

## Structural roles

Distinguish these roles before editing:

```text
Master System / Responsibility Owner
  one durable owner of a responsibility, rule set, or authoritative state

Capability Contract
  reusable semantic ability or contract owned by a system

Module / Implementation
  reusable concrete behavior that realizes or specializes a capability

Provider / Adapter
  implementation behind a capability boundary, often for external systems

Consumer / Composition Host
  composes capabilities/modules/providers and supplies identity/configuration

Definition / Profile
  durable declarative description or configuration

Runtime Instance / Scoped State
  live execution state created from definitions/configuration
```

A module is not automatically a system. A provider is not automatically a new owner. A definition is not runtime state.

## Responsibility-relative ownership resolution

`Owner` is always relative to a **named responsibility**. Distinguish the canonical owner from the current carrier/decision path, implementation anchor, capability/module/provider, consumer/composition host, data/profile, migration target, or unresolved gap.

Owner existence and reusable-seam proof are different questions. A canonical owner does **not** require multiple consumers/implementations, a unique lifecycle, or a language-level interface. Lifecycle, state proximity, and counts are evidence, not mandatory ownership criteria. Second-consumer/provider proof applies only when seam/capability reusability is material.

Code location, class/file boundaries, size, and names do not prove ownership. Multiple authoritative paths may form a parallel-owner conflict; a foreign write may instead bypass an established owner. Controlled provider/module variants behind one canonical owner are not parallel owners.

A detected gap does not authorize a new owner. Test existing owner/capability extension/composition, data/configuration, and module/provider paths first; otherwise keep ownership **unresolved**. Resolve `Responsibility → Owner → Capability Contract`; an invented interface cannot establish the owner. Centralized data does not centralize shared behavior when consumers still execute the rule. Capability identity comes from reusable semantics, not implementation count.

**Role by semantics, not by name.**

### Project Authority Artifact

A normative file/contract records project truth; it is not itself the runtime/domain owner. Keep documentation authority and semantic/runtime ownership distinct.

## Interaction semantics

When owners communicate, identify the semantic form:

- **Command** — request an authoritative owner to perform a state-changing action.
- **Query** — request information without transferring ownership.
- **Event** — report that an authoritative fact already occurred.

Do not introduce a global event bus, RPC layer, or message broker merely because these semantics exist. Use the project's smallest suitable transport.

## Change classification

Classify a requested architecture/behavior delta before implementation. Prefer the earliest sufficient form.

1. `DATA_OR_ASSET`
2. `VALUE_MODIFIER`
3. `CONFIG_OVERRIDE`
4. `SLOT_SUBSTITUTION`
5. `PROVIDER_SUBSTITUTION`
6. `COMPOSE_EXISTING_CAPABILITY`
7. `ADD_REUSABLE_MODULE`
8. `EXTEND_EXISTING_CAPABILITY`
9. `NEW_REUSABLE_CAPABILITY`
10. `NEW_ADAPTER_OR_PROVIDER`
11. `NEW_EXTENSION_POINT`
12. `EXTERNAL_CONTENT_PACKAGE`
13. `EXTERNAL_EXECUTABLE_EXTENSION`
14. `CORE_RULE_CHANGE`
15. `EXPLICIT_ONE_OFF_EXCEPTION`

`CORE_OWNER_REPLACEMENT` is not a normal extension class. Treat it as an architecture migration requiring explicit impact analysis.

Debugging, discovery, review, migration assessment, and reuse-proof tasks are not additional change classes. If no product/architecture delta is being classified, leave the change classification unset rather than inventing one.

## Decision procedure

1. Identify repository root, applicable instructions, Git state, current requirement, and relevant canonical authorities.
2. Name the exact responsibility, then resolve its current carrier/effective decision path, implementation anchor, and canonical owner status before changing behavior. Do not infer ownership from class/file names or from the mere presence/size of an implementation.
   Before adding a class, module, or owner, check an existing project index if present and search the relevant code boundary by responsibility and likely synonyms; inspect candidate symbols, callers, and tests. A missing name match does not establish that the behavior is absent. Reuse or extend a candidate only when its semantics and owner path fit.
   For quantitative requirements, record what is counted and whether the wording means exact (`5`), minimum (`5 or more`), maximum (`5 or fewer`), approximate target (`about 5`), or unresolved. A bound is not a reason to create extra components; reconcile later changes to the same requirement before selecting the implementation.
3. Ask whether the request is only data/configuration, a relative modifier, or a substitution at an existing slot.
4. Reuse or compose an existing capability/module/provider before extending architecture.
5. Add a reusable module beneath an existing capability before creating a new capability.
6. Extend/compose an existing owner/capability before another system owner; keep a gap unresolved until a distinct responsibility and owner boundary are evidenced.
7. Add a new capability only when a distinct reusable semantic contract is genuinely missing.
8. Add an adapter/provider when the variation is implementation or external integration behind an existing owner.
9. Add a new extension point only when multiple future producers/consumers genuinely need a declared seam.
10. Keep authoritative rules/state at one owner. Consumers provide composition, profiles, identity, and declared variation. External origin grants no extra authority: third-party code/content must use the same owner contracts as first-party producers.
11. Keep definitions/configuration separate from runtime instances and scoped mutable state.
12. Make dependencies explicit. A module/capability asks another owner through its contract rather than reaching into foreign state.
13. If multiple producers exist, converge them before domain behavior:

```text
manual / code / agent / builder / importer / API / external package
→ canonical semantic representation or interface
→ validation
→ canonical responsibility-owner path
→ domain behavior
```

Equivalent content or intent must not gain a producer-specific business-logic path without explicit product justification.

14. For a bug, reverse the same graph:

```text
failing observable
→ runtime/data flow
→ consumer / module / provider
→ capability contract
→ canonical responsibility owner
→ implementation anchor
→ root-cause fix
→ forward re-test
```

## Capability granularity

A capability should be a coherent reusable semantic contract that can be independently understood, implemented, tested, or consumed.

Use these tests:

- If only values differ, prefer data/profile.
- If one concrete behavior differs behind the same contract, prefer module/provider.
- If multiple implementations satisfy the same semantic contract, prefer provider/module variants.
- Do not require a second implementation before recognizing a real reusable capability; implementation count is evidence, not the definition.
- If a genuinely new reusable semantic ability is missing, add a capability.
- Avoid both god-capabilities and capability-sprawl.

## Variation semantics

Prefer explicit variation over copied resolved values.

- Data/configuration: direct declared values.
- Modifier: relative change intended to preserve base propagation.
- Slot substitution: replace one selected module/action/definition at a declared slot.
- Provider substitution: select another implementation behind the same contract.
- Core owner replacement: architecture migration, not ordinary customization.

If multiple modifiers can compose, define deterministic operation semantics, ordering/phases, precedence, scope, lifetime, and conflict behavior. Do not invent a universal modifier engine when the project does not need one.

## Governance for high-risk classes

`CORE_RULE_CHANGE` requires the canonical owner, affected contracts/consumers, compatibility/migration impact, acceptance updates, relevant authority updates, and focused evidence.

`EXPLICIT_ONE_OFF_EXCEPTION` requires proof that normal data/configuration/composition cannot express the need, exact owner/scope and isolation reason, regression evidence, and a revisit if a second meaningful consumer appears.

Use `references/EXTENSION_ARCHITECTURE_METHOD.md` for the full high-risk checklist.

## Public extension-point contract

When a declared extension seam is material, define its owner/capability path, accepted extension forms, discovery/registration, validation/dependencies, allowed variation, forbidden bypasses, runtime trace, compatibility needs, representative proof, and acceptance evidence. The extension point owns the seam, not all behavior behind it.

Use `references/EXTENSION_ARCHITECTURE_METHOD.md` for the full contract fields.

## Conditional architecture profiles

Do not force advanced machinery into every project. Activate only when material: persistent/versioned definitions; distributed/asynchronous boundaries; external/dynamic plugins; untrusted executable extensions; deterministic/reproducible execution; performance-sensitive runtime; multi-tenant/contextual configuration; or polyglot/cross-runtime contracts.

Use `references/CONDITIONAL_PROFILES.md` whenever any profile is triggered; it owns the detailed migration, delivery, trust, determinism, performance, scoping, and cross-runtime checks.

## Producer convergence

Different producers may have different ingestion adapters, but equivalent intent should converge on one semantic representation and canonical responsibility-owner path.

Warning signs:
- builder-only runtime logic;
- import-only business logic;
- provider-specific rules duplicated in consumers;
- plugin-local copies of canonical state;
- AI-authored content bypassing normal validation.

## Acceptance evidence

Use the smallest relevant proof set:

- broad responsibility coverage challenged when material;
- second-consumer/provider reuse when semantic reusability of a seam/capability is material;
- producer convergence;
- no parallel state/decision owner;
- forbidden foreign-write rejection;
- dependency rejection where applicable;
- modifier/base propagation where applicable;
- contract/schema compatibility where applicable;
- definition/runtime-state isolation where applicable;
- reverse-debug path;
- actual user-surface or externally observable behavior.

When reusability is the claim, use a meaningfully different second consumer/provider to challenge the seam. This is not an owner prerequisite. Use an adversarial scenario, contract test, fixture, or fresh-agent challenge instead of speculative production features.

## Do not overbuild

Do not create a plugin loader, registry, interface layer, service container, event bus, manifest format, dependency resolver, sandbox, or migration framework merely because extensibility could theoretically be useful.

A 150-line script can still follow canonical ownership and reuse without becoming a platform.

Prefer:
1. reuse,
2. configuration,
3. correction,
4. simplification,
5. removal,
before new architecture.

## Project artifacts

When the repository already has canonical architecture contracts, update them. Otherwise use the smallest durable representation that the project needs, such as:
- responsibility/system map;
- capability/contract map;
- extension-point registry;
- definition/profile schema;
- producer-to-owner trace;
- version/migration contract;
- focused acceptance evidence.

Do not duplicate exact project truth inside this Skill.

## Read references JIT

Use:
- `references/EXTENSION_ARCHITECTURE_METHOD.md` when broad/Greenfield responsibility coverage, ownership recovery, a declared extension seam, high-risk architecture, or detailed acceptance reasoning is material.
- `references/CONDITIONAL_PROFILES.md` whenever a conditional architecture profile is materially present.
