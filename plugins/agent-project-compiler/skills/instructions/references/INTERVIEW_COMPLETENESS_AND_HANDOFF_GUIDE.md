# Interview Completeness, Traceability, and Context Handoff Guide

# Current Precedence — v2.22 Capability-Envelope Coverage + Lossless Materialization

For every answered compiler question in a nontrivial project preserve: stable Round/Q ID, exact question and verbatim answer in the package `INTERVIEW_LEDGER`. `see context`, `same as above`, ellipsis, pointer-only bodies or summary-only substitutes do not count.

The Ledger is provenance, not the final normalized model. Every **material** answer must additionally be materialized transactionally into its real canonical destination (Vision, Decision Compendium, Reference semantics, System/Capability/Integration contract, Blueprint, Acceptance, guardrail/future constraint, etc.). Generate `verification/INTERVIEW_MATERIALIZATION.yaml` or equivalent existing verification evidence to prove materialization/closure when the project complexity warrants it.

When source transcripts/files are ingested, preserve source identity/hash where permitted and reconcile extracted material through `provenance/SOURCE_INGEST_MANIFEST.yaml` or the project's existing provenance authority. Counts/IDs must close; imported context does not excuse pointer-only Ledger entries.

After each substantial interview round update the durable product model and START round digest. Reconstruction must sample early, middle and late decisions so late answers cannot crowd older material intent out of the package.

---


## Purpose

A project compiler fails if it produces a neat package while silently discarding most of the conversation that created the project.

For nontrivial projects the compiler must prove interview completeness and context preservation here, then pass the separate reconstruction-fidelity gate defined in `FRESH_AGENT_RECONSTRUCTION_GUIDE.md`:

```text
SPECIFICATION COMPLETENESS
= all material product/design decisions needed from the user have been explored

CONTEXT PRESERVATION
= every material statement, answered question, rationale, reference and unresolved issue has a durable destination
```

A concise `PROJECT_CORE.md`, `GOAL.md`, or `SYSTEM_MAP.yaml` does not satisfy context preservation by itself.

---

# 1. Interview Completeness Is a Hard Gate

Do not end the interview merely because remaining uncertainty looks technical or reversible.

For a nontrivial project:

1. extract all known information;
2. create a draft domain/system inventory;
3. evaluate the completeness fields for every material system/domain;
4. ask a complete coherent round covering the currently known user-owned gaps;
5. update the coverage state, Q/A ledger and affected canonical authorities from the answers;
6. update the rolling Decision Compendium/System Map when the product model changed;
7. repeat until no unresolved **user-owned** material decision remains;
8. perform an adversarial completeness sweep before generation.

Do not stop after one question round simply because the current answers are sufficient to start coding. Do not truncate a round to an arbitrary number of questions. If many questions are needed, split them into thematic rounds for readability and continue after each answer until coverage passes.

The goal is not infinite detail. The goal is that every user-owned decision which could materially alter the product is either:
- confirmed;
- intentionally delegated;
- researched because it is factual;
- explicitly deferred;
- or still marked unresolved and asked.

---

# 2. System/Domain Completeness Sweep

After the initial vision has been understood, do **not** derive coverage only from nouns/features the user happened to mention. First infer a provisional product archetype and Expected Capability/Responsibility Envelope from the user's desired outcomes, references and ordinary domain expectations. Then resolve that envelope into the relevant project responsibilities/domains and check each one.

The envelope is `COMPILER` inference used to find omissions, not `USER` authority. Every material expected responsibility must end with an explicit disposition such as `modeled`, `covered_by_existing_owner`, `not_applicable`, `intentionally_deferred`, `delegated_technical`, or `needs_user_decision`. A material ordinary responsibility may not disappear as `never_considered`. Do not ask the user technical questions merely because the compiler inferred a responsibility; ask only when its product semantics are genuinely user-owned.

Typical fields:

```text
purpose / outcome
user-visible behavior
states and rules
inputs / controls / triggers
outputs / feedback
cross-system dependencies
reusable capability / extension boundary when modular growth matters
content/data/configuration
variants / modifiers / explicit replacements / exceptions
navigation / lifecycle
failure / recovery behavior
visual / audio / interaction direction
future expansion constraints
acceptance / observable success
```

