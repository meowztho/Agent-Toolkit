# APC v2.35 JIT Slice — Surface and Advanced Verification

This file is a context-bounded split of the prior canonical `DELIVERY_AND_VERIFICATION_GUIDE.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## 12. Reality / User-Surface Verification

For visible or interactive criteria, also apply `USER_SURFACE_VERIFICATION_GUIDE.md`.

Where practical:
- verify affected user-facing slices incrementally after the relevant task;
- interact with the real running product, not only tests/logs;
- inspect screenshots/rendered output for visual requirements;
- keep screenshot evidence sparse and indexed;
- run a fresh final black-box user journey before declaring the goal complete.

A technically correct internal state does not prove the final rendered/interactive state.


## Generated Orientation View Freshness

For every nontrivial compiled project, final delivery/handoff requires a current `PROJECT_ATLAS.html` plus its registered regeneration path. Validate `verification/GENERATED_VIEW_FRESHNESS.yaml`; `stale`, `missing`, or `generator_missing` means the package is not ready for fresh-agent orientation. The Atlas remains non-authoritative and cannot substitute for canonical evidence or source reads.

# Validator negative-control evidence

If the compiler generates a project validator/gate, evidence that it prints PASS on the valid package is insufficient by itself.

The package must retain existing validation evidence showing that the gate also rejects representative intentionally broken temporary cases for the invariants it claims to enforce. Typical negative controls include parse failure, broken ID/reference, orphan authority, registry/file mismatch, stale fingerprint and unmet admission evidence.

A validator that has never demonstrated failure on a known-bad case is `Declared` tooling, not verified project validation.


# v2.24 Walking-skeleton and product-realization distinction

For product implementation:

```text
walking skeleton
= smallest real path proving major architecture/integration assumptions

product completion
= all required product outcomes + acceptance + final user/external evidence
```

Never let a skeleton milestone consume or replace later product outcomes.

When visual identity is material, the early meaningful skeleton should include at least one representative normal-user surface/path using the intended Presentation/Design Core and product-specific visual direction. A generic debug/default UI may accompany it for diagnostics but cannot be the only surface proof.

# Progress truth separation

Use the existing authorities with non-overlapping ownership:

- `PROJECT_PLAN` — stage order, prerequisites and admission rules;
- `STATE` — current execution/admission pointer;
- `ACCEPTANCE_MATRIX` + evidence — maturity/verification truth;
- START/GOAL/CONTINUE/Handoff/Atlas — derived orientation only.

A completion/milestone claim must be rejected when required build/evidence/admission checks contradict it.


# v2.25 Completion-claim provenance

The final completion report itself is a derived view. It must not introduce stronger status than the canonical state/evidence supports.

For every reported material outcome, the implementation runtime should be able to answer:

```text
reported outcome
→ acceptance / outcome ID
→ required evidence IDs/types
→ actual current evidence
→ current revision/worktree
→ verdict
```

If this mapping cannot be produced for a required outcome, report it as `UNVERIFIED`, `PARTIAL`, `BLOCKED` or another project-defined non-complete state rather than inferring success from implementation volume.

A package-validation/project-gate PASS proves only the scope that gate exercised. It must never be promoted into product/runtime/user-surface success unless that scope is itself the required acceptance evidence.


# v2.26 Product-realization coverage verification

Package validation must reject an incomplete realization plan when a required product node is orphaned.

For each required APP_FLOW/workflow node verify:

```text
required node
→ reachable from entry or explicitly independent
→ plan_stage exists
→ Acceptance mapping exists
→ governing owner/authority resolves
```

For the final product verdict additionally require every required node to be `Verified` through its Acceptance evidence or explicitly removed/deferred by canonical authority.

A release-gating E2E scenario should traverse the representative normal-user chain across the whole product, not merely enter the primary runtime. Depending on the product this can include:

```text
launch
→ home/shell
→ setup/configuration
→ primary experience
→ interruption/recovery
→ completion/results
→ persistence/progression
→ replay/return/resume
```

Use project-specific nodes; never force this exact taxonomy when not applicable.


# v2.27 Product Realization authority and coverage

Generate `contracts/PRODUCT_REALIZATION.yaml` for nontrivial products. It is the canonical inventory of required `PR-*` outcomes and may reference APP_FLOW nodes for flow-based outcomes instead of copying transitions.

A generated `verification/PRODUCT_REALIZATION_COVERAGE.yaml` reconciles:

```text
PR outcome
→ source/provenance
→ Responsibility/System/Capability/Contract
→ producer / consumer / surface / content path where material
→ plan stage
→ Acceptance IDs
→ required evidence semantics
→ derived current maturity/verdict from Acceptance/Evidence
```

Coverage fails when a required PR outcome lacks a plan stage, Acceptance mapping, resolvable owner/contract or required flow/content/persistence mapping.

# v2.27 Evidence semantics

Evidence sufficiency is **criterion-specific**, not a universal numeric hierarchy. Evidence records should declare when material:

- `evidence_class`: static inspection | unit test | contract test | fixture integration | synthetic simulation | runtime integration | browser integration | representative scenario | visual inspection | endurance/performance run | differential test | human product judgment | project-specific;
- `boundary`: source | module | contract | process/runtime | browser/app | external system | human judgment;
- `scope`: exact claim/outcome IDs;
- `representative`: true/false/qualified;
- `revision/worktree` and relevant input/config/content fingerprint;
- produced artifact/log/screenshot/trace reference;
- invalidation inputs/triggers.

Acceptance criteria define the required classes/boundaries/representativeness rather than saying merely `test_passed`.

Examples:

```text
fixture integration PASS
!= representative product-path VERIFIED

