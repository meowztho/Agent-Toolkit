# Performance & Long-Run Debugger

**Trigger:** unexplained idle CPU/GPU usage, log or cache growth, polling/rendering load, resource retention or prolonged-operation slowdown.

1. Establish normal workload and meaningful idle, active, repeated-action and shutdown/restart baselines.
2. Inventory timers, polling intervals, retries/backoff, event subscribers, update/render loops, log sinks, buffers/queues, allocations, handles, sockets and persistence writes **on the relevant path**.
3. Measure where possible: CPU/GPU and wakeup activity; memory/private bytes/heap trend; handles/threads; render rate; disk/network bytes; log rate, size/retention and write frequency. Compare with a control and disclose environment/tool overhead.
4. Distinguish bounded intentional polling and logging from redundant work. Event-driven alternatives are suggestions only when same semantics and reliability can be maintained.
5. For accumulation claims use repeated actions and bounded time-series observations; isolated working-set memory values or high polling frequency alone do **not** prove leak or excessive load.
6. Check cleanup on close, deactivation, process exit, exception and reinitialization; avoid unsafe artificial long runs or disruptive production load.
7. Report reproducible measured trend and expected impact, uncertainty for extrapolations, root-cause candidates, smallest correction and post-fix idle/active regression measurements.
