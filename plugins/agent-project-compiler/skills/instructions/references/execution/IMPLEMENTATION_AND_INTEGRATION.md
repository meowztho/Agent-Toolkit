# 14. CLASSIFY_CHANGE_ARCHITECTURE

Before the first source edit for each material new user/requirement delta, apply `CAPABILITY_HIERARCHY_AND_CHANGE_GATE_GUIDE.md`.

1. identify the visible consumer/surface the request appears to target;
2. resolve the canonical master system and current capability path;
3. classify the change as data/asset, value modifier, compose existing capability, extend existing capability, new reusable capability, adapter/surface, core-rule change, or explicit justified one-off;
4. record the existing-path reuse check and, when reuse/new capability is plausible, the counterfactual second-consumer test;
5. update `STATE.json.current_change` (or the scoped ExecPlan for complex work);
6. update `CAPABILITY_GRAPH.yaml`/contracts before consumer implementation when a new reusable capability is required;
7. only then proceed to implementation routing.

A direct user request to "just add" behavior does not bypass this gate. When the owner/path and intended semantics are already clear, no material ownership, contract, producer/persistence, gate/authority, dependency, shared-behavior or authoritative-state decision remains, and a direct bounded check can establish correctness, the gate may be a concise classification and immediate continuation.

If the active Acceptance/plan stage claims reusable architecture, resolve its **Representative Proof Set** before broad consumer/content scale: canonical walking-skeleton/reference case for integration plus the minimum heterogeneous cases covering material variation axes. Once that proof passes, do not keep creating similar consumers merely to accumulate architecture evidence; return to the next admissible product outcome. A new case reopens architecture proof only when it introduces a genuinely new semantic variation axis or exposes a bypass/duplicate owner.

If a blocking pre-tool/write hook is available, require a valid current-change classification before source edits; otherwise enforce this as a phase gate.

---

# 15. RESOLVE_SKILLS_FOR_REQUIREMENT

After the active requirement and its relevant systems are known:

1. read only matching entries from `contracts/SKILL_REQUIREMENTS.yaml`;
2. inspect actually available global/project/harness skills when state may have changed;
3. select the minimum matching skill set for the requirement;
4. load selected skill instructions/references JIT;
5. if a high-value capability gap remains, follow the external/project-local discovery rules in `SKILL_NATIVE_COMPILER_GUIDE.md`;
6. record new resolution/rejection/version information when material;
7. continue without optional skills when the work remains safely executable.

Do not load every installed skill. Do not treat a skill as authority over `SYSTEM_MAP`, design, behavior, content, or acceptance contracts.

---

# 16. BLUEPRINT_OR_REUSE

Before code changes:

1. derive responsibility key;
2. check artifact/Blueprint registries;
3. inspect existing code;
4. reuse/repair/extend/simplify/supersede when possible;
5. create a new implementation/data Blueprint only if a new bounded responsibility
   genuinely exists.

When behavior or implementation structure is material, update the Blueprint BEFORE
or WITH the code so the graph remains a usable implementation map.

Do not allow implementation to drift silently away from the active Blueprint.

---

# 17. IMPLEMENT_UNIT

Implement the smallest coherent unit that can be independently reasoned about and tested.

Typical units:
- class;
- module;
- service;
- component;
- screen controller;
- state machine;
- domain object;
- shared registry/store;
- meaningful data structure/schema;
- integration adapter.

Do not create separate Blueprints for trivial local variables, tiny helper functions,
or incidental arrays with no independent semantics.

---

# 18. VERIFY_UNIT

Verify the implementation unit before broad integration when practical.

Use the narrowest suitable evidence:
- unit test;
- schema/config validation;
- deterministic behavior test;
- compile/typecheck;
- debug probe;
- serialization round trip;
- invariant check.

Each implementation/data Blueprint should declare its own verification hooks.

A unit test proves only the unit contract, not the user flow.

---

# 19. INTEGRATE / VERIFY_INTEGRATION

Wire the unit into its canonical caller/router/registry and intended producer-contract-consumer path.

Then verify:
- calls/contracts resolve;
- state/rule ownership matches System Map/Integration contracts;
- no parallel owner/bypass exists;
- expected events/data reach the declared consumer;
- configuration/data is actually consumed where claimed;
- relevant integration tests pass;
- project-contract validator passes after structural changes.

An implementation that is never reached through the intended runtime/product path is not complete.

---

# 20. AUDIT_SYSTEM_INTEGRATION

Run after material cross-system changes and before a requirement that depends on them is marked green. Use `SYSTEM_INTEGRATION_AND_RUNTIME_TRACE_GUIDE.md`.

Check applicable items:
1. one authoritative decision owner per material rule;
2. one authoritative state owner per material mutable state;
3. producer -> contract/data -> consumer -> owner path closes;
4. cross-system writes use declared mutation paths;
5. no parallel/bypass implementation exists;
6. declared fields/settings/contracts have live consumers;
7. config actually controls the claimed behavior;
8. data-driven/configurable claims pass their extension boundary test;
9. no implementation unit accidentally owns unrelated system domains;
10. changed requirement/config runtime traces reach qualifying evidence.

Inspect runtime/call/data graphs rather than inferring modularity from filenames. Search for dead parameters/config, ignored results, duplicate writes, hard-coded overrides and unconsumed definitions where relevant.

When this audit is release-relevant or must survive context loss, record/update `verification/INTEGRATION_AUDIT.yaml` with the current revision, scope, findings, feature maturity and result. The audit record is evidence; ownership remains authoritative in `SYSTEM_INTEGRATION.yaml`.

Failure returns to the earliest owner/contract/implementation phase capable of fixing the root cause.

---

# 21. VERIFY_USER_SURFACE

If the change is visible or interactive and the relevant route is runnable:

1. invoke the selected real-user adapter;
2. perform the smallest relevant interaction;
3. capture/inspect the required screenshot/rendered checkpoint;
4. record evidence IDs;
5. fix observed required failures before leaving the requirement.

This phase is mandatory when the criterion requires user-surface evidence and a
capability is available.

Do not replace tool invocation with a statement that the code "should work".

---

# 22. HYGIENE

After a requirement/milestone is green, perform scoped hygiene.

Check only project-related consequences of the work:
- duplicate responsibility owners;
- obsolete/superseded menus/screens/services;
- dead navigation routes;
- stale Blueprint/registry entries;
- orphan generated files;
- temporary debug scenes/files accidentally left in project paths;
- stale path references;
- orphan/unrouted normative authorities or Blueprints introduced by structural changes;
- untracked build/tool junk that belongs in `.gitignore`;
- obsolete compatibility copies no longer required.

Do not perform unrelated cleanup.

Update registries and documentation transactionally.

Run contract validation after structural cleanup.

---

# 23. RECORD_MILESTONE

After updating canonical decisions/systems/flows/acceptance/state, evaluate whether registered Atlas inputs changed. If yes, mark `VIEW-PROJECT-ATLAS` stale and regenerate it before the milestone is handed off or used for a fresh/context-recovery orientation.


Update:
- acceptance evidence/status;
- `STATE.json`;
- registry paths/ownership;
- Blueprint implementation/test references;
- relevant revision/worktree evidence.

When version-control policy permits:
- create a verified milestone commit;
- keep commits coherent and recoverable;
- never hide failing/unverified work behind a "done" commit message.

---

