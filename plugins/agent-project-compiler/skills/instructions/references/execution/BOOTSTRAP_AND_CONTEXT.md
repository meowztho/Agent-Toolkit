# Execution Runtime Guide

# Current Precedence — Provider-Safe Runtime, Derived Admission, Product Continuity and Verification Truth

Fresh/session recovery order: Portable Operating Kernel → root instructions if available → `PROJECT_INDEX` bootstrap/lifecycle route → refresh/inspect Atlas when required → derive exact `required_source_ids` → actually read normative authorities → record current-session `loaded_source_ids` → context/read gate → classify current change → implementation.

`loaded_source_ids` is ephemeral; reset/re-resolve after fresh session, major context loss/compaction, relevant authority revision or domain/requirement switch. START/Atlas summaries never satisfy normative reads.

Before selecting the next material requirement/work item, evaluate dependency/admission conditions routed from `PROJECT_PLAN`, Acceptance and relevant System/Capability/Integration authorities:
`unmet/reopened outcomes → resolve prerequisites → evaluate required maturity/evidence → ADMISSIBLE WORK SET → priority/risk/value selection`.

Do not choose a task merely because it is runnable, easy to measure, already has a harness or appears next/interesting. If downstream work is not admitted, only explicitly allowed exploratory synthetic/unit/integration/spike work may run; label its evidence non-authorizing for product conclusions. After prerequisite evidence changes, recompute admission.

After local fixes reconcile the original requested outcome and current evidence before moving on; nearby symptoms or test volume do not redefine the goal.


## Exact transition-gate execution
When current project authorities define an approval/admission gate around a specific transition, do not treat `awaiting approval` as a global stop unless the authorities explicitly say so. Continue authorized reversible preparation and other admissible work up to the boundary. Immediately before the gated state change/side effect, resolve the exact gate authority and require current scoped approval evidence. A broad implementation request, completed preparation, passing tests or technical admission does not substitute for that approval.

If approval is absent, preserve the transition as not crossed, record the real state, and continue other admissible work when available. Ask the user only when that approval is genuinely the next blocking user-owned decision/transition. After explicit approval, record it at the scope required by the project and cross only the transition it authorizes; do not silently reuse approval for a different revision/transition unless the authority permits it.

---


## Purpose

The project package must tell the coding agent not only WHAT the project is,
but WHEN to inspect, blueprint, implement, verify, clean up, review, commit,
and perform real-user testing.

Use a phase machine instead of an undifferentiated "work until done" loop.

---

# 1. Runtime Phases

Recommended phase order:

```text
BOOTSTRAP_REPOSITORY
→ DISCOVER_CAPABILITIES
→ BIND_AGENT_RUNTIME
→ LOAD_BOOTSTRAP_CONTEXT
→ VERIFY_AUTHORITY_REACHABILITY     # package discoverability gate
→ VERIFY_ATLAS_FRESHNESS             # nontrivial generated-view validity
→ INSPECT_ATLAS_ORIENTATION          # whole-project orientation, not authority
→ VALIDATE_PROJECT_RECONSTRUCTION   # fresh compiled project/agent when required
→ SELECT_REQUIREMENT
→ RESOLVE_REQUIRED_AUTHORITIES
→ LOAD_JIT_CONTEXT
→ VERIFY_CONTEXT_LOAD_GATE
→ CLASSIFY_CHANGE_ARCHITECTURE
→ RESOLVE_SKILLS_FOR_REQUIREMENT
→ BLUEPRINT_OR_REUSE
→ IMPLEMENT_UNIT
→ VERIFY_UNIT
→ INTEGRATE
→ VERIFY_INTEGRATION
→ AUDIT_SYSTEM_INTEGRATION          # when cross-system behavior changed
→ VERIFY_USER_SURFACE               # when observable
→ HYGIENE
→ RECORD_MILESTONE
→ repeat SELECT_REQUIREMENT
→ FINAL_CONTRACT_AUDIT
→ FINAL_BUILD_TEST
→ FINAL_USER_SURFACE_GATE           # when applicable
→ INDEPENDENT_REVIEW                # when triggered
→ FINAL_GIT_CHECK
→ COMPLETE
```

A failure returns to the earliest phase capable of fixing the root cause.

---

# 2. BOOTSTRAP_REPOSITORY

For coding projects:

