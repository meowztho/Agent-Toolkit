# 24. FINAL_CONTRACT_AUDIT

Require all mandatory generated views to be current. For nontrivial projects, `PROJECT_ATLAS.html` must exist, be reproducibly generated from registered canonical inputs, and have a current source fingerprint before final completion.


Before final build/user testing:

- no required AC remains unverified/reopened/stale;
- registries resolve;
- `verification/AUTHORITY_REACHABILITY.yaml` is current/passed with zero unreachable normative authorities/required Blueprints;
- Blueprint calls resolve;
- required implementation Blueprints map to real implementation;
- required tests/evidence mappings exist;
- no duplicate active responsibility owner;
- normal-user flow graph is complete;
- material SYSTEM_INTEGRATION ownership/runtime traces are coherent and current;
- release-relevant `verification/INTEGRATION_AUDIT.yaml` is current/passed when required;
- no known dead required config/contract or parallel authoritative path remains;
- final surface verification contract is satisfiable.

If this audit fails, return to SELECT_REQUIREMENT.

---

# 25. FINAL_BUILD_TEST

Build/package the actual target from the current intended final worktree.

Run:
- full relevant automated test suite;
- contract validator;
- build/package checks;
- artifact checks.

Do not declare complete yet for a user-facing product.

---

# 26. FINAL_USER_SURFACE_GATE

For user-facing products this is a hard release gate.

The agent MUST:

1. launch the actual final target from the normal user entry point;
2. invoke the selected interactive user-surface tool/adapter;
3. complete every release-gating E2E scenario;
4. capture the required screenshots/rendered checkpoints;
5. visually inspect them;
6. record non-stale evidence;
7. confirm no required obvious visual/runtime defect exists.

If `TOOL_CAPABILITIES.yaml` says an applicable tool is available but the evidence
index shows it was not invoked, the goal is NOT complete.

The contract validator should fail completion when required final evidence artifacts
or evidence IDs are missing/stale.

---

# 27. INDEPENDENT_REVIEW

Run only when triggered by project policy:
- consequential;
- high-risk;
- difficult to verify;
- materially blocked.

The review is read-only and independent.

Resolve material findings before completion.

Review does not replace final user-surface verification.

---

# 28. FINAL_GIT_CHECK

Before COMPLETE:

1. inspect `git status`;
2. inspect final relevant diff;
3. ensure no accidental temp/debug/secret/build junk is staged or tracked;
4. ensure registries point to current paths;
5. ensure final verification evidence corresponds to current code/worktree;
6. commit final verified project state when policy permits.

If relevant source changed after final release-gating evidence, invalidate that evidence
and rerun the affected final gate.

---

# 29. FINAL_CLAIM_RECONCILIATION

Immediately before any final completion report:

1. reread the canonical current-state authority;
2. reread the current Plan admission/completion rules and Acceptance Matrix;
3. enumerate the requested/master outcomes and required criteria;
4. bind each required criterion to evidence actually produced on the current revision;
5. execute any still-required build/runtime/browser/user-surface evidence — never replace it with a file/existence check;
6. reject stale evidence invalidated by later source/config/data changes;
7. confirm current admission/state is compatible with the claimed final status;
8. derive the report from that reconciliation.

Do not infer completion from:
- amount of code produced;
- file/module/function names;
- a green package/project-gate whose scope is narrower than product acceptance;
- an earlier milestone marked complete in prose;
- a foundation/M0/architecture gate;
- tests that do not exercise the required observable boundary.

If required runtime/browser evidence was never actually exercised, the corresponding outcome remains unverified.

# 30. COMPLETE

Only report completion when FINAL_CLAIM_RECONCILIATION and every applicable gate pass.

For user-facing products:

```text
canonical current state reconciled
+ every required AC mapped to current evidence
+ automated/build/integration gates complete
+ user-surface/runtime evidence actually exercised
+ required visual evidence complete
+ final black-box flow complete
+ repository state checked
= eligible for COMPLETE
```

The final report is a **derived view**, not a new status authority.

---

