# Core-First Governance v0.11.7

Provider-neutral governance for AI-assisted software work, currently packaged as a Codex **Skills-only** plugin.

## What v0.11.7 changes

Core-First now checks the relevant code boundary by responsibility and synonyms before adding a class, module, or owner. For large or restart-sensitive work, a small optional implementation lexicon can point from user terms to current code symbols and consumers; it remains a checked working view, not a second source of project truth. The architecture procedure also distinguishes exact counts, lower and upper bounds, and approximate targets before choosing a change.

The v0.11.6 handoff and all other Skill procedures remain intact. No new tool, mandatory artifact, or repository-wide inventory is introduced.

## What v0.11.6 changes

v0.11.6 adds one bounded hardening to the existing `observable-product-verification` owner: **freshly acquired evidence is not automatically fresh observed state**. A successful screenshot/capture/observation call or newly written artifact can still replay stale, frozen, cached, or disconnected state.

The new rule is deliberately conditional:

```text
claim materially depends on live/current state
+ concrete reason the observation path may be stale/frozen/cached/replayed/disconnected
→ establish observation-path liveness
→ use independent ongoing activity or the smallest controlled observable stimulus
→ trust that oracle only if it reflects the expected change
```

The converse is protected too: identical observations alone do **not** prove a dead oracle when the underlying state may legitimately be static. If liveness cannot be established, use another appropriate boundary or keep the affected claim `INCONCLUSIVE`.

Two OPV regression evals protect both directions: `fresh-capture-does-not-prove-oracle-liveness` and `identical-static-observations-do-not-prove-dead-oracle`. No orchestration, ownership, debugging-owner, JIT-routing, verifier, review, or tooling semantics change.

## v0.11.5 routing baseline remains intact

v0.11.5's positively defined **local short path**, material-trigger routing, and removal of subjective `trivial` / `non-trivial` labels remain unchanged. File count and apparent difficulty are not policy triggers.

## v0.11.4 exact-gate baseline remains intact

The exact approval/admission boundary from v0.11.4 is unchanged: authorized reversible preparation may continue up to a project-defined gate, while a broader implementation request does not implicitly authorize crossing the gated state transition.

## v0.11.3 responsibility-coverage baseline remains intact

The bounded Responsibility Coverage Challenge from v0.11.3 remains unchanged: broad product/subsystem work checks for ordinary material responsibilities that were never considered, while domain expectations remain discovery hypotheses rather than project authority. Explicit exclusions/deferrals remain controlling, and narrow local tasks do not trigger whole-product reconstruction.

## v0.11.2 outcome/debugging baseline remains intact

Outcome-coverage reconciliation, exact symptom identity, evidence-driven debugging, workspace reconciliation, and the complete v0.11.1 ownership semantics are preserved unchanged.

## v0.11.1 ownership baseline remains intact

### Owner existence != reusable-seam proof

```text
Responsibility
→ test existing owner/capability extension/composition
→ resolve canonical Owner boundary
→ define Capability Contract if needed
→ test reusability separately when material
```

The Core-First Skill now states explicitly:

- a canonical owner does **not** require a second consumer, second implementation, unique lifecycle, or language-level interface;
- lifecycle, state proximity, consumer count, and implementation count are evidence, not mandatory owner criteria;
- second-consumer/provider proof is for **semantic reusability of a seam/capability**, not for proving that a responsibility deserves an owner;
- a detected ownership gap does not authorize a new owner; existing owner/capability extension/composition and smaller data/module/provider paths are tested first, otherwise the gap stays `UNRESOLVED`;
- semantic order is `Responsibility → Owner → Capability Contract`; an invented interface cannot manufacture ownership;
- an unauthorized foreign write is not automatically a second canonical owner;
- existing project architecture authorities are updated instead of creating a parallel ownership document by default.

### v0.11 responsibility-first owner resolution remains intact

```text
exact responsibility
→ current carrier / effective decision path
→ implementation anchor
→ canonical owner status
→ capability / module / provider / consumer / data role
→ smallest semantic correction or explicit unresolved gap
```

The v0.11 baseline distinctions remain:

- **owner is responsibility-relative** — class/file boundaries do not define owner boundaries;
- **current placement != canonical ownership** — code location is evidence, not authority;
- **parallel owner != provider variation** — two independent active authorities over the same responsibility conflict, while controlled providers behind one capability do not;
- **unresolved stays unresolved** — do not invent an owner merely to complete a map;
- **data != behavior owner** — central values with duplicated consumer-side rule execution are still duplicated behavior;
- **implementation count != capability identity** — one implementation can realize a real reusable contract, and several implementations can remain variants of one capability;
- **name != role** — `Service`, `Manager`, `Controller`, `Repository`, `Engine`, `Factory`, `Facade`, `Helper`, `Host`, `Renderer`, etc. neither prove nor disqualify ownership.

Detailed God-class/parallel-owner/gap recovery examples live in the existing JIT method reference rather than expanding Governance with a new procedure owner.

### v0.10 behavior remains intact

Evidence-driven hypothesis invalidation/effective-runtime-geometry routing and cheap post-compaction workspace awareness/JIT re-consumption are unchanged from v0.10.0.

## Existing v0.9 surface model remains intact

For material user-surface work:

```text
PROJECT USER-SURFACE AUTHORITY
        ↓
consume before implementation
        ↓
STYLE | STRUCTURE | PLACEMENT | HIERARCHY
SPACING/SCALE | STATES | RESPONSIVE | REFERENCES
        ↓
implementation
        ↓
REAL WHOLE SURFACE
        ↓
OPV against the same applicable authority
```

The agent distinguishes `CONFIRMED | INFERRED | UNKNOWN`; relative guidance stays relative. Optional Working Views/Atlases are disposable interpretation/cache, not authority.

