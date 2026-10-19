---
name: independent-review
description: Independently review consequential, high-risk, difficult-to-verify, or materially blocked implementation work. Use for an unbiased read-only review after the primary agent has performed its own verification. Do not use for routine changes.
metadata:
  short-description: Unbiased read-only review of high-risk implementation work
---

Use a narrowly scoped read-only reviewer only for consequential, high-risk, difficult-to-verify, or materially blocked work. The reviewer may be a fresh delegated review agent, a separate model/context, or an available external model through a configured provider/model bridge. Do not wait for unavailable or rate-limited reviewers or duplicate routine investigation. Review supplements, never replaces, the primary agent's own investigation and verification.

To avoid anchoring, give the reviewer the original requirements, complete applicable instructions, relevant raw diffs and files, verification commands with their actual output, and relevant **raw observable/runtime evidence** already acquired (for example screenshots, interaction traces, before/after state, persistence read-back, or external-state observations). Do not pass the implementation agent's narrative, conclusions, confidence, or justification. When observable-product verification was performed, do not pass its interpreted status, conclusion, confidence, or finding narrative before the independent reviewer has derived its own findings from the raw evidence. The reviewer must independently derive the expected behavior from the original requirements and verify material claims directly when necessary and feasible.

Require evidence-based findings that materially affect correctness, stated requirements, regressions, security, or maintainability; exclude style-only, speculative, and unnecessary hardening suggestions. The primary agent must fix, reject with evidence, or explicitly accept each material finding, with at most one challenge-response round. Use a different model or genuinely fresh independent context for additional review only when a high-risk issue remains unresolved.
