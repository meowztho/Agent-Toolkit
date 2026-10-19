# Compact Agent-Readable Blueprint Standard — Design Draft v0.2

## Purpose
Enable a fresh agent to reconstruct the intended product and to implement, swap,
review or test one bounded area without reading the whole codebase. This is a
provider- and domain-neutral convention, not a replacement for project authorities.

## Canonical roles and precedence
1. **APC:** compiles product truth, realization truth, decisions, references,
   plan/admission and acceptance. In structured APC projects, `PROJECT_INDEX.yaml`
   stays the canonical JIT router, and existing authorities remain authoritative.
2. **Core-First:** resolves `Requirement → Responsibility → canonical Owner →
   Capability Contract → Implementation/Provider → Consumer Composition → Variation`.
   Runtime owners are not documentation files, and public contracts are not owners.
3. **Blueprint:** a compact entry / scope map that summarizes only what is needed
   for a correct whole-product mental model and links details to their owners.
4. **Scoped contracts:** normative contracts for separable semantic boundaries,
   optionally represented as APC `*.bp.yaml` behavior/data/implementation blueprints.
5. **Evidence:** tests/observations prove claims at their proper scope; evidence
   does not silently change specifications or user decisions.

Never duplicate a canonical fact in two editable files. Reuse an existing system map,
flow graph, schema, design authority, registry or acceptance matrix when present.
No additional registry or index is needed for a small project that can be navigated
from `BLUEPRINT.md`; no parallel index should be introduced into an APC project.

## Two complementary blueprint shapes
- **Product blueprint (`BLUEPRINT.md`):** short complete mental model of the product,
  with routeable authority/contract references. It is NOT a detailed implementation plan.
- **Scoped blueprint / contract:** a bounded, locally actionable slice of product behavior,
  including concrete scenarios, external boundary semantics, failures and acceptance.
  It may be one self-contained document in a small project, or an existing APC authority/
  `*.bp.yaml` file in a structured project. Do not create a parallel authority.

**Natural reading order for a scoped blueprint:** desired user behavior → exclusions →
responsibility/authority boundaries → flow/data/contract → tricky invariants/failures →
verification → target-environment mapping. This is a reading order, not a mandatory
file count or a rigid YAML schema.

## Smallest useful package
- `BLUEPRINT.md` — purpose, product outcomes, key invariants, owners, end-to-end
  path, visual identity, environment and routes to authoritative detail.
- `contracts/<area>.yaml` / existing APC `*.bp.yaml` — only when bounded behavior
  needs separate understanding, implementation, versioning, verification or handoff.
- Existing tests/reference assets — linked, not re-described.

Splitting criteria: distinct responsibility, independent lifecycle/state, a public
integration boundary, meaningful reuse, separate change cadence, or handoff need.
Do NOT create a contract per method, component, property, class or file.
One semantic scope can map to several classes/files, and one implementation can
realize several contracts if it does not create parallel canonical owners.

## Scope-specific contracts must be executable without the whole repository
A separate contract should be usable to implement/test its area with public dependency
interfaces or contract-compliant mocks. It must not silently rely on undocumented foreign
internals, assume a local port/ID is durable identity, or invent global permissions.

A consumer must distinguish:
- canonical runtime owner versus adapter/provider/implementation carrier;
- stable configuration, live identity/session generation and optional host-owned identity;
- actual runtime state versus authoritative persisted state;
- discoverability/reachability versus authorization;
- illustrative example versus normative requirement.

## Minimum contract semantics
A nontrivial contract declares when relevant:
- stable ID and single named responsibility; canonical runtime owner;
- public commands, queries, events, input/output shapes and allowed callers;
- owned/read state, forbidden foreign writes and public dependencies;
- user-observable trigger → result scenarios, preconditions/postconditions, invariants,
  non-goals and concrete failures/recovery;
- lifecycle and persistence, if significant;
- version/compatibility constraints when consumers require them;
- concurrent operations, identity/generation/fencing, retry/idempotency and ordering
  rules when the behavior is stateful, async, concurrent or security-sensitive;
