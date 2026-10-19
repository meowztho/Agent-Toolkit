# Context Runtime and Output Contract

# Current Precedence — One-Shot Discoverability and Context Evidence

`PROJECT_INDEX.yaml` is the canonical retrieval router. Every active normative/discoverability-required authority must be reachable from guaranteed bootstrap/JIT routes or registries. Generated views/evidence are not normative truth.

For current work, resolve `STATE.context.required_source_ids`, perform actual reads, and record session-scoped `loaded_source_ids`/observed read evidence before dependent edits. Reset/re-evaluate after fresh session, major context loss/compaction, relevant authority revision or domain/requirement change.

The compiler is one-shot: generated project routing must be sufficient even when the compiler chat never returns. Keep runtime context selective/JIT, but persistent project knowledge lossless.

---


# Agent Context Runtime Reference

## Active context is a cache
Repository/project authorities and current external/runtime evidence are persistent truth. Active model context is disposable working memory.

**Workspace awareness != workspace hydration.** Knowing that a file, prior decision, Working View, test result, or tool exists does not mean its current contents are loaded or still valid. If exact/canonical/contractual information has an authoritative source, reread it when needed rather than trusting old conversation memory.

Do not fight context rot by preloading the whole workspace. Discover current state cheaply, then hydrate only the sources required by the active decision.

## Context layers

### Always active
`AGENTS.md`: canonical portable runtime kernel when supported; otherwise a thin provider adapter points back to the same authorities.

### Session bootstrap
A fresh implementation agent consumes the context-rich `START_PROMPT.md`, then reads the bootstrap authorities declared by `PROJECT_INDEX.yaml` plus the compact runtime state. `PROJECT_INDEX.yaml` itself is mandatory bootstrap because it is the discoverability router; `PROJECT_REGISTRY.yaml`, `ACCEPTANCE_MATRIX.yaml`, `STATE.json`, and Blueprint registry are loaded when present/applicable.

### Just-in-time
Only authoritative sections, code, tests, assets, screenshots, and references needed for the current requirement.

### Context-rich execution prompts
`START_PROMPT.md`, `CONTINUE_PROMPT.md`, and `GOAL_PROMPT.md` are generated denormalized orientation snapshots. They intentionally inline enough product/decision/system/state context to hydrate the model before JIT retrieval; they are not canonical authorities and must be regenerated from authorities when material sources change.

A fresh agent should not need to follow a multi-hop file chain merely to understand the product or master outcome. Use `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md` for the canonical prompt policy.

## Retrieval flow

CURRENT REQUIREMENT
→ classify domain(s)
→ consult PROJECT_INDEX
→ locate authoritative source + section
→ read required section completely
→ follow only required dependencies
→ inspect implementation/assets
→ execute
→ verify

Do not preload all documentation.

## PROJECT_INDEX is routing, not knowledge

Good:
```yaml
design:
  authority: docs/DESIGN.md
  read_when: [ui_task, menu_task]
  sections:
    menu: "Menu System"
```

Bad:
```yaml
design:
  summary: "Menus use large blue panels..."
```


## Authority discoverability invariant

A normative file that exists but is not reachable from a guaranteed entry point is operationally equivalent to missing documentation.

Generated projects therefore use one explicit discovery graph:

```text
START/CONTINUE orientation
→ PROJECT_INDEX.bootstrap
→ PROJECT_INDEX domain routes
→ PROJECT_REGISTRY / Blueprint registry resolution
→ normative authorities
```

Rules:
- every active normative artifact has one stable ID in `PROJECT_REGISTRY.yaml` (Blueprints use `blueprints/REGISTRY.yaml`);
- every active normative artifact is either in `PROJECT_INDEX.bootstrap.must_read` or appears in at least one `PROJECT_INDEX.domains.*.authority_ids` route;
- a routed Blueprint may discover called Blueprints through `blueprints/REGISTRY.yaml`; unrouted/unreachable active Blueprints are invalid;
- generated views, prompts, evidence binaries, caches and support artifacts are explicitly non-normative and do not satisfy authority coverage;
- every normative prose authority includes lightweight authority metadata/backlinks (artifact ID, routed domain(s), provenance/decision refs, integration/Blueprint/Acceptance refs where applicable);
- the project validator computes reachability and emits `verification/AUTHORITY_REACHABILITY.yaml`;
- any active normative authority or required Blueprint that is unreachable makes the package NOT COMPLETE.

