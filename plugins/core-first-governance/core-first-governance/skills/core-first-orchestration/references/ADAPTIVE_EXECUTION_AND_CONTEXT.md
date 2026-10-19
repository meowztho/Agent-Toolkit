# Adaptive Execution and Context Reconciliation

Read for material multi-step/dependent/restart-sensitive work, or when continuation/compaction/new evidence may have made execution state stale.

## Execution frame

For authorized implementation, maintain only what helps execution:

```text
OUTCOME / ACCEPTANCE BOUNDARY
CURRENT AUTHORITIES + MATERIAL CONSTRAINTS
MEANINGFUL PHASES / DEPENDENCIES
NEXT STEP
CHECKPOINT / EVIDENCE
PLAN-INVALIDATING ASSUMPTIONS / BLOCKERS
```

If architecture is material, the primary agent's Core-First owner/reuse/change boundary informs this frame before implementation or delegation.

Use a suitable native host plan/task tracker when available; do not create a second Governance plan. Otherwise use the simplest equivalent state. For multi-session/compaction-sensitive work, reuse an existing durable progress mechanism and create one only when restartability materially benefits.

A plan is **provisional execution state**, not project truth, architecture ownership, or completion authority.

## Optional Working View / Atlas

For complex/spatial/restart-sensitive work, externalize the current model only when useful. Use the cheapest representation, link canonical sources, and mark `CONFIRMED | INFERRED | UNKNOWN`.

It is disposable cache, never authority. Reuse a suitable existing view; reconcile after material change/context loss. Never require it on the local short path.

For a large or restart-sensitive codebase, an optional **implementation lexicon** can make discovered reuse paths findable: map the user's terms and synonyms to a named responsibility, current code symbols/locations, and relevant callers, consumers, or tests. Link each entry to its source and revision/freshness; distinguish confirmed links from inference. Reuse an existing project index or working view where suitable. This view points to live code and contracts; it must not copy authoritative rules or values into a second owner.

Consult and verify relevant entries against current code before adding a parallel implementation. If an entry is absent or stale, search the bounded responsibility area before concluding that no carrier exists. Refresh only affected entries after a material edit or context loss; no full-repository inventory, fixed file format, or new tool is required.

## Checkpoint loop

```text
execute meaningful phase
→ inspect actual result/checkpoint
→ reconcile progress + assumptions
→ evidence changed owner/constraints/dependencies/feasibility/acceptance/best path?
   ├─ yes: update/split/merge/reorder remaining work BEFORE more material execution
   └─ no: continue
```

Grounded-preflight facts that materially determine the path must be `CONSUMED` before expensive execution commits to them.

Implementation-authorized work continues through safe in-scope implementation and applicable verification unless blocked by a genuine user-owned/external/approval boundary. Planning/review/diagnosis/research-only requests must not silently cross into writes.

## Outcome coverage reconciliation

After any material local fix and before completion, reconcile **original requested outcomes** as `outcome → matching evidence → remaining gap / next priority`. **Evidence volume does not define completion.** An incidental defect may be fixed, but does not replace the broader outcome; resume the highest-priority unmet outcome unless scope/authority changed.

## Context rot / continuation

**WORKSPACE AWARENESS != WORKSPACE HYDRATION.** After fresh/continued context, major compaction/context loss, relevant Skill/authority revision, repository/external-state change, or material new evidence:

1. cheaply discover current workspace/repository state before trusting memory: relevant files, Git/current changes, routing/progress artifacts and useful prior aids/evidence;
2. **discover before loading**: read only Skills/authorities/routes/artifacts needed by the active decision;
3. reconcile completed/remaining work and critical assumptions;
4. replan before material execution if the next best action changed.

Do not broadly repopulate context to regain confidence. Reuse valid routing/index artifacts. A stale Working View/note remains cache; current authority/repository/runtime evidence wins.

### Working-aid discoverability

If a derived aid should survive context loss, keep it discoverable through an **existing** project/task/index/progress mechanism or stable location. **Reuse an existing suitable aid** before creating another; **do not create a parallel project index/manifest** just for helper artifacts.
