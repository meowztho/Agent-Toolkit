# Agent Runtime Portability and Enforcement Guide

# Current Precedence — Portable Operating Kernel

Never assume a provider automatically loads root instructions, Skills, hooks or memories. Generated START/CONTINUE/GOAL carry a small provider-safe Portable Operating Kernel that tells the agent how to locate root instructions when present, read `PROJECT_INDEX.yaml`, derive required sources, actually load them and obey current verification/change/admission gates.

Provider-specific autoload/hooks/subagents/MCP/memory are runtime capabilities and thin bindings, never hidden correctness assumptions. Chat/provider memory is convenience cache only.

---


## Purpose

The compiled project must not depend conceptually on one coding-agent vendor.

Different harnesses expose overlapping but distinct primitives: persistent instruction files, Agent Skills, lifecycle hooks, subagents, MCP/tools/extensions, workflows/commands, memories/knowledge, worktrees/sandboxes, and user-surface tools.

The compiler must preserve one provider-neutral project model and bind it to the strongest available runtime primitives without duplicating project truth.

Core rule:

```text
PROJECT TRUTH
!=
AGENT RUNTIME CUSTOMIZATION
```

Project authorities define the product. Runtime customizations help an agent execute those authorities reliably.

---

# 1. Canonical primitive selection

Choose the mechanism by semantic purpose, not by whichever feature a provider happens to advertise.

| Need | Canonical project representation | Preferred runtime binding |
|---|---|---|
| Product behavior / exact requirement | docs/contracts/Blueprints | JIT read from authority |
| Always-applicable engineering behavior | root/local instruction kernel | `AGENTS.md` or thin provider adapter |
| Repeatable multi-step procedure | project/global Agent Skill | Agent Skills-compatible `SKILL.md` |
| Deterministic invariant / blocking gate | validator/contract | lifecycle hook + validator when supported |
| Noisy exploration / independent review | scoped task contract | isolated subagent/fresh session |
| External tool/system/context | integration contract | MCP/plugin/extension/native tool |
| Manual reusable recipe | optional workflow/command | provider workflow/command if useful |
| Learned operational convenience | non-canonical runtime memory | memory/knowledge only when safe |
| Project truth discovered during work | authoritative project file | promote from memory/chat immediately |

Do not put detailed product truth into a skill, hook, provider memory, or vendor-specific rules file merely because that mechanism is convenient.

---

# 2. Runtime profile contract

For nontrivial autonomous coding projects generate:

```text
contracts/AGENT_RUNTIME_PROFILE.yaml
```

This contract records the capabilities actually exposed by the selected harness/session and the chosen bindings.

It is not a product authority and must not contain duplicated project requirements.

Recommended capability dimensions:

```yaml
runtime:
  provider: null
  client_or_harness: null
  version: null

capabilities:
  hierarchical_instructions:
    available: false
    mechanism: null

  agent_skills:
    available: false
    standard_compatible: null
    project_path: null
    supports_multi_skill_composition: null

  lifecycle_hooks:
    available: false
    session_start_context: null
    user_prompt_context: null
    pre_tool_gate: null
    post_tool_observer: null
    pre_compact: null
    post_compact: null
    stop_or_finish_gate: null

  subagents:
    available: false
    isolated_context: null
    parallel: null

  mcp_or_external_tools:
    available: false
    mechanism: null
    permission_model: null
    read_only_mode_available: null
    trust_reviewed: false

  persistent_memory:
    available: false
    canonical_project_truth_allowed: false

  workflows_or_commands:
    available: false

  worktrees_or_sandboxes:
    available: false

bindings:
  instruction_kernel: AGENTS.md
  skill_router: null
  architecture_law_context_hook: null
  authority_reachability_validator: null
  required_source_load_observer: null
  required_source_gate_hook: null
  change_classification_gate_hook: null
  context_rehydration_hook: null
  completion_gate_hook: null
  integration_audit_hook: null
  reconstruction_executor: null
  independent_review_executor: null
  external_tool_adapter: null

fallbacks: []
```

Populate this from actual runtime discovery. Never infer a capability solely from the model name.

`verification/TOOL_CAPABILITIES.yaml` remains the authority for user-surface/browser/desktop/screenshot verification capabilities. `AGENT_RUNTIME_PROFILE.yaml` covers agent-loop/customization primitives. Keep them separate.

---

# 3. Thin provider adapters

Use one canonical project instruction kernel.

Prefer:

```text
AGENTS.md
```

when the harness supports it.

When a harness requires another persistent context file, generate a thin adapter such as a provider-specific context file that:

- identifies the canonical project authorities;
- restates only the minimum runtime invariants necessary for that harness;
- points back to `AGENTS.md`, `PROJECT_INDEX.yaml`, contracts and registries;
- is clearly marked generated/provider-specific;
- is regenerated from the canonical kernel rather than hand-maintained as another source of truth.

Do not maintain independent full copies of project behavior in several provider instruction formats.

---

# 4. Hook-backed enforcement

If the harness exposes lifecycle hooks capable of observing/blocking completion or tool execution, bind deterministic project gates to them.

Examples of appropriate deterministic bindings:

```text
agent attempts finish/stop
→ run acceptance/evidence/completion validator
→ PASS: allow finish
→ FAIL: block finish and return exact missing evidence/work
```

```text
cross-system structural change completes
→ run contract validator + integration audit
→ violations reopen requirement / block milestone
```

```text
before destructive/high-risk operation
→ enforce repository/project policy
```

```text
before first source write for a material user delta
→ require current requirement's routed authority set + current-session context-load gate
→ require current change classification + canonical system/capability path
→ block when required authorities are unread/stale, a required generated orientation view is stale/uninspected on bootstrap, or the reusable owner is unresolved
```

```text
user prompt/session start/after compaction
→ re-inject the short architecture law + master outcome/current capability pointer when supported
→ reset/re-evaluate session loaded-source evidence and route the next requirement through PROJECT_INDEX
```

The LLM may decide what to implement and how to correct failures. It must not be the sole authority deciding whether a deterministic gate ran or passed when the runtime can enforce that mechanically.

If hooks are unavailable, retain the same validator and explicit phase gate in the prompts/runtime policy. Record that enforcement is cooperative rather than hook-backed.

Do not make project semantics dependent on a vendor-specific hook event name. Store semantic events (`session_start`, `user_prompt`, `before_source_write`, `before_compact`, `after_compact`, `after_tool`, `attempt_finish`, etc.) and map them in the runtime profile. For providers that support prompt/compaction hooks, use them to re-inject the short architecture law and current master-outcome/capability pointer after steering or compaction; canonical truth remains on disk.

---

# 5. Subagent / fresh-context policy

Use isolated workers for work whose token/noise profile or independence matters:

- repository reconnaissance;
- broad research;
- test/log triage;
- independent review;
- Fresh-Agent Reconstruction;
- parallel bounded investigations.

The parent agent remains responsible for integrating results into canonical project state.

For Fresh-Agent Reconstruction, prefer an isolated context that receives only the allowed package inputs. Do not leak the original interview/chat, implementation-agent conclusions, or hidden summaries into the reconstruction worker.

Subagent output is evidence/input, not canonical project truth until validated and promoted into the proper authority.

---

# 6. Memory / knowledge hygiene

Provider memory is useful but is not a project database.

Allowed memory examples:
- local environment convenience;
- recurring non-canonical troubleshooting hint;
- temporary navigation preference;
- agent-specific operating tip.

Promote instead of leaving in memory when the information becomes:
- a product requirement;
- architecture or ownership rule;
- accepted decision/rationale;
- authoritative identifier/value;
- repeated project procedure;
- verified runtime fact needed for future acceptance.

Promotion destination:

```text
requirement/decision → project authority
repeatable procedure → skill
runtime capability → AGENT_RUNTIME_PROFILE / TOOL_CAPABILITIES
verification result → evidence index
```

Do not let hidden/private provider memory become necessary to reconstruct the project.

---

# 7. External tool / MCP trust boundary

Treat external tools, MCP servers, plugins and extensions as privileged integration dependencies. Before binding a material capability, identify:
- what data/context the tool can read;
- what external side effects it can perform;
- authentication/secrets required;
- whether read-only/restricted mode exists;
- whether the project acceptance flow truly needs write capability;
- how tool failure/absence affects verification/completion.

Prefer least privilege and read-only access for discovery/review tasks. Record the selected adapter/trust posture in the runtime profile or integration contract rather than assuming all connected tools are equally safe.

---

# 8. Portable Agent Skills

Prefer the open Agent Skills shape for reusable procedures:

```text
skill-name/
  SKILL.md
  references/   # optional JIT detail
  scripts/      # optional deterministic helpers
  assets/       # optional templates/resources
```

For the portable core, keep frontmatter minimal and standard-compatible. Put provider-specific extensions in generated overlays/adapters when they materially help.

