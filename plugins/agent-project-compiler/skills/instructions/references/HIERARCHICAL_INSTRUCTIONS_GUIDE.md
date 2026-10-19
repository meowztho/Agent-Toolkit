# Hierarchical Agent Instructions Guide

# Current Precedence — Always-On Architecture Kernel

Root/provider-equivalent instructions should carry short durable laws only: preserve master outcome; resolve required authorities; one canonical Responsibility Owner; classify/reuse before create; producer convergence; consumers compose shared behavior; external origin grants no extra authority; select only admissible work; evidence scope must match claims. Detailed policy remains in routed authorities.

Do not make correctness depend on provider autoload. START's Portable Operating Kernel must recover the same instruction/discovery behavior when autoload is unavailable.

---


## Purpose

Nested `AGENTS.md` files are useful only when a coherent repository subtree has working rules that differ from the project defaults.

Do not create one `AGENTS.md` per folder, Blueprint, screen, class, or feature.

Use hierarchy to scope engineering behavior, not to duplicate project knowledge.

---

## 1. Instruction Layers

The intended model is:

```text
global/user agent instructions
        ↓
repository-root AGENTS.md
        ↓
optional subtree AGENTS.md
        ↓
task-specific contracts / Blueprint / authoritative source
        ↓
implementation
```

Responsibilities:

- root `AGENTS.md` = rules useful across nearly all project work;
- nested `AGENTS.md` = rules useful across many tasks inside one coherent subtree;
- Project Blueprints/contracts/specifications = exact behavior of a concrete system/flow/screen;
- implementation = actual code/assets/config.

Do not move product behavior into nested `AGENTS.md`.

---

## 2. When to Generate a Nested AGENTS.md

Generate a nested instruction file only when ALL are true:

1. a coherent subtree exists or is intentionally being created;
2. multiple files/tasks inside that subtree need the same special working rules;
3. those rules materially differ from or refine repository-root behavior;
4. putting the rules in a Blueprint/spec/contract would be semantically wrong;
5. the expected benefit outweighs permanent instruction/context cost.

Typical justified scopes:
- `src/ui/`
- `src/networking/`
- `src/persistence/`
- `blueprints/`
- `tests/`
- generated-source directories
- infrastructure/deployment directories

Typical unjustified scopes:
- one screen;
- one class;
- one Blueprint;
- one trivial utility folder;
- a folder whose only rules repeat root instructions.

---

## 3. Nested Instruction Registry

When nested `AGENTS.md` files are used, register them in:

```text
PROJECT_REGISTRY.yaml
```

Recommended form:

```yaml
instruction_scopes:
  SCOPE-UI:
    root: src/ui
    instructions: src/ui/AGENTS.md
    responsibility: UI engineering conventions

  SCOPE-BLUEPRINTS:
    root: blueprints
    instructions: blueprints/AGENTS.md
    responsibility: Project Blueprint authoring and validation
```

The registry is a routing aid. It does not replace native instruction discovery in a selected harness.

---

## 4. JIT Local-Instruction Lookup

A root-started autonomous agent may work on files below a subtree without changing its working directory.

Therefore the root `AGENTS.md` should require:

```text
Before modifying a target path:
1. identify the target path(s);
2. resolve applicable registered instruction scopes;
3. inspect the path from repository root to the target for applicable
   AGENTS.md / AGENTS.override.md files;
4. read only newly applicable local instructions;
5. combine root + applicable local rules;
6. do not preload instructions from unrelated subtrees.
```

If multiple target paths span different scopes, load only the scopes required for the current change.

---

## 5. Do Not Manually Chain Parent Instructions

Nested files should not contain boilerplate such as:

```text
First read ../../AGENTS.md
```

Parent/root instructions are already part of the project's instruction model.

Nested instructions should contain only local refinements.

---

## 6. Example: UI Scope

`src/ui/AGENTS.md` might contain:

```markdown
# UI Scope Instructions

- `CONTRACT-APP-FLOW` is authoritative for required screens and transitions.
- Resolve UI Blueprint ownership through `blueprints/REGISTRY.yaml` before creating a screen or flow.
- Global navigation/setup state must use the registered application navigation/state owner.
- Do not hard-code selectable entities, stages, rules, or semantic input actions when registries exist.
- Before adding a new screen, run the duplicate-creation gate for its responsibility key.
- User-facing UI acceptance criteria require runtime evidence; visual criteria require actual visual review.
```

It should NOT repeat:
- generic Git rules;
- general reuse-before-create rules;
- global user-gate rules;
- project story or detailed menu behavior.

---

## 7. Example: Blueprint Scope

`blueprints/AGENTS.md` might contain:

```markdown
# Project Blueprint Scope Instructions

- Every active Blueprint must have one stable Blueprint ID and responsibility key.
- Register new Blueprints in `blueprints/REGISTRY.yaml`.
- Prefer `call` nodes to copying an existing behavior graph.
- Update callers and registry ownership transactionally when renaming, moving, superseding, or deleting a Blueprint.
- Run project-contract validation after structural Blueprint changes.
```

The actual behavior of `BP-UI-ITEM-SELECT` remains in its `.bp.yaml`, not here.

---

## 8. Example: Tests Scope

`tests/AGENTS.md` might contain:

```markdown
# Test Scope Instructions

- Prefer deterministic tests.
- Test externally observable contracts rather than implementation details when practical.
- Do not weaken assertions merely to make an implementation pass.
- Keep release-gating E2E scenarios separate from narrow unit/integration tests.
```

Only generate this if those rules are genuinely project-specific/local.

---

## 9. Instruction Duplication Gate

Before generating or editing a nested `AGENTS.md`:

1. compare proposed rules against root `AGENTS.md`;
2. remove exact or semantic duplicates;
3. move concrete feature behavior to the relevant Blueprint/spec/contract;
4. keep only subtree-wide working rules;
5. verify the instruction scope is registered when the project uses scope routing.

The goal is stronger locality with less instruction bloat.

---

## 10. Override Files

Use `AGENTS.override.md` only for an intentional stronger local override.

Do not generate overrides routinely.

When an override exists, its purpose should be explicit and narrow.

---

## 11. Refactor / Move Behavior

If a subtree moves:

1. update `PROJECT_REGISTRY.yaml` scope root/path;
2. move the nested instruction file with the subtree when its rules still apply;
3. search for direct references to the old path;
4. validate instruction-scope routing;
5. remove obsolete instruction files rather than leaving stale copies.

If a subtree is split, reassess whether the old local rules still apply to both children.

---

## 12. Context Principle

Nested instructions are a selective context tool, not a documentation strategy.

Generate the minimum instruction hierarchy needed to reduce ambiguity and errors.

Detailed project knowledge remains in:
- authoritative documents;
- Project Blueprints;
- machine-readable contracts;
- registries.

Nested instruction files are discovered through instruction-scope/path rules, not `PROJECT_INDEX` normative-authority reachability. They must be registered/scoped, but they do not count as project truth merely because they are always-on instructions.

Architecture invariants that must survive **every later user request regardless of target path** belong in the root always-on kernel, not only in a nested instruction. Examples: core-first capability classification, reuse-before-parallel-path, single semantic ownership, and evidence-before-completion. Nested instructions may refine how a subtree implements those invariants but must not be the only place they exist.
