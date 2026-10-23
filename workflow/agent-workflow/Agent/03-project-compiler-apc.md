# Phase 3 – APC Product Foundation & Plan

**Agent: Architecture/Planning Agent**  
**Skill: Agent Project Compiler (APC); Core-First JIT when materially relevant**  
**Git identity: Follow applicable project and harness instructions; the role is the commit author.**

Project: `<ABSOLUTE_PROJECT_PATH>`

Use APC either to compile an initial product idea or to reconsolidate a grown project against its current implementation and authorities.

**Goal:** Compile user intent, available implementation, and RORE evidence into durable, provider-neutral project authorities, a realistic implementation plan, and verifiable acceptance criteria.

Inspect the repository root, project instructions, Git status, existing authorities, source evidence, and reconstruction results. If `domain-specialist/` or an explicitly handed-off domain package exists, read its entry point and relevant `PROJECT_SYSTEM_NEEDS.md` before compiling system scope and dependencies. Treat its proposals as sourced input, not as approved requirements or a second project authority.

- Distinguish **intended product behavior**, **observed implementation behavior**, and **verified outcomes**.
- Preserve prior valid decisions and valuable working mechanics. Do not infer user requirements from code alone.
- Identify capabilities, responsibilities, canonical ownership, interfaces, workflows, dependencies, acceptance criteria, and implementation order.
- Apply Core-First yourself when architecture, state ownership, reuse, or composition is materially relevant, as APC requires.
- Use existing authorities and the project index before introducing new files. Avoid competing sources of truth.
- Mark conflicts, unresolved user-owned decisions, and evidence gaps explicitly; avoid repeated questions about established choices.
- If critical references, source access, or tools are absent, name the specific blocker and smallest required input; continue compiling all unaffected authorities without waiting on optional resources.
- In grown projects, inspect executable intent **selectively at material boundaries**: guards, type/schema constraints, state transitions, failure diagnostics, callers, and behavioral tests. Check each against current decisions and canonical owners; distinguish confirmed invariants, hypotheses, obsolete safeguards, and contract drift. Do not treat code alone as product intent.
- For confirmed actionable deficiencies, **reuse or create focused tickets in the existing project tracker**, or provide ticket-ready handoffs if none exists (no new tracker). Include exact file/function, owner, affected contract/Acceptance, observed evidence and failure mode, expected behavior, relevant regression/negative test, and open decisions. Flag missing guards or unclear diagnostics; where justified, require the error message to explain **why the guard prevents a concrete failure**, without inventing rationale or breaking public error contracts.
- **Manual ticket handoff to 04/07 is the default.** Delegate bounded implementation to available subagents only when explicitly authorized by the user; the delegated developer owns code/tests, while APC reconciles contract/evidence. Route material changes to independent 05 verification. No duplicate guard registry or repository-wide guard sweep by default.
- Compile and plan; **do not modify product code**.

**Result:** A coherent, actionable and minimally sufficient project authority package, with open decisions and evidence boundaries.

Commit only your own documentation changes locally using the specified agent identity. No push or global Git configuration changes.