- required UI/visual/data/asset references where relevant;
- acceptance IDs and observable evidence route.

Keep advanced fields conditional, not mandatory decoration. Stable IDs survive moves.
Prefer references to authoritative schema/flow/design rather than repeated bodies.
Examples must be labeled required, illustrative, reference-only or adversarial.
If samples describe distinct wire-level and adapter-level payloads, specify the translation
and field correspondence. Disagreement between `role` and `kind`, or between `sessionId`
and `streamSessionId`, is not automatically an error, but an unexplained difference is a
contract ambiguity. Validate example payloads against their governing schema when possible.

Use concise algorithm/sequence/state diagrams **only when** multiple plausible
implementations would break a material invariant (atomic admission, fencing, ordering,
security or other observably constrained logic). Otherwise specify semantics and
allow implementation freedom. A test list should cover real adversarial cases, not just
happy-path unit checks.

For deployment-sensitive behavior, link bootstrap/configuration, installation,
version-compatibility, rollback and real-host acceptance. Do not conflate build/test
success with installed/runtime success.


## Scoped reconstruction: closure rule
Given target contract ID C:
1. Load `BLUEPRINT.md` for the whole-product constraints, then resolve C by the
   canonical project router/registry if present (or by the root links otherwise).
2. Load C plus its directly referenced normative authorities and acceptance criteria.
3. Traverse dependency edges only as needed to understand C's public contracts,
   global invariants, input/output shape, security, lifecycle and observable behavior.
   Do not hydrate unrelated internal implementations or entire subsystems.
4. Preserve foreign owners behind declared public contracts; for local isolation,
   mocks/adapters may emulate those contracts but never redefine their semantics.
5. If a required reference is missing, stale, ambiguous or contradictory, mark the
   bounded issue unresolved and avoid a false reconstruction claim.
6. Validate both local acceptance and affected cross-boundary behavior when real
   integration is possible. Name the evidence level (fixture, contract, integration,
   runtime/visual); stronger claims require stronger evidence.

A scoped export can be created as a *derived*, disposable projection that bundles
C, dependency-contract closure and pertinent acceptance/references. It is not a
new owner, contract fork or second mutable source of truth. Record source IDs and
source revision for repeatable reproduction. Refresh it after authority changes.

## Specification versus evidence
Keep these logically separate, even if a small scoped handoff presents them together:
- **Required:** normative desired behavior and hard prohibitions.
- **Observed:** dated, source-/revision-/environment-scoped evidence that actually ran.
- **Unresolved:** gaps, disputed behavior, pending approval or runtime proof.

A handoff may carry an evidence snapshot and an implementation sequence to make work
convenient, but those are **non-normative snapshots**: link to acceptance/plan/evidence
owners when a canonical APC package exists. Do not create another changing source of truth.
A target integration map identifies existing lifecycle, transport, state, permission,
identity and persistence owners; missing entries remain unknown, not invented.

## Drift and validation
Update the relevant canonical specification in the same work unit when the public
interface, responsibility, lifecycle, owned state, invariant, schema or user-facing
contract changes. Internal refactors preserving semantics do not churn blueprints.

For larger projects, extend the existing APC validator / project gates to check:
- unique active responsibility and contract IDs;
- all IDs and paths resolve, with no broken references/cycles where prohibited;
- normative contract reachability through canonical routing;
- dependency direction and owner/state-write boundaries;
- acceptance links and representative external/user-surface evidence;
- valid schema/protocol examples, state transition and failure-case coverage when material;
- affected authority/code/test traceability at the current revision.

Claims have independent fidelity axes: functional, behavioral, visual, operational.
No file count, registry presence or compile success proves reconstruction fidelity.
Use a fresh agent with no source code to explain the product, discover a deep
contract, implement/reason through one scope, and reverse-trace a failure.

## Explicit anti-goals
- No giant monolithic `BLUEPRINT.md`.
- No duplicate APC `PROJECT_INDEX`, System Map, Design Authority or Acceptance Matrix.
- No new owner merely because a file/module/interface was split.
- No universal event bus, service framework or schema language just for documentation.
- No implicit assumptions masquerading as observed product behavior.
