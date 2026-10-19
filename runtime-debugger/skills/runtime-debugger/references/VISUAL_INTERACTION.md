# Visual & Interaction Debugger

**Trigger:** actual visual mismatch, interaction failures, focus or overlay behavior, rendering/game state.

1. Derive expected whole-surface appearance and interaction states from project/user authority. Observe the live program with appropriate screen/vision/computer-use tools, not a code-only approximation.
2. Record before → real user action → settled after. Check focus, hit testing, hitboxes, hover, keyboard, pointer capture, DPI/scaling, window stacking, layout hierarchy, overflow/clipping, transforms, animation timing and responsive states as applicable.
3. A screenshot proves only its visible moment; do not infer clickability, animations, persistence or successful transitions from it.
4. Differentiate wrong producer, wrong source data, wrong effective runtime geometry, stale/frozen observation path, and wrong parent constraint. Use minimal falsification rather than guessing fixes.
5. Preserve representative screenshots/traces and adjacent cheap regression checks. Do not invent pixel requirements absent from design authority.
6. Return precise failure reproduction, visual/interaction evidence and minimal correction direction. Leave code unchanged.
