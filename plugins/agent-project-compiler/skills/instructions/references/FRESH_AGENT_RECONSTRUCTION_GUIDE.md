# Fresh-Agent Reconstruction and Decision Model Guide

# Current Precedence — Reconstruction v2.22 Coverage + Proof

Fresh-Agent Reconstruction must test more than recitation. Without the original compiler chat, the fresh agent must reconstruct: whole-product intent; important decisions/rationale/rejections; responsibility-owner/capability/integration model; reference traits/exclusions; authoring/extension model; producer convergence; guardrails; roadmap + phase-admission logic; open/deferred items; one forward implementation trace and one reverse-debug trace.

Sample early/middle/late interview decisions. Require discovery of at least one deep non-bootstrap normative authority through `PROJECT_INDEX.yaml` rather than from a supplied pointer. For extensible projects include a future-change challenge that tests reuse/classification without requiring a fake production feature. Also require the fresh agent to distinguish **canonical walking-skeleton integration proof**, **heterogeneous representative reuse proof**, and **additional product breadth**, and to choose the smallest proof set by semantic variation rather than consumer count.

Add a planning challenge: given current maturity/evidence, the agent must identify the next **admissible** workstream and explain why a technically runnable downstream task may still be exploratory-only. Fixture evidence must not be promoted to representative product evidence.

---


## Purpose

A compiled package can be information-complete and still fail if a new implementation agent reconstructs the wrong mental product model.

The compiler must therefore prove a third property in addition to interview completeness and context preservation:

```text
RECONSTRUCTION FIDELITY
= a capable agent with no original chat can rebuild the same product model,
  understand why the architecture exists, distinguish rules from examples,
  and trace representative cases through the canonical systems before coding.
```

This is a package-quality acceptance criterion, not a writing-quality preference.

---

# 1. The middle layer: Decision Compendium

For nontrivial projects generate:

```text
docs/DECISION_COMPENDIUM.md
```

It sits between raw provenance and precise contracts:

```text
INTERVIEW_LEDGER / USER_VISION
        ↓
DECISION_COMPENDIUM
        ↓
SYSTEM / DESIGN / CONTENT AUTHORITIES
        ↓
SYSTEM_MAP / SYSTEM_INTEGRATION / BLUEPRINTS
        ↓
IMPLEMENTATION
```

Roles:

- `INTERVIEW_LEDGER.md` preserves exact questions and verbatim answers.
- `USER_VISION.md` preserves the holistic experience and high-signal wording.
- `DECISION_COMPENDIUM.md` is the human-readable normalized product model a fresh agent can understand quickly.
- exact behavior remains authoritative in the dedicated system/design/content/contracts.

The Compendium should summarize **decisions, rationale and relationships**, not duplicate all detailed system rules.

For each material decision record when useful:
- stable decision ID;
- concise decision statement;
- rationale / why it matters;
- source Q/VQ/reference IDs;
- affected System IDs / authorities;
- rejected alternatives or forbidden interpretations;
- whether the decision is USER, COMPILER, researched fact, delegated technical, or deferred;
- examples that illustrate the decision;
- canonical destination pointers.

Update it after every substantial interview round instead of reconstructing it only at the end.

---

# 2. Negative requirements and architecture guardrails

Positive requirements do not sufficiently constrain plausible-but-wrong implementations.

For projects with meaningful architectural/content reuse constraints generate when useful:

```text
contracts/ARCHITECTURE_GUARDRAILS.yaml
```

Examples:

```yaml
guardrails:
  GR-001:
    statement: "Consumers must not own independent validation/policy cores."
    reason: "All consumers compose the canonical validation/policy owners."
    source_ids: [DEC-017, VQ-008]
    applies_to: [SYS-VALIDATION, SYS-CONSUMER-CONTENT]
    forbidden_patterns:
      - per_consumer_validation_runtime
      - duplicated_policy_resolution

  GR-002:
    statement: "A special operating mode must not become a duplicate workflow runtime."
    reason: "Mode behavior is configured through canonical workflow/rules data."
    applies_to: [SYS-WORKFLOW, SYS-RULES]
```

Typical guardrails include:
- no duplicate core per content item;
- no second builder/runtime path;
- no hard-coded copy merely to change data values;
- no demo-only special logic when the normal product path should exercise the feature;
- no bypass of canonical ownership/integration contracts;
- no class/category split when the user expects one generic composition system.

