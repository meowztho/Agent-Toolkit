---
name: observable-product-verification
description: Verify real user/external outcomes instead of inferring them from code, tests, logs, telemetry, or tool success. For material user-visible claims, compare the real whole surface to applicable project surface/design/layout authority; reuse current screenshots for unchanged visible facts, refresh after relevant change, and never treat a static image as interaction proof.
metadata:
  short-description: Verify real observable product outcomes
---

# Observable Product Verification

## Purpose

Verify the **product outcome**, not merely the implementation or the action used to exercise it.

This Skill is provider-, framework-, and tool-neutral. Use whatever interaction and observation capabilities are actually available in the current environment. It does not require or prescribe a particular browser, computer-control system, protocol, script, screenshot tool, or model provider.

Project/repository authorities remain project truth. This Skill owns only the verification procedure for observable runtime claims.

## Core invariant

```text
Implementation evidence != runtime evidence
Tool/action success       != intended outcome
Runtime evidence          != every broader product claim
```

A successful click, key/input dispatch, request send, command invocation, build, process start, screenshot capture, log/telemetry entry, or test harness action proves only what was actually observed from it. **Logs/internal state are supporting evidence, not a substitute for a material user-visible outcome.** If a current trustworthy visible result contradicts an internal success log, the user-facing claim is not verified.

## Observable boundary

Choose the closest practical real boundary that corresponds to the claim.

Examples of boundary classes, not mandated tools:
- interactive application → live user-facing UI/runtime;
- game/simulation → live executable input, state, timing, physics/animation outcome;
- CLI → actual command invocation and externally visible output/effects;
- API/service → actual contract request/response and material external side effect/state when required;
- library/SDK → realistic consumer/integration path through the public contract;
- automation/batch → representative real input through the normal path to produced output/side effects.

Use a narrower proxy only for a narrower claim. Do not silently substitute a weaker surface for the one the requirement actually depends on.

## User-surface fidelity

When the project defines a material visual/layout result, verify against the applicable **User-Surface Authority**; when implementation was grounded from one, use that same authority. Check both (a) exact constraints actually specified and (b) holistic intent/structure actually specified: style, structure, placement, hierarchy, spacing/scale, responsive/adaptive behavior, visible states, and references.

Element presence or correct tokens alone do not prove the required surface. A correctly styled button in the wrong region, or correct components in a materially wrong composition, fails the affected visual claim. Respect the authority's precision: relative placement does not require invented pixel coordinates. Project authority outranks an agent-generated Working View/Atlas/mockup, which is only derived cache.

## Procedure

### 1. Derive the observable claim

State what must be true from the user/external point of view.

Prefer an explicit form:

```text
START STATE
ACTION / INPUT
EXPECTED OBSERVABLE DELTA
SETTLED SUCCESS STATE
```

Examples:
- slider begins at value A → user changes it → control visibly moves/value changes → dependent state reflects B;
- player is grounded → jump input → player rises → returns to valid grounded state without falling through geometry;
- CLI receives input → command exits → expected output/file/state exists;
- API receives request → documented response occurs → required persistent/external effect is visible.

### 2. Select evidence strength

Use the strongest practical evidence appropriate to the claim, while keeping cost and risk proportional.

Do not claim a real user/external outcome from static inspection alone when the executable boundary can reasonably be exercised.

If the required surface cannot be exercised, return `INCONCLUSIVE` for that observable claim and state the missing capability/evidence. Continue to report narrower static/unit/build facts separately if they were actually proven.

### 3. Establish the before state

Observe enough initial state to distinguish success from a no-op, stale state, already-satisfied state, or unrelated transition.

Where relevant record:
- applicable user-surface authority/reference for visual/layout claims;
- visible/returned value;
- current screen/state/mode;
- persisted value before the action;
- entity position/state;
- relevant external side-effect baseline.

### 3a. Establish observation-path liveness when freshness is material

A newly acquired artifact or successful observation-tool call does **not** by itself prove that the oracle reflects current state. When the claim materially depends on live/changing state **and** there is a concrete reason the observation path may be stale, frozen, cached, replayed, or disconnected, establish oracle liveness before trusting that evidence.

Use the smallest safe discriminator: either observe independently established ongoing activity or introduce a controlled observable stimulus, then confirm that the oracle reflects the expected change. Identical observations alone do not prove that an oracle is dead when the underlying state may legitimately be static.

If liveness cannot be established, do not use that source as current-state proof. Use another appropriate observation boundary when available, or mark the affected observable claim `INCONCLUSIVE`.

