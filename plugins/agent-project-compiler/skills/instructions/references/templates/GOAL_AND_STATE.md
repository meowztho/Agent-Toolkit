# APC v2.35 JIT Slice — Goal and State Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## GOAL.md Template

# GOAL.md

## Master Outcome
[Complete observable result.]

## User-Visible Success State
A user can:
1. [...]
2. [...]

## In Scope
- [...]

## Out of Scope
- [...]

## Evidence record semantics

```yaml
evidence:
  EVID-001:
    evidence_class: representative_scenario
    boundary: browser_app
    scope_ids: [PR-001, AC-001]
    representative: true
    revision: "<commit/worktree fingerprint>"
    input_fingerprints:
      - "<config/content/data fingerprint>"
    artifact_refs: ["verification/...png", "verification/...json"]
    invalidated_by:
      - source_paths: ["src/...", "content/..."]
```

Acceptance defines required evidence semantics explicitly, for example:

```yaml
required_evidence:
  - classes: [representative_scenario]
    boundary: browser_app
    representative: true
  - classes: [visual_inspection]
    boundary: browser_app
```

Do not use one global evidence-strength ranking when different evidence kinds prove different claim dimensions.

## Acceptance Criteria

### AC-01 — [Title]
[Observable condition.]

Verification:
- [...]

### AC-02 — [Title]
[Observable condition.]

Verification:
- [...]

## Completion Condition
The goal is complete only when every required acceptance criterion is satisfied by current actual evidence and required end-to-end verification succeeds.

The final completion report must be derived from canonical current state + actual evidence. File/module/function existence, code volume, a project-gate/M0 pass, or completion of an individual task/component/milestone/blueprint/delegated assignment does not complete this goal.

---

## STATE.json Template

`STATE` is the single canonical **current execution/admission pointer**. It must not duplicate product rules or Acceptance verification truth. `PROJECT_PLAN` owns transition/admission rules; Acceptance/Evidence owns verified maturity. CONTINUE/Handoff/Atlas/status prose are derived views and must reconcile to these authorities.


```json
{
  "goal_artifact_id": "DOC-GOAL",
  "current_requirement": null,
  "current_task": null,
  "current_change": {
    "id": null,
    "request": null,
    "classification": null,
    "target_consumers": [],
    "master_system": null,
    "capability_path": [],
    "existing_owner": null,
    "new_owner": null,
    "reuse_check": {
      "searched_existing_paths": false,
      "result": null
    },
    "second_consumer_test": {
      "applicable": null,
      "candidate_capability": null,
      "plausible_consumers": [],
      "shared_semantics": null,
      "variation_axes": [],
      "result": null,
      "rationale": null
    },
    "representative_proof_set_id": null,
    "one_off_exception_rationale": null,
    "status": null
  },
  "current_blueprint_ids": [],
  "verified": [],
  "in_progress": [],
  "blocked": [],
  "relevant_implementation_ids": [],
  "context": {
    "session_id": null,
    "required_source_ids": [],
    "loaded_source_ids": [],
    "required_view_ids": ["VIEW-PROJECT-ATLAS"],
    "inspected_view_ids": [],
    "view_gate_status": "not_evaluated",
    "load_evidence_mode": null,
    "load_gate_status": "not_evaluated"
  },
  "workspace": {
    "repo_root": null,
    "branch": null,
    "baseline_head": null,
    "baseline_dirty_paths": []
  },
  "next_action": null,
  "last_verification": null
}
```

Use stable IDs instead of duplicated paths when possible. Keep runtime pointers here, not project canon.
---

