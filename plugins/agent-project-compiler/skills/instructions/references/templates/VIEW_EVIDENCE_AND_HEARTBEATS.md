# APC v2.35 JIT Slice — Views, Evidence, Heartbeat and Review Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## Nested `AGENTS.md` Template

Generate this only for a coherent subtree with shared local engineering rules that materially refine repository-root behavior.

```markdown
# [Scope Name] Instructions

- [Only subtree-wide working rule that differs from/refines root behavior.]
- [Reference stable artifact/contract IDs when useful.]
- [Require local validation relevant to this subtree.]

# Do not duplicate root rules.
# Do not put concrete feature behavior here; keep it in Blueprints/specs/contracts.
```

Also register the scope in `PROJECT_REGISTRY.yaml`.

Before delivery, compare local rules against root `AGENTS.md` and remove semantic duplicates.

---

## `verification/AUTHORITY_REACHABILITY.yaml` Template

This is generated validation evidence, **not a second routing authority**. Recompute it from `PROJECT_INDEX.yaml`, registries, active Blueprint calls, and artifact metadata.

```yaml
schema_version: 1
generated_from:
  - PROJECT_INDEX.yaml
  - PROJECT_REGISTRY.yaml
  - blueprints/REGISTRY.yaml

bootstrap_roots:
  - DOC-CONTEXT-HANDOFF
  - DOC-DECISION-COMPENDIUM
  - CONTRACT-SYSTEM-MAP

counts:
  active_normative_artifacts: 0
  routed_normative_artifacts: 0
  active_normative_blueprints: 0
  reachable_normative_blueprints: 0

unreachable_artifact_ids: []
unreachable_blueprint_ids: []
unresolved_route_ids: []
status: passed
```

Rules:
- `status: passed` requires zero unreachable/unresolved required nodes;
- report paths may be included for diagnostics but stable IDs determine identity;
- do not hand-edit this report to make validation pass; correct `PROJECT_INDEX`/registries and regenerate it.

---

## Project Atlas Generator Contract

For every nontrivial project, generate/register a reproducible command (for example `tools/generate_project_atlas.py`; use an equivalent project-native tool when more appropriate). It must:

1. resolve canonical input IDs through `PROJECT_REGISTRY.yaml`/`PROJECT_INDEX.yaml`;
2. read only canonical/project-state sources selected for Atlas presentation;
3. compute a stable source-set fingerprint that changes when a selected source is added, removed, moved through registry metadata, or materially changed;
4. render `PROJECT_ATLAS.html` from `PROJECT_ATLAS_TEMPLATE.html` or an equivalent generated template;
5. embed source fingerprint + current repository/project revision + generator command in the HTML metadata/banner;
6. never parse the previous Atlas as an input or preserve manual edits;
7. fail loudly on unresolved required inputs instead of emitting a deceptively fresh view.

Register the generator as `TOOL-GENERATE-PROJECT-ATLAS` (or a stable project-equivalent ID) and the view as `VIEW-PROJECT-ATLAS`. The generator is tooling, not project truth.

## `verification/GENERATED_VIEW_FRESHNESS.yaml` Template

Generated validation evidence, never project truth.

```yaml
schema_version: 1
views:
  VIEW-PROJECT-ATLAS:
    path: PROJECT_ATLAS.html
    required_for_nontrivial_project: true
    generator_artifact_id: TOOL-GENERATE-PROJECT-ATLAS
    source_artifact_ids: []
    expected_source_fingerprint: "sha256:..."
    embedded_source_fingerprint: "sha256:..."
    generated_at_revision: "..."
    status: fresh  # fresh | stale | missing | generator_missing

status: passed
```

Rules:
- recompute the source set/fingerprint from registry/router metadata;
- any source addition/removal/change covered by the Atlas selector makes the view stale;
- a required stale/missing Atlas blocks fresh-session orientation, handoff and final completion until regenerated;
- never hand-edit fingerprint/status to pass.

## `verification/VISUAL_CHECKPOINTS.yaml` Template

Generate for projects with meaningful visual/UI state.

```yaml
checkpoints:

  example_state:
    surface: "[project-specific user/rendered surface type]"
    route:
      - "[normal user steps to reach state]"
    proves:
      - AC-XX

    expectations:
      - "[specific visible requirement]"
      - "[specific absence of failure/duplication/overlap]"

    interaction:
      - action: "[user action]"
        expect_state: "[next state]"

    evidence:
      interaction_required: true
      screenshot: true
```

Expectations must come from authoritative design/goal/flow sources.

---

## `verification/EVIDENCE_INDEX.yaml` Template

```yaml
evidence:

  EV-EXAMPLE-001:
    criterion: AC-XX
    type: screenshot_review
    checkpoint: example_state
    artifact: verification/evidence/EV-EXAMPLE-001.png
    revision: "git:<revision-or-worktree-id>"
    result: pass
    observations:
      - "[short factual observation]"
    review_projection_id: null  # optional stable observation recipe
    stale: false
```

Use this index to keep raw screenshots/videos out of routine context.

Reload raw evidence only when a current task/criterion requires it.

---

## `contracts/USER_SURFACE_VERIFICATION.yaml` Template

```yaml
policy:
  incremental_check_after_observable_change: true
  final_black_box_required: true
  final_black_box_on_current_revision: true

surfaces:
  primary:
    type: "[project-specific surface/interface/artifact type]"
    launch_method: "[normal user entry point]"
    preferred_interaction: "[computer_use|browser|playwright|engine_automation|real_cli|real_client]"
    visual_evidence: "[required|optional|not_applicable]"

evidence_budget:
  checkpoint_screenshots_only: true
  capture_on_failure: true
  summarize_immediately: true
  store_raw_artifacts_outside_active_context: true
```

---

## Representative Product Path / Heartbeat fields

Use inside the existing project-appropriate E2E/integration scenario authority; do not create a new product authority solely for this.

```yaml
scenario_id: PATH-REPRESENTATIVE-001
representative_product_path: true
regression_heartbeat: true
affected_by:
  - SYS-...
  - CAP-...
  - "[change category]"
proves: [AC-...]
notes: "Heartbeat protects only the claims/scopes mapped above."
```

## Deterministic Review Projection fields

Attach to the existing Acceptance/checkpoint/scenario/evidence mechanism that owns the criterion.

```yaml
review_projection:
  id: RPJ-001
  canonical_source_ids: [PR-..., SYS-..., DATA-...]
  fixed_setup: "[stable input/state/query/view/fixture]"
  observation: "[screenshot|render|report|diff|sample output|trace|project-specific]"
  comparison_target_ids: []
  invalidated_by: ["[relevant source/state/config changes]"]
  derived_not_authoritative: true
```

## Final Black-Box Scenario Template

Add one or more release-gating scenarios to `verification/E2E_SCENARIOS.yaml`:

```yaml
scenarios:

  final_primary_user_journey:
    release_gate: true
    regression_heartbeat: true
    affected_by: ["[project-specific responsibilities/change categories]"]
    evidence_type: user_surface_black_box
    run_on_current_revision: true

    steps:
      - build_or_package_target
      - launch_from_normal_user_entry_point
      - assert_initial_visible_state
      - perform_primary_setup_flow
      - exercise_required_interactions
      - inspect_visual_checkpoints
      - complete_primary_user_goal
      - exercise_required_interruption_recovery_completion_return_paths

    screenshots:
      checkpoints:
        - "[important stable state]"
        - "[important final state]"

    fail_if:
      - unexpected_black_screen
      - duplicate_required_ui
      - required_visible_element_missing
      - navigation_break
      - runtime_entity_missing
      - obvious_layout_failure
```


---

