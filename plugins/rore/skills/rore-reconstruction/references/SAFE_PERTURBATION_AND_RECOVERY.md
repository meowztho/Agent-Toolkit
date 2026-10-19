# Safe Perturbation and Recovery

Before a probe that can mutate persistent state, identify:
1. the exact claim/hypothesis;
2. plausible side effects and residue;
3. the least invasive representative environment;
4. a baseline/snapshot where practical;
5. cleanup/recovery and failure handling;
6. the observation that would justify the probe.

Re-check the exact target, account/environment, changed boundary and expected effects against the analysis scope immediately before each intervention. A broad analysis request and prior session permissions cover bounded reversible local probes of the named target; do not ask again merely because the next probe changes a value or observation point. A discovered address, new account, remote service or materially different external effect does not inherit scope. If that boundary is unresolved, keep only the affected probe pending and continue with in-scope evidence gathering.

Prefer reversible local copies, test profiles/accounts, snapshots, temp directories, sandbox services or controlled offline environments when they still exercise the required boundary without needless setup. A copy is not mandatory when it changes the behavior being tested or costs more than a controlled in-place probe. For an in-place change, record the original bytes/configuration/state and their identity, the exact intended writes, and a practical recovery action before applying it. Git commits can preserve source or text configuration where appropriate; hashes, backups, registry exports, database snapshots or other native state captures are needed for state Git does not cover. Verify the recovered state against the baseline, including relevant external effects.

Do not turn the preference for isolation into a default stop. For a bounded Windows portable-app probe, for example, inspect the launcher declarations and capture the exact pre-run process tree, target files, relevant `HKCU` keys and AppData paths. When a named path is absent, its pre-run state is absence; a disposable package copy plus a recorded removal-and-verification route may be enough for a short probe. When state already exists, export/snapshot it and define a non-destructive restoration before running. Capture descendants and the named paths during and after, then compare to the baseline. Network or other external effects need their own observation and recovery boundary. Modified settings, hooks or forced termination make the resulting observation an instrumented condition; follow with an unmodified run when normal behavior is the claim.

After the probe, verify restoration or explicitly record residue. Tool/cleanup success is not proof that state returned to baseline. If recovery fails, stop further mutations on that state until the residue and next safe action are understood.

If a material real-world side effect is not needed to learn the mechanism, do not create it.
