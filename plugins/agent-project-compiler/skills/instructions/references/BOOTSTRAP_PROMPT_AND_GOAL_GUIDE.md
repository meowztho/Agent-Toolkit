# Bootstrap Prompt and Goal Rehydration Guide

# Current Precedence — Rich START, Stable GOAL, Whole-Product Flow + Full Realization Roadmap

START is intentionally rich for fresh agents and major rehydration. It should directly include master outcome, product gestalt, high-signal wording, digest of every completed interview round, selected verbatim Q/A, decisions/rationale/rejections, reference anchors, Responsibility/System/Capability/Composition/Ownership model, important forward flows and reverse-debug pointer, guardrails/future constraints, acceptance/reality model, current state, and a concise build-order/admission roadmap explaining the first coherent stage and what later outcomes reuse it.

START also embeds the Portable Operating Kernel so it works when provider auto-instructions are absent. Exact authorities remain canonical and must still be read through `PROJECT_INDEX`.

GOAL stays small/stable: observable master product outcome/completion condition. Reading/validating documents is never the goal. CONTINUE rehydrates enough current product/system/change/failure/admission context to prevent task/goal substitution; after major loss use START-level rehydration.

---


## Purpose

The first implementation prompt is an execution artifact, not a file-navigation instruction.

A capable agent may technically have access to perfect project files and still form the wrong mental model if its first message is only:

```text
Read GOAL.md.
Read PROJECT_INDEX.yaml.
Follow the linked files.
```

That creates two failure modes:

1. the agent treats document inspection itself as the goal;
2. the project meaning becomes a pointer chain, so unread descendants silently disappear from active context.

The compiler must therefore generate **context-first prompts** that directly rehydrate the product model before asking the agent to navigate precise authorities.

---

# 1. Prompt hierarchy

Use three different prompts for three different jobs:

```text
START_PROMPT
= initial mental-model hydration + execution contract

CONTINUE_PROMPT
= context recovery + current-state hydration

GOAL_PROMPT
= explicit master-outcome reassertion + remaining-work continuation
```

None of these may define the product independently. They are **generated denormalized orientation artifacts** compiled from canonical authorities.

They may intentionally duplicate important context because their job is to place that context directly in the model's active window. Mark them as generated/non-authoritative and regenerate them when their source authorities change.

---

# 2. START_PROMPT is allowed to be large

There is no artificial size target for the generated first prompt.

Prefer a prompt that gives the implementation agent the correct product model immediately over a tiny prompt that forces several levels of document chasing.

The start prompt should inline enough information that the agent can explain, before opening implementation files:

- what is being built;
- who it is for;
- how it should feel/behave;
- the master outcome;
- major non-goals and forbidden interpretations;
- important user wording and material Q/A that shaped architecture/behavior;
- major reference traits and exclusions;
- canonical master systems, capability hierarchy and composition model;
- important ownership/runtime-flow constraints;
- authoring/content-extension rules;
- critical normal-user workflows;
- key acceptance/reality expectations;
- current project state when starting from an existing repository;
- what decisions are already settled versus intentionally open;
- the full product-realization roadmap and what remains after the first foundation/skeleton;
- for design-heavy products, the visual/user-surface target and its governing reference IDs.

Detailed exact values and large per-system rules remain canonical in their authorities, but the agent should not need to traverse a chain of links merely to understand the project.

---

# 3. Include Q/A when Q/A carries the mental model

A normalized Decision Compendium is useful but does not always recreate why the user meant something.

When the interview itself contains high-signal distinctions, include the relevant question + verbatim answer directly in the first prompt, grouped by domain/system.

For very large interviews:

1. include every Q/A that materially defines product behavior, architecture boundaries, extension semantics, negative requirements, or ambiguous terminology;
2. include additional high-signal Q/A that prevents plausible wrong interpretations;
3. keep the full ledger as canonical provenance for the rest.

Do not reduce an answer to `yes` when its surrounding question gives that answer meaning.

---

# 4. START_PROMPT structure

