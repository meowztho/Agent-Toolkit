# APC v2.35 JIT Slice — Registries, Blueprints and Version-Control Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## PROJECT_REGISTRY.yaml Template

```yaml
schema_version: 1

artifacts:
  DOC-PROJECT-CORE:
    kind: document
    path: PROJECT_CORE.md
    responsibility_key: DOC.PROJECT.CORE
    status: active
    owner: project
    normative: true
    discoverability_required: true

  CONTRACT-ACCEPTANCE-MATRIX:
    kind: contract
    path: ACCEPTANCE_MATRIX.yaml
    responsibility_key: CONTRACT.ACCEPTANCE.MATRIX
    status: active
    owner: project
    normative: true
    discoverability_required: true

  CONTRACT-APP-FLOW:
    kind: contract
    path: contracts/APP_FLOW.yaml
    responsibility_key: CONTRACT.APP_FLOW
    status: active
    owner: application
    normative: true
    discoverability_required: true

  VERIFICATION-AUTHORITY-REACHABILITY:
    kind: verification_report
    path: verification/AUTHORITY_REACHABILITY.yaml
    responsibility_key: VERIFICATION.AUTHORITY.REACHABILITY
    status: active
    owner: project
    normative: false
    discoverability_required: false
    generated:
      source_artifact_ids: [PROJECT-INDEX, PROJECT-REGISTRY, BP-REGISTRY]
      generator_artifact_id: TOOL-VALIDATE-PROJECT-CONTRACTS
      edit_policy: generated_only

  TOOL-GENERATE-PROJECT-ATLAS:
    kind: generator_tool
    path: tools/generate_project_atlas.py
    responsibility_key: TOOL.GENERATE.PROJECT.ATLAS
    status: active
    owner: project
    normative: false
    discoverability_required: true

  VIEW-PROJECT-ATLAS:
    kind: generated_view
    path: PROJECT_ATLAS.html
    responsibility_key: VIEW.PROJECT.ATLAS
    status: active
    owner: project
    normative: false
    discoverability_required: true
    generated:
      source_selector: atlas_v1
      source_artifact_ids: [DOC-PROJECT-CORE, DOC-USER-VISION, DOC-DECISION-COMPENDIUM, CONTRACT-SYSTEM-MAP, CONTRACT-ACCEPTANCE-MATRIX]
      generator_artifact_id: TOOL-GENERATE-PROJECT-ATLAS
      source_fingerprint: null
      generated_at_revision: null
      edit_policy: generated_only

  VERIFICATION-GENERATED-VIEW-FRESHNESS:
    kind: verification_report
    path: verification/GENERATED_VIEW_FRESHNESS.yaml
    responsibility_key: VERIFICATION.GENERATED.VIEW.FRESHNESS
    status: active
    owner: project
    normative: false
    discoverability_required: false
    generated:
      source_artifact_ids: [PROJECT-REGISTRY, VIEW-PROJECT-ATLAS]
      generator_artifact_id: TOOL-VALIDATE-PROJECT-CONTRACTS
      edit_policy: generated_only

# Artifact IDs are stable across path moves.
# Active responsibility_key values are unique.
# Use supersedes/aliases only for deliberate migrations.
# Mark generated/transformed artifacts with canonical source/recipe + generator; durable fixes go upstream, then regenerate and verify consumers.
# Active normative/discoverability_required artifacts must be reachable from PROJECT_INDEX.
# Generated views/prompts/evidence binaries/support files and ordinary implementation entries are normally normative: false.
# `owner` here is artifact maintenance/domain metadata, not rule/state decision authority.
```

---

## blueprints/REGISTRY.yaml Template

```yaml
schema_version: 1

blueprints:
  BP-EXAMPLE:
    responsibility_key: SYSTEM.EXAMPLE
    type: system
    artifact_id: BPFILE-EXAMPLE
    status: active
    owner: example_domain
    calls: []
    supersedes: null

# Exactly one active blueprint owns each Blueprint responsibility_key.
# This does not replace SYSTEM_INTEGRATION rule/state ownership.
```

---

## Reusable Definition Type / Definition composition template

Use when the product has repeatable variants realized by shared runtime/surface consumers.

This is a semantic template, not a required new file. Place it in the existing canonical domain/content/definition/Blueprint authority; do not invent a universal `ARCHETYPES.yaml`/`DEFINITION_TYPES.yaml` unless the project actually needs a dedicated owner.

