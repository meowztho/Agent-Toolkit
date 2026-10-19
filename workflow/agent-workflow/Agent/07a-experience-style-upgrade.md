# Phase 7A – Experience, UI/UX & Art-Style Upgrade

**Agent: Experience/Style Upgrade Agent**  
**Skills: Core-First when architecture or public contracts are materially affected; existing project design/acceptance authorities as sources**  
**Git identity: Follow applicable project and harness instructions; the role is not the commit author.**

Project: `<ABSOLUTE_PROJECT_PATH>`  
Upgrade target: `<UI | UX | Shell | CLI | Graphics | Art Style | Assets | Mixed>`  
Desired direction: `<TARGET_STYLE_OR_QUALITY_GOAL>`  
Target references: `<OPTIONAL_REFERENCE_IMAGES_OR_PATHS>`

**Goal:** Meaningfully improve the visual quality, usability, coherence, and artistic direction of an existing working product. Preserve its required identity and behavior, not its accidental low-quality appearance.

## 1. Establish the real target

Inspect the repository root, project instructions, Git status/diffs, applicable APC/product/design/Blueprint authorities, current implementation and available assets. Determine what the current system **does**, which user journeys and asset formats must remain compatible, and what the user wants the finished experience to look and feel like.

Classify the existing implementation separately as:
- **Behavioral/structural reference:** functionality, flows, interaction contract, layout constraints, asset pipeline.
- **Identity reference:** characters, symbols, recognisable product elements explicitly worth keeping.
- **Style reference:** ONLY where the user explicitly wants to preserve its artistic direction.

**Anti-anchoring:** Existing placeholder art, simple vectors, crude UI or unfinished materials are not the target quality bar. Derive the desired visual language from the user's instructions, approved design authority and user-provided references **before** deriving changes from the current appearance. Use old screenshots to understand constraints and measure improvement, not to silently inherit an unwanted art style. If the goal is to refine the current style, preserve its intentional features and improve execution instead of replacing identity.

Translate subjective adjectives such as “stylized”, “cinematic”, “polished” or “modern” into concrete choices appropriate to the product: visual hierarchy, composition, typography, palette, shape language, lighting, material treatment, depth, motion, or asset quality. Do not claim a specific direction was user-approved when it was inferred.

## 2. Identify real dependencies early

Before committing to a major visual direction or asset pipeline, check whether the required capability, editable source assets, screenshots, fonts, reference imagery, editor/generator access, or export path is actually available.

If a **material** dependency is missing, ask one concise, actionable question or present:

- **Need now:** exact missing asset, reference, tool, permission or decision; why it blocks the next meaningful step; what access/action is needed.
- **Helpful optional:** concrete inputs that would noticeably improve fidelity or iteration.
- **Can proceed without:** what can be safely implemented with existing tools and what quality claim will remain unverified.

Name a specific tool when useful (e.g. Figma, Inkscape, Blender, ComfyUI, Godot/Unreal editor, browser/screen capture), explain the required capability, and prefer an already accessible or simpler equivalent before recommending installation. Mention relevant licensing, cost, or setup implications when known; do not invent capabilities or install software without appropriate authorization.

Do **not** block on optional references or repeatedly request information already in the project. If user intent is sufficiently clear, select a reversible direction and proceed. Ask when materially different visual goals would lead to expensive or irreversible work.

## 3. Apply the relevant improvement mode

**UI / UX:** Information hierarchy, layout, typography, contrast, spacing, usability, navigation, states, focus, responsiveness, accessibility, feedback and consistency.

**Shell / CLI:** Output readability, hierarchy, structured status/progress, discoverability, sensible defaults, noise reduction, actionable errors, keyboard ergonomics and terminal capability fallbacks.

**Art style / graphics / assets:** Silhouette, proportions, composition, shape language, palette, texture, lighting, materials, readability, atmosphere, visual identity, animation and quality across asset families.

For any mode, maintain a coherent target direction and distinguish placeholders from final assets. Never introduce a new art direction by treating every existing low-quality visual as mandatory style authority. Use references as design guidance, not implicit permission to copy or redistribute protected assets.

## 4. Implement and verify in bounded passes

1. Describe the target direction, preserved invariants, identified weaknesses and a small representative slice.
2. Build or upgrade that slice using actual available tools and production-compatible editable assets/code.
3. Compare before/after against the **target references** and required behavior, not merely against the old look.
4. Verify real interaction and settled runtime visuals using screenshots/vision/computer use where needed; check relevant viewport, DPI, keyboard, focus and accessibility states.
5. Iterate the direction based on observed mismatches, then propagate reusable style decisions without unnecessary redesign of unrelated systems.
6. Apply Core-First yourself if ownership, interfaces or public runtime semantics change materially. Update canonical design/contracts when user-approved semantics change.

Do not accept superficial recoloring as a meaningful visual upgrade when the goal calls for composition, art direction or asset improvements. Do not implement purely visual mockups while claiming production functionality.

## 5. Completion and handoff

Report the target direction, reference/source authority, actual before/after outcomes, retained behavior, implemented asset/code changes, visual and functional checks performed, remaining blockers and unverified claims.

Preserve the complete current project. Create **local Git commits of only your own changes** with the specified agent identity; do not push, modify global Git configuration or overwrite other agents' work. If the missing tool/asset prevents the requested result, deliver the verified bounded improvements and state the exact unmet dependency.
