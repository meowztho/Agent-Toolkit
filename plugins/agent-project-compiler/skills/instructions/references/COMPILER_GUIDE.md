# Compiler, Interview, and Research Guide

# Current Precedence — v2.29 Review-Driven Product Realization + Product/Realization/Verification Truth

This section supersedes conflicting earlier examples/wording in this file.

APC is a **one-shot project compiler**. After package handoff, assume the implementation agent may never receive the compiler conversation again. No material product truth, rationale, reference interpretation, architecture law, discovery rule, future constraint, build-order/admission rule or verification requirement may remain only in chat.

Active compiler reasoning is domain-neutral. Discover Responsibilities from the current project's outcomes/state/workflows/boundaries; do not infer a system taxonomy from examples or from the domain that originally inspired APC.


## Product-archetype inference is a coverage tool, not user authority
Before freezing `SYSTEM_MAP` for a nontrivial/unclear product, use the compiler's broader domain knowledge to infer a **provisional product archetype and Expected Capability/Responsibility Envelope**. This is a completeness hypothesis: ordinary responsibilities implied by the requested product should be considered even when a nontechnical user did not name them.

Do not turn the envelope into a universal taxonomy or silently promote it to `USER` intent. Each material envelope item must be resolved through existing authorities as one of: modeled under a canonical Responsibility Owner, covered by another owner/capability, not applicable, intentionally deferred/out-of-scope, delegated technical detail, or a genuine user decision that must be asked. `Never considered` is not an acceptable final disposition for a material ordinary responsibility.

Reference phrases such as "like X" may help infer an archetype/capability envelope, but only explicitly adopted/adapted traits become product requirements. The compiler should contribute domain completeness; it must not clone the reference product by assumption.

## Core-First build order and phase admission
For every nontrivial project, the compiler owns a reasoned `COMPILER` recommendation for execution order. Do not leave sequencing to the implementation agent.

Derive order from:
`confirmed outcomes → durable responsibilities/owners → capabilities/contracts → dependency/reuse fan-out → minimum coherent core → earliest meaningful walking skeleton → dependent consumers/providers/content → remaining outcomes → hardening/release`.

Prefer earlier work when it establishes canonical state/rule ownership, producer convergence, high fan-out reuse, high-risk architecture seams, independent testability, dependency necessity or an early real end-to-end proof. Core-First does **not** mean finishing every backend/core subsystem before touching a real surface; build only enough shared core for an honest walking skeleton, then grow outward through the established owners/contracts.

Where workstreams materially depend on upstream outputs, make admission explicit through existing project authorities. Determine:
1. upstream output/System/Capability/Contract/Acceptance IDs;
2. required upstream maturity, reusing existing `Specified → Declared → Connected → Exercised → Verified`/Acceptance semantics where applicable;
3. entry evidence proving that maturity on the required path/content/data/surface;
4. current-stage completion/exit condition;
5. allowed synthetic/unit/integration/spike work before admission;
6. product conclusions forbidden before admission;
7. replan triggers/assumptions.

Core semantic rules:
`TECHNICALLY EXECUTABLE != ADMITTED FOR PRODUCT CONCLUSIONS`
`NEXT ATTRACTIVE TASK != NEXT ADMISSIBLE TASK`

Selection is `all unmet/reopened work → admission/dependency filter → admissible work set → priority/risk/value within that set`.

Synthetic/fixture evidence retains its actual scope. It may prove that an engine/algorithm/contract/simulator technically executes, but must not silently prove that representative product inputs traverse the canonical path or authorize downstream balance/performance/usability/release conclusions.

For each material plan stage record outcome, owner/capability IDs, prerequisites, required maturity/evidence, admission, why-now, implementation/integration objective, allowed pre-admission exploration, forbidden premature conclusions, completion/exit, unlocks, reuse obligations, deferred work and replan triggers. A numbered prose feature list is insufficient when dependencies are material.

After every material stage/local fix reconcile original requested outcomes, actual evidence/maturity, still-open gaps and the next coherent **admissible** stage. Passing-test volume or ease of measurement never replaces the master outcome.

### Test load-bearing premises before dependent conclusions
When a material plan, architecture choice or product claim depends on an unverified factual premise, identify the premise and the decision or stage it supports. Before relying on it, define the cheapest meaningful feasible observation that could disconfirm it, the decision threshold, and what evidence would count. Keep the dependent conclusion conditional until qualifying evidence is recorded; if no meaningful test is feasible, preserve the unknown and its effect explicitly. If the premise fails, revisit only the affected decision, admission or acceptance path. Independent admissible work continues.

Use existing authorities: put the premise and rationale with the relevant decision, its validation point and replan trigger in `PROJECT_PLAN`, and any outcome-bearing criterion and result in Acceptance/Evidence. A pilot or proof of concept needs this treatment when its result will justify a larger commitment: state the hypothesis, relevant baseline, representative inputs, pass/fail threshold and graduation boundary before the trial. Do not require a pilot, a new assumption register or a universal stop gate for every project. The ordinary low-risk `ASSUMPTION` classification below remains available; a user-owned product choice remains a user decision rather than a fact to be inferred from a test.


