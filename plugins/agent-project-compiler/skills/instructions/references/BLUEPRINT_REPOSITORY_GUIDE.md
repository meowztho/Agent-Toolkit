# Blueprint Graph, Repository Integrity, and Version Control Guide

# Current Precedence — Blueprint↔Code Modular Boundaries, Repository Anchors and Reverse Navigation

Repository discovery should compare intended ownership/contracts with derived implementation topology from filesystem/Git/AST/tests where practical. Stable implementation anchors/breadcrumb IDs connect authorities to code without duplicating rules.

Debug route: `failing evidence/user flow → runtime/data trace → consumer/module/provider → capability contract → Responsibility Owner → implementation anchor → root-cause fix → forward re-test`. Search broadly only when canonical routing/anchors are absent, stale, ambiguous or contradicted.

---


## Purpose

Large prose specifications are useful for intent but weak as an execution map.

A Project Blueprint is a small, addressable, machine-readable behavior graph inspired by node-based visual scripting. It represents one bounded responsibility as:
- stable identity;
- inputs/outputs;
- state/data;
- nodes;
- edges/transitions;
- calls to other blueprints;
- invariants;
- implementation references;
- acceptance/evidence links.

Project Blueprints are not Unreal `.uasset` Blueprints and do not require Unreal Engine. They are portable execution contracts for any project type.

## 1. Blueprint Decomposition

Prefer one blueprint per bounded responsibility.

Good boundaries:
- one screen or interactive state;
- one user flow/subflow;
- one stateful domain behavior;
- one reusable subsystem behavior;
- one integration;
- one automation/job;
- one content-authoring workflow;
- one lifecycle with a clear owner.

Do not place the entire application in one blueprint, create a blueprint for every trivial function, or split only because a file is long.

Split when a responsibility has its own state, lifecycle, reuse boundary, owner, or change cadence.

Example:

```text
BP-FLOW-LOCAL-MATCH
  calls:
    BP-UI-SESSION-SETUP
    BP-UI-ITEM-SELECT
    BP-UI-STAGE-SELECT
    BP-UI-MATCH-RULES
    BP-MATCH-LIFECYCLE
    BP-UI-RESULTS
```

Each called blueprint owns its own bounded behavior.

## 2. Blueprint Types

Common types:
- `flow`
- `screen`
- `system`
- `state_machine`
- `entity_behavior`
- `data_pipeline`
- `integration`
- `automation`
- `content_workflow`

The type helps routing; it does not change the core graph format.

## 3. Blueprint File Format

Recommended extension: `*.bp.yaml`.

```yaml
blueprint:
  id: BP-UI-MAIN-MENU
  responsibility_key: UI.SCREEN.MAIN_MENU
  type: screen
  version: 1
  authority_ids:
    - DOC-UI-DESIGN
  implementation_ids:
    - IMPL-UI-MAIN-MENU

interface:
  inputs:
    - session_state
  outputs:
    - navigation_request

state:
  owned:
    - focused_action
  reads:
    - APP-SESSION
  writes: []

nodes:
  N001:
    type: event
    op: on_enter

  N010:
    type: action
    op: render_registered_actions

  N020:
    type: decision
    op: selected_action

  N030:
    type: call
    blueprint: BP-FLOW-LOCAL-MATCH
    entry: begin_setup

edges:
  - from: N001
    to: N010
  - from: N010
    to: N020
  - from: N020
    when: start_local_match
    to: N030

invariants:
  - global_navigation_is_not_owned_by_screen
  - all_visible_actions_exist_in_app_flow_contract

acceptance:
  - AC-15
```

Use stable node IDs so edits can refer to a specific part of the graph.

## 4. Blueprint Calls Instead of Duplication

A behavior that already has a canonical blueprint must be called/referenced, not copied.

Bad:
- Main shell contains its own second copy of session-setup logic.
- Results contains another copy of entity selection.

Good:
- MainMenu calls `BP-FLOW-PRIMARY-JOURNEY`.
- Results calls `BP-UI-ITEM-SELECT`.

