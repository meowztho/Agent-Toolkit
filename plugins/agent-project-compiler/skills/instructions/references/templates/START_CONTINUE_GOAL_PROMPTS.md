# APC v2.35 JIT Slice — Start, Continue and Goal Prompt Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## START_PROMPT.md Template

The generated Start Prompt is a **context-rich denormalized orientation snapshot**, not a pointer chain. It may be long. Populate it from canonical authorities and mark it non-authoritative.

```markdown
GENERATED ORIENTATION SNAPSHOT — canonical details live in the referenced project authorities. Regenerate this prompt when those authorities materially change.

# PROJECT MISSION
[Write the actual complete product outcome in direct natural language. Do not say merely "read GOAL.md". Explain what is being built, for whom, and what observable result constitutes success.]

# USER VISION / INTENT
[High-signal vision, desired feel/outcome, product identity, important non-goals, and selected verbatim wording where paraphrase loses meaning.]

# MATERIAL INTERVIEW CONTEXT
[Group material compiler questions + verbatim user answers that define behavior, architecture, terminology, extension semantics, negative requirements, or otherwise prevent plausible misunderstanding. For large interviews include all architecturally/behaviorally material Q/A, not only one-line summaries.]

# DECISIONS THAT DEFINE THE PRODUCT
[Readable normalized decisions/rationale/rejected alternatives from DECISION_COMPENDIUM.]

# MASTER SYSTEM / CAPABILITY / COMPOSITION MODEL
[Inline the core systems, reusable capability hierarchy, what they own, how consumers compose them, important producer→contract→consumer paths, authoring/content model, value-resolution semantics, and relevant ordinary-product responsibilities/dispositions whose omission would mislead.]

# CORE-FIRST ARCHITECTURE LAW
[Classify later user deltas before source edits. Missing reusable behavior is added at the lowest canonical capability first, then composed into consumers. Local differences are data/profiles/modifiers unless an intentional new capability is required.]

# CRITICAL USER / SYSTEM FLOWS
[Normal-user journey(s), important lifecycle/failure/recovery paths, and cross-system behavior that must remain coherent.]

# ARCHITECTURE GUARDRAILS
[Important forbidden implementations / negative requirements.]

# ACCEPTANCE / REALITY MODEL
[Explain what must actually be connected, exercised and verified; include key release-gating outcomes.]

# PRODUCT REALIZATION ROADMAP
[List the complete recommended product stages/outcomes at useful granularity. Mark foundation/walking-skeleton stages as proofs, not product completion. Show the required outcomes that remain afterward.]

# VISUAL / USER-SURFACE TARGET
[When material: compact product-specific gestalt, applicable reference/baseline IDs, essential hierarchy/layout/style constraints and anti-generic-default traits. Exact work still requires inspecting the registered references.]

# CURRENT PROJECT STATE / FIRST EXECUTION TARGET
[Greenfield: first admitted coherent walking skeleton, what it proves, and what later stages it unlocks. Existing project: current admitted stage, verified state, unmet/reopened outcomes, blockers, current revision.]

# REQUIRED BOOTSTRAP AUTHORITIES
[List `PROJECT_INDEX.yaml` plus the direct `bootstrap.must_read` authority IDs/files. These MUST be loaded after this orientation and before the first material source edit. Do not make the agent discover them through multi-hop prose.]

# REQUIRED WHOLE-PROJECT ORIENTATION VIEW
[For nontrivial projects: `VIEW-PROJECT-ATLAS` / `PROJECT_ATLAS.html`. Validate/regenerate if stale, then inspect once for whole-project orientation. It is generated and non-authoritative; exact rules still require canonical source reads.]

# AUTHORITIES FOR PRECISION
[List current-domain canonical files/sections/IDs. `PROJECT_INDEX.yaml` remains the canonical JIT router for every other normative authority.]

# EXECUTION RULES
- The project mission above is the goal. Reading/validating project files is an execution step, not the goal.
- Identify repository root, applicable instructions, Git state/relevant diffs, actual runtime/verification capabilities and current evidence.
- Before creating behavior, inspect canonical system/semantic owner and existing implementation path. Reuse → Extend → Correct → intentionally Replace before creating another path.
- Load the required bootstrap authorities. For nontrivial projects validate/regenerate and inspect the routed Atlas once, then derive the active requirement's `required_source_ids` from `PROJECT_INDEX.yaml`; material source edits wait until those authorities were actually read in the current context/session.
- Resolve/load only additional JIT exact authorities/skills needed for the active requirement after this orientation.
- Treat a current task as one step toward the master outcome, never as product completion.
- Verify units, integration, value/config propagation, user-surface behavior and final release gates with the evidence required by Acceptance.
- Ask only unresolved material user-owned product/content/design questions. Do not re-ask answered interview questions or ask for reversible technical choices.
- A foundation/scaffold/walking skeleton is an early proof, not product completion. After each milestone reconcile the remaining product-realization roadmap and continue through the next admissible stage.
- For material user-surface work, load/inspect the registered visual authorities and preserve the product-specific visual target; generic/default styling is not completion when a specific visual identity exists.
- Continue autonomously while useful work remains.
```

