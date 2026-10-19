# Agent Project Compiler (APC)

A skills-only Agent Plugin that compiles ideas, interviews, references, files, and grounded research into durable provider-neutral project authorities.

This v2.36.1 package uses the portable identity `agent-project-compiler` and the user-facing name **Agent Project Compiler**. It is a new-identity package; existing APC account-plugin installs retain their own identity until separately migrated.

## Architecture

The runtime has one canonical compiler kernel plus JIT procedural references:

- `plugin.json` — Agent Plugins 1.0 manifest.
- `skills/instructions/SKILL.md` — **canonical always-active APC kernel**, JIT router, context-freshness capsule, and companion-procedure routing.
- `skills/instructions/references/` — canonical detailed compiler procedures, loaded only when their material triggers apply.

There is no Custom-GPT compatibility runtime in v2.36.0. Historical material is not part of this installable plugin snapshot and is never runtime authority.

The repository does **not** vendor Core-First Governance. If the companion `core-first-governance` plugin is installed, APC routes architecture/ownership/reuse and verification procedures to it JIT. Otherwise APC degrades to its packaged compiler/project authorities without pretending the external skill was loaded.

## Context model

The plugin deliberately does **not** solve context rot by loading more context.

- active context is disposable working memory;
- project/repository authorities and current evidence are durable truth;
- `PROJECT_INDEX.yaml` is routing, not a knowledge summary;
- `STATE` is a compact pointer/session record, not project canon;
- fresh session, compaction, project switch, authority revision, workstream switch, or material current-state change invalidates relevant cached context;
- recovery is `discover current state → route → JIT read → reconcile → replan`, not bulk history hydration;
- rich START/Handoff/Atlas artifacts orient a fresh agent but never replace exact authority reads.

Detailed rules live in `RUNTIME_GUIDE.md`, `BOOTSTRAP_PROMPT_AND_GOAL_GUIDE.md`, and `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` and are loaded JIT.

## Canonical source rules

`skills/instructions/SKILL.md` owns all always-active compiler behavior and material-trigger routing.

`skills/instructions/references/` owns detailed conditional procedures. Each concern has one detailed owner; other files may only carry a short invariant or route to that owner.

## Verify / package boundary

This installable plugin snapshot contains the runtime plugin files only; repository-only build, reproducibility, CI, and historical-source tooling are not bundled here. Validate the manifest, Skill frontmatter, JSON/YAML resources, routed JIT references, and host package shape with the current host's canonical plugin validator when publishing or installing this snapshot.

The absence of repository-only tooling does not change APC runtime semantics and must not be treated as an alternate compiler path.

## License

No open-source license has been selected in this package. Add one before publishing if you want to grant reuse rights beyond GitHub's default repository access terms.
