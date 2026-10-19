# Core-First Governance — v0.11.6 Delta Handoff

**Current release:** `0.11.6`  
**Baseline:** `v0.11.5` remains the complete semantic baseline. This file is a compact delta handoff.

## 1. Release intent

v0.11.6 closes one bounded evidence-trust gap inside the existing `observable-product-verification` owner.

A real external agent project exposed a failure where a screenshot command kept returning plausible but frozen frames while the application continued rendering. A newly written artifact, successful capture call, or fresh timestamp therefore did not prove that the observed state itself was current.

The release adds one invariant:

```text
FRESHLY ACQUIRED EVIDENCE
!=
FRESHLY OBSERVED STATE
```

This does not create a new debugging owner, capture framework, evidence database, or tool binding.

## 2. Oracle-liveness rule

When a material observable claim depends on live/changing state **and** there is a concrete reason the observation path may be stale, frozen, cached, replayed, or disconnected:

```text
identify expected live/current behavior
→ use independently established ongoing activity
   OR the smallest safe controlled observable stimulus
→ confirm the oracle reflects the expected change
→ only then trust that source as current-state evidence
```

A successful observation-tool call or newly written artifact is not enough by itself.

If liveness cannot be established:

```text
use another appropriate observation boundary
OR
keep the affected observable claim INCONCLUSIVE
```

## 3. Reverse-direction guard

The release deliberately avoids the opposite overreaction:

```text
IDENTICAL OBSERVATIONS
!=
PROOF OF DEAD ORACLE
```

A legitimately static state may produce identical samples. Equality becomes suspicious only when current-state freshness is material and independent activity or a controlled stimulus establishes that the observed state should have changed.

## 4. Why this belongs in OPV

The responsibility is evidence trust for user/external observable claims.

Existing OPV already owns:

- real boundary selection;
- before/action/settled-after verification;
- stale snapshot invalidation after relevant changes;
- visual whole-surface evidence;
- raw evidence traceability;
- `VERIFIED | FAILED | INCONCLUSIVE` status discipline.

Oracle liveness therefore extends the existing OPV capability rather than creating a new Skill or changing Core-First architecture/debug ownership.

Classification:

```text
EXTEND_EXISTING_CAPABILITY
→ observable-product-verification
```

## 5. Regression evals

Two domain-neutral OPV evals protect both directions:

- `fresh-capture-does-not-prove-oracle-liveness`
- `identical-static-observations-do-not-prove-dead-oracle`

Together they require:

```text
fresh file/capture success + plausible stale/frozen path
→ prove liveness before trusting current-state evidence

static state + identical samples only
→ do not invent a dead-oracle diagnosis
```

## 6. Changed Skill-tree files from v0.11.5

Exactly two Skill-tree files are intentionally versioned:

```text
core-first-governance/skills/observable-product-verification/SKILL.md
core-first-governance/skills/observable-product-verification/evals/evals.json
```

No other Skill body, orchestration JIT reference, agent metadata file, architecture method, verifier, or review procedure changes.

## 7. Context impact

The always-loaded Core-First context is unchanged:

```text
core-first-orchestration/SKILL.md        10,998 bytes
orchestration kernel + five JIT refs     26,444 bytes
core-first-extension-architecture        14,480 bytes
```

Only the JIT-loaded OPV Skill changes:

```text
observable-product-verification/SKILL.md
v0.11.5: 15,681 bytes
v0.11.6: 16,907 bytes
Delta:    +1,226 bytes
```

The two OPV evals are test corpus, not runtime Skill context.

## 8. Preserved v0.11.5 baseline

Everything from v0.11.5 remains controlling, including:

- five-Skill model;
- Primary Agent = orchestrator + final integrator;
- JIT/progressive disclosure;
- positively defined Local Short Path;
- material-trigger routing;
- responsibility coverage challenge;
- responsibility-relative ownership;
- `OWNER EXISTENCE != REUSABLE-SEAM PROOF`;
- outcome-coverage reconciliation and observable identity;
- evidence-driven debugging/falsification;
- workspace awareness without hydration;
- User-Surface Authority / Working View cache boundary;
- exact approval/admission gate boundary;
- fresh two-phase Core-First verifier;
- anti-anchored Independent Review;
- Skills-only/provider-neutral portability.

## 9. Explicit non-goals

v0.11.6 does not add:

- a sixth Skill;
- a generic oracle framework;
- mandatory repeated screenshots;
- a screenshot/capture implementation;
- a debugger/tool binding;
- a persistent evidence database;
- a global debug log;
- a new project authority artifact;
- a new JIT reference;
- orchestration-kernel text;
- provider/model-specific behavior.

The liveness check is conditional; normal static verification does not gain ceremony merely because an oracle exists.

## 10. Maintenance boundary

This release does **not** promote other current research candidates such as semantic-projection parity, generated-artifact ownership, experiment promotion, or durable hard-won debug knowledge.

Future changes continue to require:

```text
empirical failure
→ smallest domain-neutral intervention
→ behavioral retest
→ admit only if it measurably improves behavior
```