Recommended generated shape:

```text
GENERATED ORIENTATION SNAPSHOT — canonical details live in project authorities.

# PROJECT MISSION
[Direct natural-language description of the complete product and master outcome.]

# USER VISION / INTENT
[High-signal user wording, desired feel/outcome, non-goals.]

# MATERIAL INTERVIEW CONTEXT
[Grouped material Q/A excerpts with verbatim answers where they prevent ambiguity.]

# DECISIONS THAT DEFINE THE PRODUCT
[Readable Decision Compendium subset: decisions, rationale, rejected alternatives.]

# SYSTEM / CAPABILITY / COMPOSITION MODEL
[Master systems, reusable capability hierarchy, consumer compositions, authoring model, important ownership/runtime paths.]

# CORE-FIRST ARCHITECTURE LAW
[For later user deltas: classify before source edits; reusable behavior belongs at the lowest canonical capability, then consumers compose it. Differences are data/profiles/modifiers unless an intentional new capability is required.]

# CRITICAL WORKFLOWS
[Normal-user and important failure/recovery flows.]

# ARCHITECTURE GUARDRAILS
[Important things the implementation must not become.]

# ACCEPTANCE / REALITY MODEL
[What must be observable to call the product correct.]

# PRODUCT REALIZATION ROADMAP
[Show the complete recommended stage/outcome sequence at useful granularity. Explicitly distinguish architecture/foundation proof from product completion and show what remains after the first walking skeleton.]

# VISUAL / USER-SURFACE TARGET
[When surface identity is material: compact gestalt + key reference IDs/approved or delegated baseline + essential layout/hierarchy/style traits. State that these authorities remain binding during implementation, not only final polish.]

# CURRENT STATE / FIRST EXECUTION TARGET
[Greenfield: first admitted coherent walking skeleton and what it proves; explicitly state the next product stages it unlocks. Existing repo: verified state + current admitted stage + remaining outcomes.]

# REQUIRED BOOTSTRAP AUTHORITIES
[`PROJECT_INDEX.yaml` plus its direct `bootstrap.must_read` authorities. These are named explicitly and loaded before the first material source edit; do not hide them behind a prose chain.]

# AUTHORITIES FOR PRECISION
[Current-domain canonical files/sections. Every other normative authority remains discoverable through `PROJECT_INDEX.yaml`.]

# EXECUTION RULES
[Git, reuse-before-create, JIT exact rereads, integration/user-surface verification, autonomy/user gate.]
```

File-reading instructions are execution steps, **not the project goal**.

---


## Discoverability rule

Context-rich prompts solve mental-model hydration; they do **not** replace deterministic authority discovery.

After the START snapshot, the agent must read:
1. `PROJECT_INDEX.yaml`;
2. every direct `bootstrap.must_read` authority declared there;
3. registries/Acceptance needed to resolve IDs and status.

For each later requirement, `PROJECT_INDEX.yaml` must directly route the relevant normative authorities. A system file that merely exists in the repository, or is mentioned only by another file, is not discoverable enough.

For nontrivial projects, `PROJECT_INDEX.bootstrap.inspect_view_ids` must also name `VIEW-PROJECT-ATLAS`. After the direct bootstrap authorities are loaded, validate/regenerate the Atlas if stale and inspect it once for whole-project orientation. The Atlas is not an authority and cannot replace any required source read.

The compiler must reject packages with orphan/unreachable normative authorities. `verification/AUTHORITY_REACHABILITY.yaml` records the generated validation result; it is evidence, not a second router.

Before a material source edit, derive the current requirement's required authority IDs from `PROJECT_INDEX.yaml` and actually load them. When the harness can observe file reads, use that for the source-load gate; otherwise require explicit runtime attestation/state. Reset that loaded-source state after major context loss.

# 5. Goal rehydration

A `/goal` prompt must never be only:

```text
/goal Achieve the objective in GOAL.md
```

The prompt itself must inline:

```text
MASTER OUTCOME
NON-NEGOTIABLE PRODUCT + ARCHITECTURE CONSTRAINTS
CURRENT SYSTEM/CAPABILITY MODEL
CURRENT VERIFIED STATE
CURRENT UNMET/REOPENED REQUIREMENTS
COMPLETION CONDITION
```

Then it may point to `GOAL.md`, Acceptance, System Map and `PROJECT_INDEX.yaml` for exact-authority routing. Those files refine execution; they are not the goal.

The current task/requirement is always labelled as a **step toward the master outcome**, never as the goal itself.

Use explicit wording such as:

> Reading or validating project files is not the goal. Those are execution steps. The goal is the observable product outcome described above.

When `/goal` is reissued after context loss, regenerate the current-state portion from durable state/evidence rather than relying on old conversation memory.

---

# 6. Continue prompt

`CONTINUE_PROMPT` is smaller than START but still rehydrates enough state to avoid task/goal substitution:

- one-paragraph product/master-outcome capsule;
- current verified state;
- current admitted stage plus the remaining product-realization roadmap;
- current unmet requirement and why it matters to the full product;
- applicable visual/user-surface target when the next work affects the product surface;
- relevant system/capability/ownership context and current change classification;
- exact required sources derived from `PROJECT_INDEX.yaml`;
- next useful action;
- reminder that the current task is not completion.

For a genuinely fresh implementation agent or major context loss, use START-level orientation again rather than a pointer-only Continue prompt.

---

# 7. Prompt freshness and regeneration

START/GOAL/CONTINUE prompts are generated views.

Regenerate or update them when material changes affect:

- product vision/master outcome;
- system/capability topology/composition;
- architecture guardrails;
- material interview decisions;
- acceptance/completion conditions;
- current verified/unmet state for Goal/Continue.

Do not hand-edit prompt snapshots into a second authority. Correct the canonical source, then regenerate the prompt.

---

# 8. Fresh-agent prompt test

Fresh-Agent Reconstruction should test two levels:

## Orientation test

Give the fresh agent the generated START prompt first. Before broad file traversal, ask it to explain:

- what product it believes it must build;
- the master outcome;
- major systems/compositions;
- important negative requirements;
- one representative end-to-end flow;
- what counts as completion.

Material misunderstanding means the prompt is insufficient.

## Precision test

Then allow the package authorities and verify that the agent can resolve exact rules without inventing missing semantics.

This catches both failures:

```text
prompt too thin → wrong mental model
package too thin → exact rules still require guessing
```

---

# 9. Universal principle

Context routing optimizes repeated work. It must not prevent initial understanding.

Use:

```text
FIRST TURN
= context rich

NORMAL EXECUTION
= JIT precise

CONTEXT LOSS
= rehydrate, then JIT
```

The first prompt is therefore intentionally different from the compact runtime loop.

# Bootstrap reminder for Governance and project gate

When the generated project includes an executable project gate, START and CONTINUE must name it directly and place it before material edits. Do not hide it behind a multi-hop "read the tooling docs" pointer.

For target environments where a Core-First Governance plugin/Skill is known or likely available, the generated prompt should say to load/apply the actual bound capability for architecture-relevant work and reload it after major compaction/context loss. It must also include the fallback: if unavailable, state that fact and proceed with the project-native gate + project authorities rather than stopping or pretending it ran.

After compaction, START/CONTINUE rehydrates the current admitted stage, exact required authorities/references and the first gate command. Old session read/plugin state is not trusted.


# 10. Foundation-is-not-finish prompt invariant

For implementation projects, START/GOAL/CONTINUE must make this distinction explicit when a foundation/walking skeleton exists:

```text
FOUNDATION / WALKING SKELETON PASS
= architecture + integration path proven

MASTER PRODUCT COMPLETE
= all required product outcomes + representative/real surface + required final evidence proven
```

A prompt that names only the first execution target without showing meaningful remaining product realization is insufficient for weak/long-running agents.

# 11. Surface-target hydration

For design-heavy user-facing products, do not rely on a later JIT `ui_task` trigger to introduce the visual identity for the first time.