### Exact approval/admission transition boundaries
When confirmed project intent defines a human/project approval gate (for example before publish, deploy, send, charge, merge, delete, promote or another consequential transition), compile the **exact state-transition boundary** rather than treating the whole surrounding phase as blocked.

Distinguish through existing authorities:
1. authorized **reversible preparation** that may proceed before approval;
2. the exact **gated transition/state change/side effect** that may not occur yet;
3. the approval authority/source and the explicit evidence that counts as approval;
4. downstream work that requires the transition to have occurred;
5. independent/admissible work that can continue while the gate is waiting;
6. scope/revision/expiry rules only when materially required.

Core rules:
`APPROVAL GATE BLOCKS THE GATED TRANSITION, NOT AUTHORIZED REVERSIBLE PREPARATION`
`BROAD IMPLEMENTATION INTENT != APPROVAL TO CROSS AN EXPLICIT GATE`

Do not infer approval from successful preparation, tests, an agent/provider `done`, a general request to implement the feature, or technical admission evidence. Conversely, do not freeze all useful work merely because a later approval gate exists. If a supposedly preparatory step itself performs an irreversible/consequential transition, it belongs behind the gate.

Materialize the rule through the existing workflow/system/state authority, `PROJECT_PLAN`, Acceptance/evidence and runtime `STATE`/project-gate view as appropriate. Do not create a universal approval engine or new mandatory artifact.

### Representative architecture proof before scale
When the product materially depends on reusable systems/capabilities, the compiler should plan a bounded architecture-proof milestone before broad production-content expansion. Use the smallest **Representative Proof Set** that covers materially different variation seams: a canonical walking skeleton/reference case for integration plus the minimum heterogeneous consumers/providers/fixtures needed to prove composition and reuse. Once that set proves the same canonical owners/capabilities without consumer-local rule duplication, additional similar consumers are product/content breadth rather than further architecture acceptance. Do not create speculative production content merely to increase proof count. Route exact proof semantics through `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` and existing Acceptance/`ABSTRACTION_TESTS` authorities.

---


# Compiler Reference

## Two separate jobs

The compiler must solve two different problems:

1. Help the human express the real project.
2. Package that project so a capable implementation agent can retrieve the right knowledge at the right time.

Do not solve (2) by shrinking away information collected during (1).

## Classify incoming information

### PRODUCT_INTENT
What the result should accomplish or feel like. User-authoritative.

### CONTENT_DECISION
Mechanics, workflows, story, UI behavior, business rules, feature behavior, design choices. User-authoritative unless explicitly delegated.

### REFERENCE
An external product/source used to communicate selected traits. It must be interpreted, researched if needed, and compiled into explicit adopted/adapted/rejected traits.

### EXAMPLE
A concrete example used to explain or challenge a general rule. Mark it as required content, illustrative, adversarial, or reference-derived when the distinction matters. Never silently promote an illustration into required scope.

### NEGATIVE_REQUIREMENT
A material statement about what the product/architecture must not become. Preserve it as a guardrail when it blocks a plausible but wrong implementation.

### FACT
Externally verifiable information. Research when material.

### TECHNICAL_DECISION
Implementation detail that preserves intent. Normally delegated to the implementation agent.

### RECOMMENDATION
Compiler-proposed solution. Never silently convert into a confirmed requirement.

### ASSUMPTION
Temporary low-risk interpretation. Record only when material.

## Decision authority levels

Keep three authority levels distinct:

- **USER** — subjective product/content/design/scope/identity choices and tradeoffs only the user can settle.
- **COMPILER** — cross-system decomposition, semantic capability depth/core-first change policy, reusable defaults/profile/modifier policy, reference-derived normalization, and technical structure needed to preserve coherence without changing user intent.
- **IMPLEMENTATION_AGENT** — local reversible implementation choices inside the compiled system/contracts.

Do not push COMPILER decisions downstream merely to avoid planning. Do not silently promote a COMPILER recommendation into USER intent. If a system-boundary choice changes user-visible behavior, authoring workflow, scope, cost, or future extension expectations, treat that consequence as a USER decision.

## Solution vs goal

Users often provide a guessed implementation as shorthand for an outcome.

Determine whether a proposed technology/structure is:
- a hard requirement;
- a preference;
- an example;
- or merely a suggested solution.

Preserve the underlying intent. Ask only if the distinction materially changes the project.

## Lossless compilation

The final package should not be a summary of the conversation. It should be a normalized project specification.

Every material input should land in exactly one best authoritative location, with cross-references/index routing rather than repeated copies.

For nontrivial projects, preserve the complete material interview in `docs/INTERVIEW_LEDGER.md` and generate `CONTEXT_HANDOFF.md` for project history/rationale. Maintain `docs/DECISION_COMPENDIUM.md` as the readable normalized product model between raw Q/A and exact contracts. Detailed reconstruction/guardrail/example policy lives in `FRESH_AGENT_RECONSTRUCTION_GUIDE.md`.