`PROJECT_INDEX.yaml` is the single canonical retrieval router. Do not create a second manually maintained authority graph.

### Required-source load gate

Routing alone does not prove the current agent actually read the needed authority.

For the active requirement:
1. classify its domain(s);
2. derive `STATE.context.required_source_ids` from `PROJECT_INDEX.yaml`;
3. resolve IDs through registries;
4. read the required sources completely enough for the dependent change;
5. record the current-session `loaded_source_ids`/load evidence when the harness can observe file reads, or explicitly attest them when it cannot;
6. block material source edits while required sources for the change are missing/stale.

Loaded-source state is session/context state, not project truth. Reset/re-evaluate it after a fresh session, major compaction/context loss, repository/project switch, target-domain/workstream change, relevant Skill/authority revision, material repository/external-state change, or uncertainty that the required source was actually loaded.

## Generated-view / Atlas gate

`PROJECT_INDEX.yaml` also routes required **non-normative generated views** separately from normative authorities. For nontrivial projects, bootstrap should include `VIEW-PROJECT-ATLAS` in `inspect_view_ids`.

On a fresh session or major context recovery:
1. validate Atlas source fingerprint/freshness;
2. regenerate it from canonical sources if stale;
3. inspect it once for whole-product orientation;
4. record the view ID in `STATE.context.inspected_view_ids`;
5. then continue JIT authority loading.

The Atlas never satisfies an authority read. `loaded_source_ids` and `inspected_view_ids` are separate on purpose. A generated view may be required/discoverable while remaining `normative: false`.

Material changes to Atlas inputs mark the view stale; refresh at the next milestone and before handoff/final completion.

## Precision classes
Use sparingly:
- semantic
- structural
- exact
- canonical

Exact/canonical information should be reread before dependent changes.

## Context loss / handoff
For ordinary resume state, prefer pointers over fresh narrative summaries. A compiler-generated `CONTEXT_HANDOFF.md` is the deliberate exception: a new agent/major context-loss recovery reads that rich onboarding artifact once, then resumes pointer/JIT operation.
- goal/requirement;
- task;
- verified criteria;
- implementation paths;
- authoritative sources to reread;
- next action;
- blockers.

After context loss or another freshness invalidation:
1. cheaply identify the current repository/project root, applicable instructions, Git/current-change state, routing/index artifacts, compact `STATE` pointer, and relevant current evidence;
2. inspect the context-rich orientation only as a bootstrap aid, then consult `PROJECT_INDEX.bootstrap`;
3. reset/rebuild current-session required/loaded-source state;
4. derive and reread only the active requirement's required authorities and required dependencies;
5. reconcile completed/remaining work, blockers, assumptions, admission, and evidence against current truth;
6. replan before material execution if the next best action changed;
7. resume only after the context-load gate passes.

Do not rebuild confidence by loading all documentation, old plans, historical chats, or every Working View.

## User gate
Uncertainty is not a blocker.

Before asking the user:
1. inspect index;
2. read authoritative source;
3. inspect code/assets/state;
4. decide whether technical/reversible;
5. continue unrelated useful work if possible.

Ask only for a genuinely missing product/content/design decision that materially changes the result and blocks useful progress.

---

# Output Contract

## Base package

For a nontrivial compiled project, generate the applicable canonical set; do not omit an artifact merely because another summary mentions the same topic:

```text
AGENTS.md
PROJECT_CORE.md
PROJECT_INDEX.yaml
PROJECT_REGISTRY.yaml
GOAL.md
STATE.json
ACCEPTANCE_MATRIX.yaml
CONTEXT_HANDOFF.md

docs/
  USER_VISION.md
  INTERVIEW_LEDGER.md
  DECISION_COMPENDIUM.md
  PROJECT_PLAN.md
  systems/<SYSTEM>.md              # one per nontrivial core system

contracts/
  INTERVIEW_COVERAGE.yaml
  SYSTEM_MAP.yaml                  # when reusable master systems exist
  CAPABILITY_GRAPH.yaml             # when reusable semantic sub-capability hierarchy matters
  SYSTEM_INTEGRATION.yaml          # when cross-system ownership/runtime paths matter
  ARCHITECTURE_GUARDRAILS.yaml     # when explicit negative requirements prevent plausible wrong paths
  AGENT_RUNTIME_PROFILE.yaml       # when agent/harness customization primitives matter
  SKILL_REQUIREMENTS.yaml          # when specialist capabilities matter
  EXECUTION_POLICY.yaml            # coding/autonomous projects
  VERSION_CONTROL.yaml             # coding projects
  ...project-specific contracts

blueprints/REGISTRY.yaml           # when Blueprints are used
verification/FRESH_AGENT_RECONSTRUCTION.yaml  # nontrivial package-quality gate
verification/ABSTRACTION_TESTS.yaml            # when extensibility/composition needs adversarial proof
verification/...                    # other applicable evidence/flow/audit contracts
PROJECT_ATLAS.html                 # required generated non-authoritative orientation view for nontrivial projects
prompts/START_PROMPT.md
prompts/CONTINUE_PROMPT.md
prompts/GOAL_PROMPT.md
```