Only ask about fields that represent real user/product decisions.

Technical implementation details may remain delegated.

Illustrative envelopes vary by product. An interactive realtime product might imply input/control providers, runtime actors/instances, movement/state/action mapping, presentation, environment/surface, session/flow and authoring/content concerns. A commerce product might imply catalog, pricing, availability, cart/order/payment/fulfillment and authoring/admin concerns. These are prompts for coverage, never fixed system names.

The compiler must not deeply specify one explicitly named feature while ordinary adjacent responsibilities implied by the product remain unexamined. Only relevant domains are included; unrelated/common-but-unneeded domains must be marked not applicable rather than manufactured into systems.

---

# 3. `contracts/INTERVIEW_COVERAGE.yaml`

Generate for nontrivial compilations.

It is the machine-readable interview stop condition.

Example:

```yaml
schema_version: 1
project: PROJECT-ID

status_values:
  - confirmed
  - research_resolved
  - delegated_technical
  - intentionally_deferred
  - not_applicable
  - unresolved_user
  - contradiction

systems:
  SYS-WORKFLOW:
    fields:
      purpose: confirmed
      user_visible_behavior: confirmed
      states_rules: confirmed
      inputs_triggers: delegated_technical
      dependencies: confirmed
      capability_extension_boundary: confirmed
      variants_overrides: confirmed
      value_resolution_propagation: confirmed
      failure_recovery: not_applicable
      future_constraints: confirmed
      acceptance: confirmed
    question_ids: [Q-014, Q-021]

completion_gate:
  unresolved_user: 0
  contradictions: 0
  status: passed
```

Generation is blocked while a material field is `unresolved_user` or `contradiction`, unless the user explicitly requests a partial package. A partial package must preserve those items prominently as unresolved; never invent them.

---

# 4. `docs/INTERVIEW_LEDGER.md`

Preserve the actual interview, not only its normalized conclusions.

For every material question/answer pair store:

```text
Q-ID
question as asked
user answer verbatim
normalized interpretation / decision
classification (user decision / fact / delegated / deferred / contradiction)
affected System IDs / domains
canonical destination artifact IDs / sections
follow-up status
```

Example:

```markdown
## Q-021 — Behavior when the normal flow cannot continue

Question:
> [exact compiler question]

User answer:
> [exact user answer in original language]

Compiled meaning:
- The product should preserve the user's in-progress state and route to the defined recovery path rather than silently reset.

Affected authorities:
- SYS-WORKFLOW
- CONTRACT-APP-FLOW
- DOC-UX

Destination:
- docs/system_specs/WORKFLOW.md#Recovery behavior
```

Rules:
- preserve the user's original language and wording for answers;
- do not delete older Q/A merely because a later answer refines it; mark supersession/clarification;
- do not compress twenty answered questions into three summary bullets;
- if a question reveals a contradiction, keep both statements and record the resolution;
- all material answered questions must survive package generation.

---

# 5. `CONTEXT_HANDOFF.md`

Generate a rich onboarding artifact for a new agent/session.

This file exists because canonical project contracts deliberately normalize and distribute knowledge. A new agent also needs the **story of the project** so it understands why those contracts exist.

Include:
- what the user is trying to create and why;
- intended experience / product gestalt;
- important original wording / terminology;
- major references and exactly why they were cited;
- chronological or thematic development of the concept;
- important questions asked and what changed because of the answers;
- major decisions and rationale;
- rejected alternatives and why;
- master-system model and important composition decisions;
- known future requirements that constrain current architecture;
- unresolved questions / explicit deferrals;
- current package structure and where canonical details live;
- implementation-agent cautions where prior attempts failed or drifted.

`CONTEXT_HANDOFF.md` is a contextual bridge, not the authority for exact behavior when a dedicated contract/spec exists.

Use it:
- when handing the project to a different agent/model;
- after major context loss;
- when beginning implementation from a large compiled package.

