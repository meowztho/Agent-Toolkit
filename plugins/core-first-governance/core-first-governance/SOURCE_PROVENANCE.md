# Source provenance

## v0.7.0

### `core-first-orchestration`

Extended in its existing orchestration responsibility (`EXTEND_EXISTING_CAPABILITY`) with two provider-neutral behaviors while preserving all v0.6.0 gates:
- **Progressive Skill routing**: a compact routing capsule tells the primary agent when each sibling Skill is material, without preloading every Skill body. The primary agent must still load and apply `core-first-extension-architecture` itself whenever architecture is material; delegation never substitutes for this duty. Host Skill metadata is a discovery optimization, not a policy owner.
- **Adaptive execution / context reconciliation**: non-trivial authorized work uses a lightweight/native execution plan or checklist, reconciles checkpoints against current evidence, replans before continuing when material evidence changes the correct path, and after compaction/continuation re-inspects current state and reloads only required Skills/authorities. Trivial work does not gain planning ceremony.

The v0.6.0 Grounded Execution Preflight and external Completion Authority routing remain in the same owner.

### Protected sibling Skill bodies

The following `SKILL.md` files are intentionally byte-identical to v0.6.0:
- `core-first-extension-architecture`
- `observable-product-verification`
- `core-first-verifier`
- `independent-review`

No responsibility was moved out of those canonical procedure owners merely to make the orchestrator more informed.

## Boundary

Portable Governance owns semantic invariants. Native host capabilities (Skill discovery, planning/task tracking, subagents, read-only isolation, product-surface tools) are providers/adapters that may satisfy those invariants efficiently. Missing host capabilities use the simplest valid fallback.

**Reduce duplicate execution, not duplicate requirements.**

## v0.8.0

### Context-budget refactor inside `core-first-orchestration`

Classification: `EXTEND_EXISTING_CAPABILITY` / owner-local refactor of the existing orchestration capability.

The v0.7.0 orchestration monolith was compressed into a small always-loaded kernel plus explicit JIT references. No semantic owner was moved to another Skill. The kernel retains the non-negotiable primary-agent Core-First duty, compact sibling routing, current-truth/cache law, progressive disclosure, grounded/adaptive execution trigger, and verification/completion routing trigger.

Detailed owner-local procedures are now under:
- `references/GROUNDED_EXECUTION_PREFLIGHT.md`
- `references/ADAPTIVE_EXECUTION_AND_CONTEXT.md`
- `references/DELEGATION_CONTEXT.md`
- `references/VERIFICATION_AND_COMPLETION_ROUTING.md`

This is progressive disclosure, not deletion: each reference has an explicit material trigger in the kernel and must be read before crossing that boundary.

### Observable visual evidence hardening

Classification: `EXTEND_EXISTING_CAPABILITY` in `observable-product-verification`.

The existing ambient-observation rule is made explicit for user-visible work:
- logs/telemetry/internal success state are supporting evidence, not substitutes for the real visible surface;
- a current screenshot/frame is a whole relevant visible-state snapshot rather than a one-element assertion;
- current visual evidence may be reused for unchanged visible facts;
- relevant visual/state changes invalidate the affected old snapshot and require fresh visual evidence;
- a static screenshot does not prove interaction/temporal behavior.

No new QA/evidence owner, screenshot archive, visual-verifier Skill, or tool binding was introduced.

### Protected owners

`core-first-extension-architecture`, `core-first-verifier`, and `independent-review` Skill bodies remain unchanged from v0.7.0. `observable-product-verification` is intentionally changed only within its existing evidence responsibility.


## v0.9.0

### User-Surface Authority red thread

Classification: `EXTEND_EXISTING_CAPABILITY` in `core-first-orchestration` + `observable-product-verification`; no new Skill/owner.

Material user-surface work now consumes existing project design/layout/placement authorities before implementation, derives only a task-relevant surface working model, and verifies the rendered whole surface against the same applicable authority. Exact specified constraints and specified holistic intent both matter; relative guidance remains relative and does not create invented coordinates.

### Optional derived Working View / Atlas