START must inline a compact `VISUAL / USER-SURFACE TARGET` derived from the canonical surface authorities. It should contain only high-signal traits and reference IDs; exact visual work still requires reading/inspecting the routed authorities.

When a current or next admitted stage contains user-surface work, CONTINUE/GOAL must rehydrate the applicable target and reference IDs. This is intentional denormalization for attention, not a second design authority.


# v2.25 Final-claim capsule

GOAL/CONTINUE should make final completion semantics explicit for long-running/weak agents:

```text
Final status comes from canonical current state + actual required evidence.
A green foundation/project gate, implementation artifact, or large diff is not product completion.
```

Near finalization, the continuation context should route the agent back to current STATE, Plan/Acceptance and evidence instead of summarizing success from recent implementation narrative.


# v2.26 Whole-product flow capsule

START must not describe only the architecture and first execution target. For nontrivial products it must inline a compact normal-user/product lifecycle derived from the canonical APP_FLOW/workflow authority.

Example shape:

```text
PRODUCT FLOW
Entry/Home
→ Setup/Configuration
→ Primary Experience
→ Pause/Recovery
→ Completion/Results
→ Progression/Save
→ Replay/Return/Resume
```

Use the actual project nodes and omit inapplicable stages.

For each major node, START should make clear:
- what the user reaches/does there;
- which later nodes remain unbuilt/unverified;
- applicable visual/reference authority when material.

This capsule is generated orientation, not a second flow authority. Its purpose is to make omitted later product stages impossible to mistake for completed scope.

CONTINUE should rehydrate:
- current node/stage;
- verified predecessor path;
- remaining required product-flow nodes;
- next admissible node/stage.

A continuation that says only "next requirement: implement X" is insufficient when the agent can lose sight of the rest of the product lifecycle.


# v2.27 Build-agent role capsule

START must tell the implementation agent what is already decided and what remains technically delegated:

```text
PRODUCT DECISIONS
= do not reinterpret without USER authority

ARCHITECTURE / REALIZATION / ACCEPTANCE
= project authorities; follow/extend only through admitted change process

DELEGATED TECHNICAL DECISIONS
= build agent may choose reversible implementation details within contracts/guardrails
```

Also state the continuation law:

```text
Milestone PASS is not a stopping condition.
After every milestone: update evidence → derive admission → continue with next admissible stage.
Stop only at COMPLETE, genuine user/external blocker, or explicit stop.
```


# v2.29 Representative-path and finish/fidelity capsule

For projects with a declared representative product path, START/CONTINUE should expose a compact orientation capsule:

```text
REPRESENTATIVE PRODUCT PATH
[path/scenario ID + semantic chain]
heartbeat status: [verified/current/stale/unverified]
material impact categories: [...]
```

For projects with material finish/fidelity outcomes, also list the still-open `PR-*` outcomes alongside functional outcomes. This prevents a technically functional core from visually/operationally reading as "done" when the requested product quality is still unverified.

These are derived attention aids. The E2E/Acceptance/Product-Realization authorities remain canonical.


# v2.30 Product-engine capsule

When repeatable/domain-authored variants are material, START should summarize the project-native engine model:

```text
reusable Definition Type
→ canonical owner/capabilities
→ definition/profile source
→ generic runtime/surface consumer
→ modifier seams
→ authoring/registration path
```

Also state the expansion rule: ordinary same-type additions should be definition/composition work; new core code is justified only by genuinely new reusable semantics.

This capsule is orientation only; exact implementation still requires reading the routed System/Capability/Blueprint authorities.


# v2.31 Coherence / repair capsule

When the current stage touches a material cross-system invariant, START/CONTINUE should route the invariant ID, canonical source/owner and affected consumer IDs. This is orientation only; exact repair requires reading `SYSTEM_INTEGRATION`.

If continuing from a reported defect, CONTINUE should state whether the current diagnosis is local or coherence-related and which invariant/evidence must be restored before claiming the defect resolved.
