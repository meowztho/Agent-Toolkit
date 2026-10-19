# Routing and Replan

## Method routing

Route from the unresolved fact and needed evidence boundary. Target/product domain only narrows applicable surfaces; it does not select a privileged workflow. Domain-specific rows below are conditional profiles, not owners.

| Knowledge gap / evidence need | JIT method under `rore-reconstruction` |
| --- | --- |
| screens/views, navigation, states, UI component relationships | `SURFACE_FLOW_STATE_RECONSTRUCTION.md` |
| layout, visual hierarchy, interaction/motion/media semantics | `VISUAL_INTERACTION_RECONSTRUCTION.md` |
| archive/package/container/resources/embedded artifacts | `ARTIFACT_EXTRACTION.md` |
| cross-domain assets/media/fonts/localization, their lineage and actual use | `ARTIFACT_EXTRACTION.md` + `VISUAL_INTERACTION_RECONSTRUCTION.md` when presentation is material |
| functions/classes/control/data flow/binary structure | `STATIC_CODE_BINARY_RECONSTRUCTION.md` |
| mod/plugin extension points in one reference or interoperability points across several | `MULTI_REFERENCE_EXTENSION_SEAMS.md` with the material static/runtime/asset/protocol methods |
| loader-aware native disassembly/decompilation is material and Ghidra is selected | `STATIC_CODE_BINARY_RECONSTRUCTION.md` → `GHIDRA_STATIC_PROVIDER.md` |
| effective running behavior, process/files/network/persistence/timing | `RUNTIME_DYNAMIC_RECONSTRUCTION.md` |
| a known crash, wrong result, rejected input, hang, missing resource or failed recovery can localize the mechanism | `FAILURE_GUIDED_RECONSTRUCTION.md` with the material static/runtime/protocol method |
| live values/objects, readers/writers, authoritative state | `MEMORY_STATE_CAUSALITY.md` |
| apparently corresponding objects across source, package, runtime, wire, asset or version layers | `CROSS_LAYER_EVIDENCE_CORRELATION.md` |
| browser/client/HTTP surfaces when present | `WEB_JS_API_RECONSTRUCTION.md` (conditional profile) |
| unknown messages/framing/state machine/serialization | `PROTOCOL_RECONSTRUCTION.md` |
| schemas/records/formats/defaults/relationships | `DATA_SCHEMA_FORMAT_RECONSTRUCTION.md` |
| mobile/platform packaging/runtime semantics when present | `MOBILE_PLATFORM_RECONSTRUCTION.md` (conditional profile) |
| engine/asset-heavy runtime semantics when present (games are one example) | `GAME_ENGINE_ASSET_RECONSTRUCTION.md` (conditional profile) |
| changed builds/patches/version migration | `CROSS_VERSION_DIFFERENTIAL_RECONSTRUCTION.md` |
| formulas/state rules/cooldowns/economy/balancing | `MECHANICS_RULES_BALANCING_RECONSTRUCTION.md` |
| docs/source/history/reviews/community clues | `EXTERNAL_VERSION_RESEARCH.md` |
| hidden contract only exposed by deliberate variation | `PERTURBATION_AND_CAUSAL_PROBING.md` |
| no integrated analysis suite, or a concrete question needs an acquisition route | `ANALYSIS_ACQUISITION_RECIPES.md` + `CAPABILITY_FIRST_TOOLING.md` |

Several methods may cooperate, but use the smallest active set that can discriminate the current hypotheses.
An observed failure can be the first anchor; do not require a general inventory before investigating its exact trigger and evidence boundary. A discovered tool or capability does not require that tool for later investigations.

## Stage-exit contract

At the end of a meaningful analysis unit record:

```text
current hypothesis
supporting Evidence IDs
contradicting / negative Evidence IDs
confidence / boundary
next decision: continue | switch | stop
reason
```

`stop` may close a bounded question when its requested mechanism is sufficiently understood. For a broad reconstruction, it requires a coverage review of technically accessible areas and explicit disposition of remaining avenues; one understood mechanism, three unproductive actions or one unavailable provider cannot close the whole mission. Preserve attempted methods and evidence limits. Mark a fact as currently unresolved/blocked when a viable later probe or user-supplied input could answer it; reserve an irrecoverable conclusion for a demonstrated inability to recover or infer it from the accessible reference. No finite investigation proves that every conceivable technique has been exhausted.

## Deadlock and bias

Trigger a replan when, as a practical default, roughly three analysis actions yield no new evidence or two method switches merely bounce between the same unresolved assumptions. These numbers are heuristics, not a rigid counter.

On replan:
1. restate the unresolved claim;
2. enumerate the competing explanations;
3. name what observation would discriminate them;
4. challenge whether the current tool/method can actually observe it;
5. change anchor, evidence boundary or capability — not just command syntax.

Bias warnings: one decompiler treated as truth, runtime symptoms without stable anchors, screenshot-only claims about temporal behavior, repeated parsing without identity proof, or repeated web research replacing target-local checks.
