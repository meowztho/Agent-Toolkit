# 12. Project Atlas HTML

Agents often reason well when the project is presented as one visually scannable page. For every **nontrivial compiled project**, generate and maintain:

```text
PROJECT_ATLAS.html
```

It is a **generated view**, not a new authority.

Recommended sections:
- product/vision capsule;
- decision-model highlights and important guardrails/example semantics;
- Authority Reachability/discoverability status;
- Fresh-Agent Reconstruction status;
- master system cards;
- system dependency/composition map;
- product object compositions (e.g. entity = systems + data);
- primary screens/pages and user flow;
- visual shell/reference thumbnails/links where practical;
- current acceptance status;
- representative architecture-proof status when reuse/composition is material (integration case, heterogeneous proof cases, covered variation axes);
- unresolved decisions/blockers;
- skill/capability status;
- latest verification summary;
- links/paths/IDs to canonical project artifacts.

The Atlas should be standalone HTML/CSS when practical so it opens locally without a build step.

---

## Project Atlas vs runtime Working View

Keep two concepts distinct:

```text
PROJECT_ATLAS.html
= compiler-generated, reproducible, non-authoritative package orientation view with freshness lifecycle

Agent Working View / Working Atlas
= optional disposable runtime reasoning cache created by an implementation/orchestration agent
```

A temporary Working View never becomes project truth and does not satisfy the compiler's `PROJECT_ATLAS.html` lifecycle; conversely the Project Atlas is not a scratchpad for the running agent.

# 13. Atlas generation rule

Preferred flow:

```text
canonical project files
SYSTEM_MAP / APP_FLOW / USER_VISION / DECISION_COMPENDIUM / PROJECT_INDEX / guardrails / registries / acceptance / reachability / reconstruction / skills
        ↓
small deterministic generator or compiler generation step
        ↓
PROJECT_ATLAS.html
```

The Atlas must declare:

```text
GENERATED VIEW — NOT AUTHORITATIVE
```

Do not manually patch the Atlas when the source contracts are wrong. Fix the canonical source and regenerate.

For a nontrivial project, also generate/register a reproducible Atlas regeneration command/tool (for example `tools/generate_project_atlas.py` or an equivalent project-native command). The initial compiler may emit the first HTML directly, but delivery is incomplete if later agents have no defined way to regenerate it. Tiny/simple projects may omit the Atlas entirely when the project profile explicitly classifies it as unnecessary.

---

# 14. Atlas as context router, not context dump

The Atlas is a required **whole-project orientation view** for nontrivial projects. It does not replace JIT loading of exact contracts.

Required use on fresh implementation sessions, major context recovery, and fresh-agent reconstruction:

```text
START orientation
→ validate/regenerate PROJECT_ATLAS.html if stale
→ inspect PROJECT_ATLAS.html once for whole-project orientation
→ select current system/requirement
→ load exact authority/Blueprint via PROJECT_INDEX/REGISTRY
→ implement/verify
```

Do not embed complete source code, full specs, or every test log into the Atlas. Record inspection in runtime context (`inspected_view_ids`) when the harness can track it. A stale Atlas must be regenerated before it is used for orientation.

---

# 15. Atlas lifecycle / freshness gate

For nontrivial projects the Atlas has a lifecycle even though it is non-authoritative.

Registry metadata should declare:
- `normative: false`;
- `discoverability_required: true`;
- the generator artifact/command;
- the canonical source selector/IDs used to build the view;
- a generated source fingerprint/revision;
- `edit_policy: generated_only`.

A project validator should recompute Atlas freshness from the current registered sources. When any selected source changes, is added/removed, or the project revision/current acceptance state materially changes, the Atlas becomes **stale**.

At a minimum regenerate it:
1. after compilation before package delivery;
2. after material architecture/flow/decision/acceptance changes at the next milestone;
3. before a fresh/context-recovery agent uses it;
4. before handoff/final completion.

Do not hide stale state. If regeneration cannot run, mark the view stale and do not treat it as orientation evidence.