A `call` node references a stable Blueprint ID, not a raw filesystem path.

## 5. Blueprint Registry

Generate `blueprints/REGISTRY.yaml`.

```yaml
blueprints:
  BP-UI-MAIN-MENU:
    responsibility_key: UI.SCREEN.MAIN_MENU
    type: screen
    artifact_id: BPFILE-UI-MAIN-MENU
    status: active
    owner: UI
    calls:
      - BP-FLOW-LOCAL-MATCH

  BP-UI-ITEM-SELECT:
    responsibility_key: UI.SCREEN.CHARACTER_SELECT
    type: screen
    artifact_id: BPFILE-UI-ITEM-SELECT
    status: active
    owner: UI
```

Rules:
- active Blueprint IDs are unique;
- active `responsibility_key` values are unique;
- exactly one active blueprint owns one responsibility;
- replacements use `supersedes`;
- obsolete blueprints become `deprecated` or are removed after references migrate;
- do not keep two active blueprints "just in case".

## 6. Project Artifact Registry

Generate `PROJECT_REGISTRY.yaml`.

This is the single canonical path/identity map for durable project artifacts.

```yaml
artifacts:
  DOC-UI-DESIGN:
    kind: document
    path: docs/design/UI_DESIGN.md
    responsibility_key: DOC.UI.DESIGN
    status: active
    normative: true
    discoverability_required: true

  BPFILE-UI-MAIN-MENU:
    kind: blueprint
    path: blueprints/ui/BP_UI_MainMenu.bp.yaml
    responsibility_key: FILE.BLUEPRINT.UI.MAIN_MENU
    status: active
    normative: true
    discoverability_required: true

  IMPL-UI-MAIN-MENU:
    kind: implementation
    path: src/ui/MainMenu.cs
    responsibility_key: IMPL.UI.MAIN_MENU
    status: active
    normative: false
    discoverability_required: false
```

Stable artifact IDs survive path changes.

**Ownership namespace note:** artifact/Blueprint `responsibility_key` uniqueness prevents duplicate durable artifacts/behavior graphs. It does not replace `SYSTEM_MAP` responsibility scope, `CAPABILITY_GRAPH` reusable semantic hierarchy, or `SYSTEM_INTEGRATION` decision/state ownership. Registry `owner` fields are organizational/maintenance metadata unless a project explicitly defines otherwise.

References in `PROJECT_INDEX.yaml`, `ACCEPTANCE_MATRIX.yaml`, `STATE.json`, Blueprint files, and other machine contracts should use artifact IDs/Blueprint IDs where practical instead of duplicating raw paths.

### Discoverability invariant

Registration is necessary but not sufficient. Every active normative/discoverability-required artifact must have an incoming route from `PROJECT_INDEX.bootstrap.must_read` or a `PROJECT_INDEX.domains.*.authority_ids` entry. Active Blueprints may additionally be reachable through registered `call` edges from a routed Blueprint.

Generated prompts, Atlas views, evidence binaries, caches, support artifacts and ordinary source-code implementation entries should be explicitly marked non-normative so they neither fail nor falsely satisfy authority coverage. A non-normative artifact may still be `discoverability_required: true` (notably the Project Atlas and its generator) without becoming an authority. When reachability validation is enabled, make `normative` explicit rather than relying on kind-based guesses.

A project validator must compute this graph and fail on unreachable normative artifacts/Blueprints. Do not rely on "the file is in the folder" or prose-only chains between documents.

## 7. Duplicate Creation Gate

Before creating any durable artifact, screen, service, menu, flow, registry entry, or implementation owner:

1. derive its intended `responsibility_key`;
2. inspect `PROJECT_REGISTRY.yaml`;
3. inspect `blueprints/REGISTRY.yaml` when behavior is involved;
4. inspect applicable `SYSTEM_MAP` / `CAPABILITY_GRAPH` / `SYSTEM_INTEGRATION` / `ARCHITECTURE_GUARDRAILS` constraints;
5. search the relevant repository area for equivalent behavior/ownership;
6. inspect call sites and navigation/state ownership;
7. decide whether to reuse, extend, correct, rename/move, supersede, or create.

