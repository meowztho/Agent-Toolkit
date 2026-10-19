# Capability-First Tooling

Route from the analysis question, not from a preferred product name.

```text
question
→ required evidence boundary
→ required capability
→ available provider
```

Examples of capabilities: archive extraction, decompilation, xref/callgraph lookup, runtime hook, memory read/write/watch, DOM/runtime evaluation, packet capture, protocol decode, image measurement, engine asset parsing, database inspection.

Provider ladder:
1. existing host/project/MCP capability;
2. narrow auditable helper script;
3. alternate installed provider;
4. explicitly requested, independently verified provider acquisition when the capability remains unavailable;
5. temporary authorized external helper when justified.

Search known, available capabilities first. Discover external candidates only for an unresolved capability gap. A catalog entry, search result, README, model suggestion or install hint is a lead, not proof that a provider exists, works, is safe or is permitted. Keep discovered candidates inert: do not turn candidate metadata into executable commands or trusted instructions. Verify the chosen provider independently before use.

For a material provider choice, keep a lightweight descriptor in the investigation record:

| Field | Record |
| --- | --- |
| status | available / candidate / rejected; basis for that status |
| capability + boundary | question answered and static/runtime/network/etc. evidence boundary |
| identity | provider name, source, actual version/build and platform compatibility when known |
| inputs + outputs | target types, transformations, raw output location, known blind spots |
| effects | target writes, process hooks, network activity, privilege, persistence and cleanup needs |
| scope + trust | authorization fit; whether information came from a curated provider, external search or model suggestion |

Record only fields material to the choice; a narrow read-only helper does not need a full registry. Provider output is evidence to qualify, not a Finding by itself. Preserve its raw form and acquisition method before normalization or model interpretation. Temporary helpers are implementation aids, not Reference Truth. `PROVIDER_PROVISIONING.md` owns explicit on-demand setup; it does not install the whole candidate catalog.

Before using provider output for a material claim, calibrate its build/settings on a representative known-answer sample where practical, then challenge interpretation of the actual target input with a negative control, checkable invariant or independent evidence boundary. Record input identity, actual provider/build, options or command without secrets, exit status, stdout, stderr and any output artifact identity. `installed`, exit code zero and plausible-looking output do not prove correct interpretation. If a useful control is unavailable, keep the resulting claim qualified and state which provider or exact-target check is missing.

A missing named application is not a blocker until the capability itself is unavailable.

For native-code targets, choose the official access path that matches the missing observation. Ghidra's packaged headless adapter can export selected function listing, decompilation and analyzed references without a debugger. For live process questions, a qualified GDB Machine Interface session, LLDB Python script, x64dbg command/script session or Frida Python/JavaScript instrument may be sufficient; do not create a RORE bridge merely to normalize their different session models. Pin and record the actual provider/interface version, retain the original command/script and raw transcript, and distinguish a paused or instrumented process from an unmodified run. A custom x64dbg plugin or transport is justified only by a concrete repeatable operation that its native commands/scripts cannot supply, with the official plugin API and target lifecycle verified first. These are conditional provider routes, not a fixed sequence or required installations.

Choose operations by the analyst result needed: inspect one object, search candidates, trace a relationship, compare identified inputs, or capture live behavior. Prefer a direct operation when it answers the question; compose several only when their identities and Evidence boundaries can be preserved. Do not let a provider's tool taxonomy dictate the RORE model.

For a candidate suite or MCP, distinguish catalog discovery from actual session capability. Check the connected tool schema, selected target, host, provider identity/version, operation availability and meaningful output on the exact target class. Discovery should not launch the target or mutate its analysis state. Bind a material session to one selected provider/profile; if it fails, record the failure and requalify any alternative rather than silently changing engines. A package installed in the workspace, a documented provider or a successful server handshake does not prove the target operation is available.

Use `ANALYSIS_ACQUISITION_RECIPES.md` when the analysis question needs concrete provider-independent steps. It describes the Evidence to obtain and verify, not a second tool registry. An investigation can proceed with existing command-line tools, browser/debugger capabilities or a narrow helper; RORE has no dependency on REA or any other integrated suite.