`PROJECT_INDEX.yaml` remains the routing authority. Atlas metadata/freshness evidence is derived and must never become a second project truth.

# 16. Coverage gate

Before package delivery verify:

- Has the project been decomposed into canonical reusable systems rather than only feature/task fragments?
- Does each durable responsibility have one owner?
- Are product objects composed from systems instead of rebuilding them?
- Are data/profiles/modifiers/explicit replacements separated from shared system behavior where appropriate?
- Are material merge operators and propagation semantics explicit rather than hidden behind a generic `override`?
- Can a new consumer/page/content item be added mostly by composition/data when that was part of the intent?
- Are skill/capability requirements derived from actual systems and verification needs?
- Does the start prompt contain both product vision and execution contract?
- Does the preflight question gate prevent silent material guessing without creating a "keep asking" loop?
- Has the system model been challenged by adversarial examples when extensibility matters?
- Does `PROJECT_INDEX.yaml` route every active normative authority/required Blueprint, with zero unreachable nodes in generated reachability evidence?
- Has Fresh-Agent Reconstruction passed before final task decomposition, including a deep-authority discovery challenge?
- For a nontrivial project, is `PROJECT_ATLAS.html` present, fresh, registered, routed as a required generated view, and reproducibly regenerable from canonical sources?
- On fresh/context-recovery execution, was the fresh Atlas actually inspected before JIT implementation work?

Core invariant:

```text
Preserve the whole vision.
Define the master systems.
Compose instead of duplicate.
Use skills as tools.
Show the project as a generated Atlas.
Verify the assembled product.
```

---

# 17. Skill routing boundary

For skill discovery/review/install/routing and compiler-as-skill parity, use `SKILL_NATIVE_COMPILER_GUIDE.md`. This guide only owns the system-side capability demand and composition context.

---

---

# System Map as Interview Coverage Surface

The first `SYSTEM_MAP` draft is also an interview-discovery tool. Once candidate master systems/domains are identified, cross-check them against `INTERVIEW_COVERAGE.yaml` before freezing the architecture.

A system may be structurally obvious to the compiler but still contain unresolved user-owned behavior. Do not let an inferred system boundary silently become a final product decision. Ask when the boundary changes user-visible behavior, authoring workflow, scope, or future extension; otherwise mark it delegated technical.

# Presentation primitives and parent-slot composition

For multi-surface UI, menus or editor shells, apply Core-First to presentation as well as domain logic.

Semantic ownership:

```text
Design tokens/theme
→ Primitive/component contract
→ Layout/container slot contract
→ Page/screen composition
→ local content/data
```

A parent/container owns **placement and available-space constraints** for its slots (grid/flex/region, ordering, alignment, responsive allocation). A reusable primitive owns its **internal visual/interaction contract** (typography role, padding rules, focus/disabled/hover behavior, border/frame semantics, minimum hit area, internal icon/text arrangement).

A consumer may vary a primitive only through declared tokens/variants/properties or an explicit one-off exception. Do not let a page/container reach inside and restyle the primitive ad hoc, and do not let the primitive own page placement. If a container needs a compact button, expose/use a `compact`/size variant or slot contract rather than creating a second local button style.

A Design System is not `Exercised` because `tokens.*` or `primitives.*` files exist. For material reusable presentation, prove at least two representative consumers use the same primitive/layout contract and that a shared change propagates without page-local rewrites.

For container conformance, test representative narrow/wide/overflow/content states so children actually obey the slot constraints. A box existing on screen does not prove its contents obey the box's layout contract.


# Blueprint-backed composition

When a reusable System/Capability is material enough to need an explicit Blueprint/contract, treat it as a composable building block:

```text
Consumer / Product node
→ composes declared capabilities/modules
→ calls their public contracts
→ supplies profile/data/modifiers
```

The consumer should not absorb the internal rules/state of the composed system.

This does not prescribe an engine or visual scripting language. Code modules, services, components, resources and engine-native subsystems may all realize the same Blueprint-backed boundary.