### 4. Perform the user/external action

Exercise the normal product path rather than a private implementation shortcut when the requirement is about the normal product path.

The action itself is not the verdict.

### 5. Observe the settled after state

Verify the expected observable delta and the resulting stable/meaningful state.

Do not stop at the immediate frame/event when behavior includes:
- animation or transition timing;
- asynchronous/network work;
- navigation;
- physics;
- delayed state propagation;
- persistence/save/reload;
- queued/background effects.

Wait/advance only as much as needed to judge the intended outcome. Avoid arbitrary long sleeps when a meaningful state signal is available.

### 6. Use already-acquired evidence fully

Treat an acquired current screenshot/frame/rendered surface as a **whole relevant visible-state snapshot**, not as a single-element assertion. Inspect material facts already visible in that same evidence, including when applicable: layout/composition, hierarchy, placement/alignment, spacing/sizing, clipping/overlap, missing or incorrect assets, navigation/selection state, visible values/status, and contradictions with the required screen/journey or applicable User-Surface Authority.

Logs, telemetry, debug output, DOM/state dumps, or internal counters may explain *why* something happened, but for a material user-visible claim they do not replace the visible surface. A log saying a screen loaded successfully does not make a visibly distorted screen `VERIFIED`.

Reuse a still-current visual snapshot for unchanged visible facts; do not capture a new screenshot merely to re-prove what the existing trustworthy snapshot already shows. A relevant visual/state-changing modification invalidates the affected old snapshot for those changed claims; acquire fresh visual evidence and inspect the whole relevant surface again.

A static screenshot proves visible state only. It does **not** prove clickability, transition behavior, animation/physics over time, persistence, or hidden side effects; those still require the normal action and settled-result evidence appropriate to the claim.

This is **ambient/holistic observation**, not a full unrelated audit. Do not spend materially more time searching other surfaces merely because the current one contains rich evidence.

### 7. Perform cheap bounded adjacent exploration

After the target assertion, perform a small number of natural adjacent actions when all are true:
- they are cheap and low risk;
- they are directly connected to the exercised workflow/state;
- they have a reasonable chance of revealing an integration/regression failure;
- they do not require broad unrelated setup.

Examples:
- change → save → reopen/read back;
- move → jump → land → move again;
- open → modify → confirm → reopen;
- submit → navigate to resulting state → refresh/reload when persistence is part of the flow.

Do not turn every local fix into a complete product regression test. Stop when the target and the smallest useful adjacent path are proven or when additional exploration has sharply diminishing value.

### 8. Classify findings without expanding authority

Classify material observations by relationship to the current verification scope:

- `TARGET_FAILURE` — the requirement/acceptance claim itself fails.
- `COUPLED_REGRESSION` — a directly connected behavior is broken or likely broken by the current change/path.
- `ADJACENT_DEFECT` — a real defect is visible in the already-exercised local surface but is not required to prove the target.
- `UNRELATED_OBSERVATION` — a plausible issue outside the current change/acceptance boundary.

Broad observation does **not** grant broad write scope.

- Target failures and coupled regressions normally block the relevant completion claim.
- Adjacent defects should be reported and fixed only when the current authority/scope or project acceptance requires it.
- Unrelated observations should be reported/recorded when material, not silently converted into opportunistic cleanup.

If the acceptance requirement itself is broad (for example, an entire screen/user journey must match an approved state), then defects within that required whole are target failures, not merely adjacent findings.

### 9. Route correction through existing project truth

When a finding requires investigation/correction, reuse existing navigation and architecture artifacts before broad source discovery.

Possible project-provided routes include:
- project/repository index;
- responsibility/system map;
- capability/contract map;
- runtime/integration trace;
- user-flow/acceptance mapping;
- Blueprint/registry;
- implementation anchors.

Use this pattern:

```text
observable failure
→ existing route/index/trace
→ likely implementation anchor
→ validate anchor against current code/runtime
→ broaden discovery only if missing/ambiguous/stale/contradicted
```

Do not create a second QA/debug architecture graph when the project already has canonical routing artifacts.

When responsibility ownership, reuse, capability boundaries, or architecture are material, hand the preserved observable evidence to the primary agent's canonical Core-First reverse-debug procedure. If the host cannot concurrently load both procedures, finish this verification with evidence/findings; the primary agent then loads Core-First and continues from that evidence.

### 10. Re-test after correction

After a correction, repeat:
1. the exact previously failing observable path;
2. the settled-state check;
3. the smallest relevant adjacent regression path.

