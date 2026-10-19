# Perturbation and Causal Probing

Use deliberate authorized changes when passive observation cannot distinguish competing explanations.

This method borrows the **system-thinking** behind adversarial, CTF, pwn and patch-diff work while changing the objective: reveal mechanism and causality. It is not exploit development or exploit-impact maximization.

## Core loop

```text
1. establish baseline and the assumption/invariant being challenged
2. state competing hypotheses
3. choose one material dimension / discriminating variable or boundary
4. perturb the smallest useful amount
5. observe direct + downstream differential
6. trace readers/writers/handlers/enforcement sites
7. corroborate against stable static/data/runtime anchors
8. restore state or record residue
9. record E/FIND/PATH and what remains unknown
```

## Reproducible probe record

For a material probe, use `PROBE-###` and record the reference identity/version/environment; authorization and controlled copy or account; baseline state and raw observation; competing hypotheses; exact one changed boundary, value, timing or sequence; instrument/provider/version; raw differential including errors, downstream effects and recovery; repeated result or variation; restoration check or remaining residue; and linked `E-###`, `FIND-###`, `PATH-###` with unresolved alternatives. Retain the original raw output separately from summaries.

Distinguish behavior of the unmodified reference from behavior observed under a hook, patch, debugger or other instrumentation. A diagnostic change may establish causal influence but does not by itself establish the normal reference behavior. Reference comparison cases use the unmodified baseline unless the case explicitly describes a diagnostic condition.

Before selecting a probe, map the smallest relevant assumptions as hypotheses: input type/range/shape, required prior state, once-only action, ownership of a mutable resource, parser/loader agreement, cache freshness, retry idempotency, dependency availability, and restart/rollback behavior. Do not promote these assumptions into reference requirements without Evidence. Choose the perturbation whose settled result best distinguishes the alternatives; where behavior varies, repeat enough to report the observed variation rather than asserting determinism.

## Useful perturbation families

Depending on the authorized target:
- value/range/shape boundaries;
- sequence, replay and omitted/repeated steps;
- timing/concurrency/state drift;
- parser/normalization/source-layer differentials;
- DOM/client-state or local runtime state variation;
- files/config/database state changes;
- memory/state mutation and reader/writer tracing;
- temporary local patch/hook to isolate an enforcement layer;
- controlled failure/interruption/recovery;
- controlled malformed input or fault conditions that reveal validation, error and recovery boundaries;
- before/after version differential;
- protocol/API field variation in a controlled environment.

For a stateful flow, find the minimal skip/replay/reorder/retry sequence and record whether it duplicates side effects or changes a state gate. For shared mutable state, trace `read → check → mutate/write → commit/persist → cache/queue/event propagation` and compare a bounded reordered or concurrent run with its baseline; preserve only proven causal ordering. For parser or loader disagreement, keep the raw input plus each layer's interpreted object and the effective result, including path, case, encoding, duplicate-field, overlay and configuration precedence when material. For a failure or restart, identify what survives, rolls back or self-heals and which component performs that recovery. These are conditional discriminators, not a mandatory attack pipeline.

## Interpretation discipline

A successful mutation proves that the changed boundary can influence the outcome. It does not automatically prove canonical ownership, complete mechanism coverage or safe generalization.

Map multiple enforcement sites when the rule may be layered. One bypassed/changed check can reveal a layer without proving there are no others.

In a broad reconstruction, a successful fault or bypass probe is a causal clue, not a completion signal while material behavior, state, asset use or failure coverage remains unresolved. Preserve the broken-state trace and compare it with the unmodified baseline before claiming how the reference normally works.

## Stop condition

Stop this bounded probe at sufficient mechanism understanding: once the requested mechanism and its material causal structure are sufficiently understood. A broad reconstruction continues its remaining technically accessible coverage. Do not continue into exploit stabilization, persistence, lateral movement, credential acquisition, destructive load or impact maximization merely because those techniques exist upstream.
