"""RORE-owned, read-only artifact acquisition primitives.

These operations report source identity and exact coverage. They do not infer
runtime behavior, execute targets, extract archives, or replace source bytes.
"""

from __future__ import annotations

import hashlib
import os
import stat
import zipfile
import zlib
from pathlib import Path
from typing import BinaryIO, Callable, TypeVar

from .bundle import BundleError, _safe_relative

MAX_SOURCE_BYTES = 1024 * 1024 * 1024
MAX_WINDOW_BYTES = 4096
MAX_ZIP_MEMBERS = 100000
MAX_DIRECTORY_ENTRIES = 100000
MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_PAGE = 200
PROVIDER = {"id": "rore.stdlib-artifact", "implementation": "Python standard library", "effects": "read-only"}
_T = TypeVar("_T")


class ArtifactError(ValueError):
    """Source, operation, or resource bound prevents a reliable observation."""


def capabilities() -> dict:
    """Advertise only implemented RORE operations, not candidate providers."""
    return {"provider": PROVIDER, "operations": [
        {"name": "file-inspect", "boundary": "regular-file bytes and signature candidate", "effects": "read-only"},
        {"name": "file-bytes", "boundary": "bounded file-offset window with complete source hash", "effects": "read-only"},
        {"name": "zip-inventory", "boundary": "ZIP central-directory metadata page", "effects": "read-only"},
        {"name": "zip-member", "boundary": "bounded decoded member bytes with source/member hashes", "effects": "read-only"},
        {"name": "binary-layout", "boundary": "declared PE sections or ELF PT_LOAD segments", "effects": "read-only"},
        {"name": "map-file-offset", "boundary": "candidate PE RVA/preferred VA or ELF link-time address", "effects": "read-only"},
        {"name": "directory-inventory", "boundary": "paginated live directory metadata; no symlink traversal", "effects": "read-only"},
    ], "limits": {"source_bytes": MAX_SOURCE_BYTES, "window_bytes": MAX_WINDOW_BYTES,
                   "zip_members": MAX_ZIP_MEMBERS, "directory_entries": MAX_DIRECTORY_ENTRIES,
                   "decoded_member_bytes": MAX_MEMBER_BYTES,
                   "page_size": MAX_PAGE}}


def _identity_matches(left: os.stat_result, right: os.stat_result, *, same_channel: bool = True) -> bool:
    fields = ("st_dev", "st_ino", "st_size", "st_mtime_ns")
    if same_channel:
        fields += ("st_ctime_ns",)
    return all(getattr(left, field) == getattr(right, field) for field in fields)


def _with_file(path: str | Path, projector: Callable[[BinaryIO, dict], _T]) -> _T:
    source = Path(path)
    before = source.lstat()
    if not stat.S_ISREG(before.st_mode) or stat.S_ISLNK(before.st_mode):
        raise ArtifactError("source must be a regular file, not a symlink")
    if before.st_size > MAX_SOURCE_BYTES:
        raise ArtifactError(f"source exceeds {MAX_SOURCE_BYTES} byte limit")
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
    with os.fdopen(os.open(source, flags), "rb") as stream:
        opened = os.fstat(stream.fileno())
        if not stat.S_ISREG(opened.st_mode) or not _identity_matches(before, opened, same_channel=False):
            raise ArtifactError("source changed before opening")
        digest = hashlib.sha256()
        count = 0
        while chunk := stream.read(1024 * 1024):
            count += len(chunk)
            if count > MAX_SOURCE_BYTES:
                raise ArtifactError("source grew beyond byte limit")
            digest.update(chunk)
        if count != before.st_size:
            raise ArtifactError("source size changed during hashing")
        identity = {"path": str(source.resolve()), "sha256": digest.hexdigest(), "size": count}
        stream.seek(0)
        result = projector(stream, identity)
        stream.seek(0)
        verification = hashlib.sha256()
        verified_count = 0
        while chunk := stream.read(1024 * 1024):
            verified_count += len(chunk)
            if verified_count > MAX_SOURCE_BYTES:
                raise ArtifactError("source grew beyond byte limit during verification")
            verification.update(chunk)
        if verified_count != count or verification.digest() != digest.digest():
            raise ArtifactError("source bytes changed during inspection")
        after = os.fstat(stream.fileno())
        current = source.lstat()
        if not _identity_matches(opened, after) or not _identity_matches(before, current) or not _identity_matches(opened, current, same_channel=False):
            raise ArtifactError("source changed during inspection")
        return result