Creation is the last option.

If an active artifact already owns the same responsibility, do not create another implementation unless the requirement explicitly demands parallel variants.

## 8. Rename / Move / Delete Transaction

For any rename, move, replacement, or deletion:

1. update `PROJECT_REGISTRY.yaml`;
2. preserve the stable artifact ID when identity did not change;
3. update Blueprint Registry when applicable;
4. update all ID references if identity changes;
5. update unavoidable direct path references;
6. update generated-source declarations;
7. update tests/config/build/import references;
8. update `PROJECT_INDEX.yaml` routes if discoverability changed;
9. run registry/reference/reachability validation;
10. run the narrowest affected runtime/build tests;
11. only then consider the operation complete.

Do not leave compatibility copies unless an explicit migration window requires them.

## 9. Generated Sources and Ownership

Registry entries should declare generated/transformed artifacts and their durable producer relationship:

```yaml
generated:
  source_artifact_ids: [SOURCE-EXAMPLE]
  recipe_artifact_ids: []
  generator_artifact_id: TOOL-GENERATE-EXAMPLE
  edit_policy: generated_only
  regeneration_required_after_source_change: true
```

Canonical relationship:

```text
source / recipe / authority
→ generator / transformation / provider
→ generated artifact
→ consumer
```

A generated artifact is normally not the canonical edit owner. For a durable change, modify the authoritative source/recipe/generator, regenerate, then verify affected consumers. Direct output edits are valid only when project policy explicitly makes that output hand-maintained or as disposable diagnosis that is not promoted to canonical work.

This rule is cross-domain: generated code, documents, assets, indexes, bindings, reports, transformed datasets and compiled outputs follow the same ownership reasoning.

A responsibility should have one clear authority and one implementation owner.

## 10. PROJECT_INDEX by ID

Prefer:

```yaml
domains:
  ui_navigation:
    authority_ids:
      - DOC-UI-DESIGN
      - BP-FLOW-LOCAL-MATCH
      - CONTRACT-APP-FLOW
```

over repeated paths.

Resolve IDs through `PROJECT_REGISTRY.yaml` / Blueprint Registry when working.

## 11. Contract Validation Tool

For projects using these registries, generate a small deterministic validator when practical, for example `tools/validate_project_contracts.py`.

It should check applicable invariants:
- duplicate artifact IDs;
- active normative artifact reachability from `PROJECT_INDEX` bootstrap/domain routes;
- active normative Blueprint reachability from direct routes or routed Blueprint-call graphs;
- unresolved route IDs and deprecated active route targets;
- duplicate active responsibility keys;
- duplicate active Blueprint ownership;
- registry paths exist;
- referenced artifact IDs exist;
- Blueprint calls resolve;
- APP_FLOW transition targets resolve;
- Blueprint IDs referenced by APP_FLOW exist;
- Acceptance IDs referenced by blueprints/contracts exist;
- generated artifacts declare their source;
- deprecated artifacts are not used by active routes.

Run it after structural changes, before milestone verification, and before final completion. Emit/update `verification/AUTHORITY_REACHABILITY.yaml` as generated evidence; do not treat that report as a second router.

The validator supplements implementation tests; it does not replace runtime evidence.

## 12. Version Control Policy

Generate `contracts/VERSION_CONTROL.yaml` for autonomous coding projects. The canonical file shape lives in `RUNTIME_TEMPLATES.md`; this guide owns the policy semantics:
- Git is the default recoverability layer for coding projects unless explicitly forbidden;
- initialize it when absent only after creating an appropriate `.gitignore`;
- preserve unrelated changes and avoid destructive cleanup;
- record revision/worktree identity for verification where practical;
- use verified milestone commits automatically only where project policy permits, especially in agent-owned greenfield repositories;
- final release gates must correspond to the current intended worktree/revision.

