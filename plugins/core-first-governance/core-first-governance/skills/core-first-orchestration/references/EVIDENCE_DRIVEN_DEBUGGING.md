# Evidence-Driven Debugging

Read this procedure for an active runtime/product defect investigation when observed symptoms, negative tests, or new evidence can change the causal search space.

## Route from the real surface, not resemblance

Visual/runtime resemblance is a clue, not source identity. Start from the observable surface and runtime/ownership route. Preserve symptom facts and **observable identity**; a nearby/easier defect does not replace the reported symptom merely because it shares a subsystem, resemblance, or evidence surface. Treat it separately until evidence establishes the same causal problem. Source bounds need not match the visible artifact.

```text
observable symptom
→ owning runtime surface / flow
→ canonical owner / path
→ nearest relevant region / parent
→ candidate producer
→ effective runtime geometry / state
→ focused falsification
→ root cause
```

**VISIBLE FOOTPRINT != PRODUCER BOUNDS.** A small/differently bounded child may produce a larger artifact through content sizing, parent layout, clipping/overflow, transforms, stretch/fit/expand, or equivalents. Do not reject a candidate because declared size differs from produced pixels.

Inspect only material effective-geometry mechanisms: declared/minimum/content size, parent constraints, anchors/layout, clipping/overflow, transform, stretch/fit/expand, render bounds, or equivalents. These are categories, not provider-specific law.

## Falsification shrinks the model

A negative test is consumed only when it changes the active model. If evidence rules out an owner, subtree, dependency, or causal premise:

1. remove that premise **and hypotheses that depend on it** from the active search space;
2. do not continue generating variants of the disproven hypothesis family;
3. re-derive the remaining causal search space and next highest-information check before material work;
4. if current evidence contradicts the assumed owner/route, retrace or broaden from the observable instead of defending the stale model.

Prefer the smallest safe falsification that distinguishes causes. Preserve what it eliminates; do not accumulate tests whose consequences are never applied.