## Context budget

The always-loaded orchestration kernel remains **10,998 bytes** and the complete owner-local orchestration corpus remains **26,444 bytes** under unchanged ceilings of **11,000-byte kernel**, **4,000 bytes per JIT reference**, and **26,500-byte total**. `core-first-extension-architecture/SKILL.md` remains **14,480 bytes** under its unchanged **15,000-byte** ceiling.

Only the JIT-loaded `observable-product-verification/SKILL.md` changes in v0.11.6: **15,681 → 16,907 bytes** (+1,226). No always-loaded Core-First context is added.

## Consumer-tool decision

No mandatory consumer-tool gap is introduced. The observed failures are reasoning/attention/evidence-consumption/context-continuity problems that can be corrected with small JIT Skill guidance plus existing host read/search/runtime/vision capabilities.

No bundled:

- `.mcp.json` / MCP server;
- computer-use stack;
- debugger tool;
- workspace database;
- atlas generator;
- sixth Skill.

## Hard invariants preserved

- Primary agent = orchestrator + final integrator, not dispatcher-only.
- When architecture/ownership/reuse is material, the primary agent **MUST load and apply `core-first-extension-architecture` itself**.
- Current repository/project/runtime truth outranks memory, old plans and derived views.
- Grounded Execution remains `DISCOVERED → INSPECTED → EXTRACTED → MAPPED → CONSUMED`.
- Adaptive execution is triggered by concrete dependencies/prerequisites/state transitions/meaningful multi-step work or invalidating evidence; local short-path work gets no planning ceremony.
- Existing project routing/index artifacts are reused before broad rediscovery.
- Core-First verifier remains fresh/read-only/two-phase.
- Independent Review remains anti-anchored.
- Project-defined external completion authority remains external.
- Portable Governance remains provider/tool neutral.

## Five Skills

| Skill | Canonical responsibility |
| --- | --- |
| `core-first-orchestration` | minimal-context routing, grounded/adaptive execution, outcome-coverage reconciliation, evidence-driven debugging, delegation/completion routing |
| `core-first-extension-architecture` | responsibility discovery/coverage challenge, owner/role resolution, reuse, composition, capabilities/providers/extensions, reverse-debug architecture path |
| `observable-product-verification` | real user/external outcomes, whole-surface fidelity, evidence reuse/traceability |
| `core-first-verifier` | fresh read-only two-phase Core-First conformance |
| `independent-review` | anti-anchored consequential/high-risk review |

## Windows / Codex UI installation

From the extracted release directory:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install-personal-windows.ps1
```

The installer copies the plugin to `%USERPROFILE%\.codex\plugins\core-first-governance` and updates `%USERPROFILE%\.agents\plugins\marketplace.json`. Restart the ChatGPT desktop app, install/update **Core-First Governance** from the Personal source, and start a new Codex thread.

## Repository layout

```text
.
├── README.md
├── CONTEXT_HANDOFF_2026-10-06_v0.11.6.md
├── RELEASE_AUDIT_v0.11.6.md
├── INSTALL-WINDOWS.md
├── install-personal-windows.ps1
├── sign-installer.ps1
├── validate_release.py
├── SHA256SUMS.txt
└── core-first-governance/
    ├── .codex-plugin/plugin.json
    ├── SOURCE_PROVENANCE.md
    └── skills/
        ├── core-first-orchestration/
        │   ├── SKILL.md
        │   └── references/
        │       ├── GROUNDED_EXECUTION_PREFLIGHT.md
        │       ├── ADAPTIVE_EXECUTION_AND_CONTEXT.md
        │       ├── EVIDENCE_DRIVEN_DEBUGGING.md
        │       ├── DELEGATION_CONTEXT.md
        │       └── VERIFICATION_AND_COMPLETION_ROUTING.md
        ├── core-first-extension-architecture/
        ├── observable-product-verification/
        ├── core-first-verifier/
        └── independent-review/
```

## Development rules

- Name the responsibility before declaring its owner; current carrier/name/size does not prove canonical ownership.
- For broad product/subsystem work, challenge whether an important ordinary responsibility was never considered; domain expectations are hypotheses, not authority.
- Owner existence is separate from reuse proof; second consumers, lifecycle, implementation count, or interfaces are evidence rather than mandatory owner criteria.
- Resolve `Responsibility → Owner → Capability Contract`; do not let an invented interface establish ownership.
- One canonical owner per durable responsibility; keep unresolved gaps explicit until evidence supports a path.
- Data centralization is not behavior convergence; implementation count does not define capability identity.
- JIT detail must be explicitly routed; context optimization may not weaken semantics.
- Negative evidence must invalidate dependent hypotheses, not merely add another note.
- Do not identify visual/runtime sources from resemblance or matching visible size alone.
- After context loss, discover current workspace state cheaply before JIT loading; never hydrate everything by default.
- Working aids remain cache and reuse existing discoverability/routing mechanisms.
- A local fix never replaces the original requested outcome boundary; completion is based on outcome coverage, not passing-evidence count.
- Use the local short path only when owner/path + semantics are clear, no material boundary/dependency decision remains, shared behavior/authoritative transitions stay unchanged, and direct bounded verification is sufficient; size/file count alone never decides materiality.
- Preserve approval/admission gates at the exact state transition: authorized reversible preparation before the gate continues; a broad request does not implicitly authorize crossing the gate.
- Preserve reported observable identity; nearby defects remain separate until causal identity is established.
- Do not add consumer tools merely because the host/plugin format supports them.
- Re-run release + host validation after Skill/manifest changes.

## License

No repository license has been selected in this package. Add the intended license before public redistribution if explicit terms are required.
