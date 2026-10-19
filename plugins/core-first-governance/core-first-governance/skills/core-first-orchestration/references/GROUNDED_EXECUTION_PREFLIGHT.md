# Grounded Execution Preflight

Read this procedure only when material source/prerequisite uncertainty can change the implementation path.

## Trigger

Use before committing to a material implementation plan when one or more materially apply:

- multiple supplied/repository sources determine the solution;
- unfamiliar/proprietary/binary/legacy/generated/opaque formats are involved;
- migration, import/export, porting, decompilation, reverse engineering, or format conversion is involved;
- web/external research materially determines implementation;
- tool/dependency/runtime/parser/SDK/compiler/converter/license/credential/permission/environment compatibility is an assumption;
- a wrong prerequisite assumption could cause substantial rework, wasted execution, or context/token churn;
- user-surface work is materially constrained by existing design/layout/placement references or project authorities;
- the task is expensive/long enough that cheap uncertainty reduction materially helps.

## Source-consumption states

```text
DISCOVERED = source/tool/input is known to exist
INSPECTED  = relevant content/format/capability was actually examined
EXTRACTED  = task-relevant facts/constraints were identified
MAPPED     = those facts were connected to the requirement/plan
CONSUMED   = the plan/decision demonstrably uses them
```

`DISCOVERED != CONSUMED`. Listing files, search results, libraries, documentation, logs, or tools never satisfies the preflight by itself.

For each material source/prerequisite, inspect deeply enough for the active decision, extract the relevant facts, map them to the requirement, and make the chosen plan consume them before expensive execution.

## User-surface authority

For material user surfaces, consume existing project sources that define the visible result before implementation. A **User-Surface Authority** may be a style/design guide, UI blueprint, mockup/reference, tokens, product vision, approved surface, or project equivalent; no file format is required.

Derive only the task-relevant model: `STYLE | STRUCTURE | PLACEMENT | HIERARCHY | SPACING/SCALE | STATES | RESPONSIVE | REFERENCES`. Keep provenance; mark `CONFIRMED | INFERRED | UNKNOWN`. Relative guidance stays relative; do not invent coordinates. The derived model is cache, not project truth.

## Exact compatibility chain

For toolchain-dependent work verify the exact case, not category/name similarity:

```text
actual input / format / state
→ required operation
→ required capability
→ candidate tool / dependency
→ exact-case support verified?
→ required access / license / credential / environment available?
→ executable path proven enough to proceed
```

Challenge the few assumptions that could invalidate the whole plan. If available files, repository state, documentation, tool help/version output, or focused research can resolve one cheaply, resolve it before coding around uncertainty.

## Human boundary

Ask/surface early only when the blocker is genuinely user-owned or externally unavailable: product decision, credential/access grant, licensed/external program, unavailable hardware/data, destructive authorization, material cost, or equivalent boundary.

Do not ask the user to resolve discoverable reversible technical facts. Do not construct a speculative substitute before surfacing a real external blocker.

Skip when local-short-path criteria hold and the relevant inputs/path are already understood.
