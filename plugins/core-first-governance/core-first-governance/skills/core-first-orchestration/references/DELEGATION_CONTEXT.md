# Delegation and Context Isolation

Read this procedure before delegating implementation, architecture advice, investigation, or verification work.

## Context envelope

Every delegated lane gets minimum sufficient context, selected explicitly:

```text
ROLE
SKILL KNOWLEDGE
PROJECT/TASK CONTEXT
EXCLUDED CONTEXT
WRITE / DECISION AUTHORITY
FRESHNESS / PERSISTENCE
EXPECTED OUTPUT / EVIDENCE
```

Do not assume delegated agents inherit the primary agent's loaded Skill state.

## Targeted worker

Use when architecture/ownership boundaries are already canonical.

Give: exact requirement slice; canonical owner/capability/contract boundary; relevant files/interfaces/data flow; material grounded facts; allowed write scope; forbidden bypasses; acceptance/verification evidence.

Do **not** give Core-First "just in case". If unresolved ownership/reuse/capability/extension/foreign-authoritative-state questions appear, the worker returns `ARCHITECTURE_DECISION_REQUIRED` rather than inventing architecture.

A targeted worker may use `observable-product-verification` for a bounded runtime/product-verification lane when that procedure is material and doing so does not expand the worker's write/decision authority.

## Core-First advisor/worker

Use when the delegated lane itself must investigate architecture-relevant questions.

Give: faithful requirement; applicable project instructions; relevant canonical authorities/raw evidence; canonical `core-first-extension-architecture` fresh; specific architecture question/scope.

Avoid priming with the primary agent's preferred conclusion when independent architecture analysis is desired. A persistent advisor cannot be the final independent verifier of its own work.

## Investigator

Use for bounded evidence gathering: call graph, failing-test localization, API behavior, file discovery, profiling/benchmark evidence, product-surface observation, or similar.

Give only the evidence question and necessary context. If the lane reaches an architecture decision boundary, return evidence and escalate rather than deciding outside authority.

## Integration

The primary agent inspects every delegated result and reconciles it against the original requirement, project instructions/authorities, primary Core-First reasoning when material, current repository/diff, tests, and material real-surface behavior. A delegated conclusion is never accepted merely because a Skill was used.