Examples:
- "I want the menus to feel like X" → DESIGN.md, not merely PROJECT_CORE.
- "New content/items must be easy to add" → architecture/content blueprint plus acceptance criteria if critical.
- "Use these sprite references" → REFERENCE_MAP and ASSET_BLUEPRINT.
- "Online comes later" → scope/deferred architecture constraint, not silently omitted.


## Integration relationships are part of specification

For complex/stateful projects, features and master-system names are insufficient when important behavior crosses boundaries. Capture enough semantic structure that a later agent does not independently invent conflicting paths: authoritative rule/state ownership, producer -> contract/data -> consumer relationships, important side effects/failure paths, and operational meaning of configurable/data-driven claims. When consumers vary a shared base, capture whether variation is relative (must inherit future base changes) or an explicit replacement; do not leave `override` semantics implicit.

Do not prematurely prescribe classes/patterns. The compiler defines the relationship/authority; reversible implementation remains delegated. Use `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md` when applicable.

## Artifact language

The interview may use any language. Generated project files are English.

Preserve canonical names/identifiers exactly when intentional.

---


## Generated package size and fidelity

The generated project package has no artificial maximum number of files, systems, blueprints, contracts, questions, answers or words. Runtime context should stay selective/JIT, but persistent project knowledge must remain lossless.

Do not optimize the generated package for smallness. Optimize for:
- full recoverability without the original chat;
- coherent single-authority ownership;
- system-level separation;
- JIT retrievability;
- explicit traceability.

Keep always-loaded runtime artifacts concise, but allow detailed authorities, per-system specifications, interview provenance, context handoff, plans, contracts and Blueprints to be as extensive as the project requires. If a project has 18 meaningful systems, create 18 properly scoped system authorities rather than compressing them into a few shallow summaries.

# Interview and Research Protocol

## Interview principle

The user should not need to know how to write a specification. Good questions are an interface for programming the future agent.

## Loop

### 1. Extract before asking
Identify what is already known:
- outcome;
- user/audience;
- desired experience;
- features/behavior;
- visual/design intent;
- assets/content;
- references;
- constraints;
- future/deferred needs;
- success criteria;
- contradictions.

Never ask the user to repeat existing information.

### 2. Research vs preference
Ask: can reliable research answer this without choosing for the user?

Research:
- framework/API/platform capabilities;
- current technical constraints;
- behavior/layout of a referenced product/application;
- standards/formats/licenses;
- source availability.

Ask the user:
- what they want;
- which tradeoff they prefer;
- content/story/business behavior;
- visual/art direction when references do not settle it;
- asset cost/source preferences when material;
- irreversible or scope-defining choices.

### 3. Ask high-value questions
Prefer concrete alternatives and consequences.

Example:
Instead of "How should the menu work?"
ask:
"Should the first screen optimize for fastest play (Play highlighted, minimal navigation) or expose modes/content first? Your references suggest the first approach; I can adopt it unless you prefer otherwise."

### 4. Question-round boundary
Ask coherent thematic rounds rather than arbitrary numeric batches. `INTERVIEW_COMPLETENESS_AND_HANDOFF_GUIDE.md` owns repeated rounds, coverage and stop conditions. After substantial rounds update the durable decision model and reconstruction artifacts as routed by `FRESH_AGENT_RECONSTRUCTION_GUIDE.md`.

### 5. Research referenced examples
When the user says "like X", research only the relevant aspects and convert them into proposed project traits. Ask which traits to keep when that is not already obvious.

## Source preference
For technical facts:
1. official docs/specs;
2. primary repositories;
3. vendor docs;
4. reputable secondary sources if needed.

Do not copy research transcripts into project docs. Compile durable conclusions only.

---

# Later user requests are architecture deltas

For an existing compiled project, a later user request does not restart architecture from the visible feature. Treat it as a delta against the current master systems/capability hierarchy. `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md` owns classification/decomposition depth. Update canonical architecture when the user intentionally changes product semantics; otherwise preserve it and implement through its existing extension points.


# Skill Discovery Boundary

The compiler identifies when a project needs specialist capabilities, but `SKILL_NATIVE_COMPILER_GUIDE.md` is the canonical authority for skill discovery, external review, installation scope, routing, version drift, rejection records, and project-local skill generation.

At this layer only preserve the rule: derive capability needs from confirmed systems/surfaces/assets/verification, and do not make technically equivalent skill selection a user decision unless trust, permissions, licensing, credentials, cost, or durable behavior materially differs.

---

# Compiler-Package Coherence Audit

When auditing or releasing the **compiler package itself**, do not apply generated-project rules blindly. Verify the plugin distribution as a dependency graph:

1. **Authority map** — each detailed compiler concern has one canonical reference owner; kernels/templates may restate only the minimum invariant or file shape.
2. **No active legacy parallel** — remove or clearly archive superseded guides; do not ship an old un-routed policy file beside the current owner.
3. **Router completeness** — `REFERENCE_INDEX.md` routes every active reference and no runtime reference is an unexplained orphan.
4. **Template parity** — every artifact the compiler requires has a usable template/example or an explicit rule that free-form generation is intended; guides and templates use the same path/field terminology.
6. **Support isolation** — README, handoffs, audit reports and historical notes are support artifacts unless explicitly needed as runtime reference material.
7. **Path/version hygiene** — no stale filenames, superseded version headings, dead references or contradictory install paths remain active.
8. **Context separation** — active model context is a selective working set; never reduce persistent project fidelity merely to keep more material always loaded.
9. **Structural validation** — check Markdown/code-fence integrity, duplicate headings where unintended, internal file references, and manifest/file-count/hash consistency.
10. **Fresh-agent test** — a fresh compiler instance receiving only the installable plugin can discover the right authority without relying on release history or prior chat.

If a duplication is intentional (for example a short invariant in Instructions plus a detailed guide), label the detailed owner clearly and keep the duplicate shorter than the authority. Prefer deleting stale parallel policy over adding precedence rules for it.

# Empirical correction — executable project gates, canonical definition paths, and design admission

A real compiled project exposed three compiler failures that prose alone did not prevent:

1. a generated validator checked only whether registered paths existed and therefore reported PASS while YAML structure and semantic references were broken;
2. shared content/data was present in several surfaces but the canonical authoring/store/snapshot path was not strong enough to prevent local draft/runtime divergence;
3. a Design System, shared primitives and visual references were declared, yet implementation still proliferated page-local styling and drifted toward a generic default design.

Treat these as **compiler correctness** failures.

## Executable project gate is part of the package contract

For a nontrivial project that contains structured project authorities, generate one small **project-native executable gate** using an actually available lightweight scripting/runtime environment. Prefer the project's existing scripting runtime; Python is acceptable when it is demonstrably available. Do not emit pseudocode or a path-only checker and call it validation.

The gate is a tool, not a second Project Authority or Governance owner. Its job is to deterministically enforce facts already encoded in existing authorities.

Minimum responsibilities where applicable:
- parse every normative YAML/JSON/TOML/other structured authority with a real parser;
- validate project-specific required top-level shapes/types, not only file existence;
- resolve registry, System/Capability/Integration/Blueprint/Acceptance IDs and reject unknown/duplicate/conflicting IDs;
- verify `PROJECT_INDEX` reachability and routed reference assets;
- verify current admission/prerequisite evidence encoded in existing Plan/Acceptance/State authorities;
- detect stale generated views/state/handoff evidence from registered source fingerprints or revision metadata where the project records them;
- print a concise Core-First preflight: master outcome/current admitted stage, required authority/reference IDs, and forbidden premature conclusions;
- return non-zero on invalid project truth; never silently auto-fix it.

### Validator must prove that it can fail

A validator is not trusted merely because it prints PASS on the generated package.

Before package delivery, run its **negative-control/self-test** on temporary/in-memory mutants that must fail. At minimum challenge the failure classes the package claims to validate, such as:
- syntactically invalid structured authority;
- missing/unknown referenced ID or registered path;
- unreachable/orphaned normative authority;
- Blueprint registry/file metadata mismatch;
- stale Atlas/state fingerprint when freshness is claimed;
- unmet current phase-admission evidence.

The self-test must prove that the validator returns failure for known-bad cases and PASS for the restored valid package. Store this result in the existing contract/package validation evidence; do not invent a second acceptance engine.

## Canonical shared-definition/data path

When the same domain definition/content is used by multiple consumers or an authoring/builder workflow exists, the compiler must establish a single canonical semantic path **before** broad consumer implementation:

```text
Draft / manual / builder / import / agent producer
→ canonical Definition schema
→ validation
→ versioned publish/store/repository boundary
→ canonical read/query path
→ consumers
→ runtime instance/snapshot/scoped mutable state
```

A Builder is normally a producer/editor of drafts through this path, **not** the hidden canonical database merely because it has UI state. `localStorage`, editor memory, test fixtures or exported files are draft/cache mechanisms unless the project explicitly chooses them as the canonical store.

Required proof when material:
- two materially different consumers resolve the same published definition through the same read contract;
- one source change propagates to consumers without local copies;
- invalid/unpublished drafts cannot silently enter the representative runtime;
- running/persisted instances that require stability pin/version/snapshot definitions instead of observing later mutable authoring changes;
- runtime modifiers/state do not overwrite the canonical Definition.

Detailed runtime ownership belongs in `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md`; this section owns the compiler decision to materialize and gate the path.

## Design is admitted like any other reusable core

If visual/layout identity is material and multiple surfaces share navigation, components or shell structure, the compiler must not merely name a Design System. It must plan and admit a **Presentation/Design Core** before broad surface proliferation:
- preserve/register every material supplied visual reference;
- establish tokens/primitives/layout/slot contracts;
- exercise representative primitives/layout in at least two real consumers;
- compare a real rendered whole surface to the applicable supplied/approved visual baseline;
- only then admit broad page/screen expansion that depends on that design core.

Detailed reference/mockup policy lives in `VISION_AND_REFERENCE_PRESERVATION_GUIDE.md`; component/layout composition lives in `SYSTEM_COMPOSITION_AND_ATLAS_GUIDE.md`; user-surface evidence lives in `USER_SURFACE_VERIFICATION_GUIDE.md`.


