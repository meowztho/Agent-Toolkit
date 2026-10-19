# Optional RORE Evidence bundle v1

The bundle is a directory containing `rore-evidence.json` plus the original raw files and any narrative, traces, screenshots, models or other material the investigation needs. It is a **portable index**, not a replacement for the reference-native handoff. Additional JSON fields and additional files remain intact. A missing detail must stay unknown; this format does not turn a valid reference link into proof of semantic correctness.

```json
{
  "format": "rore-evidence-bundle",
  "version": 1,
  "target": {"identity": "sha256:<reference-artifact-hash>", "environment": "observed host/build"},
  "evidence": [{
    "id": "E-001",
    "source": {"kind": "artifact", "locator": "reference.exe"},
    "method": "read original bytes with recorded offset mapping",
    "raw": [{"path": "raw/header.bin", "sha256": "<64 lowercase hex digits>"}]
  }],
  "findings": [{"id": "FIND-001", "evidence_ids": ["E-001"], "statement": "..."}],
  "paths": [], "models": [], "unknowns": []
}
```

Each Evidence record needs a source, method and at least one raw item. A raw item references a retained relative file plus SHA-256, or states `{"access":"restricted|unavailable","reason":"..."}`. The latter is an explicit limit, not a claim that the bytes were checked. Other record classes may link through `evidence_ids`, `finding_ids`, `path_ids`, `model_ids` and `unknown_ids`; the validator checks that these IDs exist in the named class. It does **not** establish source authenticity, actual runtime behavior, independent corroboration, claim support or completeness. Those remain Reconstruction and Evidence Review work.

The CLI uses Python's standard library and never runs an analysis provider:

```text
python scripts/rore.py bundle-init <new-bundle-directory> <target-identity> [--environment TEXT]
python scripts/rore.py evidence-add <bundle-directory> <E-ID> <source-locator> <method> <raw-file> [more-raw-files...]
python scripts/rore.py validate <bundle-directory>
python scripts/rore.py inspect <bundle-directory> E-001
python scripts/rore.py compare <left-directory> <right-directory>
python scripts/rore.py export <bundle-directory> <new-output.zip>
python scripts/rore.py import <archive.zip> <new-destination-directory>
python scripts/rore.py rea-preview <rea-evidence-export.json>
python scripts/rore.py rea-import <rea-evidence-export.json> <new-destination-directory>
python scripts/rore.py rea-record <imported-bundle-directory> <original-rea-id>
```

`bundle-init` creates a new empty index; `evidence-add` appends one Evidence record, copies complete file bytes under `raw/` and records their SHA-256. Existing files already inside the bundle are linked without recopying. Both refuse an existing destination or duplicate record ID and never edit an earlier record. Use one writer at a time. The caller still supplies a truthful target identity, source locator and acquisition method; these commands do not inspect target semantics, create Findings, infer coverage or replace a narrative. For multi-step analysis, an agent can still use a focused script or another qualified tool and add its full raw output.

Export retains **every file byte for byte** in a ZIP without compression and refuses an existing output. Import accepts only new destinations, rejects links, duplicate/unsafe paths and oversized archives, validates the resulting bundle, then moves it into place. The current cap is 10,000 files and 512 MiB, with a 16 MiB index limit; larger investigations keep complete raw sources in companion directories or archives with hashes and a navigable manifest. The cap limits this transport, not RORE's investigation or the amount of reference material to acquire. No CLI operation rewrites an existing Evidence record.

The REA bridge accepts the JSON Evidence export read by REA 6.2.0's `rea evidence-import` and written by its `rea evidence-export`. It recognizes the seven top-level arrays `artifacts`, `providers`, `environments`, `scenarios`, `captures`, `unknowns` and `records`. Import retains the **entire original JSON byte for byte** at `raw/rea-evidence-bundle.json`, records its SHA-256, and projects REA Evidence IDs and each Unknown revision into the RORE index. The target identity in this projection identifies the **source bundle**, since one REA export can contain several or no artifact subjects. `rea-record` reads the original record through the verified raw source; the RORE index is only a navigational projection. Import refuses an existing destination. REA remains optional.

An existing REA session can write this JSON through its MCP `export_evidence_bundle` tool. REA's CLI `rea evidence-export <source.json> <output.json>` canonicalizes an existing REA bundle. Supply the resulting JSON file to `rore rea-preview` and `rore rea-import`; the two processes need only access to the same file path. RORE does not proxy REA's analysis commands or mutate its MCP session.

This bridge performs structural intake and RORE raw-hash checks. It does **not** reproduce REA's semantic Evidence ID calculation, canonical manifests, Unknown revision graph validation or process-capture parser. For REA authenticity/integrity claims, first validate the source with REA's own `rea evidence-import <file>` on a trusted REA runtime. A structurally accepted file alone is not qualified Reference Truth.

The optional local MCP adapter exposes read-only `rore_validate_bundle`, `rore_inspect_record`, `rore_compare_bundles`, `rore_preview_rea_export` and `rore_inspect_rea_original`. CLI performs imports; MCP does not write. Both use the same core and do not acquire target evidence or execute discovered tools. MCP responses above 256 KiB fail with a CLI recovery path instead of truncating. Install `uv` and allow the pinned `uv.lock` dependencies before connecting the packaged `mcp.json`; the CLI itself requires no package installation. MCP availability does not prove an analysis provider is available.