Do not make it artificially short. Its purpose is to preserve context that would otherwise be lost.

---

# 6. Traceability Gate

Before package delivery, every material source item must be traceable.

Check at minimum:

```text
material user statements
+ material user answers
+ important exact quotes
+ references/mockups
+ researched facts used for decisions
+ compiler recommendations accepted/rejected
+ explicit assumptions/delegations
+ unresolved questions
```

Each must have at least one durable destination:
- `USER_VISION.md` for high-signal vision anchors;
- `INTERVIEW_LEDGER.md` for Q/A provenance;
- `DECISION_COMPENDIUM.md` for the readable normalized decision model/rationale;
- system/design/content/architecture authority for exact normalized truth;
- `INTERVIEW_COVERAGE.yaml` for completeness status;
- `CONTEXT_HANDOFF.md` for project-history/onboarding context.

No material information may exist only in chat after delivery.

---

# 6A. Domain-Expert Omission Challenge

Before generation/final system freeze, ask internally:

> Could a competent domain expert look at the current product model/System Map and immediately identify an important ordinary responsibility implied by the requested product that the compiler never considered?

If yes, the package is not ready. Add the responsibility to the coverage envelope and resolve it through the normal user/research/delegation/modeling path. If a proposed gap is not actually applicable, record that disposition instead of adding a fake system.

This gate detects **coverage omission**, not implementation incompleteness. It must happen before Representative Proof Sets: first decide what the product architecture needs to cover, then prove selected reusable seams.

---

# 7. Adversarial Final Interview Sweep

Before saying "the specification is complete", challenge it from the perspective of a new agent who never saw the conversation:

1. Which user-visible systems have never been discussed?
2. Which system boundaries were inferred without user confirmation even though they affect product behavior?
3. Which references are named but not translated into concrete adopted traits?
4. Which screens/states/controls/content types exist only by assumption?
5. Which future requirements could force today's architecture to be rebuilt?
6. Which edge cases materially change the intended experience?
7. Which user answers have not yet been compiled into a canonical destination?
8. Which examples could be misread as required content rather than illustrations?
9. Which important negative requirement/forbidden architecture is only implicit?
10. Could a new agent read the package and explain the user's vision, rationale, major decisions and rejected alternatives without the original chat?

If a material gap is found, ask the next complete thematic question round instead of generating.

---

# 8. User-requested Early Generation

If the user explicitly says to generate before the completeness gate passes:

- comply;
- mark the package `PARTIAL / OPEN DECISIONS`;
- include every unresolved user decision in `INTERVIEW_COVERAGE.yaml` and `CONTEXT_HANDOFF.md`;
- include all answered questions already collected;
- never silently fill the gaps.

A partial package must be resumable: the next compiler run continues from the ledger/coverage state instead of restarting the interview.

---

# 9. Update / Resume Protocol

When new answers arrive later:

1. append/update `INTERVIEW_LEDGER.md`;
2. update affected canonical authorities;
3. update `INTERVIEW_COVERAGE.yaml`;
4. update `DECISION_COMPENDIUM.md` and affected vision/reference/system/acceptance links;
5. update guardrails/adversarial examples when the answer closes a plausible wrong interpretation;
6. regenerate/update `CONTEXT_HANDOFF.md`;
7. for nontrivial projects mark `PROJECT_ATLAS.html` stale when any Atlas source changed, then regenerate it through its registered generator before delivery/handoff;
8. rerun reconstruction fidelity when the mental product model materially changed;
9. only then deliver the updated package.

Do not treat an existing package as justification to ignore new conversational context.

---

# 10. Full-Fidelity Output Package Rule

The generated project package has **no artificial size or file-count cap**. Keep runtime bootstrap material selective, but preserve all material project truth in durable JIT authorities.

For the generated project:
- there is no artificial maximum file count;
- there is no artificial maximum Q/A count;
- there is no target summary length;
- there is no requirement to merge unrelated systems to save files;
- there is no permission to omit context because it is lengthy.

Use separation for clarity, not compression. One coherent core system should normally have one detailed canonical system authority, with additional bounded contracts/Blueprints when needed.

