# Phase 6 – Agent Blueprint

**Agent: Blueprint Agent**  
**Skill: Agent Blueprint**  
**Git identity: Follow applicable project and harness instructions; the role is not the commit author.**

Project: `<ABSOLUTE_PROJECT_PATH>`

Create or update the agent-readable documentation to enable a fresh agent to understand, reconstruct, modify, and test an isolated functional area with minimal context.

Inspect repository root, instructions, Git status, relevant diffs, APC authorities, product/runtime implementation, and verification evidence.

- Keep `BLUEPRINT.md` short and useful as the project entry point.
- Link to canonical owners, public contracts, flow/state/integration boundaries, acceptance and evidence.
- Add scoped contracts only for genuinely independent semantic boundaries; do not duplicate existing APC authorities.
- Distinguish required, observed, verified and unresolved behavior.
- Preserve important design/user-surface authority and negative/failure behavior where material.
- Avoid unnecessary documents, registries, or code summaries that become stale.
- Leave **product code unchanged**.

**Completion:** Validate project consistency and, when practical, perform a fresh-agent reconstruction challenge on one representative area. Commit only your own documentation changes locally as the specified agent. No push or global Git configuration changes.