Guardrails must derive from confirmed intent or necessary compiler architecture, not arbitrary style preferences.

---

# 3. Examples must have semantic type

A compiler must never allow an illustrative example to silently become required product content.

Every material example should be classifiable as one of:

```text
REQUIRED_EXAMPLE
= this concrete thing/content/behavior is actually required

ILLUSTRATIVE_EXAMPLE
= used only to explain a general rule or desired capability

ADVERSARIAL_EXAMPLE
= chosen specifically to challenge the abstraction/system design

REFERENCE_EXAMPLE
= external product/reference illustrating selected traits
```

Record the type in the ledger/decision model when ambiguity could matter.

Example:

```text
"ReusableAction with different daconsumer values"
```

may mean:

```text
ILLUSTRATIVE_EXAMPLE
→ proves base definition + data/override variation
```

not:

```text
REQUIRED_EXAMPLE
→ every product must ship this concrete example
```

If the user's wording is ambiguous and the distinction changes content scope, ask.

---

# 4. Adversarial abstraction examples

Before freezing system architecture, test it against deliberately different representative cases.

For substantial modular/data-driven systems generate when useful:

```text
verification/ABSTRACTION_TESTS.yaml
```

Illustrative cases for a configurable/provider-driven product:

```text
case A: standard/reference configuration
case B: materially different profile/provider
case C: adversarial async/failure/optional-capability case
```

The exact examples should match the project. They are not automatically shipping content.

Each abstraction test asks:
- Can the same canonical systems express all cases?
- Which differences are data/config/overrides?
- Which differences truly require a new reusable system/capability?
- Would supporting this case force a parallel implementation path?
- Does the test reveal a hidden category/class hierarchy that contradicts the intended composition model?

Example shape:

```yaml
tests:
  ABS-CONSUMER-DIVERSITY:
    type: architecture_expression
    systems: [SYS-INPUT-COMMAND, SYS-RUNTIME-STATE, SYS-ACTION, SYS-PRESENTATION]
    cases:
      - id: CASE-STANDARD
        role: illustrative
      - id: CASE-ALTERNATE
        role: illustrative
      - id: CASE-ADVERSARIAL
        role: adversarial
    pass_condition:
      - all_cases_use_same_canonical_owners
      - differences_are_data_profile_provider_or_declared_extension_except_explicit_new_capability
      - no_parallel_validation_action_or_state_runtime
```

Architecture should be challenged before implementation, not only repaired after a coding agent has already specialized it incorrectly.

---

# 4A. Representative proof-set reconstruction challenge

For projects that claim reusable composition, reconstruction should test whether a fresh agent understands **how much evidence is enough**.

Give it a set of current/planned cases and ask it to identify:
- which case is the canonical walking skeleton/reference path;
- which materially different cases are required to challenge distinct variation seams;
- which additional similar cases are merely product/content scale;
- which evidence would prove integration versus reuse/composition;
- whether any proposed second case would require speculative production work and can instead be an adversarial fixture/challenge.

PASS requires the agent to choose the smallest semantically sufficient proof set and explain why additional similar consumer count does not increase architecture proof.

---

# 5. Authoring/tooling is a first-class system when modularity depends on it

If the project claims content is data-driven, modular, configurable or easy to extend, ask how that content is actually authored.

When authoring materially proves the architecture, model it as a master system/domain rather than a later UI convenience.

Examples:
- entity/content builder;
- provider/content authoring;
- page/template editor;
- report designer;
- workflow configuration;
- plugin/provider registration;
- admin content tools.

The authoring system should exercise the same canonical runtime/data contracts used by hand-authored content. A builder that writes to a separate runtime path does not prove modularity.

Operational test:

```text
Can a representative new content item be created through the intended authoring/data path
without modifying the core runtime systems that are supposed to be reusable?
```

If not, the claimed extension boundary is not yet proven.

---

# 6. Reference traits, not reference names

Detailed reference compilation is owned by `VISION_AND_REFERENCE_PRESERVATION_GUIDE.md`.

Reconstruction adds one hard requirement: a fresh agent must not need to infer what "like X" means.

The Decision Compendium should expose the high-level mapping:

```text
Reference
→ adopted traits
→ adapted traits
→ rejected/out-of-scope traits
→ destination authorities
```

Do not let an external reference remain a vague architectural instruction.

---

# 7. Rolling reconstruction during the interview

Do not wait until final package generation to discover that the project model is unreadable.

After every major interview round:

