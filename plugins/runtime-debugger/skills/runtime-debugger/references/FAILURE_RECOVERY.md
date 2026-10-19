# Failure & Recovery Debugger

**Trigger:** unexpected crash, silent error, stuck retry, timeout, reconnect/restart/shutdown issue, corrupted partial work.

1. Enumerate relevant failure boundaries only: startup, I/O, dependency unavailable, invalid input, timeout, cancellation, partial write, restart, disposal and recovery.
2. Inspect exception ownership, logging severity, retry/backoff/jitter, limits, idempotency, cleanup/finally paths, connection/task lifetimes and persistence/rollback.
3. Apply safe controlled fault injection only in an isolated environment. Trace before-failure state, failure stimulus, recovery and settled post-recovery behavior.
4. Look for swallowed exceptions, retry storms, irreversible duplicate side effects, resource leaks after exceptions, stuck state and broken shutdown.
5. Distinguish intentional degradation from silent success claims. Do not trigger consequential external actions merely to reproduce a failure.
6. Return exact recovery sequence, evidence, impact and minimal corrective path with repeatable failure-regression test; do not edit product code.
