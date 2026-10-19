---
name: rore-evidence-review
description: Read-only audit of an existing RORE reconstruction for claim grounding, evidence identity/fixity, Evidence→Finding→Path traceability, contradictions, corroboration independence, coverage and overclaiming. Use before broad completeness claims, handoffs, consequential conclusions, or when context pollution/stale evidence is suspected. Do not analyze or mutate the target and do not silently repair findings during the review pass.
---

# RORE Evidence Review

Own independent review of the **evidence graph**, not reference reconstruction.

## Review boundary

During the review pass:
- use a fresh reviewer context where feasible;
- review the evidence graph and project/reference authorities, but withhold reconstruction-agent confidence, persuasive rationale and prior review conclusions before independent derivation where the host allows that separation;
- do not mutate or probe the target;
- do not reinterpret missing evidence as if acquired;
- do not silently edit a failing Finding into a passing one;
- report the exact defect and required reconstruction action.

A later `rore-reconstruction` pass may correct the model, then Evidence Review can re-check it.

## Review dimensions

1. **Target identity / fixity** — are Evidence records bound to the correct build/artifact/environment? Do recorded hashes still match where applicable?
2. **Grounding** — does every material Finding cite Evidence that actually supports the claimed boundary?
3. **Path integrity** — are Path edges grounded, or did an inference silently become a proven link?
4. **Object identity** — was the requested object/version/layer established before interpretation?
5. **Parser/transformation boundary** — is derived output reproducible and traceable to raw evidence?
6. **Coverage** — do completeness claims know their denominator/population? Are material classes visibly `covered/partial/unresolved/...`?
7. **Corroboration independence** — do multiple sources really have independent failure modes?
8. **Runtime boundary** — are `present/referenced/reachable/exercised/effective` kept distinct?
9. **Contradictions** — are conflicting observations preserved and resolved only when evidence justifies it?
10. **Hypothesis hygiene** — have rejected hypotheses or still-speculative hypotheses resurfaced after context loss as facts?
11. **Cross-version hygiene** — were semantic anchors re-established instead of carrying raw offsets/stale names forward?
12. **Reference-native fidelity** — did the reconstruction normalize/redesign the reference for a future implementation?
13. **Reviewer anchoring** — was the conclusion independently derived from the evidence graph rather than inherited from reconstruction-agent confidence, rationale or a prior review verdict?
14. **Reference comparison cases** — do identity, starting state, action, observed result, tolerance and repeatability follow from cited raw Evidence? Are instrumented observations distinguished from the unmodified reference?
15. **Evidence/projection separation** — can the reviewer reach the raw observation or see its access limit? Were corrections linked rather than silently overwritten, and did generated narrative avoid inventing or upgrading facts?
16. **Provider calibration** — for material tool-dependent claims, does an exact-case control or independent boundary support interpretation, or is the calibration gap stated?
17. **Action scope** — for material target-touching probes, is the exact target/operation/effect within the user request, supplied reference, project context or prior session permission? Do not demand a separate permission record for each covered method; discovery alone does not authorize a new target or external effect.
18. **Failure and cross-layer paths** — does a known defect have a reproduced trigger, supported producer/propagation/recovery edges and an unmodified control? Are static/runtime, source-map, native/managed and asset/surface correspondences qualified rather than silently equated?
19. **Capture and imported-record limits** — were external Evidence identities validated, and are requested observations, historical captures, truncation, partial results and asynchronous readiness accurately represented?

Read `references/REVIEW_CHECKLIST.md` for the compact audit format.

For an optional Evidence bundle, `scripts/rore.py validate` or its read-only MCP equivalent can expose broken file hashes and links. Treat a passing result as structural evidence only; independently inspect whether each claim is actually supported.

## Finding format

For every review defect:

```text
REVIEW-###
claim / artifact affected
exact evidence defect
why current claim is too strong / stale / ambiguous
required reconstruction action or evidence boundary
status: BLOCKING | MATERIAL | ADVISORY
```

`BLOCKING` means a stated claim cannot stand at its current strength. It does not mean the entire RORE investigation failed.

## Completion

Return a review verdict on the existing package only: supported claims, blocked promotions, contradictions, unlinked/stale evidence, overclaimed coverage and required re-analysis. Do not produce downstream product recommendations.