The three prompt files are generated, denormalized **orientation views**. They may repeat important context intentionally so a new agent receives the project model directly; canonical truth remains in the referenced authorities. Use `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md`.

Then create every project-specific system authority, plan, Blueprint/spec and verification contract required to preserve and implement the user's material intent. For nontrivial projects `PROJECT_ATLAS.html` is required as a generated whole-project orientation view; it is never an authority and must have a reproducible regeneration path.

**No generated-package size cap:** keep always-loaded runtime files compact for routing and orientation, but create as many detailed JIT system/spec/contract/Blueprint files as the project needs. Do not merge unrelated systems or discard Q/A/context merely to reduce active-context pressure.

## Required principle: detailed intent lives in docs/

`PROJECT_CORE.md` is orientation, not a place to compress away details.

The final `docs/` directory must contain enough authoritative information that a capable implementation agent can perform the project without needing the original interview/chat.

Typical detailed authorities include:
- `DECISION_COMPENDIUM.md` — readable normalized product/decision model; exact behavior remains in dedicated authorities
- `PROJECT_PLAN.md`
- one `docs/systems/<SYSTEM>.md` per nontrivial core system

Potential blueprints include:
- `DESIGN.md`
- `ASSET_BLUEPRINT.md`
- `ARCHITECTURE.md`
- `CONTENT_BLUEPRINT.md`
- `REFERENCE_MAP.md`
- domain/system specifications

Do not create irrelevant empty files.

### Compilation scale controls formality, not architecture law

Classify the project internally as simple/moderate/nontrivial (complex) from scope, number of workflows/systems, cross-boundary state, future extensibility and verification needs. Record the result in `PROJECT_CORE.md` rather than inventing a separate competing classification authority.

The scale decides how much formal machinery is applicable; it never permits duplicated shared behavior or hidden ownership. Tiny projects may omit Atlas/System Integration/etc. when genuinely unnecessary. Nontrivial projects use the full applicable fidelity stack.

## AGENTS.md
Small automatically loaded runtime kernel only:
- full-goal continuation;
- no "ask user to continue";
- project files over chat memory;
- JIT retrieval;
- autonomous reversible technical choices;
- strict user gate;
- inspect-before-edit;
- verification-before-completion;
- task != goal;
- resume from repository/bootstrap state.

No detailed project content.

## PROJECT_CORE.md
Concise global orientation:
- identity;
- audience;
- intended experience/outcome;
- major direction;
- non-negotiables;
- scope boundaries;
- authority note.

## PROJECT_INDEX.yaml
Canonical discoverability/retrieval routing metadata:
- `bootstrap.must_read` authorities for fresh-agent orientation before first source edit;
- domain `authority_ids`;
- `read_when`;
- sections;
- dependencies;
- optional precision;
- optional forbidden authority use.

Every active normative artifact must be reachable through this router (Blueprint calls may extend a routed Blueprint graph). No duplicated content summaries.

## GOAL.md
Master outcome:
- observable success;
- in/out scope;
- stable acceptance IDs;
- verification;
- completion condition.

## STATE.json
Minimal runtime pointer/session state:
- goal_ref;
- current_requirement;
- current_task;
- verified;
- in_progress;
- blocked;
- relevant_implementation;
- `context.required_source_ids`;
- `context.loaded_source_ids`;
- context/session identifier + load-gate status;
- next_action;
- last_verification.

Loaded-source state is ephemeral session evidence. No project canon.

## DESIGN.md when applicable
Make design buildable, not inspirational prose:
- design goals/principles;
- information architecture;
- screen/page/menu inventory;
- flows/navigation;
- layout/hierarchy;
- components/states;
- interaction/feedback/motion;
- visual direction;
- typography/color/iconography guidance;
- accessibility/input/responsiveness;
- reference-derived decisions;
- asset dependencies;
- validation.

