# Surface / Flow / State Reconstruction

Adapted from the useful `replica-recon` ideas, but reference-only.

## Surface inventory

Assign stable `SUR-###` IDs to materially distinct screens/views/surfaces. Record:
- route or reachability path;
- purpose/role;
- key components;
- visible inputs/outputs;
- observed states;
- evidence IDs and version/environment.

States matter: empty, loading, filled, error, denied, stale, offline, mobile/responsive, partial, retry, interrupted, restored, etc. Record only states actually observed or clearly label proposed probes.

## Flow inventory

Assign `FLOW-###` to user/system goals or causal flows. Record ordered surfaces/states/events and edge conditions. Do not convert click count or flow length into target-product optimization.

## Components

Record repeated UI/runtime components, variants, states, consumers and relationships as reference facts. Do not immediately translate them into a new design system.

## Inferred data model

Entities/fields/relationships inferred from surfaces must cite evidence and confidence. Form fields, confirmations, docs, storage/network/runtime evidence may cooperate. A UI field does not prove backend storage or canonical schema.

## Edge-state probing

The upstream QA matrix is useful as a **discovery prompt**, not a mandatory test suite. Depending on the target, consider empty/long/unicode input, double action, back/refresh, slow/offline, expired state, concurrent session, timezone, permission, deleted/missing data, responsive width and accessibility semantics.

The result is reference behavior, not a target acceptance requirement.
