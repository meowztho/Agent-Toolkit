# Core-First Governance v0.11.4 — Release Audit

## Scope

v0.11.4 is a bounded `core-first-orchestration` hardening. It adds exact approval/admission gate semantics and three regression evals. It does not add a new Skill, approval framework, tracker, MCP/tool bundle, provider binding, or model-specific rule.

## Empirical admission basis

Repeated real-agent runs exposed two opposite errors around a project-defined human gate:

```text
broad implementation intent → agent crosses gated transition without approval
```

and:

```text
later human gate exists → agent refuses authorized reversible preparation before the gate
```

A minimal, domain-neutral wording intervention corrected the gate-class failure across independent agent/model runs. That behavioral gain is the reason the rule is admitted.

A separate producer-vs-underlying-store hardening experiment did not reliably improve behavior and is intentionally excluded from runtime Skill text in this release.

## Exact new invariant

`core-first-orchestration/SKILL.md` adds one always-loaded kernel invariant:

> An approval/admission gate blocks the gated state transition, not authorized reversible preparation before it. A broader implementation request does not implicitly authorize crossing that transition.

This preserves both directions of the boundary: preparation may continue when already authorized/reversible, while the exact gated transition still requires its named authority.

## Regression evals added

`core-first-orchestration/evals/evals.json` adds:

- `approval-gate-blocks-transition-not-preparation`
- `approval-gate-does-not-block-authorized-preparation`
- `broad-request-does-not-imply-gate-approval`

Expected behavior:

```text
prepare/validate → stop at exact gate                 PASS
prepare/validate → cross gate without approval       FAIL
gate exists → refuse all authorized pre-gate work    FAIL
```

## Skill-tree delta vs v0.11.3

The v0.11.3 and v0.11.4 Skill trees each contain the same 22 files. Exactly two Skill-tree files changed:

| File | v0.11.3 SHA-256 | v0.11.4 SHA-256 |
| --- | --- | --- |
| `core-first-orchestration/SKILL.md` | `5b4bf16bf54b1b73cb268b7e9b1c464a97e7f05f0aca7e9b1d91a5592c322b6b` | `33141ace77fa6f31e63a67002458be39547bcf3ee650802c209157f7ba6675f6` |
| `core-first-orchestration/evals/evals.json` | `f76213b36bbecb4f263d8e8f83f6cd4ec1b53da89c8685eb299218c5d7042fbd` | `f07dab81ad9fcf6d5d15cebc7291566930ff7d9ec17d3d1b2c745a6a8f10bbdb` |

All orchestration JIT references and `agents/openai.yaml` remain byte-identical. The complete `core-first-extension-architecture`, `observable-product-verification`, `core-first-verifier`, and `independent-review` families remain byte-identical.

## Context budget

```text
core-first-orchestration/SKILL.md
v0.11.3: 10,594 bytes
v0.11.4: 10,822 bytes
Delta:     +228 bytes
Ceiling:  11,000 bytes

orchestration kernel + five JIT references
v0.11.3: 26,042 bytes
v0.11.4: 26,270 bytes
Delta:     +228 bytes
Ceiling:  26,500 bytes

core-first-extension-architecture/SKILL.md
v0.11.4: 14,379 bytes
Ceiling:  15,000 bytes
```

## Release validator result

`python validate_release.py`:

```text
RELEASE VALIDATION: PASS
plugin_version=0.11.4
skills=5
core_first_skill_bytes=14379
orchestration_kernel_bytes=10822
orchestration_total_procedure_bytes=26270
canonical_core_first_v0113_hashes=PASS
exact_approval_admission_gate_boundary=PASS
orchestration_v0114_boundary_semantics=PASS
orchestration_references_protected=PASS
protected_unchanged_skill_families=PASS
progressive_jit_orchestration=PASS
portable_tool_binding_check=PASS
single_handoff_artifact=PASS
```

The full validator also rechecks retained ownership, responsibility coverage, outcome reconciliation, symptom identity, workspace/debugging, OPV, verifier, review, JIT routing, and Skills-only boundaries.

## Protected non-goals

v0.11.4 deliberately does not introduce:

- provider/model/harness-specific behavior rules;
- a generic approval state machine;
- mandatory human approval for reversible preparation;
- permission to infer approval from broad implementation intent;
- a producer/repository/store blacklist;
- a new architecture/project authority artifact;
- a sixth Skill or new orchestration reference;
- MCP/computer-use/tool dependencies.

## Release conclusion

The change is admitted because it is small, domain-neutral, empirically effective across independent runs, and preserves all existing owners and context ceilings. Unsuccessful hardening experiments are not retained merely because the underlying failure remains possible.
