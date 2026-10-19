# Skill Lifecycle and Resolution Guide — APC v2.35

## Ownership

This file owns APC procedure for **external expertise Skills and project-local Skills**. It does not own APC plugin packaging/JIT granularity; that belongs to `PLUGIN_NATIVE_JIT_ARCHITECTURE.md`. Skills remain procedures, never project truth.

## Three layers

```text
APC Skill
  compiler/orchestrator procedure

External expertise Skills
  reusable framework/domain/tool procedures supplied by the environment/ecosystem

Project-local Skills
  repository-local repeatable procedures generated/adopted only when the project materially benefits
```

Do not encode product values, system ownership or Acceptance truth inside a Skill merely because the Skill uses them.

## Discovery trigger

Search/resolve Skills only when a recurring workflow or specialist capability can materially improve reliability. Project size alone is not a trigger.

Derive needs from confirmed systems, surfaces, assets, integrations, authoring workflows, verification procedures and runtime/tool constraints.

Preferred discovery order:
1. already installed/global Skills;
2. repository-local `.agents/skills/` or project-selected portable location;
3. harness/plugin-provided Skills;
4. trusted/curated external sources when materially needed;
5. generate a project-local Skill only when no suitable procedure already exists.

Use the minimum active Skill set. Installed/discoverable != loaded.

## External Skill review gate

Treat third-party Skills as instructional supply-chain input. Before adopting/installing when material, inspect enough to establish:
- source/repository identity and version/commit/hash when available;
- maintenance/activity is reasonable for the dependency;
- intended trigger and supported framework/runtime version;
- referenced scripts/assets/dependencies;
- permissions/tool/network expectations;
- license/provenance when relevant;
- instruction conflicts with project authorities or companion procedures;
- overlap with already-installed Skills;
- whether the Skill actually improves the target workflow.

Do not execute setup/install scripts blindly because a repository calls itself a Skill collection.

Global installation is a user/environment choice unless current policy explicitly authorizes it. Repository-local reversible installation may be automated only when authorized and reviewed.

## `SKILL_REQUIREMENTS.yaml` is a resolution router

When specialist procedures materially affect execution, compile capability requirements rather than hard-coding one provider:

```yaml
requirements:
  SKILLREQ-EXAMPLE:
    capability: "framework integration guidance"
    triggers:
      - "material framework integration work"
    resolution:
      status: resolved | planned | unavailable | rejected
      skill: "installed-or-project-skill-name"
      source: "plugin / repo-local path / reviewed external source"
      version: "..."
    project_truth_authorities:
      - "contracts/SYSTEM_MAP.yaml"
    must_not_own:
      - "product behavior"
      - "acceptance truth"
```

Record rejection/unavailable reasons so future agents do not repeatedly rediscover unsuitable procedures.

## When to generate a project-local Skill

Generate one only when all are materially true:
1. the workflow is repeated or expected to recur;
2. the procedure is stable enough to encode;
3. it benefits from specialized ordered steps/checks/tool use;
4. no installed/reviewed external Skill adequately covers it;
5. encoding it materially reduces drift, duplicate ownership or repeated setup error.

Do not generate:
- one Skill per master system;
- a Skill containing the complete product specification;
- product values that belong in canonical data/config;
- a one-off bug-fix Skill;
- dozens of speculative Skills before their first real workflow exists.

For greenfield work, a likely project-local Skill may remain `planned` until its first real workflow makes the procedure concrete.

## Project-local shape

Prefer the portable project Skill location selected by `AGENT_RUNTIME_PROFILE.yaml` (commonly `.agents/skills/` when supported):

```text
.agents/skills/<procedure-name>/
  SKILL.md
  references/       # only when JIT detail is useful
  evals/evals.json  # when the harness can run structured evals and the procedure is material
```

Keep `SKILL.md` frontmatter minimal and trigger-focused. The body should:
- identify when to use/not use the procedure;
- read project authorities rather than copy them;
- define ordered procedure/checks and stop/escalation conditions;
- name forbidden bypasses where material;
- route detailed conditional material JIT;
- avoid provider-specific law unless the Skill is explicitly a provider adapter.

## Version drift

A Skill can become stale while project truth remains current. For version-sensitive Skills:
- record source + version/commit when material;
- compare target framework/engine/tool version with the repository;
- re-evaluate after major upgrades;
- do not silently upgrade when changed guidance can alter architecture/behavior;
- keep project authorities independent so replacing a Skill does not rewrite project truth.

## Validation

Before treating a material external/project-local Skill as ready:
- validate required frontmatter and referenced paths;
- ensure it does not duplicate project canon or another better Skill;
- test representative positive and negative triggers;
- verify that it reads intended authorities and follows the intended workflow;
- keep structured evals when practical;
- compare behavior/evidence against baseline when feasible;
- revise/remove the Skill when it adds context but no measurable reliability, over-triggers or under-triggers.

## Companion and runtime boundary

The APC root orchestrator decides **when** this lifecycle procedure is material. `AGENT_RUNTIME_PORTABILITY_GUIDE.md` owns provider/harness bindings. `PLUGIN_NATIVE_JIT_ARCHITECTURE.md` owns APC's own packaged JIT layout. Core-First remains the architecture/reuse owner when material and installed.