def _candidate_format(stream: BinaryIO, size: int) -> dict:
    head = stream.read(min(size, 64))
    candidate, basis = "unknown", "no recognized leading signature"
    signatures = (
        (b"\x7fELF", "elf"), (b"PK\x03\x04", "zip"),
        (b"PK\x05\x06", "zip"), (b"PK\x07\x08", "zip"),
        (b"\x89PNG\r\n\x1a\n", "png"), (b"GIF87a", "gif"),
        (b"GIF89a", "gif"), (b"\xff\xd8\xff", "jpeg"),
        (b"%PDF-", "pdf"), (b"SQLite format 3\x00", "sqlite"),
        (b"\x00asm", "wasm"), (b"\xfe\xed\xfa\xce", "mach-o"),
        (b"\xfe\xed\xfa\xcf", "mach-o"), (b"\xcf\xfa\xed\xfe", "mach-o"),
        (b"\xca\xfe\xba\xbe", "mach-o-fat"),
    )
    for magic, name in signatures:
        if head.startswith(magic):
            candidate, basis = name, f"leading bytes {magic.hex()}"
            break
    if head.startswith(b"MZ"):
        candidate, basis = "dos-mz", "leading bytes 4d5a"
        if size >= 64:
            offset = int.from_bytes(head[0x3c:0x40], "little")
            if offset <= size - 4:
                stream.seek(offset)
                if stream.read(4) == b"PE\x00\x00":
                    candidate, basis = "pe", f"MZ plus PE signature at file offset {offset}"
    return {"candidate": candidate, "basis": basis,
            "limit": "signature observation, not complete format validation"}


def inspect_file(path: str | Path) -> dict:
    def project(stream: BinaryIO, identity: dict) -> dict:
        return {"provider": PROVIDER, "source": identity,
                "format": _candidate_format(stream, identity["size"]),
                "coverage": "complete source hash; bounded signature inspection"}
    return _with_file(path, project)


def _window(start: int, length: int, size: int) -> None:
    if type(start) is not int or start < 0 or type(length) is not int or not 1 <= length <= MAX_WINDOW_BYTES:
        raise ArtifactError(f"offset must be nonnegative and length 1..{MAX_WINDOW_BYTES}")
    if start > size or length > size - start:
        raise ArtifactError("requested byte window exceeds source; no partial bytes returned")


