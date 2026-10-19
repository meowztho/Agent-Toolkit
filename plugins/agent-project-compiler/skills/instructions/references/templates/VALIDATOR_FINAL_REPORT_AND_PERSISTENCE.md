# APC v2.35 JIT Slice — Validator, Final Report and Persistence Templates

This file is a context-bounded split of the prior canonical `RUNTIME_TEMPLATES.md`. The normative content below is preserved; routing changed, not product/compiler semantics.

## Required command semantics

```text
project_gate validate
  parse + shape + ID/reference + reachability + freshness checks

project_gate preflight
  validate
  print current admitted stage/outcome
  print exact required authority/reference IDs
  print Core-First reminder / optional Governance binding reminder
  fail if current stage prerequisites encoded by existing Plan/Acceptance/State are not satisfied
  reject production-skeleton admission when required survivability Acceptance evidence is absent

project_gate self-test
  run validator against temporary known-bad mutants
  require every declared negative control to be rejected

project_gate handoff
  validate + require applicable State/Handoff/Atlas/verification reconciliation/freshness

project_gate completion
  handoff checks
  + reread/reconcile canonical current State + Plan + Acceptance
  + require all completion-critical evidence IDs/artifacts current
  + run/require declared final build/runtime/browser gates
  + reject claims based only on file existence, M0/foundation/project-gate success, or code volume
```

## Generated validator requirements

Use a real parser for each structured format. If a required parser dependency is unavailable, report a hard validation capability failure; do not fall back to regex and claim PASS.

Generate project-specific validation tables/functions for the concrete package, such as:

```python
STRUCTURED_AUTHORITIES = [
    "PROJECT_INDEX.yaml",
    "PROJECT_REGISTRY.yaml",
    "ACCEPTANCE_MATRIX.yaml",
    "contracts/SYSTEM_MAP.yaml",
    "contracts/CAPABILITY_GRAPH.yaml",
    "contracts/SYSTEM_INTEGRATION.yaml",
    "blueprints/REGISTRY.yaml",
]

# Generated from this project's real shapes; examples only.
REQUIRED_MAPPING_KEYS = {
    "PROJECT_REGISTRY.yaml": ["artifacts"],
    "contracts/SYSTEM_MAP.yaml": ["systems"],
    "contracts/CAPABILITY_GRAPH.yaml": ["capabilities"],
}
```

Then validate referential integrity across the actual package IDs and paths. A regex search for `path:` + filesystem existence is explicitly insufficient.

## Negative-control self-test

The generated gate should exercise its validation functions against temporary/copy-on-write mutations instead of corrupting the working repository. Include only cases relevant to the generated package, but normally at least:

```text
MUTANT-INVALID-STRUCTURE
  break YAML/JSON syntax or a required mapping shape
  expected: FAIL

MUTANT-BROKEN-REFERENCE
  replace one known System/Capability/Blueprint/Acceptance reference with UNKNOWN-ID
  expected: FAIL

MUTANT-ORPHAN-AUTHORITY
  create/register a normative authority that PROJECT_INDEX cannot reach
  expected: FAIL

MUTANT-REGISTRY-MISMATCH
  make Blueprint/registry identity disagree with its file metadata
  expected: FAIL

MUTANT-STALE-VIEW-OR-STATE   # when freshness is encoded
  alter a fingerprinted source without refreshing derived evidence
  expected: FAIL

MUTANT-UNMET-ADMISSION       # when staged admission is material
  mark/select a downstream stage while prerequisite evidence is absent
  expected: FAIL

MUTANT-GATED-TRANSITION-WITHOUT-APPROVAL  # when approval gate is material
  mark/cross the exact gated transition without required approval evidence
  expected: FAIL

CONTROL-ALLOWED-PREPARATION-BEFORE-APPROVAL
  exercise explicitly authorized reversible preparation while approval is absent
  expected: PASS

MUTANT-FOUNDATION-PASS-AS-PRODUCT-COMPLETE
  leave one or more required product Acceptance outcomes/evidence absent while package/M0/foundation gate passes
  expected: FAIL

MUTANT-FILE-EXISTS-AS-RUNTIME-EVIDENCE
  satisfy a required runtime/browser criterion only by creating/naming the expected implementation artifact without exercising the boundary
  expected: FAIL

MUTANT-STALE-FINAL-EVIDENCE
  change relevant source/config/data after final evidence without rerunning affected verification
  expected: FAIL
```

Store the PASS/FAIL summary in the project's existing contract/package-validation evidence.


MUTANT-FALSE-ADMISSION
  set STATE.current_admission to a stage whose required predecessor maturity/Acceptance is not currently verified
  expected: FAIL

MUTANT-E2E-STATE-DRIFT
  mark a stage/PR outcome Verified while one of its required E2E scenarios remains pending/not exercised
  expected: FAIL

MUTANT-PARTIAL-PERSISTENCE-AS-CONTINUE
  provide a narrow serialize/deserialize field roundtrip while full Continue/Resume Acceptance requires state coverage/equivalence
  expected: FAIL

MUTANT-COMPOSITION-DRIFT
  change a canonical source/relation while leaving a required dependent projection stale/inconsistent
  expected: FAIL

MUTANT-LOCAL-SYMPTOM-PATCH
  patch one dependent consumer so a local symptom disappears while the declared shared invariant remains violated
  expected: FAIL

MUTANT-PREMATURE-SKELETON-ADMISSION
  claim production-admitted skeleton while required survivability substitution/extension evidence is absent or failing
  expected: FAIL