```yaml
definition_types:
  TYPE-EXAMPLE:
    owner_system_id: SYS-...
    capability_contract_ids: [CAP-...]
    definition_schema_id: DATA-...
    generic_runtime_consumer_id: MOD-...
    generic_surface_consumer_id: MOD-...   # optional
    instance_state_owner_id: SYS-...
    allowed_modifier_ids: [MOD-...]
    authoring_path_id: TRACE-...

definitions:
  DEF-EXAMPLE-A:
    definition_type_id: TYPE-EXAMPLE
    profile_ids: [PROFILE-...]
    capability_ids: [CAP-...]
    modifier_ids: []
    presentation:
      slot_a: ASSET-...
    parameters:
      example_value: 1
```

Acceptance should prove that another materially different `DEF-*` of the same archetype can reach the same generic consumer/runtime without a copied owner or per-instance implementation path.

## Project Blueprint `*.bp.yaml` Template

```yaml
blueprint:
  id: BP-EXAMPLE
  responsibility_key: SYSTEM.EXAMPLE
  type: system
  version: 1
  authority_ids: []
  implementation_ids: []

interface:
  inputs: []
  outputs: []

state:
  owned: []
  reads: []
  writes: []

nodes:
  N001:
    type: event
    op: entry
  N010:
    type: action
    op: example_action
  N999:
    type: exit
    op: success

edges:
  - from: N001
    to: N010
  - from: N010
    to: N999

invariants: []
acceptance: []
```

Use `call` nodes with stable Blueprint IDs for reusable behavior instead of copying graphs.

---

## contracts/VERSION_CONTROL.yaml Template

```yaml
git:
  required: true
  initialize_if_missing: true
  create_gitignore_before_first_stage: true
  inspect_on_session_start: true
  preserve_unrelated_changes: true
  destructive_cleanup_without_user_request: false

commits:
  policy: verified_milestone
  auto_commit_greenfield_agent_owned_repo: true
  auto_commit_existing_or_shared_repo: false

verification:
  record_revision: true
  final_release_gates_must_run_on_current_worktree: true
```

Adapt to explicit user/repository policy.

---

## `.agents/skills/independent-review/SKILL.md` Template

Generate this only when an equivalent applicable skill is not already available.

```markdown
---
name: independent-review
description: Run an unbiased read-only implementation review for consequential, high-risk, difficult-to-verify, or materially blocked coding work. Do not use for routine low-risk changes.
---

# Independent Review

Run a narrowly scoped read-only reviewer only for consequential, high-risk, difficult-to-verify, or materially blocked work.

The reviewer may be an isolated subagent or an available external model through an approved provider. Do not wait for rate-limited providers or duplicate routine investigation. Review supplements, never replaces, the primary agent's own investigation and verification.

To avoid anchoring, give the reviewer:
- the original requirements;
- complete applicable instructions;
- relevant raw diffs and files;
- verification commands and their actual output.

Do not pass:
- the implementation agent's narrative;
- its conclusions;
- its confidence;
- its justification.

The reviewer must independently derive expected behavior from the original requirements and verify material claims directly when necessary and feasible.

Require evidence-based findings that materially affect correctness, stated requirements, regressions, security, or maintainability. Exclude style-only, speculative, and unnecessary-hardening suggestions.

The primary agent must fix each material finding, reject it with evidence, or explicitly accept it, with at most one challenge-response round.

Use a different model for additional review only when a high-risk issue remains unresolved.
```

---

## Contract Validator Requirements

When the generated project uses registries/Blueprint contracts, generate a small deterministic validation tool appropriate to the project's language/tooling.

