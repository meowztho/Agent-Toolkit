"""Lossless, structurally checked intake of a REA Evidence JSON export.

This adapter does not implement REA's semantic-ID or unknown-graph validator.
The retained original is the authority for every projected field.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from pathlib import Path

from .bundle import BundleError, FORMAT, INDEX, MAX_BYTES, MAX_INDEX_BYTES, VERSION, validate

REA_ARRAYS = ("artifacts", "providers", "environments", "scenarios", "captures", "unknowns", "records")
RAW_PATH = "raw/rea-evidence-bundle.json"


def _reject_constant(value: str) -> None:
    raise BundleError(f"non-JSON constant: {value}")


def _read(source: str | Path) -> tuple[bytes, dict, str]:
    path = Path(source)
    if not path.is_file() or path.is_symlink():
        raise BundleError("REA source must be a regular JSON file")
    if path.stat().st_size > MAX_BYTES - MAX_INDEX_BYTES:
        raise BundleError("REA source exceeds bundle size limit")
    data = path.read_bytes()
    if len(data) > MAX_BYTES - MAX_INDEX_BYTES:
        raise BundleError("REA source exceeds bundle size limit")
    try:
        document = json.loads(data.decode("utf-8"), parse_constant=_reject_constant)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise BundleError(f"invalid REA JSON: {exc}") from exc
    if not isinstance(document, dict) or any(
        not isinstance(document.get(key), list) for key in REA_ARRAYS
    ):
        raise BundleError("REA Evidence export needs artifacts, providers, environments, scenarios, captures, unknowns and records arrays")
    for key in REA_ARRAYS:
        if any(not isinstance(item, dict) for item in document[key]):
            raise BundleError(f"REA {key} must contain objects")
    record_ids: set[str] = set()
    for record in document["records"]:
        ident = record.get("evidence_id")
        if not isinstance(ident, str) or not ident.startswith("ev_") or ident in record_ids:
            raise BundleError(f"missing or duplicate REA evidence_id: {ident!r}")
        if not isinstance(record.get("operation"), str) or not record["operation"].strip():
            raise BundleError(f"{ident}: missing REA operation")
        record_ids.add(ident)
    revisions: set[tuple[str, int]] = set()
    for unknown in document["unknowns"]:
        ident, revision = unknown.get("unknown_id"), unknown.get("revision")
        if (not isinstance(ident, str) or not ident.startswith("unk_") or
                type(revision) is not int or revision < 1 or (ident, revision) in revisions):
            raise BundleError(f"missing or duplicate REA unknown revision: {ident!r}:{revision!r}")
        revisions.add((ident, revision))
    return data, document, hashlib.sha256(data).hexdigest()


def preview_rea(source: str | Path) -> dict:
    """Identify the REA-shaped source and its limits without writing anything."""
    data, document, digest = _read(source)
    subjects = sorted({record["subject"]["digest"]["sha256"]
                       for record in document["records"]
                       if isinstance(record.get("subject"), dict)
                       and isinstance(record["subject"].get("digest"), dict)
                       and isinstance(record["subject"]["digest"].get("sha256"), str)})
    return {"format": "rea-evidence-export", "sha256": digest, "bytes": len(data),
            "counts": {key: len(document[key]) for key in REA_ARRAYS},
            "subject_sha256": subjects,
            "validation": "structural-only; REA semantic IDs, manifests and unknown graph not verified"}


def import_rea(source: str | Path, destination: str | Path) -> dict:
    """Project REA records into a new RORE bundle; retain the entire source byte-for-byte."""
    source, destination = Path(source), Path(destination).resolve()
    if destination.exists() or source == destination or source in destination.parents:
        raise BundleError("destination must be a new directory outside the REA source")
    data, original, digest = _read(source)
    projection = {
        "format": FORMAT, "version": VERSION,
        "target": {"identity": f"rea-export-sha256:{digest}", "identity_scope": "source-bundle",
                   "note": "REA records may cover multiple or absent artifact subjects"},
        "source_bundle": {"format": "rea-evidence-export", "path": RAW_PATH, "sha256": digest,
                          "validation": "structural-only; verify with REA before treating REA IDs as authentic"},
        "evidence": [], "findings": [], "paths": [], "models": [], "unknowns": [],
    }
    raw = [{"path": RAW_PATH, "sha256": digest}]
    record_ids = {record["evidence_id"] for record in original["records"]}
    projection["evidence"].append({
        "id": f"E-REA-EXPORT-{digest}",
        "source": {"kind": "rea-evidence-export", "locator": RAW_PATH},
        "method": "retain original REA JSON bytes; structural projection only",
        "raw": raw,
    })
    for index, record in enumerate(original["records"]):
        projection["evidence"].append({
            "id": record["evidence_id"],
            "source": {"kind": "rea-evidence-record", "locator": RAW_PATH,
                       "json_pointer": f"/records/{index}", "subject": record.get("subject"),
                       "provider": record.get("provider")},
            "method": record["operation"], "raw": raw,
            "rea_predicate_type": record.get("predicate_type"),
            "rea_confidence": record.get("confidence"),
            "rea_authority": record.get("authority"),
            "projection_limit": "Original REA record and raw/normalized results are in the retained JSON",
        })
    for index, unknown in enumerate(original["unknowns"]):
        related = []
        for field in ("supporting_evidence_ids", "contradicting_evidence_ids", "mutation_evidence_ids"):
            value = unknown.get(field, [])
            if isinstance(value, list):
                related.extend(item for item in value if isinstance(item, str) and item in record_ids)
        projection["unknowns"].append({
            "id": f"{unknown['unknown_id']}:r{unknown['revision']}",
            "rea_unknown_id": unknown["unknown_id"], "revision": unknown["revision"],
            "source": {"kind": "rea-unknown-revision", "locator": RAW_PATH,
                       "json_pointer": f"/unknowns/{index}"},
            "question": unknown.get("question"), "status": unknown.get("status"),
            "previous_revision_digest": unknown.get("previous_revision_digest"),
            "revision_digest": unknown.get("revision_digest"),
            "scope_digest": unknown.get("scope_digest"),
            "rea_supporting_evidence_ids": unknown.get("supporting_evidence_ids", []),
            "rea_contradicting_evidence_ids": unknown.get("contradicting_evidence_ids", []),
            "rea_mutation_evidence_ids": unknown.get("mutation_evidence_ids", []),
            "evidence_ids": sorted(set(related)),
            "projection_limit": "Full revision, relationships and contradictions are in the retained JSON",
        })
    encoded = (json.dumps(projection, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if len(encoded) > MAX_INDEX_BYTES or len(data) + len(encoded) > MAX_BYTES:
        raise BundleError("projected bundle exceeds index or total size limit")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".rore-rea-import-", dir=destination.parent))
    try:
        (temporary / "raw").mkdir()
        (temporary / RAW_PATH).write_bytes(data)
        (temporary / INDEX).write_bytes(encoded)
        if hashlib.sha256((temporary / RAW_PATH).read_bytes()).hexdigest() != digest:
            raise BundleError("REA source changed during import")
        result = validate(temporary)
        if destination.exists():
            raise BundleError("destination already exists")
        temporary.rename(destination)
        return {"destination": str(destination), "rea_sha256": digest,
                "rea_validation": "structural-only", **result}
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def inspect_rea_original(bundle: str | Path, record_id: str) -> dict:
    """Return the unmodified REA record addressed by a projected RORE ID."""
    validate(bundle)
    root = Path(bundle)
    index = json.loads((root / INDEX).read_text(encoding="utf-8"))
    source = index.get("source_bundle")
    if not isinstance(source, dict) or source.get("format") != "rea-evidence-export" or source.get("path") != RAW_PATH:
        raise BundleError("bundle has no REA Evidence source")
    raw_bytes = (root / RAW_PATH).read_bytes()
    if hashlib.sha256(raw_bytes).hexdigest() != source.get("sha256"):
        raise BundleError("REA source bundle hash mismatch")
    original = json.loads(raw_bytes.decode("utf-8"))
    for group, identifier in (("records", "evidence_id"), ("unknowns", "unknown_id")):
        for record in original.get(group, []):
            expected = record.get(identifier)
            if group == "unknowns":
                expected = f"{expected}:r{record.get('revision')}"
            if expected == record_id:
                return {"kind": group, "record": record, "source_sha256": source["sha256"]}
    raise BundleError(f"REA record not found: {record_id}")
