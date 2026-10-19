# RORE v0.4.0 — CoreReplica migration matrix

## Boundary
RORE reconstructs the reference as faithfully and deeply as practical. It stops before target-product selection, redesign, implementation, replica verification, release, branding, or project compilation.

## Current CoreReplica lanes
| Current lane/file | Action | RORE destination | Reason |
|---|---|---|---|
| corereplica-orchestration | REWRITE | rore-orchestration | Keep JIT routing, context invalidation, evidence boundary; remove APC/product/build/release routing |
| corereplica-reference | EXPAND | rore-reconstruction | Canonical reference reconstruction owner |
| corereplica-product | REMOVE ACTIVE / KEEP HISTORICAL PROVENANCE | none | Target product decisions are downstream |
| corereplica-design | REMOVE ACTIVE; ABSORB RE methods only | surface-visual JIT references | Current skill mostly target design-system work; raw reference measurement belongs in RORE |
| corereplica-build | REMOVE ACTIVE | none | Implementation is downstream |
| corereplica-verify | REMOVE ACTIVE; ABSORB methods | rore-evidence-review + probing references | Target acceptance/parity out; read-only evidence review and safe real-boundary probing stay |
| corereplica-market | REMOVE ACTIVE; ABSORB review research | external-research JIT | Reviews can reveal reference behavior/defects/version differences; branding/positioning/launch out |
| corereplica-release | REMOVE ACTIVE | none | Release is downstream |

## Existing references
| Reference | Action | Notes |
|---|---|---|
| EVIDENCE_QUALIFICATION.md | KEEP + strengthen | Cross-cutting invariant; add negative evidence, fixity, finding promotion rules |
| REVERSE_ENGINEERING_WORKFLOW.md | SPLIT/REFINE | Keep as core loop; route to narrower JIT methods |
| RUNTIME_CORROBORATION.md | KEEP | Preserve PRESENT→REFERENCED→REACHABLE→EXERCISED→EFFECTIVE |
| MEMORY_AND_RUNTIME_STATE_ANALYSIS.md | KEEP + expand | Controlled mutation, reader/writer causality, authoritative-state discovery |
| CAPABILITY_FIRST_TOOLING.md | KEEP | Route capability before provider/tool |
| ADVERSARIAL_LIMIT_PROBING.md | RENAME/EXPAND | PERTURBATION_AND_CAUSAL_PROBING.md |
| EXTERNAL_RESEARCH_AND_CORROBORATION.md | KEEP + expand | Include reviews/changelogs/community as discovery evidence |
| SIDE_EFFECT_SAFE_VERIFICATION.md | ABSORB/RENAME | SAFE_PERTURBATION_AND_RECOVERY.md |
| FLOW_AND_PARITY_VERIFICATION.md | SPLIT | Keep flow/state comparison against reference observations; remove target acceptance/parity |
| REVIEW_RESEARCH.md | ABSORB | External evidence lane; remove roadmap/positioning semantics |

## Upstream replica-skill concepts
| Concept | Action | RORE interpretation |
|---|---|---|
| Stable screen IDs Sxx | ADMIT | Stable reference Surface IDs |
| Stable flow IDs Fxx | ADMIT | Stable reference Flow IDs |
| Screen states empty/loading/error/permission/mobile | ADMIT | State inventory and transition evidence |
| Component inventory | ADMIT | Reference component roles/variants/states |
| Inferred data model + evidence/confidence | ADMIT | Reference data model; never auto-promote to target schema |
| Screenshot/layout measurement | ADMIT | Preserve raw values + semantic role; DO NOT snap/normalize |
| Edge/negative case matrix | ADMIT | Probe catalog for reference behavior where authorized |
| Behavior diff | ADMIT AS DIFFERENTIAL OBSERVATION | Compare states/versions/surfaces of reference; not replica ship score |
| Review research | ADMIT AS DISCOVERY EVIDENCE | Defects/hidden states/version clues, not roadmap |
| Clone priority/sizing/build handoff | REJECT | Downstream product work |
| Target design tokens/primitives | REJECT | Downstream design |