Validate applicable invariants:
- unique artifact IDs;
- every active artifact with `discoverability_required: true` is reachable from the appropriate `PROJECT_INDEX` bootstrap/domain/view/tool route, regardless of whether it is normative;
- every routed authority/Bootstrap ID resolves;
- every active normative Blueprint is directly routed or reachable through registered `call` edges from a routed Blueprint;
- generated/non-normative artifacts never satisfy normative authority coverage; required generated views/tools are validated through their separate explicit routes;
- zero unreachable normative authorities/required Blueprints; emit `verification/AUTHORITY_REACHABILITY.yaml`;
- unique artifact IDs;
- unique active responsibility keys;
- unique active Blueprint responsibility ownership;
- every implemented active Blueprint resolves to registered implementation anchor(s);
- implementation boundaries do not claim duplicate durable responsibilities;
- known internal implementation artifacts are not used as public cross-system entry points when the Blueprint declares a public boundary;
- registry paths exist;
- artifact references resolve;
- Blueprint `call` targets resolve;
- definitions referencing a reusable Definition Type resolve its owner/capabilities/generic consumer;
- same-type production definitions do not register conflicting active runtime/surface owners;
- modifier definitions target declared seams and do not claim target ownership;
- CAPABILITY_GRAPH parent systems/capabilities/consumers/Acceptance IDs resolve and has no cycles where cycles are forbidden;
- SYSTEM_INTEGRATION referenced systems/artifacts/contracts/Acceptance IDs resolve;
- ARCHITECTURE_GUARDRAILS referenced decisions/systems/Acceptance IDs resolve when present;
- ABSTRACTION_TESTS case/system references resolve when present;
- FRESH_AGENT_RECONSTRUCTION references a real required Acceptance ID and has an allowed evidence mode/status;
- duplicate active decision/state owners are rejected where ownership is declared;
- APP_FLOW states/transitions resolve;
- Acceptance IDs referenced by Blueprints/contracts exist;
- deprecated artifacts are not active route targets;
- generated artifacts declare source/generator when required;
- required generated views have current source fingerprints/revisions; stale required views fail generated-view freshness;
- `VIEW-PROJECT-ATLAS` exists/is fresh for nontrivial projects and its generator resolves.

Run after structural changes and before milestone/final verification.

### Runtime convergence/progress checks

Where the compiled project can express them deterministically, the project-native gate should support progress checks in addition to package-structure checks:

- current `STATE` stage/admission pointer is valid under `PROJECT_PLAN`;
- claimed stage completion has required Acceptance/Evidence;
- required build/typecheck/test commands for that gate currently pass;
- generated/derived views do not claim a conflicting current stage;
- registered active implementation owners remain unique;
- affected material Composition Invariants have current evidence when their canonical source/relationship changed;
- a `production_admitted` skeleton has all declared survivability Acceptance evidence satisfied;
- project-specific producer→canonical data/store/query→runtime probes pass where data-driven behavior is a material claim;
- every required product-flow/workflow node has a valid plan stage + Acceptance mapping;
- required flow nodes are reachable from entry or intentionally declared independent;
- the realization graph includes required completion/result/return/resume paths rather than stopping at the first runnable core experience.

Do not hard-fail arbitrary unregistered files solely from filename heuristics. Suspicious `*_corrected`, `*_full`, `*_new`, `*_v2`, etc. may be surfaced for review, but semantic duplicate ownership requires stronger project-specific evidence.

### Reference authority-reachability algorithm

The generated validator should implement the equivalent of:

```text
artifact_roots =
  PROJECT_INDEX.project.core_id
  + PROJECT_INDEX.project.goal_id
  + PROJECT_INDEX.project.acceptance_id
  + PROJECT_INDEX.bootstrap.must_read
  + existing PROJECT_INDEX.bootstrap.when_present
  + PROJECT_INDEX.bootstrap.inspect_view_ids
  + PROJECT_INDEX.bootstrap.maintenance_tool_ids
  + all PROJECT_INDEX.domains.*.authority_ids that are artifact IDs

blueprint_roots =
  all routed Blueprint IDs from bootstrap/domain routes

reachable_blueprints =
  DFS/BFS(blueprint_roots, blueprints/REGISTRY.yaml calls)

required_discoverable_artifacts =
  active PROJECT_REGISTRY artifacts
  where discoverability_required == true

required_normative_artifacts =
  active PROJECT_REGISTRY artifacts
  where normative == true and discoverability_required != false

required_blueprints =
  active normative Blueprints

FAIL if:
  any route/root ID is unresolved
  OR required_discoverable_artifacts - artifact_roots is non-empty
  OR required_normative_artifacts - artifact_roots is non-empty
  OR required_blueprints - reachable_blueprints is non-empty
```

Do not infer reachability merely from a filename appearing in arbitrary prose. Explicit router/registry graph edges are the machine contract.

---

