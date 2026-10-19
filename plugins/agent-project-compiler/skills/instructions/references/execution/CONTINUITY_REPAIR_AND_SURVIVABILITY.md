# Compiled-context bootstrap note

For projects produced by the compiler, a fresh implementation agent consumes the context-rich START snapshot, then reads `PROJECT_INDEX.yaml` and its direct `bootstrap.must_read` authorities (normally including `CONTEXT_HANDOFF.md` + `docs/DECISION_COMPENDIUM.md`) before source edits. Confirm authority-reachability and reconstruction gates are passed/current. `INTERVIEW_LEDGER.md` remains JIT provenance unless the current decision needs exact history. If `INTERVIEW_COVERAGE.yaml` is partial and a material unresolved user decision blocks correct implementation, ask it before committing to the affected behavior; do not silently infer it.

# Executable preflight and validator-quality gate

For a generated project that includes the project-native gate, insert it into execution rather than leaving it as an unused utility.

Required sequence for material work:

```text
fresh / resume / major compaction
→ reload bound Core-First Governance procedure if actually available
→ project gate: validate/preflight
→ resolve current admission + required authority/reference IDs
→ actually read/inspect them
→ classify Core-First change
→ material implementation
```

A failing gate blocks the dependent material edit until project truth or validation itself is repaired. Do not bypass it because unit/build/runtime code happens to execute.

Before moving to another material plan stage:
1. rerun admission evaluation;
2. verify required upstream maturity/evidence;
3. update current `STATE.current_admission` from the existing canonical Plan/Acceptance authorities;
4. only then select within the admissible work set.

After material authority/validator changes, run the gate's negative self-test. A validator change is incomplete until at least one known-bad mutant is rejected. Path existence alone is never sufficient structural validation for structured authorities.

After context compaction, an old green preflight/loaded-source record is stale session cache. Re-run preflight and reconsume the exact currently required inputs before more material edits.


# v2.24 Product-continuity checkpoint

At bootstrap, context recovery, and every material milestone transition:

```text
reconcile actual repository/runtime/evidence
→ read current STATE execution/admission pointer
→ read PROJECT_PLAN admission rules
→ read Acceptance/Evidence verification truth
→ compute admissible work
→ restate remaining master-product outcomes
→ choose next admissible stage/task
```

Do not allow a completed foundation/scaffold/walking skeleton to collapse the master goal.

`STATE` is the single current execution/admission pointer authority. It does not own product canon or verification truth. Derived views (`CONTINUE`, Handoff, Atlas, status prose) must be regenerated/reconciled from STATE + Plan + Acceptance/Evidence and must not disagree about current stage.

## Surface-fidelity routing before surface work

When the selected stage materially affects the user-visible surface:

1. resolve applicable User-Surface Authority/reference IDs through `PROJECT_INDEX`;
2. inspect the underlying visual references with an available capable tool before material styling/layout work;
3. load the shared Presentation/Design Core contracts and parent/slot composition rules;
4. carry the current visual target/baseline into the bounded work context;
5. after the smallest runnable change, inspect the whole relevant rendered surface, not only isolated controls.

If the project has material visual identity and only a generic/debug surface exists, treat that as connectivity evidence, not product-surface completion.

## Milestone convergence gate

Before `RECORD_MILESTONE` or admission advance, run the project-native convergence checks that exist for the project:

- prerequisite maturity/admission;
- required build/typecheck/test commands;
- required current evidence;
- canonical current-state consistency;
- project-specific canonical data/runtime probes where declared;
- registered active-owner uniqueness;
- milestone-boundary hygiene for disposable scratch/patch artifacts.

An interrupted session may contain temporary artifacts. Do not classify them as durable architecture until they are registered/consumed/claimed as such; however, do not carry unexplained scratch/shadow implementations across a clean milestone/handoff boundary.


# v2.26 Realization-graph driven continuation

After each verified milestone, do not select the next task only from architecture dependencies.

Reconcile:

