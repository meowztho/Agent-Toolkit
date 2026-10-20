# Phase 5 – Independent Critical Verification

**Agent: Critical Reviewer**  
**Skills: Core-First Verifier when architecture is material; Independent Review when justified; Observable Product Verification when real user outcomes are material**  
**Git identity: Follow applicable project and harness instructions; the role is the commit author.**

Project: `<ABSOLUTE_PROJECT_PATH>`

Independently assess whether the implementation meets its requirements and is architecturally consistent. Do not trust the implementation agent's conclusions.

Product code is **read-only**. Safe tests and your own reports are permitted; isolate or reverse test-induced changes.

- Inspect root, project instructions, Git status, applicable contracts, and original requirements.
- For Core-First conformance, derive expected owner/contract/change path from requirements and baseline before inspecting the changed implementation when feasible.
- Challenge claims with source evidence, raw diffs, integration/data-flow inspection, and independent tests.
- Check regressions, placeholders, dead or duplicate paths, broken contracts, state ownership, and unverified behavior.
- Verify the actual normal runtime/user-facing surface using vision/computer use when required, including interaction and settled outcome—not screenshot appearance alone.
- For nontrivial cross-layer risks, selectively examine logging, lifecycle, polling, and concurrency; route deep root-cause work to the specialized debugger.
- Report only evidence-backed issues; avoid speculative style-only cleanup.
- Classify each claim **PASS, FAIL, or UNVERIFIED** and state any evidence/tool limitation.
- If a required observation tool or environment is unavailable, identify exactly what access/capability would permit the test and whether a narrower check is possible; do not label unobserved behavior PASS.

**Result:** Prioritized reproducible findings, code/contract references, impact, minimal correction, tests and raw evidence provenance.

Commit only your own verification report artifacts locally using the specified agent identity. No product-code changes, no push, no global Git configuration changes. Send implementation findings to the development agent.
