# Evidence Review Checklist

Use proportionally; a narrow claim does not require a whole-product audit.

## Reviewer independence
- fresh reviewer context used where feasible?
- evidence graph/reference authorities available without reconstruction-agent confidence or persuasive rationale?
- prior review conclusion withheld before independent derivation where feasible?

## Identity / fixity
- target/build/revision/environment identified?
- raw artifact hash recorded where material?
- hash/fixity still valid?
- derived view tied to the same target identity?
- external Evidence ID, bundle or imported run actually checked for content, format/version, build and source identity rather than accepted by name?

## Evidence graph
- every material Finding has Evidence?
- every Path edge has Evidence/Finding support?
- unlinked Evidence intentionally retained or accidentally ignored?
- raw vs normalized vs derived views distinct?
- corrections linked to prior records, with generated narrative unable to replace raw observations?
- unresolved questions retain evidence, contradiction and revision history across a resumed investigation?

## Claim boundary
- static claim presented as static?
- static-sufficient versus runtime-sensitive claims classified by their actual assertion boundary, with unobserved runtime marked unchecked rather than treating static presence as effective behavior?
- runtime-sensitive claim has appropriate same-build/environment runtime evidence or explicit limitation?
- memory-local values not promoted into cross-version truth?
- byte findings bound to the correct artifact, file offset and established virtual/runtime mapping?
- debugger/fault observations separated from uninstrumented behavior, with trigger, module/build and raw trace retained?
- known failure traced past the detection site to supported producer, propagation and recovery edges, with alternatives still marked?
- cross-layer correspondence gives the mapping basis, all plausible candidates and digest/path mismatch rather than silently choosing one?
- loaded/resident/reachable/exercised/effective and historical/live boundaries kept distinct?
- model-assisted annotation still marked derived until grounded?

## Qualification
- correct object/layer/version identity?
- parser/transformation semantics validated?
- material provider output calibrated on a known-answer/control/invariant or explicitly limited?
- completeness denominator known or limitation stated?
- unrequested capture fields, transport truncation, failed acquisition and incomplete extraction kept distinct from absence?
- corroborating sources materially independent?
- recovered assets retain source lineage/native properties and evidence of actual use, including material unknowns?

## Analysis quality
- negative evidence preserved?
- contradictory evidence visible?
- rejected hypotheses resurrected?
- deadlock/tool bias hidden behind repeated similar evidence?
- cross-version semantic anchors re-established?
- target-touching probe bound to the exact authorized target, operation and effects?

## Fidelity
- reference's own awkward/legacy/duplicated structure preserved when evidenced?
- any unexplained normalization, design translation or target-product language introduced?
- reference comparison cases grounded in original identity, preconditions, actions, raw outcomes, tolerances and repeatability?
- asynchronous cases name a readiness condition and requested observation fields; concurrent traces retain only supported causal ordering?
- instrumented or perturbed observations separated from the unmodified reference oracle?

## Coverage
For broad claims, inspect material classes for `covered | partial | unresolved | not_applicable | out_of_scope` and challenge any silent gap.
