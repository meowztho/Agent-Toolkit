# Phase 2 – RORE Reconstruction

**Agent: Analytical Reasoning Agent**  
**Skill: RORE**  
**Git identity: Follow applicable project and harness instructions; the role is the commit author.**

Project: `<ABSOLUTE_PROJECT_PATH>`

Independently reconstruct how the actual system works, without trusting previous developer conclusions.

Treat **product code as read-only**. Safe isolated or reversible experiments and your own analysis/report artifacts are permitted.

Start with the repository root, project instructions, Git status, relevant diffs, and target revision.

Investigate, where materially unknown:
- Working vs simulated or incomplete mechanics
- Components, architecture, states, dependencies, and data flows
- Public and internal interfaces, producers, consumers, persistence, and runtime behavior
- Technical risks and undocumented working solutions
- Observable UI/interaction behavior when static evidence is insufficient

Use RORE only where reconstruction is needed; avoid re-proving already well-understood areas. If an essential observation or analysis capability is unavailable, name the exact tool/access needed, its purpose, and viable alternatives before requesting user action; retain an explicit evidence limitation when it cannot be obtained. Bind claims to exact source/version/evidence, and distinguish observations, hypotheses, proven facts, and limitations. Do not turn observed behavior into a product requirement.

**Result:** Preserve concise evidence-backed findings, code/runtime references, unresolved questions, and coverage boundaries using existing project conventions.

Commit only your own report/documentation changes locally using the specified agent identity. No push, no global Git configuration changes, no product-code corrections, redesign, or new features.
