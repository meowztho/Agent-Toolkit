---
name: agent-blueprint
description: >-
  Create, update, audit, or reconstruct agent-readable BLUEPRINT.md specifications
  and independent scoped software contracts. Use for whole-product handoff,
  reverse-engineering a feature or interface, cross-agent implementation,
  architecture/behavior capture, or blueprint-to-code/acceptance drift review.
  Reuse existing APC/Core-First project authorities instead of duplicating them.
---

# Agent Blueprint — compact, reconstructable software contracts

## Goal

Enable an unfamiliar agent to understand a whole product from a short `BLUEPRINT.md`,
then implement, replace, review, or test a bounded area using only its scoped contract,
public dependency contracts, necessary references, and acceptance evidence.
Optimize for accurate reconstruction with **minimum authoritative duplication and context**.

**Two forms:**
- Product `BLUEPRINT.md` = short mental model and routing surface, **not** a code dump.
- Scoped contract/blueprint = bounded, actionable behavioral/interface definition.

Do not create two editable authorities for the same truth. In APC projects the
existing `PROJECT_INDEX.yaml`, system/capability/integration contracts, design,
flows, acceptance and registries remain canonical. Link to them. For small projects,
`BLUEPRINT.md` alone may suffice; create no registry merely to satisfy this Skill.

## Entry and evidence

1. Identify task mode: **extract from existing software**, **compile intended product**,
   **scoped handoff/reconstruction**, **audit drift**, or **revise blueprint**.
2. In a repository, inspect root/project instructions, current Git status and relevant
   diffs, then the smallest relevant authoritative sources. Check the actual runtime,
   tests, protocols, and UI when the requested claim depends on them. If no repository
   is available, work from supplied inputs and label unknowns.
3. Distinguish **Required** (normative intended behavior), **Observed** (dated, sourced,
   revision-/environment-specific facts), and **Unresolved** (gaps or contradictions).
   No inferred behavior silently becomes project truth; no passing-evidence claim
   without the matching executed verification.
4. If Core-First Governance is available and responsibilities/reuse/interfaces are
   material, use its canonical extension-architecture procedure. If APC is available
   for project compilation, use its authority/index/acceptance model rather than
   generating competing docs. This Skill does not require either plugin to function.

## Author the smallest useful product overview

Start from **user-visible outcomes**, not a file/class inventory:
- identity, purpose, audience, environment and distinctive UX/design;
- scope, non-goals, representative success and recovery journeys;
- required capabilities and global invariants;
- responsibility-to-canonical-runtime-owner map and public boundaries;
- end-to-end entry/exit, persistence and material external dependencies;
- links/IDs to the authoritative detailed contracts, assets, design and tests;
- verified/unverified scope, material unknowns and reconstruction fidelity target.

Keep the root short enough for a fresh agent to read first. Prefer a link over
repeating any detailed contract. Remove irrelevant headings; there is **no line quota**.
Use `references/PRODUCT_BLUEPRINT_TEMPLATE.md` as a starting shape when needed.

## Decide whether to split a scoped contract

Split only for a materially separate responsibility, independent lifecycle/state,
public integration boundary, meaningful reuse/change cadence, or isolated handoff.
One contract is a **semantic boundary**, not necessarily one class or file.
Resolve: `Requirement → Responsibility → canonical Owner → public Capability Contract
→ implementation/provider → consumer composition → data/config variation`.
A document is not the runtime owner; an adapter is not authorized to own another
system's rules or canonical state. Reuse or extend before creating an owner.

Read `references/BLUEPRINT_STANDARD.md` when creating complex boundaries, planning
scoped exports, or auditing conformance. Use `references/CONTRACT_TEMPLATE.yaml` only
when a distinct machine-readable contract benefits the task; existing APC `*.bp.yaml`
or project-native interface definitions can fulfill the same role.

## Scoped contract contents (conditional, not boilerplate)

Write in this natural order:
1. Concrete user/consumer trigger → observable result; explicit exclusions.
2. Named responsibility and canonical runtime owner; what it **must not** own.
3. Public commands/queries/events, inputs/outputs, schemas and versioning;
   declare translation if two layers use different field names.
4. Dependencies through **public** contracts; owned/read/writable state,
   invariants, persistence and lifecycle.
5. Significant failure/recovery and negative/security/permission behavior.
6. If material, concurrency, race handling, identity vs session, ordering,
   retry/idempotency/fencing; concise diagrams/pseudocode **only when semantics
   would otherwise remain ambiguous**.
7. Applicable UI/assets/reference fidelity and focused acceptance/adversarial tests.
8. Target-environment owner/implementation-anchor map and evidence boundary.

Samples are tagged normative vs illustrative/adversarial/reference-only.
State which validations/tests are still pending. Do not copy foreign internals.

## Isolated consumption and handoff

For target contract `C`, load the product overview, C, global invariants that apply,
public dependency-contract closure, and C's acceptance/references. Do **not** load the
entire project's unrelated code or capabilities. Contract-conformant mocks are
allowed for isolated tests; they cannot redefine dependency semantics.
An exported slice is a **derived, revision-scoped snapshot** with source IDs, not
an independently editable authority or a hidden fork of project truth.

## Check before delivery

Check as applicable: correct coverage of requested outcomes and negative behavior;
no unresolved contradictions disguised as facts; stable resolvable IDs and dependencies;
unique semantic ownership; no foreign-state writes/parallel business-rule owners;
protocol example/schema consistency; meaningful success/failure/race scenarios;
traceable acceptance criteria; correct evidence strength (static, unit, integration,
installed runtime, visual, or privileged operation); and fresh-agent ability to
explain product intent and reconstruct one representative scope without chat history.

Update canonical contracts in the same work unit when their public semantics change;
internal refactors alone must not cause blueprint churn. Report what was actually
created/verified versus what still needs a real running-product check.

**Anti-goals:** giant monolithic documents; duplicate APC routing/registries;
interface-per-method proliferation; schema machinery without a consumer;
algorithm overprescription; presumed permissions; non-verifiable completion claims.