After the direct orientation above, the agent may consult `CONTEXT_HANDOFF.md`, `docs/DECISION_COMPENDIUM.md`, `contracts/SYSTEM_MAP.yaml`, `contracts/CAPABILITY_GRAPH.yaml`, `contracts/SYSTEM_INTEGRATION.yaml`, `ACCEPTANCE_MATRIX.yaml`, registries and detailed system authorities for precision.

Before implementation, ensure `verification/AUTHORITY_REACHABILITY.yaml` is passed/current, then inspect `contracts/INTERVIEW_COVERAGE.yaml` and `verification/FRESH_AGENT_RECONSTRUCTION.yaml`. A COMPLETE package should not need new product questions; PARTIAL packages ask only unresolved material user-owned items.

---

## CONTINUE_PROMPT.md Template

`CONTINUE_PROMPT` rehydrates product + state; it must not be only a list of files.

```markdown
GENERATED CONTINUATION SNAPSHOT — canonical details remain in project authorities.

# PRODUCT / MASTER OUTCOME
[One compact but concrete paragraph describing the actual product outcome.]

# VERIFIED STATE
[What is currently proven on this worktree/revision.]

# REMAINING PRODUCT REALIZATION
[Current admitted stage + concise remaining roadmap/outcomes. A completed foundation/skeleton must not look like master completion.]

# VISUAL / USER-SURFACE TARGET
[When the current/next stage affects the user surface, rehydrate the applicable gestalt/reference IDs/baseline.]

# CURRENT UNMET REQUIREMENT
[Requirement + why it matters to the full product. Explicitly label it as a step, not the goal.]

# RELEVANT SYSTEM / CAPABILITY / OWNERSHIP CONTEXT
[Systems, capability path, canonical owner/runtime path, composition/value-resolution context and current-change classification required for this work.]

# REQUIRED SOURCES TO REREAD
[Authority IDs/files/sections derived from `PROJECT_INDEX.yaml` for this requirement. These form the current context-load gate.]

# NEXT USEFUL ACTION
[Concrete next action from durable state.]

Resume from actual repository/Git/evidence state. Preserve unrelated changes. Do not recreate verified work or infer project truth from old conversation memory. Load only JIT context/skills after this rehydration, verify the affected unit/integration/user-surface slice, update evidence/state, then select the next unmet requirement. Continue until the full master outcome is verified or a genuine user-only product decision blocks useful work.
```

If the implementation agent is genuinely fresh or suffered major context loss, use START-level orientation again, including Atlas freshness/inspection for nontrivial projects, before the normal continuation loop.

---

## GOAL_PROMPT.md Template

A Goal Prompt must **state the goal directly**. Do not make `GOAL.md` inspection the apparent objective.

```markdown
/goal

# MASTER OUTCOME
[Inline the complete observable product outcome from GOAL.md in direct natural language.]

# NON-NEGOTIABLE PRODUCT + ARCHITECTURE CONSTRAINTS
[Key system/capability/composition/behavior/negative constraints, including the core-first change law.]

# CURRENT VERIFIED STATE
[Fresh summary generated from durable Acceptance/Evidence/STATE, not conversation memory.]

# REMAINING / REOPENED REQUIREMENTS
[List the actual unmet product requirements. A document-read/validation task may support them but is never itself the master goal unless the product really is that artifact.]

# COMPLETION CONDITION
[Inline the required acceptance/evidence/end-to-end condition. State that the final report is derived from canonical current state + actual evidence, never code/file existence.]

Reading `GOAL.md`, contracts, Blueprints, source and evidence is an execution step for precision, not the goal. The current task is one step toward the master outcome. Continue autonomously through successive unmet/reopened requirements until the master outcome above is verified on the current final worktree.

Before creating/changing behavior, classify the request against the canonical system/capability hierarchy; add missing reusable capability first, then compose the consumer. Reuse/extend/correct before parallel implementation. Treat field/API/config existence only as declaration; trace and exercise its live consumer/effect. For user-facing work, completion requires applicable real-surface interaction/visual evidence. If a blocking finish hook exists, its validator verdict governs eligibility to stop.
```

The generated Goal Prompt should directly include current master outcome/state each time it is issued. It may then point to `GOAL.md`, `ACCEPTANCE_MATRIX.yaml`, `SYSTEM_MAP`, `CAPABILITY_GRAPH`, `SYSTEM_INTEGRATION`, registries and exact authorities for detail.

---

