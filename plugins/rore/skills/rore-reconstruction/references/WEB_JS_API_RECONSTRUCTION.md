# Web / JavaScript / API Reconstruction

Use browser/runtime evidence to connect UI behavior to client logic, requests, responses, storage and navigation.

A useful loop adapted from the reviewed JS methodology is:

```text
Observe → Capture → Reconstruct → Corroborate → Deepen if needed
```

## Observe
Identify the user action, DOM/state change, relevant network request, initiator/call source and candidate scripts/modules. Do not guess an environment before observing it.

## Capture
Acquire the smallest runtime sample that reveals parameter shape, call ordering and state dependencies. Prefer light observation/hooks before disruptive breakpoints when both can answer the question.

## Reconstruct
Connect:

```text
user action
→ DOM/event handler
→ client state / transform
→ request / protocol message
→ response
→ route/render/persistence effect
```

A public OpenAPI/GraphQL/schema source may reveal semantics, but correlate it with actual client/runtime behavior when the claim is target-specific.

## API projection and layer identity

Shared business names or matching sample values do not establish a shared wire contract. An internal/legacy endpoint, frontend projection and public/versioned API may expose the same entity with different field case/names, types, authentication, defaults, validation, request shape or response projection. Bind each captured request/response and schema to its endpoint, version and environment; compare them field by field before carrying a finding across layers. A public schema is evidence about that public API, not automatically about the private client path. Where a field is transformed, trace the client/server mapping or mark the edge unresolved.

## Differential probing
Within authorized scope, manually vary DOM/client state, request shape, method, omitted/extra fields, sequence or version only when it helps distinguish client-side vs server-side logic, validation, derived fields, state transitions or source precedence. Do not escalate impact after the mechanism is understood.

Record what the UI hides relative to the response and what the server recalculates/ignores rather than assuming the client representation is canonical.

## Shipped JavaScript and runtime correspondence

For an Electron, bundled web or comparable JavaScript target, inventory the shipped container and sidecars first: entry points, packages, chunks, source maps, native add-ons, storage/configuration, main/preload/renderer or worker boundaries and candidate IPC channels. An ASAR or other bundle may reference external unpacked bytes; an incomplete extraction is not evidence that those components are absent.

Trace a feature from a concrete route, visible string, API endpoint, event or IPC seed through reachable code/data relationships. Dynamic imports, computed properties, aliases, mutable objects, parser recovery and duplicate structural fingerprints can leave candidate or unknown edges. A static reachable path is not an exercised user flow. Capture the actual browser/Electron script, frame/worker, request and state where runtime use matters, then apply `CROSS_LAYER_EVIDENCE_CORRELATION.md`. Exact captured bytes plus mapped location give a stronger relation than a unique path; a digest mismatch stays a mismatch. A loaded bundle does not prove that each embedded module initialized or produced an effect.

Source-map declarations and `sourcesContent` are derived mapping evidence. Verify the paired generated script/map bytes and coordinate convention before tracing a position. A source name, path convention or embedded text does not by itself prove the original source file was shipped or that code executed.

For a reproducible UI reference case, state the initial state and action, wait for a target-specific readiness predicate when asynchronous work matters, and request the observations that answer the question: DOM/accessibility, screenshot/canvas, network/events, storage or navigation as applicable. An unrequested artifact is `not_observed`, not absent. A complete URL-only capture cannot establish rendered content, and an already-visible stale result is not proof that the new action completed.
