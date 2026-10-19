# Visual / Interaction Reconstruction

Reconstruct what the reference actually presents and how it behaves.

Measure when useful:
- raw colors plus semantic role;
- typography values and role;
- spacing/gaps/dimensions;
- radius/shadow/border;
- layout/grid/max width/breakpoints;
- component variants/states;
- focus/hover/active/disabled/loading/error behavior;
- animation/motion timing and transition conditions;
- image/icon/media/audio relationships where material.

**Do not snap measured values to a cleaner scale.** Keep raw measurement and optionally record an inferred design rule separately. The reference's inconsistencies are part of Reference Truth.

Screenshots prove only the captured state. Temporal/interactive claims need runtime evidence. Comparable screenshots or image diffs may support structural observations but never prove hidden behavior, persistence or causality.

For two captured reference versions or states, an optional local PNG differential can identify regions worth inspecting. Use `scripts/rore_imgdiff.py` only with a stated capture state, viewport/scale, target build/environment and acquisition time for each input. Its pixel or coarse layout indicator is a search aid, not a parity score or proof of equal UI; inspect the original images and capture dynamic behavior separately. A height difference or cropped comparison remains explicit.