1. identify the intended project/repository root;
2. inspect applicable instructions;
3. determine whether Git exists;
4. if no Git repository exists:
   - initialize Git unless explicit project/user policy forbids it;
   - create/update an appropriate `.gitignore` before staging;
   - never stage obvious secrets, credentials, build caches, generated binaries,
     temporary evidence, or tool-specific junk unless intentionally versioned;
5. inspect branch/HEAD when available;
6. inspect `git status`;
7. inspect relevant existing diffs;
8. preserve unrelated changes.

`git init` is repository setup, not permission to rewrite user files.

For a new agent-owned project, create a recoverable baseline/verified milestone commit
when project policy permits it.

For an existing/shared project, follow `contracts/VERSION_CONTROL.yaml`.

---

# 3. DISCOVER_CAPABILITIES

Before planning verification, determine what the current harness can actually do. User-surface tools are recorded here; agent-loop/customization primitives are bound separately in `AGENT_RUNTIME_PROFILE.yaml`.

Generate/update:

```text
verification/TOOL_CAPABILITIES.yaml
```

Example:

```yaml
capabilities:
  interactive_desktop:
    available: true
    adapter: computer_use
    verified_by: tool_exposed

  browser_interaction:
    available: false

  screenshot_capture:
    available: true
    adapter: computer_use

  engine_runtime:
    available: true
    adapter: unreal_editor

  shell:
    available: true

selected:
  user_surface_adapter: computer_use
  screenshot_adapter: computer_use
```

Do not assume a model/provider capability implies the current harness exposes it.

If a suitable tool is exposed, a user-facing final gate MUST actually invoke it.
"Available but unused" is a verification failure.

If unavailable, choose the strongest real alternative:
- headed browser automation;
- editor/runtime automation;
- OS screenshot utility;
- engine screenshot/frame capture;
- rendered artifact capture;
- real CLI/client.

If required user-surface evidence cannot be produced by any available method,
the affected criterion stays unverified/blocked. Do not claim completion.

---

# 4. BIND_AGENT_RUNTIME

For a nontrivial autonomous project, discover the actual agent/client/harness customization primitives and generate/update:

```text
contracts/AGENT_RUNTIME_PROFILE.yaml
```

Record actual support and selected bindings for persistent instructions, Agent Skills, lifecycle hooks, subagents/fresh contexts, MCP/external tools, provider memory, workflows/commands, and worktrees/sandboxes.

Rules:
- project authorities remain provider-neutral;
- use one canonical instruction kernel plus thin provider adapters when needed;
- bind deterministic completion/integration/policy validators to blocking lifecycle hooks when available;
- otherwise preserve the same validators as explicit phase gates;
- use isolated subagents/fresh sessions for reconstruction/review/noisy exploration when available;
- never require provider memory or session history to reconstruct the project.

Use `AGENT_RUNTIME_PORTABILITY_GUIDE.md`. Refresh the profile when the harness/provider/session capabilities materially change.

---

# 5. LOAD_BOOTSTRAP_CONTEXT

On a fresh implementation turn, consume the generated context-rich `START_PROMPT` orientation first. It should state the product/master outcome, material decision context, systems/compositions/guardrails and execution intent directly.

Then read `PROJECT_INDEX.yaml` and every direct `bootstrap.must_read` authority declared there before the first material source edit. Also load the compact routing/state layer:

- root/applicable `AGENTS.md`;
- `PROJECT_REGISTRY.yaml`;
- `ACCEPTANCE_MATRIX.yaml`;
- `STATE.json`;
- Blueprint registry;
- execution/verification policies.

`PROJECT_INDEX.yaml` is the canonical discoverability router. Do not replace it with prose chains such as "read A, then A tells you to read B". Do not preload every JIT authority after bootstrap; initial understanding is context-rich, exact repeated execution is routed JIT.

---

# 6. VERIFY_AUTHORITY_REACHABILITY

Run the generated project contract/reachability validator before trusting the package structure on a fresh compiled project, after structural documentation/registry changes, and before final completion.

The validator must compute reachability from:
- `PROJECT_INDEX.bootstrap.must_read`;
- every `PROJECT_INDEX.domains.*.authority_ids` route;
- `PROJECT_REGISTRY.yaml` artifact identity/`normative` metadata;
- routed Blueprint IDs plus registered Blueprint `call` edges.

It must reject:
- unresolved route IDs;
- active normative/discoverability-required artifacts that have no incoming bootstrap/JIT route;
- active normative Blueprints that are neither routed nor reachable from a routed Blueprint;
- deprecated/superseded artifacts still used as active routes.