A large project should therefore be allowed to produce, for example:

```text
docs/
  USER_VISION.md
  INTERVIEW_LEDGER.md
  PROJECT_PLAN.md
  systems/
    INPUT_COMMAND.md
    RUNTIME_STATE.md
    ACTION_POLICY.md
    WORKFLOW.md
    PRESENTATION.md
    NAVIGATION.md
    DATA_CONTENT.md
    CONTENT_AUTHORING.md
    ...

contracts/
  SYSTEM_MAP.yaml
  INTERVIEW_COVERAGE.yaml
  ...

blueprints/
  ...

CONTEXT_HANDOFF.md
```

The exact file set is derived from the project, not from a target count.

# 11. System Authority Depth Gate

Before final delivery, every identified **core system** must be sufficiently described for an implementation agent that never saw the interview. For each applicable system, cover:
- purpose and user-visible role;
- confirmed user intent and relevant Q/VQ provenance;
- states/rules/lifecycle;
- inputs/triggers and outputs/feedback;
- owned state/data;
- dependencies and consumers;
- configuration/content model;
- variants, modifiers, explicit replacements and exceptions;
- whether central/default changes should propagate through consumer deltas;
- extension points and future constraints;
- design/asset implications;
- relevant skill/capability needs;
- behavior Blueprint ownership/calls;
- implementation/data Blueprint expectations when material;
- acceptance criteria and required evidence;
- unresolved/deferred items.

A `SYSTEM_MAP.yaml` entry alone is not a substitute for a detailed system authority when the system is nontrivial.

# 12. Project Planning Artifact

Generate `docs/PROJECT_PLAN.md` for nontrivial projects. During compilation it may exist as a high-level draft (walking skeleton, dependencies, milestones), but do not freeze fine-grained task decomposition until the Fresh-Agent Reconstruction gate passes. The final plan is implementation-oriented and derived from the confirmed system topology, decision model and acceptance graph. Include:
- project phases/milestones;
- walking skeleton / first integrated route;
- dependency-aware system order;
- which systems can be developed/tested independently;
- composition/integration milestones;
- required skills/capabilities by phase;
- verification gates;
- deferred/future work that must not distort current scope.

The plan must reference stable System/Blueprint/Acceptance IDs rather than duplicate detailed behavior. If reconstruction reveals a misunderstood system boundary or rationale, update the authorities first and regenerate the affected plan instead of preserving stale task decomposition.

# 13. Final Independent-Handoff Precheck

Before the dedicated Fresh-Agent Reconstruction gate, perform a local precheck that the package alone can answer:
1. What is the user trying to build and what should it feel like?
2. What were the important questions and exact answers?
3. Which core systems exist and why?
4. What does each system own and how does it interact with the others?
5. Which compositions create concrete products/entities/screens?
6. What is planned first and why?
7. Which contracts/Blueprints govern implementation?
8. Which skills/capabilities are expected?
9. How is each important requirement verified?
10. What remains open/deferred and why?

If any answer requires the original chat, the package is incomplete. The formal independent/self-isolated reconstruction evidence and acceptance criterion are defined only in `FRESH_AGENT_RECONSTRUCTION_GUIDE.md`.


# v2.26 Whole-product lifecycle completeness sweep

Before interview coverage can pass for a nontrivial product, reconstruct the expected normal-user/product lifecycle from the user's vision plus the Product Capability Envelope.

Challenge whether the package has considered:
- entry/onboarding/home/shell where applicable;
- required setup/configuration/selection;
- primary experience/workflow;
- interruption/back/cancel/pause/recovery;
- completion/result/success/failure;
- persistence/save/resume/progression;
- replay/return/next-use path;
- settings/accessibility/options when material to the stated product;
- content authoring/admin/operator paths when they are part of the product.

These are discovery hypotheses, not a mandatory universal feature list. Resolve each material item as modeled, covered elsewhere, not applicable, intentionally deferred/out-of-scope, delegated technical, or requiring a user decision.

Interview completeness fails if an ordinary material lifecycle area implied by the requested product was never considered.