# v2.24 — Real-agent eval calibration and product-realization continuity

A weak or interrupted implementation-agent run is evidence about the compiled package only after the compiler distinguishes the failure class.

Before adding new governance/policy for an observed failure, ask:

```text
Did the compiled project already express the required invariant?
```

Classify the observation as one of:

- `SEMANTIC_GAP` — the project package did not define enough truth/guidance;
- `ADHERENCE_OR_EXECUTION_DRIFT` — the invariant already existed but the agent violated/lost it;
- `INCOMPLETE_RUN_ARTIFACT` — the session ended before normal convergence/hygiene could occur;
- `VALIDATION_GAP` — the invariant existed but the executable project gate could not detect a material violation it reasonably should detect.

Do not add another portable rule merely because a weaker model ignored an existing one. Prefer small project-specific executable checks for `VALIDATION_GAP`.

## Product realization must remain visible after foundation

A recurring agent failure is:

```text
foundation / scaffold / walking skeleton works
→ agent interprets this as the practical end of the assignment
```

For a product implementation project, the walking skeleton is an **early proof of architecture and product path**, not the master outcome.

The compiler must therefore materialize and repeatedly expose:

```text
MASTER PRODUCT OUTCOME
→ full realization roadmap
→ current admitted stage
→ current stage completion condition
→ remaining required product outcomes/stages
→ final whole-product acceptance
```

`PROJECT_PLAN` owns the recommended order/admission rules. `STATE` owns only the current execution/admission pointer. Acceptance/Evidence owns verification truth. START/GOAL/CONTINUE/Handoff/Atlas are derived views and may not become independent progress truth.

A milestone transition is invalid when its prerequisites/evidence/build gate are unmet even if implementation files exist.

## Surface fidelity is cross-cutting product realization, not late polish

When visual identity/layout/interaction experience is material, do not schedule "design" only as a late cosmetic phase.

The compiler should establish a **surface-fidelity spine** through the implementation roadmap:

1. preserve and route the visual/user-surface authorities;
2. expose a compact visual-target/reference capsule in START/GOAL;
3. establish the minimum shared Presentation/Design Core needed for a representative product surface;
4. render one meaningful normal-user surface/path early;
5. compare the whole rendered surface against the applicable user/approved/delegated baseline;
6. keep surface authorities attached to later surface milestones;
7. scale out only after the representative surface proves both architecture and product-specific visual direction.

A debug/default/generic surface may prove connectivity but does **not** satisfy product-specific visual realization when the project has a material visual identity.

If the user's references are coherent but implementation repeatedly falls back to generic model defaults, create/use a concrete derived baseline/mockup before broad surface work rather than adding more inspirational prose.

## Runtime convergence gate

The generated project gate should evolve from package-structure validation into lightweight implementation-progress validation where the project can express deterministic checks.

Prefer checks such as:

```text
current claimed stage
→ dependency maturity satisfied?
→ required build/typecheck/test gate passes?
→ required evidence exists and is current?
→ STATE pointer consistent with Acceptance/Plan?
→ derived views do not claim a conflicting current stage?
```

For data-driven or canonical producer-path claims, prefer a project-specific executable probe proving:

```text
representative producer
→ canonical validation/store/query
→ runtime consumer
```

rather than merely checking that a registry/data file exists.

For duplicate implementation ownership, hard-fail registered/conflicting active owners. Unregistered suspicious alternate files may be reported for review when deterministic ownership cannot be proven safely; do not pretend a filename heuristic is semantic proof.

Temporary scratch/debug/patch artifacts from an interrupted run are not automatically architecture defects. They become a convergence/hygiene failure when they are promoted into active architecture, conflict with canonical owners, or remain at a milestone/handoff/completion boundary without an intentional project-tooling role.


# v2.25 — Completion is an evidence-derived claim

A completed implementation session can still fail at the last mile if the agent summarizes progress from recent code production rather than reconstructing the final verdict from project truth.

The compiler must therefore materialize a distinct final-claim reconciliation:

```text
requested/master outcomes
+ canonical current State
+ Plan admission/completion rules
+ Acceptance requirements
+ actual current evidence
+ current revision/worktree
→ final verdict/report
```

Never let these proxies become completion evidence:

```text
file/module/function exists
large code/diff volume
project package validates
M0/foundation/walking-skeleton passes
agent says done
test count without Acceptance mapping
```

The final report is a derived view. It may summarize only verdicts supported by the canonical State/Acceptance/Evidence authorities and evidence actually exercised at the required boundary.

If a browser/runtime/user-surface claim requires real exercise and that exercise did not occur, preserve the narrower implementation/build evidence but keep the product claim unverified.

This is primarily a finalization/verification calibration, not a new architecture system.


# v2.26 — Whole-product realization graph before build order

The compiler must not confuse **architecture proof order** with **complete product scope**.

