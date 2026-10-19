# User-Surface and Reality Verification Guide

# Current Precedence — Evidence Scope Cross-Check

A technically runnable surface or fixture-driven UI path is not automatically representative product evidence. When a phase/admission claim depends on real user/external behavior, exercise the canonical representative path/data/configuration required by Acceptance. Preserve the distinction between synthetic exploration and product-conclusion evidence.

---


## Purpose

Code, tests, logs, and static inspection describe implementation state.

They do not automatically prove the state a user actually sees or experiences.

For user-facing products, the agent must distinguish:

```text
IMPLEMENTATION TRUTH
    code/config/assets appear correct

RUNTIME TRUTH
    the built/running product actually behaves correctly

USER-SURFACE TRUTH
    the user can see, understand, and operate the intended result
```

A goal that contains user-visible behavior cannot be completed from implementation truth alone.

---

# 1. Choose Verification by Product Surface

Use the strongest practical verification surface for the criterion.

## Desktop / native / editor-hosted application

Prefer:
1. build/package the actual target;
2. launch it as a normal user would;
3. use Computer Use or equivalent UI automation when available;
4. interact through real menus/controls;
5. capture screenshots at meaningful checkpoints;
6. inspect the rendered result.

## Website / browser app

Prefer:
1. run the actual local/target build;
2. use an interactive browser / Playwright / equivalent;
3. navigate the real route;
4. exercise controls;
5. inspect rendered state;
6. capture screenshots at checkpoints;
7. use DOM/console/network inspection only as supporting evidence.

## CLI

Run the real command from the intended entry point using realistic arguments/stdin.

## API / service

Use a real client/request path against the runnable service and inspect returned behavior/state.

## Data / generated artifact

Open/render/parse the actual produced artifact in the environment a user/tool will consume it.

Do not use screenshots when the product surface does not benefit from them.

---

# 2. Incremental User-Surface Verification

After a task that changes observable behavior, verify the smallest relevant user-facing slice as soon as it is runnable.

Examples:

```text
Changed Main Menu navigation
→ launch app
→ open Main Menu
→ activate Start Local Match
→ confirm expected next screen
→ capture one checkpoint screenshot if useful
```

```text
Changed website card layout
→ open affected route
→ test target viewport(s)
→ inspect rendered card
→ capture screenshot
```

```text
Changed pause flow
→ launch a minimal match
→ pause
→ inspect pause overlay
→ resume
```

Benefits:
- catches reality gaps while the responsible task is still active;
- keeps visual evidence close to the relevant context;
- reduces late discovery of black screens, duplicate UI, broken navigation, bad layout, missing actors, or incorrect colors.

If a user-surface check is not yet possible because an upstream dependency is missing:

```yaml
verification_state: deferred_integration_check
reason: "[blocking dependency]"
required_when: "[integration point]"
```

Do not silently convert deferred visual verification into verified.

---

# 3. Visual Checkpoint Contract

For projects with meaningful visual/UI output, generate:

```text
verification/VISUAL_CHECKPOINTS.yaml
```

Example:

```yaml
checkpoints:

  main_menu:
    surface: desktop_app
    route: [launch, main_menu]
    proves: [AC-UI-01]
    expectations:
      - one canonical main menu is visible
      - menu is centered within intended safe area
      - no duplicate menu layer exists
      - primary action is readable and focusable
      - background/render surface is not black unless specified
    interaction:
      - activate: start_local_match
        expect_state: player_setup
    evidence:
      screenshot: true

  active_match:
    surface: rendered_application
    route: [launch, main_menu, setup, start_match]
    proves: [AC-MATCH-01]
    expectations:
      - primary content region is visible and stable
      - required entities/participants are spawned
      - active participants/content remain inside the intended viewport
      - status/presentation is visible and reflects selected configuration
      - no unexpected black frame or missing render layer
    evidence:
      screenshot: true
```

The expectations must derive from authoritative design/flow/goal sources.

Do not use vague checkpoints such as `looks_good: true`.

---

# 4. Interaction Evidence vs Visual Evidence

They prove different things.

## Interaction evidence

Proves:
- controls can be activated;
- navigation works;
- focus/state transitions work;
- workflow completes;
- real user input reaches the correct behavior.

Use Computer Use, browser interaction, Playwright, engine automation, or another real interaction mechanism.

## Visual evidence

Proves:
- correct elements are visible;
- layout is coherent;
- duplicates/overlaps are absent;
- colors/style/layout meet requirements;
- expected primary entities/content/status/presentation appear;
- no black screen or obvious visual corruption exists.