1. update `INTERVIEW_LEDGER.md` / coverage state;
2. update the draft `USER_VISION` anchors when the whole-product intent changed;
3. update `DECISION_COMPENDIUM.md` with newly settled decisions/rationale;
4. update the provisional Product Capability Envelope and its dispositions when the product model changes;
5. update the draft `SYSTEM_MAP` when new responsibilities/owners emerge;
6. update guardrails/examples when an answer closes a plausible wrong interpretation;
7. mentally reconstruct the product from only these durable artifacts;
8. ask the next question round if a plausible wrong product model or material ordinary-responsibility gap remains.

This is a rolling compression check, not permission to discard the original Q/A.

---

# 8. Start Prompt is a continuously tested reconstruction artifact

The final `prompts/START_PROMPT.md` is not created from scratch at the end. Maintain it during compilation and test it as an **active-context reconstruction artifact**.

A Start Prompt may be deliberately detailed and denormalized. It is generated from canonical authorities, marked non-authoritative, and should inline enough vision, material Q/A, decision rationale, system/composition context, guardrails and acceptance intent that a fresh agent forms the correct product model **before** chasing file pointers.

After major interview/system milestones ask:

> If I forgot the original chat and received this prompt first, would I understand the same product and master outcome before opening implementation files?

Then test whether the referenced authorities resolve exact details without invention.

The canonical policy and prompt shapes live in `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md`.

---

# 9. Fresh-Agent Reconstruction Test

For nontrivial compiled packages generate:

```text
verification/FRESH_AGENT_RECONSTRUCTION.yaml
```

and include a required package-quality acceptance criterion such as:

```text
AC-PACKAGE-RECONSTRUCTION
```

The test agent receives the generated Start Prompt first, then the generated package and explicitly allowed runtime metadata; it receives no original chat, compiler reasoning/history, provider memory, or implementation-agent conclusions. When `AGENT_RUNTIME_PROFILE.yaml` provides isolated subagents/fresh sessions, use that binding.

It must reconstruct, at minimum:

1. product vision and intended experience;
2. major actors/capabilities/workflows;
3. canonical master systems and why they exist;
4. important ownership/integration relationships;
5. major decisions and rationale;
6. important rejected alternatives / negative requirements;
7. what named examples actually mean (required vs illustrative/adversarial);
8. what each major external reference contributes and does not contribute;
9. how one representative concrete example flows through the systems;
10. how content is authored/extended when modularity/data-driven behavior is claimed;
11. which decisions remain open/deferred;
12. which authorities must be read for exact behavior;
13. how to discover a deep system/feature authority through `PROJECT_INDEX.yaml` without guessing filenames or relying on prose chains.
14. which ordinary responsibilities were expected from the inferred product archetype and how each was modeled, covered elsewhere, deferred, rejected/not-applicable, delegated or left for a user decision.

As a discoverability challenge, give the fresh agent at least one domain/task whose authority is not part of the bootstrap set (for example Guard, an importer, a settings subsystem, or a verification contract). PASS requires the agent to use `PROJECT_INDEX.yaml`/registries and reach the canonical authority. The reconstruction must be compared against expected concepts from canonical sources, not wording similarity.

---

### Domain-expert coverage challenge

Ask the fresh agent to inspect the vision + compiled architecture and name any **ordinary material responsibility implied by this particular product** that appears to have no modeled owner/capability and no explicit disposition. Compare plausible findings against the compiler's coverage envelope and canonical intent.

- If a material responsibility was genuinely never considered, reconstruction/coverage FAILS and compilation reopens.
- If the responsibility is intentionally covered by another owner, deferred/out-of-scope or not applicable, the package must make that disposition discoverable.
- Do not treat speculative architecture or optional industry features as automatic gaps.

This challenge tests whether the compiler modeled the product space sufficiently; the Representative Proof Set separately tests whether selected reusable seams work.

---

### Atlas orientation challenge

For nontrivial projects, give the fresh agent the normal START/bootstrap package and require it to:
1. validate/regenerate the Atlas if stale;
2. inspect the Atlas and summarize the whole-product/system/flow picture;
3. state that the Atlas is non-authoritative;
4. use `PROJECT_INDEX.yaml` to find one exact deep authority needed to answer a precision question.

PASS requires both orientation **and** exact-source navigation. Skipping the Atlas or treating it as project truth fails the Atlas portion; reading only the Atlas never satisfies the deep-authority requirement.

# 10. Independent vs fallback reconstruction evidence

