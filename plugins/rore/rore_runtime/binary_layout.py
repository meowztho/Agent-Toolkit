"""Conservative PE/ELF file-layout observations and file-offset candidates.

Addresses here are declared image/link-time values, never live process VAs.
"""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

from .artifact_tools import ArtifactError, PROVIDER, _with_file

MAX_HEADERS = 4096
MAX_REPORTED_OVERLAPS = 128


def _integer(data: bytes, start: int, width: int, order: str = "little") -> int:
    if start + width > len(data):
        raise ArtifactError("truncated binary header")
    return int.from_bytes(data[start:start + width], order)


def _pe(stream: BinaryIO, size: int) -> dict:
    if size < 64:
        raise ArtifactError("truncated MZ header")
    stream.seek(0x3c)
    pe_at = int.from_bytes(stream.read(4), "little")
    if pe_at > size - 24:
        raise ArtifactError("PE header offset exceeds file")
    stream.seek(pe_at)
    coff = stream.read(24)
    if len(coff) != 24 or coff[:4] != b"PE\0\0":
        raise ArtifactError("MZ file has no PE signature at declared offset")
    sections_count = _integer(coff, 6, 2)
    optional_size = _integer(coff, 20, 2)
    if sections_count > MAX_HEADERS or pe_at + 24 + optional_size + sections_count * 40 > size:
        raise ArtifactError("PE optional header or section table is incomplete or exceeds limit")
    optional = stream.read(optional_size)
    if len(optional) != optional_size:
        raise ArtifactError("truncated PE optional header")
    magic = _integer(optional, 0, 2) if optional_size >= 2 else None
    image_base = None
    if magic == 0x10B and optional_size >= 64:
        image_base = _integer(optional, 28, 4)
    elif magic == 0x20B and optional_size >= 64:
        image_base = _integer(optional, 24, 8)
    size_headers = _integer(optional, 60, 4) if optional_size >= 64 else None
    sections = []
    for index in range(sections_count):
        item = stream.read(40)
        if len(item) != 40:
            raise ArtifactError("truncated PE section table")
        name = item[:8].split(b"\0", 1)[0].decode("ascii", errors="replace")
        virtual_size, rva, raw_size, raw_offset = (_integer(item, at, 4) for at in (8, 12, 16, 20))
        sections.append({"index": index, "name": name,
                         "file_offset": raw_offset, "file_size": raw_size,
                         "rva": rva, "virtual_size": virtual_size,
                         "raw_range_backed": raw_offset + raw_size <= size})
    raw_sections = sorted((item for item in sections if item["file_size"]),
                          key=lambda item: item["file_offset"])
    overlaps = []
    overlap_truncated = False
    for left_at, left in enumerate(raw_sections):
        for right in raw_sections[left_at + 1:]:
            start = right["file_offset"]
            end = min(left["file_offset"] + left["file_size"],
                      right["file_offset"] + right["file_size"])
            if start >= left["file_offset"] + left["file_size"]:
                break
            if start < end:
                if len(overlaps) == MAX_REPORTED_OVERLAPS:
                    overlap_truncated = True
                    break
                overlaps.append({"section_indices": [left["index"], right["index"]],
                                 "file_offset_start": start,
                                 "file_offset_end_exclusive": end})
        if overlap_truncated:
            break
    diagnostics = {
        "overlapping_raw_ranges": overlaps,
        "overlaps_truncated": overlap_truncated,
        "zero_raw_sections": [item["index"] for item in sections if item["file_size"] == 0],
        "unbacked_raw_sections": [item["index"] for item in sections if not item["raw_range_backed"]],
        "limit": "declared section-header facts; zero raw size may be normal, and loader treatment is not inferred",
    }
    return {"format": "pe", "machine": f"0x{_integer(coff, 4, 2):04x}",
            "optional_magic": None if magic is None else f"0x{magic:04x}",
            "preferred_image_base": image_base, "size_of_headers": size_headers,
            "sections": sections, "raw_layout_diagnostics": diagnostics,
            "limit": "declared layout only; preferred image base is not a loaded runtime address"}