Adapt these semantics to explicit user/repository policy rather than maintaining a second YAML template here.

## 13. Session Git Protocol

At session start, after context loss, or working-directory change:

1. identify repository root;
2. read applicable instructions;
3. inspect branch and HEAD;
4. inspect `git status`;
5. inspect relevant diff(s);
6. record baseline dirty paths if useful;
7. do not reset, clean, discard, or overwrite unrelated changes;
8. reconstruct only context needed for the active requirement.

Before a broad/high-risk change, ensure work is recoverable.

For agent-owned greenfield repositories, verified milestone commits are a good default.

For existing/shared repositories, do not auto-commit unless project policy permits it.

## 14. Verification Revision Binding

Evidence should record the revision/worktree it verified when practical.

```yaml
evidence:
  - type: e2e_scenario
    scenario: primary_flow
    revision: "git:abc1234"
```

If dependent implementation changes after verification, affected criteria may require recheck.

Final release-gating scenarios must run against the current final worktree/revision.

## 15. Independent Review

For consequential, high-risk, difficult-to-verify, or materially blocked coding work, use an `independent-review` skill when available.

Keep the detailed review workflow inside the skill rather than permanently expanding `AGENTS.md`.

If the environment already provides an equivalent skill, reference it instead of creating a duplicate. Otherwise a self-contained repository may provide `.agents/skills/independent-review/SKILL.md`.

The reviewer:
- is read-only;
- receives original requirements/instructions/raw implementation evidence;
- does not receive the implementation agent's conclusions or confidence;
- derives expected behavior independently;
- reports only material evidence-based findings.

Review supplements, never replaces, the primary agent's own investigation and verification.


---

# 15A. Runtime Ownership / Integration Gate

Registry/file ownership is necessary but not sufficient. When `contracts/CAPABILITY_GRAPH.yaml` / `SYSTEM_INTEGRATION.yaml` are present, structural work must also preserve reusable capability depth, semantic ownership and runtime paths.

Before adding/changing an implementation owner:
1. resolve the system/rule/state owner;
2. inspect existing producers/consumers and call/data paths;
3. prefer reuse/extend/correct/intentional replacement;
4. reject a second path that independently decides the same rule or writes the same canonical state;
5. update integration traces when public runtime relationships change;
6. audit dead config/contracts and bypasses after cross-system changes.

Do not declare a repository "modular" from folders/classes alone. Compare implementation responsibilities against System Map/Integration ownership and the actual runtime graph.

---

# 16. Behavior Blueprints vs Implementation Blueprints

Use separate Blueprint layers when the project is nontrivial.

## Behavior Blueprint

Describes WHAT a bounded system/flow should do.

Examples:
- `BP-FLOW-PRIMARY-JOURNEY`
- `BP-UI-ITEM-SELECT`
- `BP-SYS-RECOVERY`

## Implementation Blueprint

Describes HOW one bounded code unit fulfills one or more behavior/data contracts without duplicating source code.

Recommended suffix:

```text
*.impl.bp.yaml
```

Examples:
- `BP-IMPL-APP-ROUTER`
- `BP-IMPL-ITEM-SELECT-CONTROLLER`
- `BP-IMPL-MATCH-STATE-MACHINE`

Recommended shape:

```yaml
blueprint:
  id: BP-IMPL-APP-ROUTER
  responsibility_key: IMPL.NAVIGATION.APP_ROUTER
  type: implementation_class
  version: 1
  implements:
    - BP-FLOW-LOCAL-MATCH
  artifact_id: IMPL-APP-ROUTER

interface:
  public_operations:
    - navigate
    - back
  inputs:
    - navigation_request
  outputs:
    - active_screen_changed

state:
  owns:
    - active_screen_id
    - navigation_history
  must_not_own:
    - entity_catalog
    - match_rules

dependencies:
  reads:
    - CONTRACT-APP-FLOW
  calls:
    - BP-IMPL-SCREEN-FACTORY

operations:
  navigate:
    preconditions:
      - target_screen_registered
    postconditions:
      - exactly_one_active_screen
    failure_behavior:
      - reject_unknown_screen

invariants:
  - one_navigation_owner
  - no_screen_local_global_router_copy

verification:
  unit:
    - TEST-APP-ROUTER-NAVIGATE
    - TEST-APP-ROUTER-BACK
  integration:
    - E2E-NAVIGATION-SMOKE
  debug_probes:
    - active_screen_id
```

