# Data / Schema / Format Reconstruction

Reconstruct records, entities, fields, constraints, defaults, relationships, indexes and transforms without assuming a target implementation schema.

Evidence may come from files/databases, serialized records, UI forms, API payloads, runtime objects, code, docs or cross-record population analysis.

Distinguish:
- observed field/value;
- inferred type/enum/default;
- relationship hypothesis;
- persistence/canonical-source claim;
- complete-population claim.

For generated/defaulted values, identify where they originate and whether they are stored, derived, cached or recomputed.

Custom formats should preserve raw bytes plus parsed/normalized views. Parser success must be challenged with identity, boundaries, multiple samples and round-trip/independent evidence when material.