Do not substitute a new static/code proof for the runtime failure that originally motivated the correction.

## Raw evidence traceability

For every **material** observable completion claim, keep the raw evidence traceable at least through the current completion/review boundary. A later reviewer/primary agent must be able to determine what actually established the before state, action, settled-after state, and material adjacent findings instead of receiving only `VERIFIED | FAILED | INCONCLUSIVE`.

Prefer reuse over new machinery:
1. if the project already has an Evidence store, acceptance record, CI/test artifact location, project-index evidence pointer, or equivalent canonical mechanism, use it according to the project's rules;
2. otherwise retain the raw evidence in the current working/session artifact boundary and return precise references/locations sufficient for the primary agent or reviewer to inspect it;
3. do **not** create a new repository-wide evidence database, QA graph, screenshot archive, or persistence framework solely to satisfy this Skill.

Evidence provenance should identify, where applicable:
- before-state evidence/reference;
- action/input actually exercised;
- settled-after evidence/reference;
- material adjacent-check evidence/reference;
- revision/run/scope identity needed to avoid confusing stale evidence with the current change.

If raw evidence cannot be retained or referenced reliably enough for a material claim, state that limitation. Do not strengthen the status beyond what the remaining evidence supports.

## Status rules

For the target observable claim, return one status:
- `VERIFIED` — the required observable outcome was exercised on an appropriate real boundary and matched the requirement with sufficient evidence;
- `FAILED` — the target outcome or a completion-blocking coupled behavior demonstrably failed;
- `INCONCLUSIVE` — the necessary surface, state, capability, or trustworthy evidence was unavailable/ambiguous enough that the claim cannot be verified.

Absence of evidence is never `VERIFIED`.

Ambient/adjacent findings are reported separately and affect the target status only when they contradict the target acceptance scope or materially block the required user/external journey.

## Output contract

Use a compact evidence-oriented shape:

```text
STATUS: VERIFIED | FAILED | INCONCLUSIVE
CLAIM: ...
SURFACE/BOUNDARY: ...

EXERCISE:
- before: ...
- action: ...
- settled after: ...
- adjacent checks: ...

FINDINGS:
- TARGET_FAILURE | COUPLED_REGRESSION | ADJACENT_DEFECT | UNRELATED_OBSERVATION: ...

EVIDENCE:
- raw/provenance refs: ...
- before ref: ...
- settled-after ref: ...

LIMITATIONS:
- ...
```

Omit empty sections except `STATUS`, `CLAIM`, `SURFACE/BOUNDARY`, and `EVIDENCE`.

## Safety and side effects

Prefer reversible, isolated, non-destructive verification paths. Do not create irreversible external side effects merely to gain stronger evidence unless the user/project explicitly authorizes that operation or a safe test environment makes the action appropriate.

When realistic verification could mutate important data, spend money, contact real users, publish content, or trigger other consequential effects, use the project's safe test/sandbox path where available or report the limitation.

## Anti-patterns

Do not:
- infer product success from code appearance alone;
- infer outcome success from a successful interaction/tool call;
- stop at the first transient frame when settled behavior matters;
- inspect only the target element while ignoring material layout/design/placement/state contradictions already visible in the same acquired screenshot/frame;
- treat element presence or correct style/tokens as proof when applicable surface authority requires different layout, placement, hierarchy, or composition;
- invent exact coordinates when the project authority specifies only relative spatial intent;
- treat a generated Working View/Atlas/mockup as project authority;
- treat logs/telemetry/internal success state as a substitute for a material user-visible result;
- capture redundant screenshots to re-prove unchanged visible facts already established by a current trustworthy snapshot;
- reuse a stale visual snapshot after a relevant visual/state-changing modification;
- treat a newly written evidence artifact or successful capture/observation call as proof that the observation path is live/current when freshness is material;
- declare an observation path dead from identical samples alone when the observed state may legitimately be static;
- treat a static screenshot as proof of interaction or temporal behavior;
- perform a full-product exploratory audit for every local change;
- fix unrelated observations without scope/authority;
- silently downgrade a required real-surface check to static evidence;
- create a parallel project map or ownership graph for QA;
- persist every verification into a new evidence system when the project has no such requirement;
- return only an interpreted status for a material observable claim when the raw evidence cannot be traced through the current completion/review boundary;
- bypass the normal product path to prove a user-facing workflow unless the requirement explicitly concerns the bypassed interface;
- require any specific provider, browser, computer-use implementation, scripting language, tool protocol, or interaction technology.