serialize/deserialize selected fields PASS
!= full Continue/Resume VERIFIED
```

# v2.27 Derived admission engine

`STATE.current_admission` is a cached/current pointer, never authority to create admission.

For a requested/current stage, project_gate derives admission from:

```text
PROJECT_PLAN dependencies + required maturity
→ required PR outcomes / Acceptance IDs
→ current Acceptance verification
→ evidence existence/freshness/scope/representativeness
→ required build/runtime gates
→ DERIVED ADMITTED / BLOCKED
```

If STATE claims a later stage than this derivation permits, fail with a precise contradiction. Do not silently trust or auto-upgrade STATE.

# v2.27 Product Complete vs Release Ready

Use explicit semantics:

- `Implementation Complete` — implementation scope for a bounded item exists; says nothing about final verification unless specified;
- `Product Complete` — every required master-outcome `PR-*` realization outcome is `Verified` with sufficient current evidence;
- `Release Ready` — Product Complete plus project-defined release-only requirements (packaging, deployment, migration, compliance, endurance, release sign-off, etc.).

Do not universally make package-maintenance checks such as Atlas freshness or Fresh-Agent Reconstruction part of **Product Complete**. They are required for compiler/handoff/governance integrity and may be Release Ready gates when the project contract says so. Keep claim scopes explicit.


# Blueprint/code modularity evidence

When modular subsystem boundaries are a material architecture claim, acceptance should prove more than Blueprint files existing.

Representative evidence may include:
- two consumers use the same public module/capability boundary;
- internal source decomposition can change without consumer contract changes;
- a forbidden direct-internal dependency is rejected by static/project-gate validation where feasible;
- runtime/integration trace reaches the canonical implementation boundary;
- consumer-local duplicate domain rules are absent.

A clean Blueprint document without corresponding implementation-boundary conformance is `Declared`, not `Verified`.


# v2.29 Representative product-path heartbeat

When Acceptance contains a representative cross-boundary path, an existing E2E/integration scenario may declare:

```yaml
regression_heartbeat: true
affected_by:
  - "[responsibility/system/capability/change category]"
```

Semantics:
- first prove the scenario normally;
- after a material change that intersects `affected_by`, rerun the narrowest applicable heartbeat before relying on downstream/product-wide claims;
- a heartbeat PASS protects integration continuity but does not prove unrelated Product Realization outcomes;
- do not rerun expensive product-wide scenarios after every trivial edit when dependency/impact information allows a narrower check.

Representative paths are project-neutral: they may be UI/user journeys, API/CLI workflows, jobs, automations, data pipelines, generation pipelines, device/runtime flows or any other observable cross-boundary path.

# v2.29 Deterministic review projections

Where Acceptance requires qualitative/opaque review, define a reproducible observation recipe using existing verification authorities. The recipe should specify, as applicable:
- canonical input/state/artifact/source revision;
- fixed setup/query/view/viewport/fixture;
- generated observation/artifact;
- comparison target or expected traits;
- evidence class and required reviewer/automation;
- invalidation triggers.

The projection is derived evidence, never Product Truth. A failed projection sends repair back through the canonical owner/producer path.

# v2.29 Finish/fidelity verification

Material finish/fidelity requirements belong in Product Realization + Acceptance exactly like functional requirements. They are not satisfied by "implementation exists" or a generic late cleanup pass.

Require evidence appropriate to the criterion: deterministic checks where meaningful, real-surface/output review where observable quality matters, and explicit human product judgment only when the criterion genuinely requires it.


# v2.30 Definition-driven product-engine verification

Where the product claims repeatable/data-driven variants, verification should distinguish:

```text
one example works
!=
the project is reusable as a product engine
```

Preferred representative checks:

1. create/register a second materially different same-type definition;
2. observe it through the normal generic runtime/surface without copied product logic;
3. apply a declared modifier/profile and verify deterministic resolution;
4. change a canonical base/default and prove relative modifiers/consumers inherit the intended change;
5. replace placeholder content/presentation through the declared slot without changing owner/runtime architecture.

When an authoring/admin/builder path is part of the product, the strongest proof creates the new definition through that canonical producer path and observes it in the normal consumer.

If these checks require a new parallel implementation for every instance, mark the claimed reusable Definition-Type/engine seam unverified.


# v2.31 Composition-coherence verification

For each material Composition Invariant, Acceptance should state the observable relationship and adequate evidence boundary.

Preferred pattern:

```text
establish canonical source state
→ exercise representative source change/state
→ allow declared propagation/recompute/regeneration
→ inspect all required dependent projections
→ verify one coherent result
```

A local consumer PASS does not prove the invariant if another required projection was not exercised.

# v2.31 Production-skeleton survivability gate

`Production-Admitted Skeleton` is an evidence-derived claim.

The Plan declares the representative survivability cases; Acceptance defines pass/fail; Evidence records actual results. The gate should reject production admission when any required representative substitution/extension still requires replacing/bypassing the intended canonical owner/runtime path.

Do not require broad production content. The goal is to prove the **shape survives**, not to finish product breadth early.