MUTANT-INSTANCE-LOCAL-RUNTIME
  add a second same-archetype definition but route it through a copied/per-instance runtime or surface instead of the registered generic consumer
  expected: FAIL

MUTANT-MODIFIER-COPIES-OWNER
  implement a modifier by copying or directly owning the target capability/state instead of using its declared modifier seam
  expected: FAIL

MUTANT-PLACEHOLDER-REQUIRES-ARCHITECTURE-REPLACEMENT
  replace a declared placeholder with production content only by bypassing/replacing the canonical owner/consumer path
  expected: FAIL

MUTANT-TEST-CONTENT-LEAKAGE
  route test_fixture/debug_only content into a normal shipping/default/progression/user flow
  expected: FAIL

MUTANT-CONSUMER-FOREIGN-WRITE
  allow a consumer/adapter to directly mutate state owned by another Responsibility Owner outside its declared command contract
  expected: FAIL

MUTANT-BLUEPRINT-INTERNAL-BYPASS
  route a cross-system consumer directly to a known internal implementation artifact while a canonical public Blueprint/module boundary exists
  expected: FAIL

MUTANT-TEST-VOLUME-AS-PRODUCT-COMPLETE
  leave a required PR outcome unverified while many unit/integration tests pass
  expected: FAIL

## `STATE.json` admission/context extension

When stage admission is material, prefer a machine-checkable current slice of the canonical plan rather than asking the gate to infer prose:

```json
{
  "current_admission": {
    "stage_id": "STAGE-...",
    "plan_source_id": "DOC-PROJECT-PLAN",
    "plan_fingerprint": "...",
    "prerequisites": [
      {
        "id": "AC-OR-CAP-...",
        "required_maturity": "Exercised",
        "required_evidence_ids": ["EVID-..."]
      }
    ],
    "allowed_exploration": ["..."],
    "forbidden_conclusions": ["..."],
    "exit_evidence_ids": ["..."],
    "status": "admitted|blocked|complete"
  },
  "transition_gate": {
    "gate_id": "GATE-...",
    "gated_transition": "...",
    "reversible_preparation_allowed": true,
    "approval_authority_source_id": "...",
    "approval_evidence_ids": [],
    "transition_status": "waiting|approved|crossed"
  },
  "context": {
    "required_source_ids": [],
    "loaded_source_ids": [],
    "required_reference_ids": [],
    "inspected_reference_ids": [],
    "inspected_view_ids": []
  }
}
```

`STATE.current_admission` and optional `transition_gate` are runtime slices derived from existing Plan/Workflow/Acceptance authorities, not a second planner or approval engine. `project_gate preflight/completion` must independently re-derive admissibility from Plan + Product Realization + Acceptance + current evidence and fail when STATE claims a stage/status that the derivation does not permit. Omit `transition_gate` when the project has no material human/project gate.

## Root `AGENTS.md` / START kernel addition

```text
Before material work and after fresh/compacted context:
1. load/apply bound Core-First Governance if actually available;
2. otherwise use the declared project-native fallback;
3. run the project gate preflight;
4. read/inspect every required authority/reference it reports;
5. implement only within the current admitted stage and canonical owner path.
Never claim a plugin/tool ran unless it actually did.
```

## Reference-routing extension

For material visual work, `PROJECT_INDEX` routes actual reference assets with stable IDs, and `STATE.context.required_reference_ids` / `inspected_reference_ids` track task-local consumption. A file in `references/` that lacks routing/inspection does not satisfy design-source consumption.


## FINAL_REPORT.md / final response template

The final report is a generated/derived view. It does not own status.

```markdown
# Final Verification Report

## Canonical current state
- State source/revision: [...]
- Current admission/final status: [...]

## Requested outcomes and evidence
| Outcome / AC | Required evidence | Actual current evidence | Verdict |
|---|---|---|---|
| ... | ... | ... | VERIFIED / UNVERIFIED / BLOCKED |

## Final gates actually executed
- build/typecheck: [command + result]
- integration: [...]
- runtime/browser/user-surface: [...]
- visual/black-box: [...]
- project_gate completion: [...]

## Reconciliation
- contradictory/stale evidence: [...]
- remaining unmet/deferred outcomes: [...]

## Verdict
`COMPLETE` only if every required row and gate above supports it.
```

Do not populate this report from filenames, code-count summaries, old milestone prose or project-gate/package validation beyond the claim scope those checks actually exercised.


## `contracts/PERSISTENCE_COVERAGE.yaml` Template (conditional)

Generate when save/resume/continue/restart recovery is material.

```yaml
runtime_state_coverage:
  STATE-EXAMPLE:
    owner: SYS-...
    disposition: persisted    # persisted|deterministically_reconstructed|intentionally_transient|forbidden_to_persist
    schema_or_reconstruction_contract: CONTRACT-...
    acceptance_ids: [AC-...]

continue_equivalence:
  required: true
  checkpoint_definition: "..."
  comparison_horizon: "N deterministic steps/ticks/actions"
  tolerances: {}
```

Preferred strong Continue/Resume evidence when deterministic behavior is expected:

```text
State A
→ persist → restore → N deterministic steps

vs

same State A
→ no reload → N deterministic steps

compare declared observable/state outputs within project tolerances
```

A selected-field serialize/deserialize roundtrip proves only those fields unless Acceptance explicitly scopes the claim that narrowly.
