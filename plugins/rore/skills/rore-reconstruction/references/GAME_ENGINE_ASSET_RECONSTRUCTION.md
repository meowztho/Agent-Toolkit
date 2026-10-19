# Game / Engine / Asset Reconstruction — Conditional Profile

This is a conditional domain/surface profile, not a RORE owner and not a primary target declaration. Games are useful stress tests because they often combine asset pipelines, runtime state, timing, physics, scripting and interaction, but RORE must remain equally applicable to web, API, ERP/CRM, desktop/mobile, protocol and other system classes.

Activate this profile only when engine/asset/runtime semantics materially exist in the reference.

Reconstruct as material:
- engine/runtime/build identity;
- packages/bundles/Paks/scenes/maps/prefabs/resources;
- entities/components/actors/blueprints/scripts;
- materials/shaders/textures/meshes/animation/audio;
- data tables/config/curves/abilities/stats;
- map topology/navigation/spawn/mission relationships;
- runtime entities and generated state;
- mechanics/state machines/physics/timing;
- load/override/DLC/mod/layer relationships.

Asset presence does not prove active use. Use `PRESENT → REFERENCED → REACHABLE → EXERCISED → EFFECTIVE` where material.

Memory/state probing can expose authoritative gameplay values and connect them back to components, data tables or code paths. For example, a value mutation that changes behavior is a causal clue; trace readers/writers before declaring ownership.

Record asset properties and provenance/usage relationships. Analysis access does not imply redistribution rights.

For a mod entry-point question or an investigation involving two games, read `MULTI_REFERENCE_EXTENSION_SEAMS.md`. Recover each relevant game's runtime/code/asset contract and load order separately, including the decompiled paths that expose candidate callbacks, registries, override points or engine handoffs. Test candidate reachability and effect before calling one a usable entry point; keep the later mod or mashup design outside RORE.
