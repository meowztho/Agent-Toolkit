# Memory / State / Causality Reconstruction

Use live memory/state when it can expose authoritative values, generated/decrypted content, object layouts or reader/writer causality unavailable elsewhere.

Typical loop:

```text
known state/value
→ search / snapshot / diff
→ state changes
→ narrow candidates
→ inspect surrounding object/relationships
→ trace readers/writers or access path
→ controlled mutation if discriminating
→ observe response
→ connect to semantic object/path
```

A changed memory value producing an effect proves a relationship, not automatically canonical ownership. If the value is immediately overwritten, trace the writer; the address may be a cache/mirror/derived field.

Preserve addresses, registers, raw offsets and pointers as session/build-local Evidence. Durable Findings prefer semantic identities such as `Entity → HealthComponent → CurrentHealth → Damage/Death path`.

When connecting a memory observation to file bytes, record the loaded module/build, base address and established file-to-memory mapping. Relocation, unpacking, generated code and runtime writes can break a direct offset equivalence. Compare the relevant raw snapshots before and after a controlled trigger rather than treating one plausible value as the authoritative field.

Controlled mutation is valid when authorized and informative. Use the smallest change needed to discriminate the hypothesis and restore/record state afterward.