Preferred evidence is an isolated fresh agent/subagent/separate model instance selected through `AGENT_RUNTIME_PROFILE.yaml` when the harness exposes one at reasonable cost.

The fresh agent should not receive the compiler's own summary/conclusions beyond the generated project package.

Fallback when no independent agent capability exists:
- isolated re-read from the package only;
- explicit checklist against the reconstruction contract;
- mark evidence as self_reconstruction rather than independent_reconstruction.

A self-check is weaker but still better than no reconstruction gate. Do not claim independent evidence when it was not independent.

---

# 11. Reconstruction result contract

Example:

```yaml
schema_version: 1
criterion: AC-PACKAGE-RECONSTRUCTION
mode: independent_agent
status: passed

required_concepts:
  start_prompt_orientation: passed
  product_vision: passed
  system_model: passed
  decision_rationale: passed
  guardrails: passed
  example_semantics: passed
  reference_traits: passed
  representative_runtime_flow: passed
  authoring_extension_model: passed
  open_decisions: passed
  authority_routing: passed
  deep_authority_discovery: passed
  authority_reachability_report: passed

material_misconceptions: []
missing_context: []
```

Fail the gate when the fresh agent:
- invents a plausible but forbidden architecture;
- confuses an illustration with required content;
- cannot explain why a core system exists;
- cannot identify canonical ownership;
- cannot trace a representative case;
- cannot distinguish approved traits from generic "like X" imitation;
- cannot discover a required deep authority through the canonical router;
- needs the original chat to answer a material question.

Fix the package/authorities, not the fresh agent's prompt, unless the prompt itself is the missing artifact.

---

# 12. Task decomposition happens after reconstruction fidelity

Preferred compiler order for complex projects:

```text
Idea
→ Vision interview
→ Verbatim ledger
→ Reference trait analysis
→ Draft System Map
→ Adversarial examples
→ System/integration interview
→ Decision Compendium
→ Authoring/content model
→ Architecture guardrails
→ Acceptance & verification
→ Fresh-Agent Reconstruction Test
→ Task decomposition / final implementation plan
→ final Start Prompt
```

Task decomposition before reconstruction fidelity risks optimizing implementation around a misunderstood product.

---

# 13. Completion rule

A nontrivial compiled package is `COMPLETE` only when all three are true:

```text
INTERVIEW COMPLETENESS
+ CONTEXT PRESERVATION
+ RECONSTRUCTION FIDELITY
= PACKAGE COMPLETE
```

Information-complete but unreconstructable is not complete.


## Future-change reconstruction

For modular/extensible projects, reconstruction is incomplete unless a fresh agent can also preserve the architecture when given a **new user delta after the original package was compiled**. Use `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` for the canonical test. At minimum, ask one scenario that forces the agent to choose between a quick consumer-local patch and a reusable lower-level capability. PASS requires core-first classification before implementation.

Core question:

> If a capable agent received only this package, what important behavior, relationship, rationale or prohibition could it still reasonably misunderstand?

Any material answer means the package needs clarification, an authority/guardrail/example, or another user question before finalization.

# v2.20 empirical reconstruction challenges

For substantial generated packages, add representative challenges for these failure classes when applicable:

1. **Validator challenge** — introduce/use a temporary malformed structured authority or broken reference; the project gate must reject it. A path-only validator fails reconstruction quality.
2. **Plugin-absence/compaction challenge** — assume the preferred Core-First Governance capability is unavailable or context was compacted; the agent must reload project truth, run the project-native gate and continue without inventing that the plugin ran.
3. **Shared-definition challenge** — add/edit one reusable definition consumed by two surfaces/runtimes; the agent must route through one canonical validated/versioned store/read path, not create consumer-local copies.
4. **Visual-reference challenge** — give a surface task with a registered image reference; the agent must discover and actually inspect the image, preserve its scope, use shared design primitives/layout contracts, and compare the whole rendered result rather than default to generic styling.
5. **Container/primitive challenge** — a parent needs a differently sized child control; the agent should use a declared variant/slot constraint rather than page-local internal restyling of the primitive.

A package that can recite these concepts but whose own tool/router cannot exercise them is not sufficiently reconstructable.


## v2.23 exact transition-gate challenge
When the project contains a human/project approval boundary, reconstruction must test both failure directions. Give the fresh agent a broad implementation request while approval for the later transition is absent. PASS requires it to continue authorized reversible preparation, stop at the exact gated transition, identify the approval authority/evidence, and avoid downstream work that depends on the transition. FAIL if it auto-crosses the gate **or** refuses all authorized preparation merely because a later gate exists.