Before freezing `PROJECT_PLAN`, derive the complete required product realization graph from:
- confirmed user vision/outcomes;
- Product Capability/Responsibility Envelope;
- normal-user journeys and lifecycle;
- required screens/states/modes/workflows;
- setup/configuration/authoring where user-visible or operationally required;
- primary experience;
- interruption/recovery/error states;
- result/completion/return/replay paths;
- persistence/resume/progression where required;
- material visual/user-surface authorities;
- required content/data/provider paths.

For a multi-screen or multi-state product, `contracts/APP_FLOW.yaml` is mandatory unless an equivalent existing canonical workflow/state graph already owns the same truth.

The graph is not limited to UI screens. Nodes may represent user-visible modes, workflow states, lifecycle phases or externally observable states.

## Two-axis planning

Plan from two dimensions simultaneously:

```text
AXIS A — architecture readiness
Responsibility → Owner → Capability → Contract → integration maturity

AXIS B — product realization
Entry → setup/configuration → primary experience → interruption/recovery
→ completion/result → persistence/progression → return/replay/next-use
```

`PROJECT_PLAN` must interleave both. A walking skeleton proves that at least one vertical path through these axes works. It does **not** cover every node on Axis B.

Every required realization node/outcome must have:
- stable ID;
- owning System/Capability where applicable;
- governing product/design/reference authorities;
- planned milestone/stage;
- Acceptance IDs;
- required evidence;
- reachable predecessor/transition or explicit independent-entry rationale.

A required node with no plan stage or Acceptance mapping is a compiler defect.

## Product-scope coverage gate

Before package delivery and before final product completion, prove:

```text
every required realization node
→ reachable/intentional
→ assigned to a plan stage
→ mapped to Acceptance
→ eventually Verified or explicitly removed/deferred by authority
```

The compiler must not hide omitted product areas behind a good primary/core skeleton.

For design-heavy products, visual realization is attached to each material surface node, not isolated in one late "design overhaul" milestone. Shared Presentation/Design Core may be established early, but each required surface must still receive its product-specific composition/fidelity evidence.


# v2.27 — Three-truth compiler model

The compiler must keep three questions separate:

```text
PRODUCT TRUTH
What must the product be/feel/do?
Owned by Vision, Decisions, detailed product/system/design authorities and user-approved scope.

REALIZATION TRUTH
What outcomes, flows, responsibilities, contracts, content/surface/persistence obligations and plan stages are required to realize Product Truth?
Owned by the Product Realization authority plus bounded owners such as APP_FLOW, SYSTEM_MAP/CAPABILITY_GRAPH/SYSTEM_INTEGRATION, CONTENT_REGISTRY, conditional persistence contracts and PROJECT_PLAN.

VERIFICATION TRUTH
Which required outcomes are actually proven on the current revision, at what evidence scope?
Owned by Acceptance requirements + evidence records/results. STATE is not verification truth.
```

A later build agent may choose reversible implementation details but may not silently change Product Truth, remove required Realization outcomes, weaken Acceptance or manufacture a higher completion state by editing STATE.

## Canonical Product Realization outcome inventory

For every nontrivial product generate `contracts/PRODUCT_REALIZATION.yaml` as the canonical inventory of required product outcomes. It complements rather than replaces `APP_FLOW`:

- `APP_FLOW` owns user/workflow state-transition topology;
- `PRODUCT_REALIZATION` owns the complete required outcome inventory, including non-linear/cross-cutting outcomes such as persistence, performance, content authoring, physics relevance, accessibility/readability, scoring/progression, compatibility or operational behavior;
- `PROJECT_PLAN` owns sequencing/admission;
- Acceptance owns verification requirements/status;
- `verification/PRODUCT_REALIZATION_COVERAGE.yaml` is a derived coverage/result view, never another authority.

Each `PR-*` outcome records stable ID, provenance/authority source, required/optional/deferred disposition, responsibility owner/System/Capability/Contract refs, relevant producer/consumer/surface/content refs, plan stage and Acceptance IDs. Do **not** store mutable verification status as canonical truth in this file; derive it from Acceptance/Evidence.

## Build-agent decision boundary

Classify material decisions as:

- `USER_DECISION` — changes intended product/scope/experience; resolve with user before handoff unless explicitly deferred;
- `COMPILER_DECISION` — stable consequence of product truth/architecture;
- `DELEGATED_TECHNICAL_DECISION` — reversible technical choice the build agent may make inside contracts/guardrails.

Do not over-specify libraries, internal data structures, file layout, algorithm variants or rendering technique unless those choices are themselves product/architecture constraints.

## Agent-run learning loop

Before changing compiler policy after an implementation run:

```text
observed failure
→ was the invariant already present?
→ classify SEMANTIC_GAP / ADHERENCE_OR_EXECUTION_DRIFT / INCOMPLETE_RUN_ARTIFACT / VALIDATION_GAP
→ identify smallest compiler/gate intervention
→ add regression mutant/eval when repeatable
→ retest
```

Prefer project-specific executable gates over duplicate prose when the semantic rule already exists.


# v2.28 — Blueprint-backed modular implementation