The Blueprint should be concise enough that an agent can reason about/test the unit
without loading the full application.

---

# 17. Data Blueprints

Create a separate Data Blueprint for a shared/stateful/invariant-rich data responsibility.

Recommended suffix:

```text
*.data.bp.yaml
```

Examples:
- input action registry;
- entity catalog;
- route registry;
- session state;
- rules configuration;
- persistence schema;
- job queue;
- shared collection with ordering/uniqueness/lifecycle rules.

Do NOT Blueprint incidental local arrays/lists that have no independent contract.

Example:

```yaml
blueprint:
  id: BP-DATA-INPUT-ACTIONS
  responsibility_key: DATA.INPUT.ACTION_REGISTRY
  type: data_registry
  artifact_id: DATA-INPUT-ACTIONS

schema:
  key: action_id
  fields:
    - label
    - contexts
    - remappable
    - default_bindings

collection_invariants:
  - action_id_unique
  - every_required_action_has_display_label
  - every_required_gameplay_action_has_supported_default_or_explicit_unbound_policy

operations:
  - register
  - lookup
  - rebind
  - serialize
  - restore_defaults

verification:
  - TEST-INPUT-ACTION-UNIQUENESS
  - TEST-INPUT-ACTION-ROUNDTRIP
```

---

# 18. Code Topology Rule

For substantial autonomous coding projects, the Blueprint registry should make code topology explicit.

Prefer separate implementation/data Blueprints for:
- nontrivial classes;
- modules/services/components;
- stateful controllers;
- shared registries/stores;
- important schemas/data structures;
- integration adapters;
- complex algorithms with independent invariants.

Do not create one huge "CODE.bp.yaml".

Do not create one Blueprint per tiny method/local collection.

Each Blueprint should have:
- one responsibility;
- stable ID;
- implementation artifact link;
- dependencies;
- invariants;
- verification hooks;
- debug probes when useful.

Behavior Blueprints may call/reference implementation Blueprints, but behavior intent remains independent from a specific code organization where appropriate.

---

# 19. Blueprint-to-Test Mapping

Every active implementation/data Blueprint should declare how its own contract can be checked.

The project contract validator should flag a nontrivial active implementation Blueprint
with no verification mapping unless explicitly marked:

```yaml
verification:
  policy: integration_only
  reason: "[why isolated verification is not meaningful]"
```

This encourages classes/data units to be independently testable without forcing artificial
unit tests for trivial glue.

---

# 20. Blueprint Drift Gate

When source changes materially affect:
- public interface;
- owned state;
- invariants;
- dependencies;
- lifecycle;
- data schema;
- responsibility;

update the corresponding Blueprint in the same work unit.

When source implementation changes without changing its contract, do not churn the Blueprint.

The Blueprint is a durable implementation map, not a line-by-line mirror of code.


---

# 21. Git Initialization and Maintenance

For coding projects, Git is the default recoverability layer.

If no repository exists:
- initialize Git unless explicit user/project policy forbids it;
- create/update `.gitignore` before first staging;
- exclude secrets, credentials, caches, build outputs, temporary screenshots/evidence,
  editor caches, and dependency/vendor artifacts according to project conventions;
- inspect files before the first commit;
- establish a baseline/verified milestone commit for a new agent-owned project when safe.

During work:
- inspect status at session start/context recovery;
- keep unrelated user changes untouched;
- use milestone commits according to policy;
- inspect untracked files during hygiene/finalization;
- do not use destructive reset/clean operations merely to obtain a clean status.

Git state is part of project health, not only a final delivery step.

