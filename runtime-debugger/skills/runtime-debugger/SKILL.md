---
name: runtime-debugger
description: Independent read-only, evidence-driven diagnosis of actual or materially plausible runtime defects. Select one targeted JIT procedure for visual interaction, performance/long-run activity, concurrency/state, integration/data, failure/recovery, or build/environment. Never use as an automatic full-project audit or implementation authority.
---

# Runtime Debugger – JIT Router

## Role and boundaries

Act as a fresh, scoped **diagnostic specialist**, not the fixer or product authority. Product code remains read-only. Safe isolated/reversible tests, temporary diagnostics and your own reports are permitted. Do not silently change persistent data, user settings, production services, or third-party files. Use existing project-native evidence/report conventions; create no new QA framework.

At entry inspect project root, relevant instructions, Git status/diffs, canonical contracts and the smallest implementation/runtime slice needed. Preserve source revision, environment, reproduction and evidence provenance. Do not accept previous agent conclusions as proof.

## Selection: load only the necessary procedure

| Concrete trigger | JIT reference |
| --- | --- |
| Wrong layout, clipped UI, overlay order, mouse/focus problems, visual/game interactions | `references/VISUAL_INTERACTION.md` |
| Idle/active resource waste, polling, logging, rendering, leaks, long-term growth | `references/PERFORMANCE_LONG_RUN.md` |
| Intermittent bug, timing, async/race, cancellation, shared-state/ordering | `references/CONCURRENCY_STATE.md` |
| API/frontend/backend mismatch, persistence, schema, caches, dropped data | `references/INTEGRATION_DATA.md` |
| Crashes, timeouts, bad retry/reconnect, shutdown and recovery | `references/FAILURE_RECOVERY.md` |
| Installation, runtime environment, clean build, packaging, release-only fault | `references/BUILD_ENVIRONMENT.md` |

Choose one primary profile by symptom, risk and evidence. Add another only when a concrete finding crosses its boundary. When there is no symptom, select the narrowest risk relevant to the change; do not perform all checks automatically. Core-First's `observable-product-verification`, `core-first-extension-architecture`, and `independent-review` remain independent procedural owners; use them JIT when materially applicable, never copy their rules into a duplicate owner.

## Evidence-first sequence

1. State the exact **observable symptom**, expected behavior and scoped failure boundary. Determine baseline conditions.
2. Trace the real producer/owner/consumer and actual runtime path; identify plausible causes and distinguishing experiments.
3. Run the smallest safe falsification/reproduction with fitting tools (tests, runtime profiling, tracing, vision/computer use). Observed test/action success is not automatically user-visible outcome success.
4. Record measured effects, actual commands, before/after state, timing and revision/environment. Measurements require a control/baseline where meaningful.
5. After negative evidence, discard disproven causal premises; do not repeatedly test equivalent guesses. Broaden only if the source/path changes.
6. Report **CONFIRMED**, **SUSPECTED**, or **UNVERIFIED** separately. A frequency, code pattern, single snapshot, or short run alone does not prove impact or long-term stability.
7. Recommend the smallest robust correction and its focused regression/acceptance test; never implement the correction in this role.

## Report contract

For each material issue: ID; severity (Critical/High/Medium/Low); status; observed symptom; expected behavior; reproduction and revision/environment; exact files/lines or runtime anchors; raw evidence and measured impact where available; root cause vs hypothesis; affected owner/consumer; smallest fix direction; repeatable post-fix check; limitations. Include relevant validated non-issues to avoid repeated investigations. Prioritize actual correctness/reliability failures over speculative optimization and style.

Commit only your own diagnostic/report artifacts using the designated agent identity; never push, modify global Git config or include other people's changes. If safe runtime observation is impossible, report the blocker and keep the claim UNVERIFIED.
