# Failure-Guided Reconstruction

Use when a known crash, wrong result, rejected input, hang, missing asset, protocol error or recovery defect gives a more informative entry point than a general inventory. A failure is an observed behavior of the reference, not automatically an explanation of its cause. This method also applies to intentionally induced failures within the authorized target and action boundary.

## Work backward from the observable

1. Bind the failing reference build, environment, inputs, prior state and observation path. Preserve the exact error text/code, trace, screenshot, dump or response and its acquisition time. Separate a user report or historical capture from a fresh reproduction.
2. Reproduce the smallest sequence that still fails, preferably against an unmodified baseline. Record how often it fails, when it does not, and which preconditions matter. A non-reproduction does not erase the original observation.
3. Define competing explanations at the boundary where the first meaningful divergence appears. Examples: invalid input, wrong parser or version, client transform, server validation, race, stale cache, missing resource, loader mapping, memory corruption, or failed cleanup.
4. Trace both directions: backward to the producer of the bad value/state and forward through error handling, retries, cleanup and visible effects. Identify the command/query/event, caller/callee, reader/writer, message or file edge at each layer. Mark any edge whose identity or execution is still unknown.
5. Compare a successful control or neighboring build with the failure using the same observation boundary where possible. Vary one input, state, timing or environment dimension per causal probe; capture direct and downstream differences. Use `PERTURBATION_AND_CAUSAL_PROBING.md` for deliberate faults, hooks or patches.
6. Reconnect the failure to stable artifact, function, schema, route, protocol, asset or component identities. A top stack frame, last log line, exception message or patched check may be a detection site rather than the originating fault or sole enforcement site.
7. Preserve the outcome as Evidence → Findings → Paths and a Failure/Recovery Model. Record the exact failure case as an `ORACLE-###` only when it describes repeatable behavior of the original under stated conditions; keep diagnostic interventions labeled separately.

## Select the evidence boundary

| Symptom | High-information observations | Important limit |
| --- | --- | --- |
| Crash or failed launch | exit/signal, faulting thread, module/build, stack/registers, loaded image, files and child processes | historical dump PID or address does not identify a current process or binary |
| Wrong UI result | action/state, DOM/accessibility/canvas, request/response, client transform, persistence | click success or unchanged URL says nothing about rendered content |
| Rejected request or malformed data | exact wire bytes, endpoint/version, parser, validation, state before/after | an error response need not reveal every validation layer |
| Hang or race | timestamps, partial event order, wait/dependency edges, timeout and cancellation state | one observed event ordering need not be the required order |
| Missing resource | container inventory, extraction lineage, load request, fallback, rendered effect | absent from one extractor or capture is not global absence |
| Recovery defect | pre-fault snapshot, triggering fault, partial output, retries, cleanup and residue | cleanup success does not erase the execution failure; cleanup failure does not erase earlier observations |

For a dump or trace, verify format/architecture and map recorded addresses through the correct module image, load base, section and build. Keep historical process/thread IDs distinct from live targets. When an instrument changes scheduling or behavior, retain an uninstrumented control and downgrade unsupported normal-runtime claims.

## Failure record

```text
failure ID / target identity / environment
minimal trigger + starting state + frequency
raw symptom and capture boundary
successful control or baseline
first observed divergence and competing hypotheses
backward producer path + forward recovery/effect path
discriminating probes and negative evidence
stable anchors, unresolved edges and coverage
E-### / FIND-### / PATH-### / optional ORACLE-###
```

Stop when the requested causal structure and material failure/recovery behavior are understood well enough for Reference Truth, or state the exact inaccessible boundary. A reproducible crash alone is not a complete reconstruction of the surrounding system.