For interactive applications, include the relevant shell/navigation surfaces, selection/configuration screens, active-workflow status, result/settings flows, focus/input behavior and transitions.

## ASSET_BLUEPRINT.md when applicable
Specify:
- asset inventory/groups;
- source/generate/create/buy/placeholder strategy;
- style/quality;
- technical specs;
- licensing/attribution;
- naming/path/import rules;
- replacement strategy;
- validation.

## ARCHITECTURE.md when applicable
Define:
- system boundaries;
- modules/components;
- data ownership/flow;
- interfaces/contracts;
- extensibility;
- platform constraints;
- persistence/network/runtime considerations;
- implementation freedoms vs hard constraints.

## CONTENT_BLUEPRINT.md when applicable
Define reusable content models, templates/schemas, authoring rules, progression/catalog structure, and expansion workflow.

## REFERENCE_MAP.md when applicable
Translate external references into explicit adopted traits, deviations, and destinations. Do not leave "like X" unresolved.

## Domain/System Specs
Each coherent system spec should include:
- purpose;
- user-visible behavior;
- states/rules and decision ownership;
- inputs/outputs and producer/consumer relationships;
- state/data ownership and allowed mutation paths;
- dependencies;
- edge cases;
- data/config needs;
- relevant design/assets;
- validation;
- future extension constraints.

## Prompts
START/CONTINUE/GOAL are context-rich generated orientation snapshots. START directly hydrates the product model with mission, vision, material Q/A/rationale, systems/compositions, guardrails, flows, acceptance and state before JIT file traversal. CONTINUE rehydrates product + current requirement + relevant owner/runtime path. GOAL directly states the master outcome, non-negotiables, current verified state, remaining requirements and completion condition; document inspection is never substituted for the goal.

Use `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md` for canonical prompt policy and `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` for reconstruction acceptance.

## Final coverage gate
Before delivery verify:
- all material user input and Q/A provenance is represented;
- `INTERVIEW_COVERAGE` passes or the package is explicitly partial;
- `CONTEXT_HANDOFF` can onboard a fresh agent without chat;
- `DECISION_COMPENDIUM` provides a coherent middle-layer product model without replacing exact authorities;
- explicit negative requirements and example semantics are preserved where material;
- Fresh-Agent Reconstruction passes before task decomposition/final delivery, including correct first-prompt orientation;
- every active normative authority/required Blueprint is registered, routed and reachable from bootstrap/JIT discovery; `AUTHORITY_REACHABILITY` passes with zero unreachable nodes;
- reference implications are compiled;
- master systems/compositions are explicit where reuse matters, with deterministic modifier/replacement semantics and base-propagation expectations;
- material cross-system rule/state ownership is singular and runtime-traceable;
- design/asset/architecture/content blueprints exist where needed;
- future requirements that constrain today's design are preserved;
- no important fact exists only in chat;
- no information is duplicated unnecessarily.

If coverage is incomplete, continue compiling before delivery.

---

# Execution and Verification Contracts

For nontrivial goals, `ACCEPTANCE_MATRIX.yaml` is the machine-readable bridge between `GOAL.md`, authoritative project sources, implementation work, and evidence.

For nontrivial cross-system behavior, use `contracts/SYSTEM_INTEGRATION.yaml` to record material rule/state ownership and runtime traces.

For interactive/stateful products, use the conditional contracts defined in `DELIVERY_AND_VERIFICATION_GUIDE.md`:
- `contracts/APP_FLOW.yaml`
- `contracts/INPUT_ACTIONS.yaml`
- `contracts/CONTENT_REGISTRY.yaml`
- `verification/E2E_SCENARIOS.yaml`

`STATE.json` is not the authority for whether an acceptance criterion is truly verified. It may point to current work, but verification state belongs in the acceptance/evidence contract.

A completion audit must reread the acceptance contract and run the release-gating scenarios. A successful compile/build or subsystem test cannot substitute for stronger required runtime/visual evidence.

---

# Routing, identity, and semantic ownership are different layers

Do not use the word "owner" as if all ownership were the same:

- `PROJECT_INDEX.yaml` — **canonical discoverability/retrieval routing**: bootstrap must-reads plus what authority to read for each domain/task. It must route every active normative authority.
- `PROJECT_REGISTRY.yaml` — **artifact identity/path ownership**: which durable artifact ID maps to which responsibility/path. Registry `owner` metadata is maintenance/domain metadata, not domain-rule authority.
- `blueprints/REGISTRY.yaml` — **behavior-graph identity**: which active Blueprint owns a bounded Blueprint responsibility and which Blueprints it calls.
- `contracts/SYSTEM_MAP.yaml` — **top-level system topology/responsibility scope**: which canonical master system covers a durable domain.
- `contracts/CAPABILITY_GRAPH.yaml` — **reusable semantic hierarchy** below/among master systems: which lower-level capability must exist before consumers compose it.
- `contracts/SYSTEM_INTEGRATION.yaml` — **semantic runtime authority**: per-rule decision owner, mutable-state owner, allowed writers, producers/consumers, side-effect ownership and material runtime edges.

A single project concept may be referenced by several layers, but its detailed truth must have one canonical owner at the correct layer. Do not maintain competing ownership matrices in registries, system specs, and integration contracts.

Cross-references should prefer stable artifact/System/Blueprint IDs and resolve paths through the registries.

# Repository Maintenance Gate

Before adding a durable artifact or behavior path, inspect registries, `SYSTEM_MAP`, `CAPABILITY_GRAPH`/`SYSTEM_INTEGRATION` when present, and the relevant runtime path. Classify the requested delta before source edits: data/modifier, composition, capability extension/new capability, adapter/surface, or core-rule change. Prefer reuse/extend/correct/intentional replace over a parallel implementation.

After create/move/rename/delete operations, update registries/references and run contract validation before considering structural work complete.

At session start/context loss, identify repository root, inspect Git state/relevant diffs, and preserve unrelated changes.


---

# Hierarchical Local Instructions

Root `AGENTS.md` is the always-active repository kernel.

Nested `AGENTS.md` files are optional subtree refinements and must not become a second project knowledge system.

When work targets a path below the repository root:
1. determine target path(s);
2. resolve registered instruction scopes from `PROJECT_REGISTRY.yaml`;
3. inspect the path to each target for applicable local `AGENTS.md` / `AGENTS.override.md`;
4. read only newly applicable instructions;
5. apply them together with root rules;
6. do not preload unrelated subtree instructions.

Use `HIERARCHICAL_INSTRUCTIONS_GUIDE.md` when deciding whether local instruction files should exist.


---

# User-Surface Reality Gate

For user-facing criteria, implementation state and runtime/user-surface state are separate evidence layers.

After an observable change, perform the smallest runnable user-surface check when practical.

Before master-goal completion, perform a fresh full black-box verification on the current final build/worktree.

Use `USER_SURFACE_VERIFICATION_GUIDE.md` for:
- surface-specific verification;
- interactive runtime checks;
- visual checkpoints;
- screenshot evidence budgeting;
- final black-box release gates.

Do not infer visual/layout/navigation correctness from code inspection, build success, or headless subsystem tests.


---

# Phase-Based Execution

For autonomous coding projects, use `EXECUTION_RUNTIME_GUIDE.md`.

Do not treat implementation as one continuous undifferentiated loop.

The agent should move through explicit gates:
repository bootstrap → capability discovery/runtime binding → authority-reachability check → requirement selection → required-authority resolution/load gate → core-first change classification → requirement-scoped skill routing → Blueprint/reuse →
unit implementation → unit verification → integration → system-integration audit when applicable → user-surface verification →
scoped hygiene → milestone → final contract/build/surface/Git gates.

For user-facing products, final completion depends on actual user-surface evidence,
not on the agent's confidence that code appears correct.

---


# Agent Runtime Portability Layer

When `contracts/AGENT_RUNTIME_PROFILE.yaml` is present, treat it as the provider/harness binding layer, never as project truth.

It records actual support for instruction files, Agent Skills, lifecycle hooks, subagents, MCP/external tools, memory, workflows/commands, worktrees/sandboxes, and chosen semantic bindings. Use `AGENT_RUNTIME_PORTABILITY_GUIDE.md` for primitive selection.

Prefer one canonical instruction kernel and thin generated provider adapters. Product behavior must remain in normal authorities. Provider memory, skills, hooks, workflows and session transcripts cannot become required hidden project state.

When blocking lifecycle hooks are available, bind deterministic completion/integration/policy validators to the appropriate semantic lifecycle events. If hooks are unavailable, execute the same validators explicitly in the phase machine.

