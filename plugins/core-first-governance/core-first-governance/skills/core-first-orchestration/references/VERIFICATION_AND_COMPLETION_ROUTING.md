# Verification, Review, and Completion Routing

Read this procedure when product verification, Core-First verification, Independent Review, finding reconciliation, or external completion authority is material.

## Observable product verification

Trigger when a claim materially depends on a real user/external-system boundary: interactive UI/web/desktop/mobile/game/device behavior; navigation/control/animation/input/visual state/persistence/workflow; CLI/API/service output or side effects; realistic library/integration/automation output; runtime-only symptoms.

Load `observable-product-verification` JIT and use the strongest suitable real interaction/observation capability. Logs/tests/implementation/tool success may support diagnosis but do not replace the real surface for a user-visible claim. `INCONCLUSIVE` is not verified.

If it finds a material defect: preserve raw evidence/finding class; return control to the primary agent; route through existing project authorities and Core-First when architecture is material; correct within scope; rerun the affected observable path.

## Core-First verifier

Use `core-first-verifier` for material architecture/reuse/ownership conformance or important/final architecture milestones.

Required semantics:
- separate fresh verification context when feasible;
- read-only;
- load verifier + canonical Core-First fresh;
- two-phase anti-rationalization: when enforceable, freeze expected owner/path/classification/allowed writes from requirement + authorities + baseline before change evidence; then compare actual diff/files/tests/runtime evidence;
- no implementer rationale/confidence/conclusions or prior verifier conclusion before independent derivation.

If freshness/order/read-only isolation cannot be guaranteed, use the strongest available mechanism and disclose the limitation.

## Independent Review

Use `independent-review` only for consequential/high-risk/difficult-to-verify/materially blocked work. It supplements rather than replaces primary verification, OPV, or Core-First verification.

Before independent derivation, withhold implementer rationale/conclusions/confidence, Core-First-verifier conclusions, and OPV interpreted conclusions. Pass original requirements/instructions, relevant raw diffs/files, verification output, and raw observable/runtime evidence. Project truth is never hidden to manufacture independence.

## Reconcile findings

For each material finding: fix when required/in-scope; reject with direct evidence; report valid adjacent/unrelated observations without scope expansion; or explicitly accept permitted risk. Resolve disagreements by evidence, not majority vote.

## Completion coverage

Before self-certifying, reconcile each material **original requested outcome** with evidence that actually matches it and any remaining gap. **Passing-test/evidence volume does not measure completion.** Partial, inconclusive, blocked, or explicitly deferred outcomes remain open/explicit; a local fix cannot silently narrow the requested scope.

## Existing external completion authority

Determine whether the project/repository defines a separate acceptance/completion owner or validator (project evidence/acceptance store, CI/release gate, regulated approval, or equivalent).

If present, follow its project-defined acceptance contract and route required raw evidence through the existing mechanism. Governance, verifier PASS, OPV status, or reviewer result never replaces that authority's decision. If unavailable/unsatisfied, report the actual completion state.

If none exists, do not invent one and do not hardwire Governance to a specific external compiler/validator product.
