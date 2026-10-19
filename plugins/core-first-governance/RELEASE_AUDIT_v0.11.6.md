# Core-First Governance v0.11.6 — Release Audit

## Scope

v0.11.6 is a bounded extension of the existing `observable-product-verification` evidence responsibility. It adds freshness-sensitive oracle-liveness semantics and two regression evals. The complete v0.11.5 orchestration/Core-First architecture baseline remains unchanged.

## Canonical change

```text
FRESHLY ACQUIRED EVIDENCE != FRESHLY OBSERVED STATE
```

When a material claim depends on live/current state and the observation path may plausibly be stale/frozen/cached/replayed/disconnected, OPV now requires the smallest safe liveness discriminator before trusting that source. A successful capture/tool call or fresh artifact does not by itself establish liveness.

The reverse guard is equally explicit:

```text
IDENTICAL OBSERVATIONS != PROOF OF DEAD ORACLE
```

A static state may legitimately produce identical samples.

## Intentional Skill-tree changes

| File | v0.11.5 SHA-256 | v0.11.6 SHA-256 | Bytes 0.11.5 → 0.11.6 |
| --- | --- | --- | ---: |
| `observable-product-verification/SKILL.md` | `d66063733db024abd3ae2b3a4e95c615906851125c29fd76b24a41c342ccd102` | `1d2f4531089fa2ac3ccbbfa1c878475b0401433d9e8b3d842c67ac1bfa7404cb` | 15,681 → 16,907 |
| `observable-product-verification/evals/evals.json` | `4f1ea27b798cf694e1711f7588d239a5d12868f8d53229e4fdd24b8d87723372` | `b973dbccbafe8c4237c2e5c4af45c5f9276235b6bea2239c56202cb4c2e13ac7` | 8,469 → 9,747 |

`observable-product-verification/agents/openai.yaml` remains unchanged.

## Protected unchanged runtime owners

The release validator continues to hash-protect:

- the complete v0.11.5 `core-first-orchestration` runtime/JIT corpus;
- the complete canonical `core-first-extension-architecture` family;
- `core-first-verifier`;
- `independent-review`;
- unchanged OPV agent metadata.

No new Skill or JIT reference is admitted.

## New eval coverage

### `fresh-capture-does-not-prove-oracle-liveness`

Protects against:

```text
successful capture
+ new file/timestamp
+ plausible image
→ incorrectly treated as current-state proof
```

Required response: establish observation-path liveness from independent ongoing activity or a controlled observable stimulus, otherwise use another boundary or keep the claim inconclusive.

### `identical-static-observations-do-not-prove-dead-oracle`

Protects against:

```text
identical samples
→ automatically declare oracle dead
```

Required response: identical samples alone are insufficient when the underlying state may legitimately be static.

## Context budget

No always-loaded context changes:

```text
core-first-orchestration/SKILL.md        10,998 / 11,000 bytes
orchestration kernel + five JIT refs     26,444 / 26,500 bytes
core-first-extension-architecture        14,480 / 15,000 bytes
```

Only JIT-loaded OPV grows by 1,226 bytes.

## Non-goals confirmed

v0.11.6 does not add an oracle subsystem, capture implementation, screenshot loop, MCP server, debugging tool, evidence store, tracker, model/provider rule, or project authority format.

## Validation expectation

Release is acceptable only if:

```text
validate_release.py                          PASS
Codex/plugin validator                       PASS
exactly five Skills                          PASS
orchestration/Core-First protected hashes    PASS
OPV v0.11.6 hashes                           PASS
new two-direction oracle-liveness evals       PRESENT
```

## Executed validation

Executed on the assembled v0.11.6 tree:

```text
python validate_release.py
→ RELEASE VALIDATION: PASS
→ plugin_version=0.11.6
→ skills=5
→ orchestration_kernel_bytes=10998
→ orchestration_total_procedure_bytes=26444
→ oracle_liveness_current_state_guard=PASS
→ identical_static_samples_reverse_guard=PASS

python validate_plugin.py <plugin-root>
→ Plugin validation passed
```

A direct recursive comparison of the v0.11.5 and v0.11.6 Skill trees reports exactly two changed files:

```text
observable-product-verification/SKILL.md
observable-product-verification/evals/evals.json
```

The regression eval definitions are release-validated for presence and structure. No external multi-model behavioral eval runner was executed as part of packaging; do not interpret release validation as a measured cross-model behavior result.
