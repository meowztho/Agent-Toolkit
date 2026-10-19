# Reference Reconstruction: <target / slice>

## Target identity
- target:
- version/build/revision/hash:
- platform/runtime/engine/environment:
- observation date/range:
- authorized analysis boundary:

## Sources / evidence fixity
| Evidence ID | boundary | source/artifact | identity/hash | method | limitations |
| --- | --- | --- | --- | --- | --- |

This index points to the preserved raw observation where allowed. Normalized, decoded and model-generated views cite their source Evidence ID and transformation; they do not replace the raw record. If a record is corrected, link the superseding record and retain the earlier identity and reason.

## Stable reference identities
Create only the tables that exist for this target.

### Surfaces (`SUR-###`)
| ID | identity/purpose | reachability | states | evidence | notes |
| --- | --- | --- | --- | --- | --- |

### Flows (`FLOW-###`)
| ID | goal/path | states/surfaces | edge conditions | evidence | unknown edges |
| --- | --- | --- | --- | --- | --- |

### Components / subsystems (`COMP-###`)
| ID | observed responsibility | relationships | evidence | confidence/limitations |
| --- | --- | --- | --- | --- |

### Entities / schemas (`ENT-###`)
| ID | fields/relationships | source/canonicality evidence | evidence | limitations |
| --- | --- | --- | --- | --- |

### Protocol messages (`PROTO-###`)
| ID | direction/type | fields/framing | state transition | evidence | unknowns |
| --- | --- | --- | --- | --- | --- |

### Assets / resources (`ASSET-###` when useful)
| ID | source/container + raw identity/hash | format/native properties + variants | references | observed runtime/surface use | derived views/transform | evidence + limits |
| --- | --- | --- | --- | --- | --- | --- |

Keep present, referenced, reachable, exercised and effective use distinct. Include material missing, duplicate, unused or inaccessible assets in coverage; a preview or converted copy does not replace source bytes.

## Findings
| Finding ID | conclusion | evidence IDs | status | boundary | contradictions/limitations |
| --- | --- | --- | --- | --- | --- |

## Paths
| Path ID | type | ordered steps/edges | evidence/findings | unknown edges |
| --- | --- | --- | --- | --- |

Suggested path types: `user`, `call`, `data`, `runtime`, `causal`, `protocol`, `load`, `persistence`.

For cross-layer edges, record both source identities, mapping/match basis, candidate count, evidence boundary and mismatch/ambiguity status. See `../references/CROSS_LAYER_EVIDENCE_CORRELATION.md`; an inferred correspondence does not become an observed call or cause.

## Known failures and recovery when material

| Failure ID | reference identity + initial state | minimal trigger + frequency | raw symptom | first observed divergence | producer/effect/recovery Paths | controls, unknowns + Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Use `../references/FAILURE_GUIDED_RECONSTRUCTION.md` to trace a known defect or controlled fault into the reference's behavior. Preserve the unmodified baseline and any diagnostic intervention separately.

## Reference-native models
Use one or more sections as the reference demands: Behavioral/State/Rules Model, Component/Architecture/Data-Flow Model, Interface/Navigation/Interaction/Accessibility Model, Data/Schema/Defaults/Configuration Model, Protocol/API Model, Causal Model, Asset/Resource/Media Model, Mechanics Model, Timing/Concurrency Model, Failure/Recovery Model, and Observed Implementation Constraints (platform, framework, performance or timing only where evidenced).

Do not merge them merely for compactness when separate views preserve important structure.

## Reference comparison cases (`ORACLE-###` when useful)
Record repeatable observations of the original reference, not target-product acceptance criteria. Use cases that discriminate material behavior, edge conditions and failures. Keep exploratory or instrumented observations labelled as such; a changed reference is not silently the oracle for the unmodified reference.

| Case ID | reference identity/version + environment | starting state/preconditions | action/input/sequence | observed outcome incl. errors/recovery | tolerance/variation | Evidence/Finding/Path IDs | repeatability/limits |
| --- | --- | --- | --- | --- | --- | --- | --- |

For each comparison dimension, distinguish `observed`, `corroborated`, `inferred`, and `unknown` without replacing the finer Evidence qualification status. Preserve raw traces, screenshots, network captures or measurements behind material expected outcomes when available.

When a case depends on asynchronous state, record a readiness predicate rather than only a fixed delay. Name the requested observations (such as DOM, screenshot, network, storage, process tree or files) and mark unrequested, truncated or failed captures separately. State required causal/partial event order where material; one incidental total order is not automatically part of the reference contract. A `complete` capture covers only the requested fields and window.

## Hypotheses and negative evidence
| hypothesis | status | supporting evidence | contradicting/negative evidence | next discriminator |
| --- | --- | --- | --- | --- |

## Runtime status
For material runtime claims, distinguish `PRESENT | REFERENCED | REACHABLE | EXERCISED | EFFECTIVE` or record why the ladder is not applicable.

## Coverage
Use `covered | partial | unresolved | not_applicable | out_of_scope`.

| class | status | evidence / gap |
| --- | --- | --- |
| surface / flow / state | |
| architecture / components / paths | |
| data / schema / content population | |
| algorithms / transforms | |
| packages / assets / resources / layering | |
| runtime / persistence / recovery | |
| memory / state / causality | |
| web / API / protocol | |
| visual / interaction / media | |
| mechanics / rules / balancing | |
| config / flags / version / precedence | |
| install / update / environment | |
| timing / concurrency / resources | |
| failures / limits / trust boundaries | |
| reference comparison cases / observable edge conditions | |

## Portable reference handoff
For a downstream reader, link the current target identity, Evidence index/raw locations or access restrictions, Findings/Paths/Models, reference comparison cases, coverage, contradictions and unknowns. Keep source observations and derived narrative visibly separate. A downstream project process may choose requirements from this material; RORE does not turn every observed feature into a required target feature.

## Open questions / next high-information probes

For each material unresolved question keep supporting and contradicting Evidence, required authority/environment, current status, next discriminator and linked prior revisions when the investigation is resumed. Do not replace an unresolved question with a polished summary.
