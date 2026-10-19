# Core-First Governance v0.11.5 — Release Audit

## Scope

v0.11.5 is a bounded routing-language clarification. It removes subjective `trivial` / `non-trivial` labels from active Core-First runtime text and replaces them with explicit material triggers plus a positively defined local short path. The v0.11.4 exact approval/admission gate semantics and all prior ownership/outcome/debugging/verification invariants remain intact.

No new Skill, owner, planner, complexity score, file-count threshold, tracker, MCP/tool bundle, or provider/model-specific rule is introduced.

## Runtime contract

Local short path is eligible only when all hold:

```text
owner/edit location + semantics are clear
no material architecture/contract/producer/persistence/gate/authority/dependency decision remains
shared behavior / authoritative state transitions are unchanged
direct bounded verification is sufficient
```

`FILE COUNT / APPARENT DIFFICULTY != MATERIALITY`.

Adaptive execution is triggered by concrete dependency/prerequisite/state-transition/multi-step/evidence-invalidating properties rather than a subjective task-size adjective.

## Skill-tree delta vs v0.11.4

Exactly six Skill-tree files changed:

| File | v0.11.4 SHA-256 | v0.11.5 SHA-256 | Bytes 0.11.4 → 0.11.5 |
| --- | --- | --- | ---: |
| `core-first-extension-architecture/SKILL.md` | `444e938a4fb7d27143231019b2dee6f58c8a53c0091d9994540e58f177abbadb` | `d1732b2eb6861cf3a9c0137f054e23ea95f062912cce71ee2458e6d100432e2c` | 14,379 → 14,480 |
| `core-first-extension-architecture/references/EXTENSION_ARCHITECTURE_METHOD.md` | `9457f85fc9259d6df32f7ddde819c232e9b476cfd4b044c87208886f262149d7` | `55ba875d5d2e1b2ba42bef92ce5cbaf08c38008a9a4ee45fbbd990261730248f` | 14,656 → 14,871 |
| `core-first-orchestration/SKILL.md` | `33141ace77fa6f31e63a67002458be39547bcf3ee650802c209157f7ba6675f6` | `d29e8601a90b51c9fe7cbc023f2652a2702e9d645424263c648acba73c201ec6` | 10,822 → 10,998 |
| `core-first-orchestration/evals/evals.json` | `f07dab81ad9fcf6d5d15cebc7291566930ff7d9ec17d3d1b2c745a6a8f10bbdb` | `4cede292e10a3bd57ea5d197098671558e6d6ae7912fb135cbf624b9fd35385b` | 24,456 → 25,885 |
| `core-first-orchestration/references/ADAPTIVE_EXECUTION_AND_CONTEXT.md` | `74791843b196c28d41f56b6aeaaa0e4652bfadd466fe738ae0b4486b8b1fbbb0` | `409cf938d5b77146809203dd0c7957512789d7c0121ce43616a3416fc1261e23` | 3,688 → 3,695 |
| `core-first-orchestration/references/GROUNDED_EXECUTION_PREFLIGHT.md` | `c75e19feec7e9406abc359245b329b2221088b7c1a56ab81341ab0176701f911` | `4bcb77ddaaa59eb5b8e1d4826d94ef1c6d28c168e0f10e037ad67ba4c0ca6799` | 3,465 → 3,456 |

All other Skill-tree files remain hash-protected and unchanged.

## Eval delta

Ambiguous eval names/prompts were rewritten around explicit conditions:

- `trivial-local-edit` → `local-short-path-static-label`
- `nontrivial-adaptive-execution-before-edits` → `dependency-driven-adaptive-execution-before-edits`
- `trivial-edit-no-planning-ceremony` → `local-short-path-no-planning-ceremony`

Two new domain-neutral evals were added:

- `small-edit-crosses-material-boundary`
- `large-mechanical-edit-can-use-local-short-path`

The first prevents “small-looking” from bypassing material architecture/authority/gate boundaries. The second prevents file count alone from forcing Core-First/adaptive planning ceremony.

## Context budget

```text
orchestration kernel:                 10,998 / 11,000 bytes
orchestration kernel + 5 JIT refs:   26,444 / 26,500 bytes
largest orchestration JIT ref:        3,695 / 4,000 bytes
core-first-extension-architecture:   14,480 / 15,000 bytes
```

## Validation evidence

Executed on the packaged v0.11.5 tree:

```text
python validate_release.py
→ RELEASE VALIDATION: PASS
→ plugin_version=0.11.5
→ skills=5
→ explicit_materiality_short_path=PASS
→ exact_approval_admission_gate_boundary=PASS
→ consumer_tool_bundle=ABSENT_BY_DESIGN
→ single_handoff_artifact=PASS

python /mnt/data/validate_plugin.py core-first-governance
→ Plugin validation passed
```

The release validator also rejects ambiguous `trivial` / `non-trivial` routing labels if they reappear in the active orchestration/Core-First runtime corpus.

## Preserved boundaries

v0.11.5 deliberately does not introduce:

- a complexity score or “task size” classifier;
- line-count/file-count thresholds;
- a mandatory plan for multi-file edits;
- a sixth Skill;
- a new architecture/project authority artifact;
- a new approval mechanism;
- model/provider-specific hardening;
- an MCP/tool bundle.

The semantic rule is intentionally small: route by **material properties**, not by subjective labels.