Keep `AGENT_RUNTIME_PROFILE.yaml` separate from `verification/TOOL_CAPABILITIES.yaml`: the former describes agent-loop/customization mechanisms; the latter describes real user-surface verification tools.

---

# Skill Routing Layer

When `contracts/SKILL_REQUIREMENTS.yaml` is present, treat it as a capability-resolution router, not project knowledge.

After selecting the current requirement and loading its required project authorities:

```text
current requirement
→ relevant SYSTEM_MAP system IDs
→ matching SKILL_REQUIREMENTS entries
→ inspect available global/project/harness skills
→ load minimum resolved skills JIT
→ execute
```

Repository-local skills belong under `.agents/skills/` when the agent ecosystem supports that shared path and the workflow is genuinely repeated/project-specific.

Do not add every possible project skill at compilation time. Planned workflows may remain unresolved/planned until their first real authoring task makes the procedure concrete.

No skill may override canonical user vision, System Map ownership, design/behavior/content authorities, acceptance criteria, or evidence requirements.


---

# Interview State and Context Handoff

For nontrivial compiled projects, durable context has four distinct roles:

- `docs/USER_VISION.md` — selected high-signal verbatim intent anchors;
- `docs/INTERVIEW_LEDGER.md` — complete material question/answer provenance;
- `docs/DECISION_COMPENDIUM.md` — readable normalized product model, rationale, examples and rejected alternatives;
- `CONTEXT_HANDOFF.md` — rich onboarding/history/rationale for a new agent/session.

`contracts/INTERVIEW_COVERAGE.yaml` is the compiler stop-condition ledger for relevant systems/domains. Do not treat compilation as complete while material user-owned fields remain unresolved unless the package is explicitly marked partial.

A new implementation agent or major context-loss recovery should read the `PROJECT_INDEX.yaml`-routed handoff and decision/product-model authorities (typically `CONTEXT_HANDOFF.md` + `DECISION_COMPENDIUM.md`) and rehydrate the architecture law plus system/capability authorities (typically `SYSTEM_MAP`/`CAPABILITY_GRAPH`) once for holistic orientation, then use normal JIT routing for exact authorities. Bound project-native equivalents must preserve the same orientation and decision context. Do not repeatedly preload the full interview ledger. Before first implementation, the compiled package must satisfy the Fresh-Agent Reconstruction contract; use `FRESH_AGENT_RECONSTRUCTION_GUIDE.md`.

# Project-native executable gate and visual-reference load evidence

For nontrivial projects with structured authorities, the output package includes an actual executable project gate such as:

```text
tools/project_gate.py
# or an equivalent project-native script when Python is not the available runtime
```

This tool is `normative: false`. It validates existing authorities; it does not become project truth.

The generated `AGENTS.md`, START and CONTINUE flows route through it:

```text
fresh/resumed/compacted context
→ load root operating kernel
→ if bound Core-First Governance capability exists, load/apply it fresh
→ run project gate preflight
→ PROJECT_INDEX exact authority/reference routing
→ read/inspect required inputs
→ material edit
```

If the external Governance capability is absent, continue through the project-native gate + project authorities. Do not block merely because an optional plugin is missing, and do not claim it was loaded when it was not.

For visual/design work extend ephemeral context state, where useful, with:

```yaml
context:
  required_source_ids: []
  loaded_source_ids: []
  required_reference_ids: []
  inspected_reference_ids: []
  inspected_view_ids: []
```

A visual reference that exists on disk but is not registered/routed/inspected is not consumed context. `required_reference_ids` are resolved through the same Registry/Index discipline as other project inputs while remaining correctly typed as reference assets, not prose authorities.

The gate should provide modes equivalent to:
- `validate` — full structural/reference/reachability checks;
- `preflight` — validate + report current admission and exact required inputs before material work;
- `self-test` — prove known-bad mutants fail;
- `handoff`/`completion` — require applicable freshness/reconciliation evidence before claiming a clean handoff.

Exact command names may vary with the project's runtime. The semantics may not.


# v2.24 Current-state and product-realization routing

For implementation projects, routing must preserve both:
- **local precision** for the current admitted work; and
- **global realization continuity** so the agent knows what product work remains after the current milestone.

`STATE` owns the current execution/admission pointer only. Plan/Acceptance remain separate authorities. Generated status/orientation views must reconcile to them.

For design-heavy products, the compact bootstrap/continuation context carries the applicable visual-target capsule even before detailed design authorities are loaded JIT. Exact surface edits still require actual inspection of the routed visual authorities.