For complex/spatial/multi-system/restart-sensitive work, orchestration may externalize its current model as compact notes/Markdown/ASCII/HTML/SVG/storyboard. It must link canonical sources and distinguish `CONFIRMED | INFERRED | UNKNOWN`. This view is disposable cache, never project truth or a new authority.

### Consumer-tool decision

No MCP server or new consumer tool is introduced. The current failure class is solvable by compact Skill guidance plus existing host read/search/visual capabilities. Tooling remains admitted only for a concrete bounded gap where it reduces repeated deterministic work, errors, or context/token cost without creating a parallel owner or general-purpose toolbox.

## v0.10.0

### Evidence-driven debugging

Classification: `EXTEND_EXISTING_CAPABILITY` in `core-first-orchestration`; no new Skill/owner.

A focused JIT debugging reference now requires negative evidence to invalidate the causal premises and dependent hypothesis families it disproves. Visual/runtime source identity is routed from the actual observable owner/path rather than resemblance or visible artifact size alone; effective runtime geometry may differ from declared/local bounds. The rule remains provider/domain neutral.

### Workspace reconciliation after context loss

Continuation/compaction now explicitly uses `WORKSPACE AWARENESS != WORKSPACE HYDRATION`: cheaply rediscover current repository/workspace state and existing routing/working aids first, then JIT-read only material sources. Derived aids remain cache, current authority/runtime state wins, suitable aids are reused, and no parallel helper index/manifest is created merely for discoverability.

### Tool and ownership boundary

No MCP server, computer-use stack, debugging tool, workspace database, sixth Skill, or new architecture owner is introduced. The observed failures are attention/evidence-consumption/context-continuity problems that remain solvable by concise Skill guidance plus host-native read/search/runtime capabilities.

## v0.11.0

### Responsibility-relative ownership and role resolution

Classification: `EXTEND_EXISTING_CAPABILITY` in canonical `core-first-extension-architecture`; no new Skill/owner.

Repeated ownership-audit tests exposed a semantic interpretation gap: an agent could decompose responsibilities yet still infer owners from class boundaries/names, treat current code placement as canonical ownership, centralize data while leaving behavior duplicated, or equate capability identity with implementation count.

v0.11.0 hardens the existing architecture owner with these invariants:
- name the responsibility before declaring an owner;
- distinguish canonical owner, current carrier/effective decision path, implementation anchor, capability/module/provider, consumer, data/profile, migration target, and unresolved gap;
- current code location/size/name is evidence of placement, not proof of canonical ownership;
- parallel owners mean independent active authority over the same responsibility, not multiple controlled providers behind one capability;
- unresolved ownership stays unresolved until evidence supports the smallest semantic path;
- centralized data does not centralize duplicated semantic behavior;
- capability identity is semantic, not a function of implementation count;
- architectural role is determined by semantics/authority/runtime flow, not symbol naming conventions.

The detailed recovery examples live in the existing `EXTENSION_ARCHITECTURE_METHOD.md` reference. The five-Skill model, orchestration JIT structure, OPV, verifier, independent review, and Skills-only tooling boundary remain unchanged.

## v0.11.1

v0.11.1 is a bounded clarification of the v0.11 ownership-resolution method after fresh MiniMax regression tests. It distinguishes owner existence from reusable-seam proof, treats lifecycle/state proximity/consumer count/implementation count as evidence rather than mandatory owner criteria, makes `Responsibility → Owner → Capability Contract` order explicit, separates unauthorized foreign writes from true parallel-owner claims, and strengthens the gap-resolution gate before new owner creation. No new Skill, tool, MCP, authority-map format, or orchestration procedure is added.

## v0.11.2

v0.11.2 is a bounded `core-first-orchestration` correction from real MiniMax continuation/debugging runs. A small, easy-to-measure incidental defect plus many passing tests could displace a broader user request and inflate the completion claim even though several original outcomes remained unaddressed.

The existing orchestration owner now performs lightweight **outcome-coverage reconciliation** after material local fixes and before completion: original requested outcome → matching evidence → remaining gap / next priority. Evidence volume does not define completion, and an incidental defect cannot silently replace the broader outcome.

`EVIDENCE_DRIVEN_DEBUGGING.md` additionally preserves **observable identity**: a nearby/easier defect stays separate from the reported symptom until evidence establishes the same causal problem.