## Upstream reverse-skill concepts
| Concept | Action | RORE interpretation |
|---|---|---|
| Hypothesis-driven stage exit | ADMIT | Each stage records hypothesis + continue/switch/stop |
| Negative evidence | ADMIT | Checked absence is explicit evidence |
| Finding promotion bar | ADMIT | validated needs independent/cross-boundary support when material |
| Runtime back-annotation | ADMIT | Dynamic observation should be anchored into static/data/runtime structure when possible |
| Stage/tool bias detection | ADMIT | Detect fixation and re-route |
| Deadlock→replan | ADMIT | Replan after repeated actions/stage switches without new evidence |
| Context pollution detection | ADMIT | Re-read evidence/timeline when rejected hypotheses reappear |
| Content hash/fixity | ADMIT | Bind artifacts and derived analysis to target identity/hash |
| Case review | ADMIT | Read-only Evidence→Finding→Path integrity review |
| Protocol reconstruction | ADMIT | Frame layout, state machine, serialization, compression/encryption semantics |
| JS Observe→Capture→Rebuild→DeepDive | ADAPT | Observe→Capture→Reconstruct→Corroborate; no target clone rebuild |
| Mobile/APK static+dynamic+network | ADMIT | Platform-specific reconstruction lane |
| Binary diff semantic anchors | ADMIT | Cross-version semantic remapping; no raw-offset transplant |
| Patch diff root-cause inference | ADMIT | Before/after change analysis to infer mechanism and validation boundaries |
| Pwn primitive/mitigation discovery | ADAPT | Use controlled trigger/state/memory observations to understand mechanism; stop at understanding |
| Exploit stabilization/remote weaponization | REJECT | Not needed for reference reconstruction |
| Attack chain initial access/lateral/persistence | REJECT AS GOAL | Only local causal/state ideas may be reused when directly relevant to authorized target understanding |

## RORE owners
1. `RORE_ORCHESTRATION` — selects the next analysis method from target/surface + knowledge gap + required evidence boundary + available capabilities.
2. `RORE_RECONSTRUCTION` — acquires/interprets/reconciles reference evidence into Findings, Paths, and reference-native models.
3. `RORE_EVIDENCE_REVIEW` — read-only review of evidence sufficiency, traceability, fixity, contradictions, coverage, and overclaiming. It does not perform target analysis or repair Findings itself.

## RORE reconstruction JIT methods
- SURFACE_FLOW_STATE_RECONSTRUCTION
- VISUAL_INTERACTION_RECONSTRUCTION
- ARTIFACT_EXTRACTION
- STATIC_CODE_BINARY_RECONSTRUCTION
- RUNTIME_DYNAMIC_RECONSTRUCTION
- MEMORY_STATE_CAUSALITY
- WEB_JS_API_RECONSTRUCTION
- PROTOCOL_RECONSTRUCTION
- DATA_SCHEMA_FORMAT_RECONSTRUCTION
- MOBILE_PLATFORM_RECONSTRUCTION
- GAME_ENGINE_ASSET_RECONSTRUCTION
- CROSS_VERSION_DIFFERENTIAL_RECONSTRUCTION
- MECHANICS_RULES_BALANCING_RECONSTRUCTION
- EXTERNAL_VERSION_RESEARCH
- PERTURBATION_AND_CAUSAL_PROBING

## Cross-cutting invariants
- CLAIM STRENGTH <= PROVEN EVIDENCE BOUNDARY
- Tool success != semantic correctness
- Parseable output != correct identity
- Correct subset != population completeness
- Tool agreement != independent corroboration when failure assumptions overlap
- Present != referenced != reachable != exercised != effective
- Dynamic observation should be back-annotated to stable semantic anchors when possible
- Raw/normalized/derived artifacts remain distinct
- Unknown remains unknown
- Reference-native structure is preserved; RORE does not redesign it for a future builder
- Perturbation is an epistemic instrument; stop when mechanism understanding is sufficient
- No APC/project compiler/product/build/release dependency

## Release-lineage note
CoreReplica v0.3.6 remains available as the previous immutable plugin release. v0.4.0 intentionally supersedes its active Product/Design-target/Build/Verify-target/Market/Release owners rather than silently repurposing those owner IDs. Methodology retained from those lanes is explicitly named above and re-homed under RORE Reconstruction or Evidence Review.

## v0.4.1 domain-neutrality correction
The v0.4.0 wording that called games a primary RORE target was incorrect. RORE is domain-neutral. Games remain a useful stress-test profile because they expose many interacting system classes, but web, APIs, ERP/CRM, desktop/mobile, protocols and other software are equally valid targets. Domain-specific reconstruction files are conditional JIT profiles beneath the same canonical Reconstruction owner.