Write generated evidence to `verification/AUTHORITY_REACHABILITY.yaml`. That report is diagnostic evidence, not a second routing authority.

If reachability fails, fix the canonical router/registries first. Do not compensate by manually reading the orphan file and continuing.

---

# 7. VERIFY_ATLAS_FRESHNESS

For every nontrivial compiled project, resolve `VIEW-PROJECT-ATLAS` and its registered generator/source metadata. Recompute whether the generated view matches the current canonical Atlas inputs.

If stale or missing:
- regenerate it from canonical sources;
- update its generated source fingerprint/revision metadata;
- do not manually edit project truth into the HTML;
- fail/block bootstrap if a required Atlas cannot be regenerated and no honest stale status is recorded.

The Atlas remains `normative: false`. Freshness is a generated-view validity property, not authority precedence.

---

# 8. INSPECT_ATLAS_ORIENTATION

On a fresh implementation session, major context recovery, or Fresh-Agent Reconstruction, actually inspect the fresh Atlas once before task-local JIT work. Record `VIEW-PROJECT-ATLAS` in `STATE.context.inspected_view_ids` when the harness can track/attest it.

Use it to restore the whole-product picture: vision capsule, decisions/guardrails, systems/capabilities/compositions, user flow, current acceptance state, blockers and canonical IDs. Then use `PROJECT_INDEX.yaml` for exact authorities.

The Atlas cannot satisfy `required_source_ids`; orientation-view inspection and normative-source loading are separate gates.

---

# 9. VALIDATE_PROJECT_RECONSTRUCTION

For a fresh nontrivial compiled project, inspect `verification/FRESH_AGENT_RECONSTRUCTION.yaml` before implementation work. Read `CONTEXT_HANDOFF.md` + `docs/DECISION_COMPENDIUM.md` once for the holistic product model.

If the reconstruction criterion is already passed with valid package-level evidence, do not rerun it on every resume. If it is missing/pending/stale after material specification changes, run the reconstruction procedure defined in `FRESH_AGENT_RECONSTRUCTION_GUIDE.md` before task implementation. Prefer an independent fresh agent/subagent when the harness exposes one; otherwise record the weaker self-isolated fallback honestly.

A material misconception is a specification/package defect or bootstrap-context defect. Fix/clarify canonical authorities and regenerate the Start/Goal orientation snapshot; ask the user only for genuinely unresolved product intent. Do not compensate with undocumented private explanation.

---

# 10. SELECT_REQUIREMENT

Choose the highest-priority required criterion that is:

- unverified;
- reopened;
- stale;
- blocked by work the agent can now resolve.

Prefer requirements that restore the walking skeleton / normal user flow.

Do not optimize for easiest-to-complete criteria if a broken core route blocks the
actual product.

---

# 11. RESOLVE_REQUIRED_AUTHORITIES

For the active criterion/change:

1. classify the relevant `PROJECT_INDEX.yaml` domain route(s);
2. expand declared route dependencies only as needed;
3. collect authority IDs and any routed Blueprint IDs;
4. resolve current paths through `PROJECT_REGISTRY.yaml` / Blueprint registry;
5. write the exact set to `STATE.json.context.required_source_ids`;
6. if a required normative authority is missing/unrouted, stop implementation and repair package routing.

Do not infer the source set from filenames, old chat, or memory when the router exists.

---

# 12. LOAD_JIT_CONTEXT

For the active criterion:

1. read the criterion entry;
2. read every `STATE.context.required_source_ids` authority needed for the dependent change;
3. load only relevant behavior/data/implementation Blueprints reached by the route/call graph;
4. inspect current implementation and call sites;
5. load applicable local `AGENTS.md` for target paths;
6. inspect relevant tests/evidence;
7. record current-session loaded-source evidence when possible;
8. do not reread unrelated stable context.

---

# 13. VERIFY_CONTEXT_LOAD_GATE

Before the first material source edit, compare `STATE.context.required_source_ids` with the authorities actually loaded in the current context/session.

PASS requires every required source to be current enough for the change. If the harness exposes file-read/tool hooks, derive `loaded_source_ids` from observed reads. Otherwise record explicit runtime attestation after actual reads; do not mark sources loaded merely because they exist.

Reset/re-evaluate this gate after:
- a fresh session;
- major compaction/context loss;
- material authority changes;
- switching to a requirement/domain whose required-source set differs.

A missing required authority blocks source edits. Reading an implementation file is not a substitute for reading its project authority.

---

