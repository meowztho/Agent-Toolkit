# Concurrency & State Debugger

**Trigger:** intermittent failure, race, async ordering, lock contention, stale callbacks or inconsistent shared state.

1. Identify shared mutable state, canonical owner, threads/tasks/event loops, locks, queues, callbacks, transaction boundaries and lifecycle.
2. Build a narrow happens-before timeline and expected invariants for the reported symptom.
3. Test applicable classes: race/lost update; TOCTOU; reentrancy; duplicate event/initialization; lock-order deadlock; livelock/starvation; stale snapshot; cancellation vs completion; non-atomic publish; idempotency violations; shutdown races.
4. Use deterministic scheduling or controlled repeated concurrency tests where available; preserve thread/task IDs, timestamps, event order and revision.
5. A flaky failure not reproduced is not proven absent; distinguish true data races from eventual-consistency behavior explicitly allowed by contracts.
6. Identify the canonical owner and smallest ordering/state-lifecycle correction; do not introduce locks or frameworks by default and do not modify product code.