def _elf(stream: BinaryIO, size: int) -> dict:
    stream.seek(0)
    ident = stream.read(16)
    if len(ident) != 16 or ident[:4] != b"\x7fELF":
        raise ArtifactError("missing ELF signature")
    width, order_code = ident[4], ident[5]
    if width not in (1, 2) or order_code not in (1, 2):
        raise ArtifactError("unsupported ELF class or byte order")
    order = "little" if order_code == 1 else "big"
    header_size = 52 if width == 1 else 64
    if size < header_size:
        raise ArtifactError("truncated ELF header")
    stream.seek(0)
    header = stream.read(header_size)
    type_value = _integer(header, 16, 2, order)
    machine = _integer(header, 18, 2, order)
    phoff = _integer(header, 28 if width == 1 else 32, 4 if width == 1 else 8, order)
    phentsize = _integer(header, 42 if width == 1 else 54, 2, order)
    phnum = _integer(header, 44 if width == 1 else 56, 2, order)
    minimum_entry = 32 if width == 1 else 56
    if phnum == 0xffff:
        raise ArtifactError("extended ELF program-header count is not supported")
    if phnum > MAX_HEADERS or (phnum and (phentsize < minimum_entry or phoff + phentsize * phnum > size)):
        raise ArtifactError("ELF program header table is incomplete or exceeds limit")
    segments = []
    for index in range(phnum):
        stream.seek(phoff + index * phentsize)
        item = stream.read(minimum_entry)
        if len(item) != minimum_entry:
            raise ArtifactError("truncated ELF program header")
        if _integer(item, 0, 4, order) != 1:
            continue
        if width == 1:
            file_offset, virtual_address, file_size, memory_size = (
                _integer(item, at, 4, order) for at in (4, 8, 16, 20))
        else:
            file_offset, virtual_address, file_size, memory_size = (
                _integer(item, at, 8, order) for at in (8, 16, 32, 40))
        segments.append({"program_header_index": index, "file_offset": file_offset,
                         "file_size": file_size, "link_time_vaddr": virtual_address,
                         "memory_size": memory_size,
                         "raw_range_backed": file_offset + file_size <= size})
    return {"format": "elf", "class_bits": 32 if width == 1 else 64,
            "endianness": order, "type": f"0x{type_value:04x}",
            "machine": f"0x{machine:04x}", "program_headers": phnum,
            "load_segments": segments,
            "limit": "PT_LOAD file mapping only; runtime load base and memory-only bytes are not inferred"}


def _layout(stream: BinaryIO, identity: dict) -> dict:
    head = stream.read(4)
    if head[:2] == b"MZ":
        body = _pe(stream, identity["size"])
    elif head == b"\x7fELF":
        body = _elf(stream, identity["size"])
    else:
        raise ArtifactError("file is not a supported PE or ELF binary")
    return {"provider": PROVIDER, "source": identity, **body}


def inspect_binary_layout(path: str | Path) -> dict:
    return _with_file(path, _layout)


def map_file_offset(path: str | Path, offset: int) -> dict:
    if type(offset) is not int or offset < 0:
        raise ArtifactError("file offset must be a nonnegative integer")
    layout = inspect_binary_layout(path)
    size = layout["source"]["size"]
    if offset >= size:
        raise ArtifactError("file offset exceeds source")
    candidates = []
    if layout["format"] == "pe":
        if layout["size_of_headers"] is not None and offset < layout["size_of_headers"]:
            candidates.append({"region": "headers", "rva": offset,
                               "preferred_va": None if layout["preferred_image_base"] is None else layout["preferred_image_base"] + offset})
        for section in layout["sections"]:
            delta = offset - section["file_offset"]
            if section["file_size"] and 0 <= delta < section["file_size"] and section["raw_range_backed"]:
                rva = section["rva"] + delta
                candidates.append({"region": "section", "section_index": section["index"],
                                   "section_name": section["name"], "rva": rva,
                                   "within_declared_virtual_size": delta < section["virtual_size"],
                                   "preferred_va": None if layout["preferred_image_base"] is None else layout["preferred_image_base"] + rva})
    else:
        for segment in layout["load_segments"]:
            delta = offset - segment["file_offset"]
            if segment["file_size"] and 0 <= delta < segment["file_size"] and segment["raw_range_backed"]:
                candidates.append({"region": "PT_LOAD", "program_header_index": segment["program_header_index"],
                                   "link_time_vaddr": segment["link_time_vaddr"] + delta,
                                   "within_declared_memory_size": delta < segment["memory_size"]})
    return {"provider": PROVIDER, "source": layout["source"], "coordinate_space": "file-offset",
            "offset": offset, "candidates": candidates,
            "status": "unmapped" if not candidates else "ambiguous" if len(candidates) > 1 else "mapped",
            "limit": layout["limit"]}