Skill design rules:
- one coherent job per skill;
- strong description that says when it should and should not trigger;
- progressive disclosure: small `SKILL.md`, large details in referenced files;
- imperative workflow with explicit inputs/outputs/checkpoints;
- scripts only when determinism/tooling is useful;
- test positive triggers, negative triggers and representative execution;
- pin/review external skill source, version/commit and integrity when practical;
- inspect scripts, dependencies, permissions and license before trust;
- project truth remains outside the skill.

Do not require simultaneous activation of several skills for correctness. Runtime support for skill composition varies. A project must remain executable when the harness can load only one procedural skill at a time; a top-level procedure may JIT-read references/contracts and call external tools without requiring another skill to be concurrently active.

`contracts/SKILL_REQUIREMENTS.yaml` describes needed capabilities and resolved candidates, not an unconditional list of everything to install or load.

---

# 9. Capability-based skill categories

Do not hard-code a universal catalog by product type. Derive skills from the actual systems, surfaces, integrations and verification needs.

Common capability families worth considering when relevant:
- skill creation/evaluation;
- codebase reconnaissance/onboarding;
- framework/language expertise;
- testing and user-surface QA;
- debugging/build/CI;
- code/security review;
- external integration/MCP authoring;
- design-system/frontend implementation;
- database/migration/data pipelines;
- deployment/release;
- artifact production (documents, spreadsheets, slides, PDFs, media);
- observability/performance;
- agent governance/supply-chain safety.

Resolve the smallest sufficient set. Reject irrelevant or overlapping skills with reasons so later agents do not repeatedly rediscover them.

---

# 10. External skill supply-chain contract

For an external skill resolution, record when practical:

```yaml
source:
  repository: "..."
  path: "..."
  version_or_commit: "..."
  content_hash: "..."
  license: "..."

review:
  scripts_reviewed: true
  dependencies_reviewed: true
  permissions_reviewed: true
  trigger_scope_reviewed: true
  overlap_reviewed: true

resolution:
  status: accepted
  capability_ids: []
  reason: "..."
```

Never treat popularity/star count as sufficient trust evidence.

---

# 11. Provider-neutral completion authority

Completion semantics are project-level and provider-neutral:

```text
required acceptance
+ required evidence
+ current non-stale revision
+ required integration/surface/reconstruction gates
→ validator PASS
→ eligible for COMPLETE
```

A provider event such as turn-end, agent-stop, subagent completion, workflow completion or successful tool call is only a runtime event.

When a blocking finish hook exists, attach the validator there.
When it does not, execute the same validator explicitly in the phase machine.

This preserves the completion model when switching agents/harnesses.

---

# 12. Portability audit

Before delivering a nontrivial compiled package, ask:

1. Is any important project truth stored only in a provider-specific primitive?
2. Can the package run with a different capable agent by replacing only runtime adapters?
3. Are provider instruction files thin adapters rather than duplicate authorities?
4. Are deterministic invariants implemented as validators and hook-bound when possible?
5. Can skills be resolved JIT and do they remain optional execution aids?
6. Does Fresh-Agent Reconstruction run in isolated context when the runtime supports it?
7. Is memory non-canonical and promotable?
8. Are external tools integrations explicit rather than assumed?
9. Are external skills pinned/reviewed sufficiently for the project's risk level?
10. Is the project still understandable without any provider account/session history?

A failure here is a portability/reliability defect, not a reason to duplicate all project knowledge into each provider format.

# Optional Core-First Governance binding with project-native fallback

A compiled project may prefer a runtime capability such as `core-first-governance`, but project correctness must not depend on that plugin being installed, remembered, or automatically inherited by the host.

When the user's target environment exposes such a capability, record a thin runtime binding in `AGENT_RUNTIME_PROFILE` (actual discovery/invocation mechanism, freshness behavior, and fallback). Generated START/CONTINUE/root instructions should say, semantically:

```text
architecture-relevant work or fresh/compacted context
→ if actually available, resolve current `core-first-orchestration` routing semantics JIT
→ when architecture/ownership/reuse/composition is material, primary agent loads + applies `core-first-extension-architecture` before freezing the change boundary
→ load verifier/observable/review procedures only on their material triggers
→ run the project-native project gate
→ consume exact project authorities
```

If unavailable:

```text
→ state/use project-native fallback
→ run the same project gate
→ follow root architecture law + System/Capability/Integration/Plan/Acceptance authorities
```

Never fabricate a plugin invocation or mark it loaded from memory alone. Remembered Skill/plugin content is cache. The project-native gate cannot prove that a model followed an external Skill; it guarantees only deterministic project checks and keeps the package usable without that Skill.

Where host lifecycle hooks exist, bind the project gate to suitable pre-edit/resume/stop boundaries. Without hooks, make the same commands explicit execution gates. Do not add a second Governance platform.
