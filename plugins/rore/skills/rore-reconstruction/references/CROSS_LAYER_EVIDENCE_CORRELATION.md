# Cross-Layer Evidence Correlation

Use when the same apparent object or behavior appears in different layers: shipped bytes and runtime scripts, source map and generated bundle, native function and stack frame, managed method and native call, asset and rendered surface, protocol schema and wire capture, or two versions of a component. Preserve each layer's own authority; a correlation is a separate, evidence-backed Finding or Path edge.

## Identity and candidate set

1. Fix both observations to their original target/build/environment, source boundary and coverage. Preserve raw bytes or records, exact source ranges, provider/transform versions and known exclusions.
2. Define the candidate population and identity domain before matching. File path, URL, symbol name, display name, method token, module ordinal, load address and source-map source name can have different scopes. Do not compare them as one global namespace.
3. Establish mappings explicitly: container member → extracted file; file offset → section/virtual address → loaded module; generated position → source-map entry; runtime URL/root → shipped artifact path; managed declaration → native export. Record mapping version, assumptions and any unreadable or unbacked region.
4. Prefer exact content identity plus a compatible location and version. A unique exact digest can support a narrower content match without location. A unique mapped location without captured bytes is a weaker candidate. Structural signatures, names, strings and call patterns are hypotheses until independently constrained.
5. If candidates tie, keep all of them `AMBIGUOUS`; never choose a convenient one. If mapped location and captured bytes disagree, record `MISMATCH`; the path does not override the digest. Missing mappings, inaccessible bytes, bounded/truncated capture or incomplete candidate inventory remain `UNKNOWN` for the affected claim.
6. Emit the relationship with its basis, candidate count, Evidence on both sides, confidence and scope. Reconcile negative evidence only within the captured population and observation window. Repeat with another boundary when the relationship materially changes the model.

Useful result classes are `EXACT_CONTENT_AND_LOCATION`, `UNIQUE_CONTENT`, `UNIQUE_LOCATION`, `INFERRED_STRUCTURE`, `AMBIGUOUS`, `MISMATCH` and `UNKNOWN`. They describe correspondence, not runtime execution or causality. Corroboration requires a materially independent producer or observation boundary, not merely two projections of one parser result.

## Bound the conclusion

- A browser-observed script can establish loaded/present under a mapped capture; an embedded module may only be resident in that asset. Neither establishes module initialization, feature execution, call ordering or effect.
- A source map maps generated coordinates under a verified file/map pairing. A source name or embedded `sourcesContent` is not the generated runtime bytes or independently captured original file; duplicate entries and unmapped ranges remain visible.
- A decompiled/native function matching a stack address needs the exact image, load mapping and instruction/source range. A function-shaped pseudocode view is not original source or proof that a specific path executed.
- A managed method token is build-local. A P/Invoke declaration or matching export is a boundary candidate, not proof of the native body called or its runtime effect.
- An API schema, captured request and client projection may disagree legitimately across endpoint/version/environment. Preserve field transforms and unresolved edges rather than selecting one as globally canonical.
- An asset referenced in metadata is not necessarily loaded or rendered; tie use to the observed surface/state and preserve variants and fallback paths.
- Cross-version `added` or `removed` requires adequate coverage of the side where the counterpart was not found. Otherwise use `UNKNOWN` or a candidate delta.

Use a compact table when many entities are involved:

| Left identity + Evidence | right identity + Evidence | mapping / match basis | candidate count | status | claim permitted / gap |
| --- | --- | --- | --- | --- | --- |

Keep the raw Evidence for each layer unchanged. Correction of a mapping creates a linked revision of the Finding/Path, not a silent rewrite of source observations.
