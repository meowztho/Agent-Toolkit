# Cross-Version / Differential Reconstruction

Use changed builds, patches, old/new binaries, schemas or behavior to reveal semantics.

Bind each side to a strong identity. Align using semantic anchors rather than raw addresses:
- exports/symbols;
- strings and xrefs;
- constants/magic values;
- types/vtables/schema fields;
- call relationships;
- code/control patterns;
- data references;
- runtime behavior.

Diffs can reveal newly added validation, locks, zeroing, bounds, state transitions or removed paths. Infer the mechanism cautiously: a patch pattern suggests a hypothesis, not automatically the complete root cause.

Names recovered from an older symbolized build may be useful hypotheses for a newer build, but re-establish the mapping in the current artifact before promoting them.

Never transplant old raw offsets as durable truth merely because nearby code looks similar.

Pair an entity across versions only when the chosen identity basis produces one defensible candidate on each side. Compare exact content first where available, then qualified source/artifact identity and stable semantic structure. A duplicate digest, minified name, ordinal, fuzzy text similarity or shared string alone can leave several candidates; retain them as ambiguous. Record the matching tier, candidate count, changed dimensions and both Evidence IDs. A lower-confidence match does not override an exact contradictory match.

Call a counterpart `added` or `removed` only when the relevant population on the other side was adequately inventoried. If parsing, capture, extraction or mapping was partial, classify the affected delta as unknown or candidate. A different runtime result can expose changed behavior, but a static patch alone does not prove the changed path executed or caused that result. Use `CROSS_LAYER_EVIDENCE_CORRELATION.md` when artifacts and runtime observations must first be reconciled.
