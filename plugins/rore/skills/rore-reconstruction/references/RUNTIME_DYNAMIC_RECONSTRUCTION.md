# Runtime / Dynamic Reconstruction

Use when effective behavior cannot be established from static artifacts alone.

Observe the closest practical authorized boundary: process tree, loaded modules/resources, files/config/registry, database/storage, network/IPC, DOM/runtime state, timing, persistence, recovery and user-visible results.

For a broad investigation, move from static capability candidates to actual scenarios: launch and normal exit, representative user actions, state creation/change/deletion, errors and recovery, and relevant concurrent or network interactions. Capture an unmodified baseline before interpreting an instrumented condition. If no observer exists for a material boundary, route to a qualified host tool or a focused script; absence of one preferred tool is not evidence that the behavior cannot be learned. Scale captures by process, flow, endpoint or subsystem while retaining raw traces and the population still untested.

Classify content/state transitions where useful:

```text
PRESENT → REFERENCED → REACHABLE → EXERCISED → EFFECTIVE
```

Do not claim the rightmost state from evidence of a leftmost state.

Runtime observations should be back-annotated into stable static/data/runtime anchors when possible. If a symptom cannot be tied to a durable identity, record it as runtime-local/candidate rather than inventing ownership.

Failed launches, crashes and recovery paths can be informative evidence when the failure boundary is captured.

For a selected command or process scenario, record starting files/configuration and environment, exact executable/arguments/input, terminal dimensions if relevant, stdout/stderr, exit/signal, child/descendant state, selected file/network effects, timing and cleanup. A root process exit does not mean its descendants settled. An observation path names what was watched; it does not confine what a running target could change. Preserve partial output when execution fails and independently record whether cleanup restored the baseline or left residue. Use `FAILURE_GUIDED_RECONSTRUCTION.md` when the error is the strongest entry point.

Compare concurrent or asynchronous traces by proven causal/partial-order constraints and state outcomes. Do not require one incidental total event order across runs. A timeout, missing event or interrupted capture can leave equivalence unknown rather than false or true.

## Debugger / trace observations

When a debugger, watchpoint, hook or trace answers a material question, capture the uninstrumented baseline and the exact input/state transition that triggers the observation. Bind the trace to process, thread, module/build and address mapping; retain the material call stack, instruction/event order, registers or memory values, and file/network/UI side effects as raw Evidence. State which breakpoint, watchpoint or instrumentation was active, when it was attached, and whether it changed timing, control flow or the outcome. Repeat or corroborate a decisive trace where practical. Resolve observed addresses back to stable functions, data objects or behaviors; an address or crash signature alone is build/session-local. For deliberate faults or temporary patches, use `PERTURBATION_AND_CAUSAL_PROBING.md` and record recovery/residue.
