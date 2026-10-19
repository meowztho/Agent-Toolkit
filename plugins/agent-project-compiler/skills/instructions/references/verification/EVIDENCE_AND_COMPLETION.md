# APC v2.35 JIT Slice — Evidence and Completion

This file is a context-bounded split of the prior canonical `DELIVERY_AND_VERIFICATION_GUIDE.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## 7. Evidence Strength Rule

Evidence must be at least as strong as the criterion.

Examples:

```text
"code exists"
≠ feature reachable

"scene loads"
≠ full flow works

"binary launches"
≠ match completes through Results

"headless interaction tests pass"
≠ menus or visuals work

"placeholder boxes exist in code"
≠ coherent visual quality

"one remap control works"
≠ complete remapping UI
```

Code inspection may verify structural criteria.
It cannot verify user-visible runtime or visual criteria unless the criterion explicitly requires only structure.

---


## 7A. Feature Maturity and Runtime Trace

For material features distinguish:

```text
specified -> declared -> connected -> exercised -> verified
```

A parameter, setting, API, schema field, service or data definition at `declared` is not evidence that the feature works. `connected` requires a real consumer/runtime path; `exercised` requires execution; `verified` requires qualifying observed evidence.

For important options/rules/configuration, bind Acceptance to a runtime trace:

```text
Requirement/Setting
-> authority
-> producer/reader/consumer
-> decision/state owner
-> observable effect
-> evidence
```

Use `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md` for ownership, dead-contract detection and integration audit rules.

---

## 8. Contradiction / Invalidation Rule

New stronger evidence overrides old weaker evidence.

If:
- the user reports a reproducible failure;
- a runtime scenario fails;
- a required screen is missing;
- a later integration change breaks a previously verified route;

then:
1. mark the directly affected criterion `needs_recheck` or `unverified`;
2. invalidate dependent completion criteria;
3. return to the highest-priority broken requirement;
4. do not preserve a stale "goal complete" state.

Example:

`Start Local Match` is broken.

Therefore a previous claim that:
- full menu flow works;
- end-to-end slice works;
- exported build completes a match;

cannot remain verified.

---

## 9. E2E Scenarios

For interactive products, scenarios should describe observable steps.

Example:

```yaml
scenarios:
  primary_full_match:
    environment: exported_build
    steps:
      - launch_application
      - assert_screen: main_menu
      - action: start_local_match
      - assert_screen: player_setup
      - select_participants
      - select_entitys
      - select_stage
      - configure_rules
      - start_match
      - assert_active_participants_visible
      - assert_stage_stable_and_visible
      - complete_match
      - assert_screen: results
      - rematch
      - return_main_menu
    proves: [AC-14, AC-15, AC-16, AC-18, AC-22]
```

For games, include runtime sanity checks where relevant:
- intended stage/level remains in correct position;
- expected participants spawn;
- primary participants/content are visible within the intended viewport;
- input controls intended participant;
- status/presentation reflects selected setup;
- no debug command is required.

---

## 10. Final Completion Gate

Before an implementation agent may report the master goal complete, derive the claim from the **current canonical state plus actual evidence**, never from code volume, filenames, modules/functions existing, or prior milestone prose.

Required final reconciliation:

0. reread the canonical current-state authority (`STATE` or project equivalent);
1. reread the persistent master-goal authority (normally `GOAL.md`), the plan/admission authority (normally `PROJECT_PLAN.md`) and the acceptance authority (normally `ACCEPTANCE_MATRIX.yaml`) as bound through `PROJECT_INDEX.yaml`; an existing equivalent must preserve each role's full contract;
2. enumerate every required criterion/outcome and its required evidence;
3. execute the required evidence on the current intended final worktree/revision — do not substitute existence checks;
4. verify every required criterion is actually `verified` and no dependency/admission condition contradicts the claim;
5. confirm release-relevant integration audit evidence is current/passed when cross-system semantic integrity is in scope;
6. run all release-gating E2E scenarios on the final build/commit;
7. for required browser/app/user-surface/runtime claims, actually exercise that boundary and record current evidence;
8. perform required visual checks using actual runtime output/screenshots;
9. ensure no known user report or contradictory runtime evidence invalidates the claim;
10. ensure required APP_FLOW / INPUT_ACTIONS / canonical content-data paths are reachable through the normal product;
11. reconcile the final report with current STATE/admission/evidence before emitting `COMPLETE`.

Hard invariants:

```text
FILE / MODULE / FUNCTION EXISTS
!= BEHAVIOR VERIFIED

PROJECT_GATE / M0 / FOUNDATION PASS
!= PRODUCT COMPLETE

REQUIRED RUNTIME/BROWSER EVIDENCE NOT EXERCISED
= CORRESPONDING OUTCOME UNVERIFIED

THE FINAL REPORT
= CANONICAL CURRENT STATE + ACTUAL CURRENT EVIDENCE
!= AMOUNT OF CODE PRODUCED
```

If a required check was not actually run, it remains unverified.

---

## 11. PROJECT_INDEX Routing

Machine contracts must be first-class routed sources.

Example:

```yaml
bootstrap:
  must_read:
    - DOC-CONTEXT-HANDOFF
    - DOC-DECISION-COMPENDIUM
    - CONTRACT-SYSTEM-MAP

domains:
  app_flow:
    authority_ids: [CONTRACT-APP-FLOW]
    read_when: [navigation_task, screen_task, end_to_end_task]

  input_actions:
    authority_ids: [CONTRACT-INPUT-ACTIONS]
    read_when: [input_task, options_task, remapping_task]

  acceptance:
    authority_ids: [DOC-GOAL, CONTRACT-ACCEPTANCE-MATRIX]
    read_when: [planning_task, requirement_selection, verification_task, completion_audit]
```

For an active acceptance criterion, the agent should derive the exact required authority IDs from these routes, resolve them through registries, and load them before dependent source edits. The generated reachability validator must also prove that every active normative authority has an incoming bootstrap/JIT route (Blueprint call reachability may extend a routed Blueprint).

This is stronger than asking the agent to infer documents from filenames, folder contents, chat memory, or another prose file.


---

# Stable-ID Routing Note

When `PROJECT_REGISTRY.yaml` and Project Blueprints are enabled, treat raw paths in older examples as illustrative only.

Prefer:
- `authority_ids`
- `implementation_ids`
- Blueprint IDs
- artifact IDs

Resolve the current path through the canonical registries.

This prevents path duplication and stale references after moves/renames.


---