# v2.24 Product-realization continuity challenge

For implementation projects, reconstruction must prove that a fresh agent distinguishes:

```text
first foundation / walking skeleton
from
complete product outcome
```

The agent should be able to state the remaining product-realization stages/outcomes after the first skeleton and identify the next admissible stage from Plan + State + Acceptance rather than stopping at the first runnable milestone.

For design-heavy products, the agent must also reconstruct the visual/user-surface target, identify the governing reference/baseline IDs, and explain why a generic/default UI would not satisfy product completion when a specific visual identity is authoritative.


# v2.25 Completion-claim challenge

A fresh-agent reconstruction/review should be able to reject these false-completion patterns:

- package/project-gate or M0/foundation succeeds while later required product outcomes remain unverified;
- an implementation artifact exists but required runtime/browser evidence was never exercised;
- many tests/code changes exist but do not map to all requested Acceptance criteria;
- a derived status/report claims more than canonical STATE + Acceptance/Evidence support.

PASS requires explaining that the final claim is reconstructed from canonical current state + actual evidence at the current revision.


# v2.26 A-to-Z product reconstruction challenge

A fresh agent must be able to reconstruct the complete required normal-user/product lifecycle, not only the core mechanic/runtime architecture.

Ask the agent to enumerate:
1. entry/start state;
2. setup/configuration states;
3. primary experience;
4. interruption/recovery;
5. completion/result;
6. persistence/progression/resume where applicable;
7. replay/return/next-use;
8. which plan milestone and Acceptance IDs own each required node.

Use the project's actual domain model; the numbered categories are a challenge scaffold, not mandatory features.

FAIL if the agent treats the first runnable skeleton/core experience as the product boundary while required downstream flow nodes exist.


# v2.27 Verification-truth reconstruction

A fresh implementation/review agent must reconstruct not only the intended product/architecture but also:
- which `PR-*` outcomes define required product completion;
- which are actually Verified vs merely implemented/Connected/Exercised;
- which evidence supports each verified claim and at what boundary/scope;
- current derived admission and why;
- what remains unverified;
- the distinction among Product Complete, Release Ready and package/handoff governance integrity.

Challenge the agent with a contradictory STATE or a large green test suite while one required PR outcome lacks sufficient evidence. PASS requires rejecting false completion and tracing the contradiction back to Plan/Product Realization/Acceptance/Evidence.


# v2.29 Representative-path / generated-output reconstruction

When applicable, a fresh agent must be able to identify:
- the representative product path(s) used as regression heartbeats and what claims they do/not prove;
- any deterministic review projections and their canonical source/owner;
- generated artifacts and the source/recipe/generator that must be changed for durable edits;
- material finish/fidelity Product Realization outcomes still open or verified.

FAIL if the agent treats a generated/review artifact as the canonical edit owner or interprets one heartbeat as proof of unrelated product scope.


# v2.30 Product-engine reconstruction challenge

A fresh agent should be able to answer for each materially repeatable product type:

- What is the canonical reusable Definition Type/Blueprint contract?
- Which System/Capability owns its reusable behavior?
- What belongs in a Definition/Profile versus runtime instance state?
- Which generic runtime/surface consumer realizes the definition?
- How is a new same-type variant added?
- How are modifiers/upgrades/policies composed without copying the owner?
- Which placeholder slots can be replaced by production content without architectural replacement?

Adversarial challenge:

> Add a materially different second variant and one modifier.

PASS when the agent routes both through existing definition/composition seams or identifies a genuine missing reusable Capability before extending the core.

FAIL when the agent proposes another per-instance controller/page/runtime/state owner merely because the content differs.


# v2.31 Composition-coherence reconstruction challenge

Give the fresh agent a defect whose visible symptom appears in one consumer but whose cause is a shared cross-system relation.

PASS when the agent reconstructs:

```text
symptom
→ applicable Acceptance / Composition Invariant
→ canonical source/owner
→ all affected consumers/projections
→ repair owner/derivation
→ required re-verification
```

FAIL when it immediately patches the visible consumer while leaving the declared invariant broken.

Also ask whether the first runnable skeleton is merely exploratory, production-candidate or actually production-admitted, and require the agent to cite the survivability Acceptance/evidence rather than infer the answer from build success.