When the product benefits materially from modular systems, compile clean Blueprint-backed responsibility boundaries inspired by visual composition systems but portable to ordinary code.

The compiler should specify semantic module boundaries, not prescribe one file/class per Blueprint.

Desired relation:

```text
System / Capability owner
→ bounded Blueprint / public contract
→ implementation boundary
→ internal code
```

and:

```text
Consumer
→ composes/calls public boundaries
→ does not become owner of their internals
```

This improves implementation-agent navigation and lets systems remain replaceable/testable without turning the package into interface-per-function enterprise architecture.


# v2.29 — Review-driven product realization (domain-neutral)

The source case that motivated this calibration came from an interactive product, but the compiler must preserve only the cross-domain mechanisms. Do not encode source-domain-specific phases, artifacts, actors, surfaces or tools as universal structure.

## 1. Representative Product Path / Heartbeat

When a project has a meaningful end-to-end or cross-boundary path, identify the smallest **representative product path** whose continued health gives high information about integration quality.

Examples of semantic shapes, not required taxonomies:

```text
request → validation → state change → response
input/import → normalization → canonical data → output/export
entry → configure → execute → observe result
source → generator → artifact → consumer
command → workflow → side effect → externally observable result
```

A verified representative path may be marked as a **regression heartbeat** in existing E2E/integration verification authorities. It is not a new product authority and does not replace complete Acceptance coverage.

Rerun an affected heartbeat after **material changes that can invalidate it**, not after every local edit. The compiler should declare likely impact categories/owners when useful so the build agent can choose the narrowest relevant heartbeat.

## 2. Deterministic Review Projection

For outcomes whose quality is hard to judge from source/tests alone, define a reproducible projection from the canonical product into a stable review surface:

```text
canonical product/state/artifact
→ fixed input/state/query/view/viewport/fixture
→ deterministic derived observation
→ agent/human review
```

Possible projections include screenshots, rendered views, reports, diffs, sample API/CLI outputs, generated documents, data-quality summaries, performance traces or other project-appropriate observations.

Invariant:

```text
REVIEW PROJECTION != PRODUCT AUTHORITY
```

If the projection exposes a defect, fix the canonical owner/source/producer, regenerate/re-exercise, then review the projection again. Do not patch the review artifact itself as the durable solution.

Define projections inside existing Acceptance/Evidence/E2E/visual-checkpoint mechanisms where possible; do not create a new authority solely to store screenshots or observations.

## 3. Reproducible Producer Pipeline

Where an artifact is generated or transformed, model the durable relationship:

```text
canonical source / recipe / authority
→ generator / transformation / provider
→ generated artifact
→ consumer
```

The generated artifact is normally **not** the canonical edit owner. A requested durable change should resolve back to the source/recipe/generator, regenerate the output and verify downstream consumers unless project policy explicitly declares the output hand-maintained.

This applies equally to generated code, documents, assets, indexes, bindings, reports, compiled outputs, transformed datasets and similar products.

## 4. Finish/Fidelity outcomes are product outcomes, not late polish

Functional correctness may be necessary but insufficient for the user's intended product quality. During Product Realization discovery, identify any material finish/fidelity outcomes implied by Product Truth or accepted compiler inference, such as:

- clarity/readability/usability;
- consistency/coherence;
- accessibility;
- error/recovery quality;
- output/content completeness;
- interaction/response quality;
- presentation/visual/audio fidelity where relevant;
- stability, latency, throughput or resource behavior where product-significant;
- operator/developer usability where part of the requested product;
- human judgment criteria where no deterministic substitute is adequate.

Represent these as ordinary `PR-*` outcomes with owner, plan stage, Acceptance and evidence requirements. Do not create a universal `POLISH` phase and do not infer aesthetic or quality requirements the user did not request or the product archetype does not materially imply.

## 5. Optional parallel workstreams are a planning heuristic, not architecture

A project may benefit from separating functional/behavioral work from experiential/presentation/content work, or from other responsibility-specific streams. This is only a planning heuristic. Canonical decomposition still follows Responsibility → Owner → Capability/Contract, and integration checkpoints must preserve the representative product path.


# v2.30 — Project-native product engine / definition-driven composition

A compiled package should make the finished product behave like a small domain-specific engine/toolkit rather than a sequence of individually hardcoded instances.

Use this semantic model when the product contains repeatable variants:

```text
Responsibility Owner/System
→ reusable Capability / public Contract
→ Reusable Definition Type / Blueprint contract
→ Definition / Profile / Composition
→ generic runtime or surface consumer
→ runtime instance / observable product
```

Not every project needs every layer. Use the smallest structure that makes repeated variants data/composition work rather than repeated architecture work.

Examples of the same general pattern:

```text
CatalogDefinition → generic detail/list consumers
WorkflowDefinition → canonical workflow runtime
ReportDefinition → generic report renderer/exporter
PolicyDefinition → canonical policy evaluator
IntegrationProfile → canonical integration adapter/runtime
```

The compiler must discover the project-specific equivalent instead of imposing these names.

## Definition-driven instance test

For every materially repeatable product type ask:

> If we add a second semantically similar instance, what must change?

Preferred answer:

```text
new/changed definition
+ existing capabilities/modules
+ declared profiles/modifiers
+ existing generic consumer/runtime
```

Warning signs:

```text
copy an existing page/controller/service/runtime
create a second state owner
duplicate validation/rules
hardcode another branch for instance N
```

If a new variant genuinely introduces reusable behavior absent from the current engine, extend the lowest correct Capability/Contract first and then compose the variant.

## Reusable Definition Type / Definition / Instance separation

Keep distinct:

- **Reusable Definition Type / Blueprint contract** — what fields, capability slots, lifecycle hooks, presentation slots and modifier seams this kind of thing supports;
- **Definition / Profile / Composition** — the declarative values and selected capabilities for one variant;
- **Runtime instance/state** — mutable execution/session state;
- **Generic consumer/runtime** — the reusable code/surface that realizes definitions.

Do not copy runtime state into definitions or encode one instance's values as new shared architecture.

## Modifier composition

Cross-cutting additions such as upgrades, policies, pricing rules, feature flags, transforms, permissions or other modifiers should normally reference stable capability/field seams and apply explicit merge operators or bounded behavior modules.

Prefer:

```text
Base Definition
+ Modifier Definition(s)
→ Effective Composition
```

over:

```text
copy Base Definition
→ hardcode modified variant
```

A modifier must not silently become a second owner of the capability it changes.

## Generic surface/runtime realization

When multiple definitions share the same presentation or execution semantics, compile one generic consumer and bind it to definitions.

Adding a new catalog item should not require a new detail-page implementation if the product model already supports a generic detail surface. Adding a new workflow type should not require copying the workflow engine if only configuration/composition differs.

User-visible exceptions that truly require a different semantic structure remain valid, but must be classified as a new capability/consumer type rather than hidden as instance-specific hardcode.

# v2.30 — Production-survivable composition

The early skeleton must establish the canonical composition model that ordinary finished-product breadth will reuse.

Allowed temporary elements:
- placeholder assets/content;
- provisional values/tuning;
- reduced production breadth;
- delegated provider/implementation choices behind stable contracts.

Not acceptable as a production-admissible skeleton:
- throwaway state/rule owners;
- fake runtime paths bypassing the intended owner;
- per-instance temporary architecture that later variants cannot reuse;
- placeholder composition that requires replacing canonical ownership to introduce production content.

Survivability challenge:

```text
replace placeholder content/presentation/provider
add a second representative definition
apply a representative modifier
add another consumer/variant through the same contract
→ canonical ownership and product path remain intact
```

Failure means the current path is exploratory scaffolding, not the production foundation. Explicit disposable scaffolding is allowed only when isolated from canonical product paths and given a removal milestone.


# v2.31 — Composition coherence invariants

System ownership is insufficient when product correctness depends on a relationship that must remain coherent across multiple owners, representations or projections.

For every material cross-system relationship ask:

```text
What canonical source/owner defines the relationship?
Which consumers/projections depend on it?
How do they stay coherent when the source changes?
What observable evidence proves the relationship still holds?
```

Examples are intentionally abstract:

```text
canonical source/value/geometry/state
→ runtime decision
→ persisted projection
→ rendered/published/exported projection
```

Do not create a new universal Invariants authority. Material cross-system invariants belong in the existing `SYSTEM_INTEGRATION` contract and point to their canonical owners, consumers and Acceptance evidence.

A Composition Invariant owns **no state**. It records a required relationship between existing owners.

## Repair-by-invariant compiler rule

When a user-visible defect can arise from cross-system drift, compile enough relationship information that the implementation agent can reason:

```text
observed defect
→ violated Acceptance / Composition Invariant
→ canonical source/owner
→ affected dependent consumers/projections
→ repair highest correct owner/relationship
→ rerun affected invariant + product-path/review evidence
```

Do not encourage:

```text
observed defect
→ nearest file/value
→ local patch
```

unless the defect is truly local and no shared relationship is violated.

A repeated defect caused by the same hidden relationship is evidence that the package lacks a material invariant or canonical derivation seam.

# v2.31 — Skeleton survivability is an admission claim

Distinguish:

```text
Exploratory Skeleton
= runnable learning/prototype path; may contain explicitly disposable scaffolding

Production Candidate Skeleton
= uses intended owners/contracts/composition path but survivability not yet proven

Production-Admitted Skeleton
= representative substitution/extension evidence proves the canonical path survives
```

These are derived maturity claims, not a new status authority.

`PROJECT_PLAN` declares which survivability Acceptance checks are required. Acceptance/Evidence proves them. `STATE` may point at the resulting admitted stage but cannot manufacture the admission.

Before calling a skeleton production-admitted, challenge representative future evolution such as:

- replace a placeholder through its declared production slot;
- add a materially different second same-type definition through the same reusable Definition Type;
- apply a representative modifier/profile/capability composition;
- add or substitute a supported consumer/provider through the declared contract.

If ordinary product completion requires replacing the canonical owner/runtime path, the skeleton remains exploratory.