No new Skill, tracker, acceptance engine, MCP, tool bundle, or architecture owner is introduced. The always-loaded orchestration kernel, the complete `core-first-extension-architecture` family, `observable-product-verification`, `core-first-verifier`, and `independent-review` remain unchanged. Three existing orchestration JIT references and orchestration evals are intentionally versioned; the total orchestration corpus changes by only +45 bytes after compression.

## v0.11.3

v0.11.3 is a bounded refinement of the existing `core-first-extension-architecture` responsibility-discovery method after compiler/project tests showed a related omission risk: a broad product can have locally valid owners/capabilities yet still never consider an ordinary material responsibility implied by the requested product.

The existing Core-First owner now adds a **Responsibility Coverage Challenge** for Greenfield/broad product or subsystem work. Before accepting the responsibility set, ask whether a competent domain expert could immediately identify an important ordinary responsibility that was never considered. Domain/product expectations are discovery hypotheses, not project authority; explicit exclusions/deferrals remain controlling, the challenge does not authorize a new owner, and narrow local tasks do not trigger whole-product reconstruction.

The main Core-First Skill is also context-trimmed by moving detailed conditional-profile rules to the existing `CONDITIONAL_PROFILES.md` JIT reference and the full public extension-point contract to `EXTENSION_ARCHITECTURE_METHOD.md`. No semantics are removed, and no Skill, tracker, compiler pipeline, MCP, tool bundle, or new project authority format is introduced.

## v0.11.4

v0.11.4 is a bounded `core-first-orchestration` hardening derived from repeated real-agent tests of project-defined approval/admission workflows. Independent runs exposed both false-positive gate crossing (broad implementation intent treated as implicit approval) and false-negative blocking (the existence of a later approval gate used to refuse authorized reversible preparation before it).

The orchestration kernel therefore preserves the gate at the **exact state transition**: an approval/admission gate blocks that transition, not authorized reversible preparation before it, and broad implementation intent does not implicitly authorize crossing the gate. Three domain-neutral regression evals cover preparation-before-gate, broad-request non-authorization, and exact transition scope.

A separate experiment attempted to harden producer/authoring-boundary reuse against direct use of underlying stores/repositories. The stronger wording did not reliably change agent behavior across the tested runs, so it is intentionally **not** added as permanent runtime Skill text in this release. This avoids accumulating model-specific or ineffective prompt weight.

No new Skill, approval engine, tracker, provider binding, MCP/tool bundle, or authority artifact is introduced. The v0.11.3 Core-First architecture family and all other Skill families remain byte-identical.

## v0.11.5

v0.11.5 clarifies existing orchestration/Core-First routing language after the term `non-trivial` proved too subjective to be a reliable agent trigger. Runtime decisions now use explicit material properties and a positively defined local short path. Small-looking changes can still be material when they cross ownership, contract, producer/persistence, gate, authority, dependency, shared-behavior, or authoritative-state boundaries; large mechanical edits can remain on the short path when those semantics are already settled and direct bounded verification is sufficient. File count and apparent difficulty are evidence, not policy triggers. No new owner, Skill, planner, tracker, or tool is introduced.

## v0.11.6

v0.11.6 is a bounded extension of the existing `observable-product-verification` evidence responsibility after a real external agent project documented a plausible but frozen screenshot oracle that kept returning stale frames while the application continued rendering. The release distinguishes **fresh evidence acquisition** from **fresh observed state**: when a material claim depends on live/current state and there is concrete reason an observation path may be stale, frozen, cached, replayed, or disconnected, establish oracle liveness with independently established activity or the smallest controlled observable stimulus before trusting that source. Identical observations alone do not prove a dead oracle when the underlying state may legitimately be static. If liveness cannot be established, use another appropriate boundary or keep the claim `INCONCLUSIVE`.

This change remains inside the existing OPV owner. `core-first-orchestration`, `core-first-extension-architecture`, `EVIDENCE_DRIVEN_DEBUGGING`, `core-first-verifier`, and `independent-review` remain unchanged. No new Skill, oracle framework, capture tool, evidence database, MCP/tool bundle, or provider-specific rule is introduced.
