# Package Shape, Authority Binding, and Open Decisions — APC v2.35.2

## Ownership

This procedure owns compilation-time **package shape and coexistence** decisions. It does not own product semantics, implementation behavior, or verification truth.

Use it when the target is not a normal source repository, when an existing project already owns APC-equivalent authorities, when the package is small enough that artifact proliferation is a risk, or when user-owned decisions remain unavailable during an autonomous compile.

## 1. Classify the workspace shape before choosing paths

Do not assume every target is a Git source repository. Classify the active workspace as applicable:

- source repository;
- binary/distribution package;
- installed application/runtime;
- generated/artifact bundle;
- mixed workspace;
- other project-native layout.

Distinguish:

```text
control-plane / compiler-authority root
!=
runnable / shippable target root
```

If compiler metadata inside the runnable/shippable target would contaminate validation, packaging, signing, deployment, or user-visible contents, place APC authorities in an adjacent or otherwise project-approved control-plane root and bind the target explicitly.

Git/VCS state is evidence when present, not a universal prerequisite. For non-VCS targets use the smallest adequate revision identity: content hash/fingerprint, package version, run/revision label, or another project-native immutable identifier. Never invent a fake Git revision.

## 2. Existing canonical authority fulfills the role

APC requires semantic roles, not duplicate filenames.

If the current project already has a canonical authority that fulfills an APC role, **bind it** through `PROJECT_INDEX.yaml` / registry metadata instead of creating a second normative copy.

Examples:

```text
existing responsibility map
→ fulfills System/Owner role

existing product requirements
→ fulfills Product Truth / Acceptance source role

existing evidence registry
→ fulfills Verification Truth source role
```

A projection/adapter may be generated only when a consumer needs a different shape. Mark it derived/non-authoritative and point back to the canonical source.

```text
CANONICAL AUTHORITY
→ optional derived projection
→ consumer/orientation

projection != second owner
```

Do not create `SYSTEM_MAP`, Acceptance, Vision, Decision, or other APC-named artifacts merely because a template exists.

The durable master-goal role is mandatory even when its file shape varies. Keep `GOAL.md` when the package uses it: its observable outcome, scope, acceptance IDs and completion condition must survive context loss and feed START/CONTINUE/`/goal` rehydration. Bind an existing project-native goal authority only when it preserves that same contract and `PROJECT_INDEX.yaml` routes to it; do not replace it with a transient prompt, milestone or summary.

## 3. Scale-aware minimal durable package

`ARTIFACT COUNT != COMPLETENESS`.

Generate the smallest durable authority set that preserves:

- exact Product Truth and unresolved decisions;
- ownership/contracts needed for future work;
- required Product Realization scope;
- Acceptance/Verification Truth;
- JIT reachability and fresh-agent reconstruction.

For a small coherent project, several semantic roles may share one canonical file when their ownership/lifecycle are the same and `PROJECT_INDEX` can route unambiguously to headings/IDs. Split only when independent authority, lifecycle, access, context cost, or change frequency justifies it.

Existing project authorities count toward this set. Do not mirror them just to make an APC folder look complete.

## 4. Autonomous compile with unresolved user decisions

A missing user answer must not be guessed into Product Truth, but it also must not make a useful handoff impossible.

Use three distinct notions:

```text
COMPLETE
= all required user-owned decisions for the declared scope are resolved
  + normal APC completion conditions pass

PACKAGE_READY_PENDING_USER
= durable/reconstructible package is ready for handoff or bounded continuation
  + unresolved user-owned decisions are explicit and impact-bounded
  + affected outcomes/transitions remain blocked/deferred
  + no provisional interpretation is promoted to USER truth

PARTIAL
= package is intentionally incomplete beyond the bounded pending-user condition
  or required reconstruction/routing/coverage is not yet sufficient
```

`PACKAGE_READY_PENDING_USER` is a **derived delivery status**, not Product Complete, not Release Ready, not a new project authority, and not permission to cross an affected gate.

For each pending user decision record:
- stable question/decision ID;
- exact unanswered question;
- why user authority is required;
- provisional interpretation, if any, labeled `COMPILER_HYPOTHESIS` / `USER_CONFIRMATION_REQUIRED`;
- affected outcomes/owners/transitions;
- what work may safely continue without the answer.

If remaining compilation work does not depend on the unresolved decision, continue it. Stop at `PACKAGE_READY_PENDING_USER` only when the remaining material compile scope is blocked by those explicit user-owned decisions.

## 5. Fresh-agent challenge

A fresh agent should be able to answer:

1. What is the real runnable/shippable target root?
2. Where do compiler/control-plane authorities live?
3. Which authority is canonical for each semantic role?
4. Which APC artifacts are derived projections only?
5. Which user decisions remain open and exactly what do they block?
6. Can safe work continue without turning a provisional interpretation into Product Truth?

Fail if the package invents repository/Git identity, duplicates an existing canonical owner, or calls itself COMPLETE merely because it is handoff-ready.
