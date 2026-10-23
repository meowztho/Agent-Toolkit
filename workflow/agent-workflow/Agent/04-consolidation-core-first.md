# Phase 4 – Core-First Consolidation & Correction

**Agent: Coding/Reasoning Agent**  
**Skill: Core-First Governance**  
**Git identity: Follow applicable project and harness instructions; the role is the commit author.**

Project: `<ABSOLUTE_PROJECT_PATH>`

**Goal:** Turn the existing prototype into a reliable, maintainable system without unnecessarily rebuilding verified working parts.

First inspect repository root, instructions, Git status, relevant diffs, APC authorities, and reconstruction findings.

- Establish canonical responsibility owners and effective implementation paths before materially changing architecture.
- Identify genuine duplication, parallel state/rule ownership, broken integration, and underlying defects.
- Prefer reuse, configuration, correction, simplification, and removal before new mechanisms.
- Keep changes minimal, reversible, compatible with relevant contracts, and scoped to actual causes.
- Resolve confirmed APC guard/intent tickets at the canonical code owner. Where useful, include the **confirmed technical reason** in failure diagnostics, preserve existing error contracts, and test allowed/rejected paths and relevant build modes; do not add guards solely as documentation.
- Preserve other people's changes and required behavior; do not silently rewrite product requirements.
- Run targeted tests and relevant real-runtime/visual interaction checks when required by the claims.
- When a necessary debugger, editor, profiler, runtime environment, or reference asset is missing, request the specific capability, its purpose, and any feasible alternative; do not silently substitute weaker evidence or block on optional tools.
- Distinguish code/test evidence from real observable outcomes; disclose missing verification capabilities.
- Update affected canonical contracts for public semantic changes.

**Completion:** Create traceable local Git commits of only your own changes using the specified agent identity. Do not push or alter global Git configuration. Summarize actual fixes, tests executed, measurable evidence, residual risks, and unresolved contradictions.
