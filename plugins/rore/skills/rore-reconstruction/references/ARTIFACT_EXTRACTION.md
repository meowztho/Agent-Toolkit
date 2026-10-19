# Artifact / Extraction Reconstruction

Use format-first dispatch.

1. identify container/file/package type and strongest target identity;
2. inventory before deep extraction;
3. choose a compatible extractor/parser;
4. validate semantic output, not just exit status;
5. use bounded fallback/alternate providers if expected information value remains high;
6. recurse through nested containers intentionally while preserving parent→child lineage;
7. keep originals authoritative and derived outputs reproducible/disposable where practical.

`extractor exit 0 != meaningful extraction success`.

Record failed extraction/parser attempts when they narrow the format hypothesis. Preserve source/layer precedence for base + patch/override/resource combinations.

For application packages, retain the outer archive identity and member path/size/hash before materializing files. Inventory symlinks, encrypted entries, aliases, external sidecars, unpacked resources and unsupported formats; a path convention is only a role candidate until the manifest/plist/configuration or runtime confirms it. For firmware or mixed containers, record each recognized region and decoder version with its source range. A successfully extracted region is not a complete inventory of the device or application. Treat a decoded child as a derived artifact with an explicit parent mapping rather than a replacement for the original bytes.

For an executable or protected package, distinguish compression/packing, obfuscation, encryption and inaccessible source from one another before choosing a method. Decoding or decryption is a capability question tied to an authorized key, available runtime boundary or observed plaintext; a plausible decompiler view is not proof that protected content was recovered. Preserve original bytes and parent→derived lineage. If the content cannot be recovered, reconstruct observable behavior through other authorized boundaries and mark internal structure unknown rather than inventing code.

## Asset census across domains

For material images, icons, fonts, audio, video, localization, documents, shaders, models or other resources, inventory the source container and each recovered asset with stable identity/hash and parent→child lineage. Record format/encoding, dimensions, duration or other native properties, variants/languages/layers and conversion steps where applicable. Map references and runtime/UI use separately: `present != referenced != reachable != exercised != effective`. Connect an asset to the surface, state, component or behavior where it is actually used; keep unmatched, duplicated and inaccessible assets visible in coverage rather than silently dropping them. Preserve original bytes and measured properties before generating previews or normalized replacements. Record access and redistribution limits separately from the ability to analyze.