---

# 22. Vision Anchors and Parent Context References

For design/experience-sensitive behavior Blueprints, reference canonical vision/design authorities instead of copying their prose.

Optional fields:

```yaml
blueprint:
  id: BP-UI-HOME
  authority_ids:
    - DOC-USER-VISION
    - DOC-DESIGN
    - CONTRACT-VISUAL
  vision_anchor_ids:
    - VQ-001
    - VQ-004
  parent_context_ids:
    - VISUAL-SHELL-PRIMARY
```

Rules:
- `vision_anchor_ids` point to active anchors in `docs/USER_VISION.md`.
- `parent_context_ids` identify the bounded screen/shell/flow context needed to prevent local implementation drift.
- Do not paste user quotes into every Blueprint.
- A local Blueprint may remain implementation-focused while the JIT router loads the referenced Gestalt Context Envelope.
- If a vision anchor is superseded/rejected, validator/routing should flag active Blueprint references to it.

For projects using `contracts/VISUAL_DESIGN_CONTRACT.yaml`, extend deterministic validation where practical to check:
- referenced vision anchor IDs exist and are active;
- approved reference/artifact IDs resolve;
- visual-contract screen IDs referenced by acceptance/checkpoints exist;
- screen-level visual criteria are not marked verified without required non-stale evidence.


# 18. Blueprint ↔ Code Modular Boundary

The useful architectural lesson from visual Blueprint systems is **not** that every behavior needs a graph or one source file. It is that a bounded responsibility should expose a clean contract and remain internally modular.

For every material System/Capability/Behavior Blueprint that reaches implementation maturity, establish an implementation boundary:

```text
Responsibility / Capability
→ Behavior/System Blueprint
→ public contract/interface
→ cohesive implementation boundary
→ internal files/classes/functions
```

The implementation boundary may be:
- a module/package;
- service/component;
- state machine/controller;
- cohesive group of source files behind one public facade/contract;
- engine-native subsystem/resource/component;
- another project-appropriate unit.

Do **not** require `1 Blueprint = 1 source file/class`. Internal decomposition is a delegated technical decision unless architecture semantics require otherwise.

## Boundary rules

A good boundary has:
- one durable semantic owner;
- declared public operations/events/data contracts;
- explicit owned state and forbidden foreign state;
- explicit allowed dependencies/calls;
- internal implementation details hidden from unrelated consumers;
- stable implementation anchors;
- acceptance/evidence that exercises the public behavior.

Consumers should compose/call the public boundary rather than reach into internal helpers or duplicate the behavior locally.

Bad:

```text
System A consumer
→ imports System B internal store/helper
→ mutates B state directly
```

Good:

```text
System A consumer
→ B public command/interface
→ B canonical owner
→ B internal implementation
```

## Blueprint/code conformance

A project must not become "modular on paper, monolithic in code".

When practical, the project gate/repository audit should compare Blueprint responsibilities against implementation topology:

- every implemented active Blueprint has at least one registered implementation anchor;
- no two active implementation boundaries claim the same durable responsibility;
- one implementation boundary does not silently own unrelated System responsibilities without an explicit architecture decision;
- declared public calls/dependencies resolve to the canonical target boundary;
- consumers do not bypass a public boundary through known internal implementation anchors;
- deprecated/replaced implementation boundaries are no longer active consumers;
- runtime traces reach the implementation boundary named by the authority.

Static checking may use imports/dependency graphs/AST/module manifests where reliable. Runtime tracing or tests may be needed for dynamic systems. If conformance cannot be proven automatically, report `INCONCLUSIVE` rather than pretending filenames prove architecture.

## Composition principle

Prefer systems as reusable "building blocks":

```text
Product flow / Consumer
  composes
    Capability A
    Capability B
    Capability C
```

Each capability/system keeps its own owner and contract. Composition coordinates them; it does not merge their domain rules into the consumer.

This is the portable equivalent of clean visual Blueprint composition and remains equally valid when the actual implementation is ordinary code.
