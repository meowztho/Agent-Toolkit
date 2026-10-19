# Workspace and Target Identity

Classify the analyzed workspace before placing RORE artifacts. It may be a source repository, an immutable binary/distribution package, an installed application, a loose artifact bundle, or a mixture of these. An install or package directory may itself be the reference: adding metadata there can change signatures, discovery, validation, size or behavior. Do not treat an installed application as a writable source repository.

Keep these roles distinct where material:

```text
raw/reference evidence
scratch/intermediate derivatives
RORE control/evidence graph and durable handoff
actual analyzed target/runtime
```

Place the control/evidence graph outside a target payload when its presence could alter that payload. Record the target path, control-plane path, raw-evidence path and scratch path in the handoff when their distinction matters. A controlled target copy is useful when representative; keep its identity and changes separate from the original. Scratch output is disposable working material, not Reference Truth merely because it is under a project directory. Clean it only after preserving any raw Evidence or failed-run traces needed for the investigation, and verify that cleanup did not remove or alter the target.

Local-only or non-shareable reference material must not enter tracked source, collaborative uploads or a portable handoff that cannot retain it. If a project gate claims to prevent that, challenge it with a representative negative control. Apply `SOURCE_USE_AND_DISTRIBUTION.md` to the handling decision.

Bind analysis state to the strongest practical target identity available: SHA-256/content hash, signed build ID, package version plus hash, Git revision, URL+deployment/environment identity, dataset revision, or a generated evidence-run identity with recorded hashes. A target without Git still has an identity; do not invent a commit or confuse the RORE control repository's revision with the analyzed target's revision.

A previous workspace from another version is evidence/history, not current truth. Re-resolve semantic anchors before carrying names, offsets, structure or findings forward.