def _byte_view(data: bytes) -> dict:
    return {"hex": data.hex(), "ascii": "".join(chr(byte) if 32 <= byte < 127 else "." for byte in data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_file_bytes(path: str | Path, offset: int, length: int) -> dict:
    def project(stream: BinaryIO, identity: dict) -> dict:
        _window(offset, length, identity["size"])
        stream.seek(offset)
        data = stream.read(length)
        if len(data) != length:
            raise ArtifactError("source changed while reading byte window")
        return {"provider": PROVIDER, "source": identity,
                "coordinate_space": "file-offset", "offset": offset, "length": length,
                "bytes": _byte_view(data),
                "mapping_limit": "no section, virtual-address or runtime-memory mapping inferred"}
    return _with_file(path, project)


def _zip_infos(stream: BinaryIO) -> zipfile.ZipFile:
    try:
        archive = zipfile.ZipFile(stream)
        if len(archive.infolist()) > MAX_ZIP_MEMBERS:
            archive.close()
            raise ArtifactError(f"ZIP exceeds {MAX_ZIP_MEMBERS} member limit")
        return archive
    except (zipfile.BadZipFile, zipfile.LargeZipFile) as exc:
        raise ArtifactError(f"invalid or unsupported ZIP: {exc}") from exc


def _member_metadata(index: int, info: zipfile.ZipInfo) -> dict:
    try:
        _safe_relative(info.filename.rstrip("/"))
        safe = True
    except BundleError:
        safe = False
    mode = info.external_attr >> 16
    return {"index": index, "name": info.filename, "directory": info.is_dir(),
            "symlink": stat.S_ISLNK(mode), "safe_relative_path": safe,
            "compressed_size": info.compress_size, "uncompressed_size": info.file_size,
            "compression_method": info.compress_type, "encrypted": bool(info.flag_bits & 1),
            "crc32_declared": f"{info.CRC:08x}"}


def inventory_zip(path: str | Path, offset: int = 0, limit: int = MAX_PAGE) -> dict:
    if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= MAX_PAGE:
        raise ArtifactError(f"offset must be nonnegative and limit 1..{MAX_PAGE}")
    def project(stream: BinaryIO, identity: dict) -> dict:
        with _zip_infos(stream) as archive:
            infos = archive.infolist()
            total = len(infos)
            if offset > total:
                raise ArtifactError("page offset exceeds ZIP member count")
            page = [_member_metadata(i, infos[i]) for i in range(offset, min(total, offset + limit))]
            return {"provider": PROVIDER, "source": identity, "total_members": total,
                    "offset": offset, "members": page,
                    "next_offset": offset + len(page) if offset + len(page) < total else None,
                    "coverage": "central-directory metadata page; payload CRC and content not verified"}
    return _with_file(path, project)


def read_zip_member(path: str | Path, index: int, offset: int, length: int) -> dict:
    if type(index) is not int or index < 0:
        raise ArtifactError("member index must be nonnegative")
    def project(stream: BinaryIO, identity: dict) -> dict:
        with _zip_infos(stream) as archive:
            infos = archive.infolist()
            if index >= len(infos):
                raise ArtifactError("member index exceeds ZIP member count")
            info = infos[index]
            metadata = _member_metadata(index, info)
            if metadata["directory"] or metadata["symlink"] or metadata["encrypted"]:
                raise ArtifactError("directory, symlink or encrypted member cannot be decoded here")
            if info.file_size > MAX_MEMBER_BYTES:
                raise ArtifactError(f"decoded member exceeds {MAX_MEMBER_BYTES} byte limit")
            _window(offset, length, info.file_size)
            digest = hashlib.sha256()
            position = 0
            selected = bytearray()
            try:
                with archive.open(info) as member:
                    while chunk := member.read(64 * 1024):
                        digest.update(chunk)
                        end = position + len(chunk)
                        if offset < end and position < offset + length:
                            selected.extend(chunk[max(0, offset - position):min(len(chunk), offset + length - position)])
                        position = end
                        if position > MAX_MEMBER_BYTES:
                            raise ArtifactError("decoded member grew beyond byte limit")
            except (OSError, RuntimeError, NotImplementedError, EOFError, zipfile.BadZipFile, zlib.error) as exc:
                raise ArtifactError(f"member decoding failed: {exc}") from exc
            if position != info.file_size or len(selected) != length:
                raise ArtifactError("decoded member size or requested window is incomplete")
            return {"provider": PROVIDER, "source": identity, "member": metadata,
                    "member_sha256": digest.hexdigest(), "coordinate_space": "decoded-member-file-offset",
                    "offset": offset, "length": length, "bytes": _byte_view(bytes(selected)),
                    "coverage": "complete decoded member hash and CRC-checked requested byte window",
                    "mapping_limit": "ZIP member offset is not an offset in the outer archive"}
    return _with_file(path, project)


def inventory_directory(path: str | Path, offset: int = 0, limit: int = MAX_PAGE) -> dict:
    """Enumerate a live tree once; page metadata without following reparse points."""
    if type(offset) is not int or offset < 0 or type(limit) is not int or not 1 <= limit <= MAX_PAGE:
        raise ArtifactError(f"offset must be nonnegative and limit 1..{MAX_PAGE}")
    root = Path(path)
    before = root.lstat()
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    if not stat.S_ISDIR(before.st_mode) or stat.S_ISLNK(before.st_mode) or bool(getattr(before, "st_file_attributes", 0) & reparse_flag):
        raise ArtifactError("source must be a real directory, not a symlink")
    entries: list[dict] = []
    errors: list[dict] = []
    pending = [root]
    while pending:
        parent = pending.pop()
        try:
            with os.scandir(parent) as iterator:
                children = []
                for child in iterator:
                    children.append(child)
                    if len(children) + len(entries) > MAX_DIRECTORY_ENTRIES:
                        raise ArtifactError(f"directory exceeds {MAX_DIRECTORY_ENTRIES} entry limit")
                children.sort(key=lambda entry: entry.name)
        except OSError as exc:
            errors.append({"path": parent.relative_to(root).as_posix(), "error": str(exc)})
            continue
        directories = []
        for child in children:
            relative = (parent / child.name).relative_to(root).as_posix()
            try:
                meta = child.stat(follow_symlinks=False)
            except OSError as exc:
                errors.append({"path": relative, "error": str(exc)})
                continue
            is_link = stat.S_ISLNK(meta.st_mode) or bool(getattr(meta, "st_file_attributes", 0) & reparse_flag)
            kind = "link" if is_link else "directory" if stat.S_ISDIR(meta.st_mode) else "file" if stat.S_ISREG(meta.st_mode) else "other"
            entries.append({"path": relative, "kind": kind, "size": meta.st_size,
                            "mtime_ns": meta.st_mtime_ns})
            if len(entries) > MAX_DIRECTORY_ENTRIES:
                raise ArtifactError(f"directory exceeds {MAX_DIRECTORY_ENTRIES} entry limit")
            if kind == "directory":
                directories.append(parent / child.name)
        pending.extend(reversed(directories))
    if offset > len(entries):
        raise ArtifactError("page offset exceeds directory entry count")
    after = root.lstat()
    return {"provider": PROVIDER, "root": str(root.resolve()), "total_entries": len(entries),
            "offset": offset, "entries": entries[offset:offset + limit],
            "next_offset": offset + limit if offset + limit < len(entries) else None,
            "errors": errors, "root_metadata_stable": _identity_matches(before, after),
            "coverage": "partial" if errors else "enumerated-once",
            "limit": "live directory traversal is not atomic; entries are metadata only, inspect files for byte identity"}
