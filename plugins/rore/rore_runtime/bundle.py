"""Validate and move complete RORE Evidence bundles without rewriting them."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

INDEX = "rore-evidence.json"
FORMAT = "rore-evidence-bundle"
VERSION = 1
KINDS = ("evidence", "findings", "paths", "models", "unknowns")
MAX_FILES = 10000
MAX_BYTES = 512 * 1024 * 1024
MAX_INDEX_BYTES = 16 * 1024 * 1024


class BundleError(ValueError):
    """A bundle is invalid, incomplete, or outside the supported size bound."""


def _safe_relative(value: str) -> Path:
    if not isinstance(value, str) or not value or "\\" in value:
        raise BundleError(f"invalid relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in ("", ".", "..") for part in value.split("/")) or ":" in value:
        raise BundleError(f"unsafe relative path: {value!r}")
    for part in path.parts:
        stem = part.split(".", 1)[0].upper()
        if (part.rstrip(" .") != part or any(ord(char) < 32 or char in '<>"|?*' for char in part)
                or stem in {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}):
            raise BundleError(f"unsafe relative path: {value!r}")
    return Path(*path.parts)


def _files(root: Path) -> list[tuple[str, Path]]:
    if not root.is_dir() or root.is_symlink():
        raise BundleError("bundle must be a real directory")
    found: list[tuple[str, Path]] = []
    size = 0
    for base, dirs, names in os.walk(root, followlinks=False):
        for name in dirs + names:
            item = Path(base) / name
            if item.is_symlink():
                raise BundleError(f"symlink in bundle: {item.relative_to(root)}")
        for name in names:
            item = Path(base) / name
            if not item.is_file():
                raise BundleError(f"non-file bundle member: {item.relative_to(root)}")
            size += item.stat().st_size
            if size > MAX_BYTES or len(found) >= MAX_FILES:
                raise BundleError("bundle exceeds file or byte limit")
            found.append((item.relative_to(root).as_posix(), item))
    return sorted(found)


def _digest(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            sha.update(chunk)
    return sha.hexdigest()


def _records(document: dict, kind: str) -> list[dict]:
    value = document.get(kind, [])
    if not isinstance(value, list) or any(not isinstance(row, dict) for row in value):
        raise BundleError(f"{kind} must be a list of objects")
    return value


def init_bundle(destination: str | Path, identity: str, environment: str = "") -> dict:
    """Create one new empty Evidence bundle without touching an existing path."""
    if not isinstance(identity, str) or not identity.strip():
        raise BundleError("target identity is required")
    if not isinstance(environment, str):
        raise BundleError("environment must be text")
    destination = Path(destination).absolute()
    if destination.exists() or destination.is_symlink():
        raise BundleError("destination already exists")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".rore-init-", dir=destination.parent))
    try:
        (temporary / "raw").mkdir()
        document = {"format": FORMAT, "version": VERSION,
                    "target": {"identity": identity, "environment": environment},
                    **{kind: [] for kind in KINDS}}
        (temporary / INDEX).write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        validate(temporary)
        if destination.exists() or destination.is_symlink():
            raise BundleError("destination already exists")
        temporary.rename(destination)
        return {"destination": str(destination), **validate(destination)}
    finally:
        if temporary.exists():
            if temporary.resolve().parent != destination.parent.resolve():
                raise BundleError("bundle-init cleanup path escaped destination parent")
            shutil.rmtree(temporary)


def capture_evidence(root: str | Path, record_id: str, source: str, method: str,
                     paths: list[str | Path]) -> dict:
    """Append one file-backed Evidence record, retaining complete raw bytes."""
    if not isinstance(record_id, str) or not record_id.strip() or any(ord(char) < 32 for char in record_id):
        raise BundleError("evidence id must be nonempty text without control characters")
    if not isinstance(source, str) or not source.strip():
        raise BundleError("evidence source is required")
    if not isinstance(method, str) or not method.strip():
        raise BundleError("evidence method is required")
    if not paths:
        raise BundleError("at least one raw file is required")
    existing = validate(root)
    root = Path(root).resolve()
    index = root / INDEX
    original_index = index.read_bytes()
    document = json.loads(original_index.decode("utf-8"))
    if any(row["id"] == record_id for kind in KINDS for row in _records(document, kind)):
        raise BundleError(f"duplicate record id: {record_id}")
    inputs = []
    seen = set()
    for path in paths:
        item = Path(path)
        if item.is_symlink() or not item.is_file():
            raise BundleError(f"raw source must be a regular non-symlink file: {item}")
        resolved = item.resolve()
        if resolved in seen or resolved == index:
            raise BundleError(f"duplicate or index raw source: {item}")
        seen.add(resolved)
        inputs.append(resolved)
    external_inputs = [item for item in inputs if root not in item.parents]
    new_bytes = sum(item.stat().st_size for item in external_inputs)
    if existing["bytes"] + new_bytes > MAX_BYTES or existing["files"] + len(external_inputs) > MAX_FILES:
        raise BundleError("captured evidence would exceed bundle file or byte limit")
    created_files = []
    created_directories = []
    replaced_index = False
    try:
        raw = []
        bucket = root / "raw" / hashlib.sha256(record_id.encode("utf-8")).hexdigest()[:16]
        for number, item in enumerate(inputs):
            try:
                relative = item.relative_to(root)
            except ValueError:
                relative = None
            if relative is None:
                name = _safe_relative(f"raw/{bucket.name}/{number}-{item.name}").as_posix()
                target = root / _safe_relative(name)
                if target.exists():
                    raise BundleError(f"raw destination already exists: {name}")
                if not bucket.parent.exists():
                    bucket.parent.mkdir()
                    created_directories.append(bucket.parent)
                if not bucket.exists():
                    bucket.mkdir()
                    created_directories.append(bucket)
                source_hash = _digest(item)
                with item.open("rb") as reader, target.open("xb") as writer:
                    created_files.append(target)
                    shutil.copyfileobj(reader, writer)
                digest = _digest(target)
                if digest != source_hash or _digest(item) != source_hash:
                    raise BundleError(f"raw source changed while capturing: {item}")
            else:
                name = _safe_relative(relative.as_posix()).as_posix()
                digest = _digest(item)
            raw.append({"path": name, "sha256": digest})
        document.setdefault("evidence", []).append({
            "id": record_id, "source": source, "method": method, "raw": raw,
        })
        fd, temporary = tempfile.mkstemp(prefix=".rore-index-", dir=root)
        os.close(fd)
        temporary_path = Path(temporary)
        try:
            temporary_path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            os.replace(temporary_path, index)
            replaced_index = True
        finally:
            if temporary_path.exists():
                temporary_path.unlink()
        info = validate(root)
        return {"bundle": str(root), "evidence_id": record_id, "raw": raw, **info}
    except Exception:
        if replaced_index:
            fd, temporary = tempfile.mkstemp(prefix=".rore-restore-", dir=root)
            with os.fdopen(fd, "wb") as writer:
                writer.write(original_index)
            os.replace(temporary, index)
        for item in reversed(created_files):
            item.unlink(missing_ok=True)
        for directory in reversed(created_directories):
            directory.rmdir()
        raise


def validate(root: str | Path) -> dict:
    """Check structure, references, retained raw bytes, and archive boundaries."""
    if Path(root).is_symlink():
        raise BundleError("bundle root must not be a symlink")
    root = Path(root).resolve()
    files = dict(_files(root))
    if INDEX not in files:
        raise BundleError(f"missing {INDEX}")
    if files[INDEX].stat().st_size > MAX_INDEX_BYTES:
        raise BundleError(f"{INDEX} exceeds index size limit")
    try:
        document = json.loads(files[INDEX].read_text(encoding="utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise BundleError(f"invalid {INDEX}: {exc}") from exc
    if not isinstance(document, dict) or document.get("format") != FORMAT or document.get("version") != VERSION:
        raise BundleError("unsupported bundle format or version")
    target = document.get("target")
    if not isinstance(target, dict) or not isinstance(target.get("identity"), str) or not target["identity"].strip():
        raise BundleError("target.identity must identify the reference")
    all_ids: dict[str, str] = {}
    counts: dict[str, int] = {}
    for kind in KINDS:
        rows = _records(document, kind)
        counts[kind] = len(rows)
        for row in rows:
            ident = row.get("id")
            if not isinstance(ident, str) or not ident.strip() or ident in all_ids:
                raise BundleError(f"missing or duplicate record id: {ident!r}")
            all_ids[ident] = kind
    for row in _records(document, "evidence"):
        if not isinstance(row.get("source"), (str, dict)) or not row.get("source"):
            raise BundleError(f"{row['id']}: source is required")
        if not isinstance(row.get("method"), str) or not row["method"].strip():
            raise BundleError(f"{row['id']}: method is required")
        raw = row.get("raw")
        if not isinstance(raw, list) or not raw:
            raise BundleError(f"{row['id']}: raw must list retained material or an access limit")
        for item in raw:
            if not isinstance(item, dict):
                raise BundleError(f"{row['id']}: raw item must be an object")
            if "path" in item:
                name = _safe_relative(item["path"]).as_posix()
                if name not in files:
                    raise BundleError(f"{row['id']}: missing raw file {name}")
                claimed = item.get("sha256")
                if not isinstance(claimed, str) or len(claimed) != 64 or claimed.lower() != _digest(files[name]):
                    raise BundleError(f"{row['id']}: raw hash mismatch for {name}")
            elif item.get("access") not in ("restricted", "unavailable") or not isinstance(item.get("reason"), str) or not item["reason"].strip():
                raise BundleError(f"{row['id']}: raw item needs path+sha256 or access+reason")
    links = {"evidence_ids": "evidence", "finding_ids": "findings", "path_ids": "paths", "model_ids": "models", "unknown_ids": "unknowns"}
    for kind in KINDS:
        for row in _records(document, kind):
            for field, expected in links.items():
                if field not in row:
                    continue
                refs = row[field]
                if not isinstance(refs, list) or any(not isinstance(x, str) or all_ids.get(x) != expected for x in refs):
                    raise BundleError(f"{row['id']}: invalid {field}")
    return {"format": FORMAT, "version": VERSION, "target": target, "counts": counts,
            "files": len(files), "bytes": sum(p.stat().st_size for p in files.values())}


def inspect(root: str | Path, record_id: str) -> dict:
    validate(root)
    document = json.loads((Path(root) / INDEX).read_text(encoding="utf-8"))
    for kind in KINDS:
        for row in _records(document, kind):
            if row["id"] == record_id:
                return {"kind": kind, "record": row}
    raise BundleError(f"record not found: {record_id}")


def compare(left: str | Path, right: str | Path) -> dict:
    left_info, right_info = validate(left), validate(right)
    left_files = {name: _digest(path) for name, path in _files(Path(left))}
    right_files = {name: _digest(path) for name, path in _files(Path(right))}
    left_doc = json.loads((Path(left) / INDEX).read_text(encoding="utf-8"))
    right_doc = json.loads((Path(right) / INDEX).read_text(encoding="utf-8"))
    ids = lambda doc: {row["id"] for kind in KINDS for row in _records(doc, kind)}
    return {"same_target": left_info["target"] == right_info["target"],
            "only_left_files": sorted(left_files.keys() - right_files.keys()),
            "only_right_files": sorted(right_files.keys() - left_files.keys()),
            "changed_files": sorted(name for name in left_files.keys() & right_files.keys() if left_files[name] != right_files[name]),
            "only_left_ids": sorted(ids(left_doc) - ids(right_doc)),
            "only_right_ids": sorted(ids(right_doc) - ids(left_doc))}


def export_bundle(root: str | Path, output: str | Path) -> dict:
    info = validate(root)
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents or output.exists():
        raise BundleError("output must be a new file outside the bundle")
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".rore-", suffix=".zip", dir=output.parent)
    os.close(fd)
    try:
        expected = {name: _digest(path) for name, path in _files(root)}
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_STORED) as archive:
            for name, path in _files(root):
                archive.write(path, arcname=name)
        with zipfile.ZipFile(temporary) as archive:
            for name, digest in expected.items():
                sha = hashlib.sha256()
                with archive.open(name) as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        sha.update(chunk)
                if sha.hexdigest() != digest:
                    raise BundleError(f"source changed during export: {name}")
        try:
            os.link(temporary, output)
        except FileExistsError as exc:
            raise BundleError("output already exists") from exc
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return {"output": str(output), **info}


def import_bundle(source: str | Path, destination: str | Path) -> dict:
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if destination.exists():
        raise BundleError("destination already exists")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".rore-import-", dir=destination.parent))
    try:
        try:
            with zipfile.ZipFile(source) as archive:
                members = archive.infolist()
                if len(members) > MAX_FILES or sum(m.file_size for m in members) > MAX_BYTES:
                    raise BundleError("archive exceeds file or byte limit")
                seen: set[str] = set()
                for member in members:
                    if member.is_dir():
                        continue
                    name = _safe_relative(member.filename).as_posix()
                    if name in seen or stat.S_ISLNK(member.external_attr >> 16):
                        raise BundleError(f"duplicate or symlink archive member: {name}")
                    seen.add(name)
                    target = temporary / _safe_relative(name)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with archive.open(member) as input_stream, target.open("xb") as output_stream:
                        shutil.copyfileobj(input_stream, output_stream)
                    if target.stat().st_size != member.file_size:
                        raise BundleError(f"incomplete archive member: {name}")
        except (OSError, zipfile.BadZipFile) as exc:
            raise BundleError(f"archive read failed: {exc}") from exc
        info = validate(temporary)
        temporary.rename(destination)
        return {"destination": str(destination), **info}
    finally:
        if temporary.exists():
            if temporary.resolve().parent != destination.parent:
                raise BundleError("import cleanup path escaped destination parent")
            shutil.rmtree(temporary)