Use screenshots/appshots/rendered output and inspect them.

A screenshot of a menu does not prove the button works.
A successful click does not prove the menu is visually correct.

User-facing criteria may require both.

---

# 5. Evidence Budget / Context Control

Visual verification must not flood the active context.

Use this policy:

1. Capture screenshots only at meaningful checkpoints, on unexpected failure, or when the criterion is visual.
2. Prefer one representative screenshot per stable state unless multiple viewports/states are required.
3. Inspect the screenshot immediately while the relevant task is active.
4. Convert findings into a short structured evidence record.
5. Save evidence files outside the conversational knowledge path when practical.
6. Store references/metadata in `verification/EVIDENCE_INDEX.yaml`.
7. Do not repeatedly reload old screenshots unless re-evaluation needs them.
8. On later context recovery, reread the evidence index first; reload raw evidence only when the current criterion requires it.

Example:

```yaml
evidence:
  EV-UI-004:
    criterion: AC-UI-01
    type: screenshot_review
    artifact: verification/evidence/EV-UI-004-main-menu.png
    revision: "git:abc123"
    checkpoint: main_menu
    result: pass
    observations:
      - exactly one menu layer visible
      - primary controls centered
      - no black render area
```

The evidence summary is a pointer, not a substitute for rerunning final release checks after relevant changes.

---

# 6. Final Black-Box Verification Gate

Incremental verification is necessary but not sufficient.

Before reporting the master goal complete, run a fresh final verification against the current final build/worktree from the user's point of view.

For a user-facing application:

```text
build/package
→ start from normal user entry point
→ do not use developer shortcuts
→ perform required primary flows
→ interact with required controls
→ inspect visual checkpoints
→ complete the user journey
→ exercise required interruption/recovery/completion/return paths
→ record evidence
```

For an interactive rendered application this commonly includes:
- packaged/external launch;
- visible normal entry surface;
- complete required setup flow;
- required selectable/configurable content;
- real input;
- active primary workflow;
- required content/status regions;
- interruption/recovery where applicable;
- completion/result state;
- return/continue path;
- no blank/corrupt render;
- no duplicate required surface;
- no obviously broken framing/layout.

For a website:
- production-like/local target build;
- required viewport sizes;
- navigation/forms/interactions;
- visual layout/style checkpoints;
- error/loading/empty states when in scope.

The final gate is a black-box acceptance pass, not code review.

---

# 7. Final Verification Must Use the Final Revision

If a relevant change occurs after a visual/interactive pass:

- mark affected evidence stale;
- identify impacted acceptance criteria;
- rerun the narrow affected checks;
- rerun all release-gating final scenarios before goal completion.

Old screenshots do not prove a changed build.

---

# 8. Visual Failure Rule

If the agent observes an obvious mismatch while verifying any task, it must not ignore it merely because the current code task is technically complete.

Classify the mismatch:

```text
blocks current acceptance criterion
→ fix now

violates another required goal criterion
→ record/reopen that criterion and schedule next

clearly out of scope
→ record only if useful; do not expand scope
```

Examples:
- black screen;
- duplicate main menu;
- uncentered UI violating design;
- selected entity does not spawn;
- primary content falls outside the intended viewport;
- wrong color/theme;
- overlapping controls;
- required button invisible;
- wrong page/scene opens.

---

# 9. Computer Use / Browser Availability

When a suitable interactive visual tool is available, use it for user-surface verification.

If unavailable:
1. use the strongest available alternative (headed test runner, engine automation, rendered screenshot, browser automation, video/frame capture, etc.);
2. explicitly mark criteria that could not receive required user-surface evidence;
3. do not claim full visual/user-facing verification from static code inspection.

Tool availability may change by harness; project contracts should express the required evidence, not depend on one vendor-specific tool name.

---

# 10. Acceptance Matrix Evidence Types

Recommended evidence types:

```text
static_inspection
build
unit_test
integration_test
runtime_smoke
interactive_runtime
e2e_interaction
screenshot_review
multi_viewport_visual_review
artifact_render_review
user_surface_black_box
independent_review
```

Criteria should declare the minimum required types.

Example:

```yaml
AC-UI-01:
  evidence_required:
    - interactive_runtime
    - screenshot_review

AC-RELEASE-01:
  evidence_required:
    - user_surface_black_box
```

---

# 11. Completion Rule

For any criterion whose success state is visible or interactive:

```text
CODE LOOKS CORRECT
!= VERIFIED

TESTS PASS
!= VISUALLY VERIFIED

APP LAUNCHES
!= USER FLOW VERIFIED
```

The criterion becomes verified only after the required real user-surface evidence has been observed on the applicable build/revision.


---

# 12. Mandatory Capability Discovery

At project/session bootstrap, inspect the actually exposed tools and record
`verification/TOOL_CAPABILITIES.yaml`.

Do not infer tool availability from the model name/provider.

For each applicable user-facing surface, record:
- whether interactive control is available;
- whether screenshots/render capture are available;
- selected adapter;
- fallback adapter.

If interactive/screenshot capability is available and the final criterion requires it,
the agent MUST invoke it. Merely recording that the tool exists is insufficient.

---

# 13. Deterministic Surface Evidence Gate

When user-surface verification is required, the project validator should enforce:

- `TOOL_CAPABILITIES.yaml` exists;
- a final user-surface adapter is selected;
- every release-gating scenario has a result;
- every required interactive evidence ID exists;
- every required screenshot/render artifact exists;
- referenced evidence is not stale;
- evidence is tied to the applicable worktree/revision;
- final completion is rejected when an applicable exposed tool was never invoked.

Example:

```yaml
surface_gate:
  required: true
  capability_ref: verification/TOOL_CAPABILITIES.yaml
  final_scenario: final_primary_user_journey
  require_interactive_invocation: true
  require_visual_artifacts: true
  status: pending
```

The goal cannot become complete while `surface_gate.status != passed`.

This changes user-surface testing from a recommendation into a completion dependency.

# Design-Core admission and whole-surface fidelity gate

For projects where visual identity/layout is material, broad page/screen expansion is downstream of the reusable Presentation/Design Core.

Before treating that core as admitted/exercised, verify where applicable:
- all task-material visual references are registered, routed and actually inspected;
- tokens + primitives + shell/layout contracts exist at canonical owners;
- at least two representative consumers use the same primitive/layout path;
- a shared token/primitive change propagates to both without page-local reimplementation;
- parent slot/container constraints are obeyed at representative viewport/content states;
- the real rendered whole surface is compared against the applicable user-supplied or approved derived visual baseline.

Do not accept:
- "the page contains the right controls" as visual fidelity;
- a component styled correctly while placed in a materially wrong region/hierarchy;
- a generic framework/default design when the project has a specific surface authority;
- source-code tokens/primitives alone as evidence that consumers use them;
- screenshots of isolated controls as proof of whole-screen composition.

When the user's desired style repeatedly collapses toward a generic model default, require the implementation agent to externalize a concrete visual target (existing user reference or derived approved/delegated mockup) **before** broad styling. Then use screenshot-to-baseline comparison at meaningful milestones, not only at final polish.


# v2.24 Surface-fidelity spine

For projects where product identity materially depends on visual/layout/interaction quality, surface fidelity is not only a final verification concern. It must be exercised early enough to steer the rest of implementation.

Preferred proof sequence:

```text
canonical visual/user-surface authorities
→ inspected references / extracted traits
→ shared presentation primitives + layout/slot contracts
→ one representative normal-user surface/path
→ whole-surface screenshot/render comparison
→ correct drift at the shared owner
→ broader surface expansion
```

The representative surface should be chosen for information value, not ease: it should exercise the product's characteristic composition/hierarchy and enough shared primitives to expose generic-default drift.

A visually generic surface that merely exposes working controls can prove connectivity, but not product-specific surface fidelity.

When exact reference reproduction is not intended, compare against the compiled adopt/adapt/reject traits and approved/delegated derived baseline rather than inventing a new generic aesthetic.


# v2.26 Whole-product surface chain

For multi-surface products, final surface verification must cover the complete required normal-user chain, not merely the primary runtime surface.

Build evidence per required APP_FLOW/workflow node, then run at least one release-gating journey across the connected sequence.

Visual fidelity is progressive:
- establish shared Design/Presentation Core early;
- verify each material surface against its applicable authority as it becomes runnable;
- perform a final coherence pass across the connected product journey.

Do not postpone all product-specific design to one late "visual overhaul" after dozens of generic surfaces have already diverged.


# v2.29 Deterministic surface-review projection

When visual/user-surface quality is material, specialize the generic deterministic review-projection rule with stable states/viewports/inputs rather than ad-hoc screenshots. Reuse the same recipe before/after meaningful changes so drift is comparable.

The screenshot/render/capture is derived evidence, not a design or product authority. If it exposes a defect, fix the canonical design/layout/content/runtime owner and capture again.
