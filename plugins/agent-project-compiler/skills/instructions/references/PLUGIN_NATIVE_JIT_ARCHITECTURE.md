# Plugin-Native JIT Architecture — APC v2.35.2

## Purpose

This file owns APC plugin packaging/context-routing semantics. It does **not** own project truth, product architecture, Acceptance, or implementation behavior.

The canonical runtime shape is:

```text
one APC orchestrator Skill
→ compact always-active kernel
→ material-trigger router
→ smallest JIT procedural/reference slice
→ project authorities and companion procedures as needed
```

`ALL INFORMATION MUST BE REACHABLE != ALL INFORMATION MUST BE LOADED`.

## No Custom-GPT file-count policy

The historical Custom-GPT 20-Knowledge-file limit is not an APC architecture rule in the plugin host.

```text
REFERENCE FILE COUNT != MATERIALITY
```

Split or combine references according to:
- one coherent procedural responsibility;
- a meaningful independent trigger;
- context cost of loading the whole file;
- whether the agent can act correctly after loading only that slice;
- preservation of one canonical detailed owner for each rule.

Do not split merely to create smaller files when the slices always need to be read together.

## JIT granularity

`skills__read` loads a selected supporting file as a whole. Therefore instructions such as “read only one section of a 98 KB file” are not a real context boundary in this host.

A JIT reference should be small enough that loading the whole reference is appropriate for its trigger. Large template libraries should be grouped by artifact family; procedural guides should be split only at stable material decision boundaries.

## Router ownership

The APC root Skill remains the single orchestrator. Supporting references are procedure/detail owners, not sibling orchestrators and not project authorities.

Do not create a second APC router merely because a reference family is large. Add a separately discoverable top-level Skill only after empirical evals show that independent host triggering materially improves reliability without creating competing compiler ownership.

## Context-rot prevention

The root kernel always preserves:
- Product Truth != Realization Truth != Verification Truth;
- project authorities outrank chat/provider memory and generated views;
- one canonical owner per durable responsibility;
- project-native routing/read gates;
- evidence-derived completion;
- exact approval/admission boundaries;
- context invalidation and minimal JIT rehydration;
- companion Core-First routing when architecture/reuse/ownership is material.

After context loss, rediscover current state and load the smallest active owner set. Do not load the full APC reference catalog to regain confidence.

## Compatibility redirects

Old monolithic paths may remain as tiny compatibility routers because account plugin updates cannot delete files. A compatibility router must:
- declare itself non-authoritative;
- point to the current canonical JIT slices;
- contain no competing copy of the old policy;
- never be the preferred route from the root Skill or `REFERENCE_INDEX.md`.

Legacy lookup files may remain as explicit inactive markers when deletion is unavailable.


## Host resource-snapshot drift

Account-plugin release metadata, the root Skill, and supporting-resource exposure may refresh at different times. A routed `Resource not found` therefore does **not** by itself prove the release omitted that file.

When a canonical routed reference cannot be loaded:

1. rediscover the installed APC Skill through host Skill discovery;
2. re-read the current root Skill / `REFERENCE_INDEX.md`;
3. retry the canonical path once if the route is still current;
4. if the mismatch persists, classify `PLUGIN_RESOURCE_SNAPSHOT_DRIFT`;
5. continue only with actually reachable current references + project authorities where that is sufficient;
6. do not silently promote a legacy compatibility path into canonical policy and do not claim a procedure was loaded when it was not;
7. report the degraded compiler boundary and leave any claim depending on missing procedure detail unresolved/inconclusive.

A compatibility redirect may help only when its current canonical target is itself reachable. Refreshing/restarting the host context can be the correct recovery when release propagation is the cause.

Plugin maintenance verification should distinguish:

```text
file absent from current release inventory
!=
file present in release but unavailable in current host resource snapshot
```

Use account-plugin source/readback to test the first claim and host `skills__read` behavior to test the second.

## Validation

A plugin-native APC release should prove:
1. every active JIT reference is reachable from the root routing capsule or `REFERENCE_INDEX.md`;
2. compatibility files are not preferred routes;
3. no historical file-count ceiling constrains policy decomposition;
4. a template request routes to one artifact-family slice rather than the legacy template monolith;
5. context-loss recovery loads current project routing/state + only material APC references;
6. architecture materiality routes to companion Core-First when installed;
7. Fresh-Agent Reconstruction can still recover the complete compiler/project model through routing, despite selective active context;
8. a missing JIT resource is classified as release absence vs host resource-snapshot drift before falling back.