```text
current verified flow nodes
+ remaining required APP_FLOW/workflow nodes
+ architecture admission/dependencies
+ Acceptance gaps
→ next admissible product-realization stage
```

A runnable primary experience does not authorize stopping while required shell/setup/result/persistence/replay/other lifecycle nodes remain unverified.

When several architecture tasks are possible, prefer work that unlocks the next required normal-user flow node unless risk/dependency evidence justifies another order.

At context recovery, restate the remaining required product-flow nodes before resuming implementation.


# v2.27 Derived admission / autonomous continuation

The implementation agent does not create admission by editing STATE.

At every milestone boundary:

```text
produce/update evidence
→ project_gate derives current maturity/admission
→ reconcile STATE pointer to the derived result
→ choose next admissible realization stage
→ continue automatically
```

Stop only for:
- Product Complete / requested terminal status;
- a genuine blocking USER_DECISION;
- a demonstrated external dependency/capability blocker that cannot be resolved within authorization;
- explicit user stop.

Do not stop merely because one milestone passed.

When `STATE` disagrees with derived admission, the gate wins the **validation verdict**; correct the pointer/derived views, do not weaken Plan/Acceptance.

# v2.27 Shipping-content and consumer-rights runtime checks

Where the relevant contracts exist:
- reject `test_fixture`/`debug_only` content reachable from production defaults, progression or normal user flow;
- require explicit promotion before `prototype` becomes production;
- verify consumer/adapter mutations travel through allowed commands/contracts rather than direct foreign writes.

# v2.27 Persistence verification

When Continue/Resume is a required product outcome, load the persistence coverage contract and verify every material runtime state owner is classified as persisted, deterministically reconstructed, intentionally transient or forbidden to persist. Use the strongest project-required restore equivalence test; do not inflate a partial snapshot roundtrip into full Continue verification.


# v2.29 Review-driven continuation

When the compiled project declares representative product-path heartbeats or deterministic review projections:

1. identify whether the current material change can invalidate any declared heartbeat/projection;
2. rerun the narrowest affected heartbeat after the change reaches a runnable state;
3. regenerate/re-exercise affected review projections from canonical sources/state;
4. repair failures at canonical owners/producers rather than patching derived review/generated outputs;
5. continue through the Product Realization roadmap after evidence is reconciled.

Do not turn this into unconditional full-regression-after-every-edit behavior.

Finish/fidelity `PR-*` outcomes are ordinary product obligations. Do not defer them automatically to a final cleanup phase, and do not treat them as complete merely because the underlying feature is functional.


# v2.31 Repair-by-Invariant runtime loop

For a reported defect, do not begin with the nearest implementation file.

Use:

```text
REPRODUCE
→ identify failed observable/Acceptance
→ determine LOCAL_DEFECT vs COHERENCE_DEFECT
→ resolve applicable SYSTEM_INTEGRATION invariant/trace
→ inspect canonical source/owner and dependent consumers
→ repair the highest correct owner/derivation seam
→ rerun affected invariant evidence
→ rerun affected Product Heartbeat / Review Projection
```

A bounded local repair is correct when the owning implementation itself is wrong and no shared relationship is violated.

A consumer-local patch is suspect when:
- the same corrective value/rule appears in multiple consumers;
- the fix compensates for stale/duplicated canonical data;
- changing the canonical source would re-break the consumer;
- another projection remains inconsistent after the patch.

Do not turn a symptom workaround into permanent architecture.

# v2.31 Skeleton survivability admission

A runnable skeleton may be used for learning before production admission.

Before advancing a stage whose claim is `production foundation/skeleton ready`, require the project-declared survivability Acceptance evidence. Re-derive the claim from Plan + Acceptance/Evidence; never infer it from `STATE`, a green build, or the fact that the path runs.

If the survivability challenge fails, keep the current path classified as exploratory/provisional, correct the owner/contract/composition seam, and repeat the smallest representative challenge before widening production breadth.
