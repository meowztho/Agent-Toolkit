"""On-demand, user-scoped provisioning for RORE's tested Windows Ghidra provider."""

from __future__ import annotations

import hashlib
import os
import platform
import shutil
import stat
import sys
import urllib.request
import uuid
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path

from .ghidra_adapter import GhidraError, probe


class SetupError(ValueError):
    """A provider cannot be installed or qualified at the requested boundary."""


@dataclass(frozen=True)
class Archive:
    name: str
    url: str
    sha256: str
    size: int
    directory: str


# Exact upstream release artifacts qualified on Windows x64. Bump only after a
# new release, its checksum, extraction structure and adapter smoke are checked.
GHIDRA = Archive(
    "ghidra_12.1.4_PUBLIC_20260921.zip",
    "https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.1.4_build/ghidra_12.1.4_PUBLIC_20260921.zip",
    "ddac49f903da9d5bac833e5cc79395098b9c33cfd3279be5f31bd00387d2d4db",
    569649598,
    "ghidra_12.1.4_PUBLIC",
)
JDK = Archive(
    "OpenJDK25U-jdk_x64_windows_hotspot_25.0.4.1_1.zip",
    "https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25.0.4.1%2B1/OpenJDK25U-jdk_x64_windows_hotspot_25.0.4.1_1.zip",
    "00c847d804f4a78e9f04f2683faf14fed898535b177b7fc704486cb0284e9283",
    141167264,
    "jdk-25.0.4.1+1",
)
ARCHIVES = (GHIDRA, JDK)
MAX_UNPACKED_BYTES = 4 * 1024**3
MAX_MEMBERS = 100_000


def default_root() -> Path:
    if os.name == "nt":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
        return base / "RORE" / "providers"
    return Path.home() / ".local" / "share" / "rore" / "providers"


def _root(path: str | Path | None) -> Path:
    return Path(path or default_root()).expanduser().resolve(strict=False)


def _io_path(path: Path) -> Path:
    """Use Windows extended paths for deeply nested upstream archive members."""
    if os.name != "nt":
        return path
    absolute = str(path.absolute())
    if absolute.startswith("\\\\?\\"):
        return Path(absolute)
    if absolute.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + absolute[2:])
    return Path("\\\\?\\" + absolute)


def windows_x64() -> bool:
    return os.name == "nt" and platform.machine().lower() in {"amd64", "x86_64"}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _archive_status(path: Path, artifact: Archive) -> dict:
    if not path.is_file():
        return {"status": "missing", "path": str(path)}
    actual_size = path.stat().st_size
    actual_hash = _sha256(path)
    return {"status": "verified" if actual_size == artifact.size and actual_hash == artifact.sha256 else "mismatch",
            "path": str(path), "size": actual_size, "sha256": actual_hash}


def plan(root: str | Path | None = None, archives: str | Path | None = None) -> dict:
    destination = _root(root)
    source_dir = Path(archives).expanduser().resolve(strict=True) if archives else destination / "downloads"
    return {
        "schema_version": 1,
        "platform": {"system": platform.system(), "machine": platform.machine(),
                     "automatic_install_supported": windows_x64()},
        "root": str(destination), "archive_source": str(source_dir),
        "artifacts": [{**asdict(item), "archive_status": _archive_status(source_dir / item.name, item),
                       "installed_directory_exists": (destination / item.directory).exists()}
                      for item in ARCHIVES],
        "effects": ["download two pinned HTTPS ZIPs unless verified local archives are supplied",
                    "create versioned directories under root only", "retain ZIPs and extracted provider",
                    "execute installed java -version to qualify the JDK",
                    "do not modify PATH, registry, system JDK, plugin files or target programs"],
        "status": "ready_for_explicit_install" if windows_x64() else "manual_platform_route_required",
    }


def _download_verified(item: Archive, destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if _archive_status(destination, item)["status"] != "verified":
            raise SetupError(f"existing archive has wrong size or SHA-256: {destination}")
        return destination
    temporary = destination.parent / f".{item.name}.{uuid.uuid4().hex}.part"
    request = urllib.request.Request(item.url, headers={"User-Agent": "RORE-provider-setup/1"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, temporary.open("xb") as output:
            length = response.headers.get("Content-Length")
            if length is not None and int(length) > item.size:
                raise SetupError(f"download exceeds pinned size: {item.name}")
            count = 0
            while chunk := response.read(1024 * 1024):
                count += len(chunk)
                if count > item.size:
                    raise SetupError(f"download exceeds pinned size: {item.name}")
                output.write(chunk)
        if _archive_status(temporary, item)["status"] != "verified":
            raise SetupError(f"download size or SHA-256 mismatch: {item.name}")
        temporary.rename(destination)
        return destination
    finally:
        if temporary.exists():
            temporary.unlink()


def _verified_archive(item: Archive, source_dir: Path | None, root: Path) -> Path:
    path = source_dir / item.name if source_dir else root / "downloads" / item.name
    if source_dir:
        if _archive_status(path, item)["status"] != "verified":
            raise SetupError(f"supplied archive is missing or does not match pinned size/SHA-256: {path}")
        return path
    return _download_verified(item, path)


def _members(archive: zipfile.ZipFile, item: Archive) -> list[tuple[zipfile.ZipInfo, tuple[str, ...]]]:
    members = archive.infolist()
    if len(members) > MAX_MEMBERS or sum(info.file_size for info in members) > MAX_UNPACKED_BYTES:
        raise SetupError(f"archive exceeds extraction bounds: {item.name}")
    normalized = []
    seen = set()
    for info in members:
        raw = info.filename
        if not raw or "\\" in raw or raw.startswith("/") or "\x00" in raw:
            raise SetupError(f"unsafe archive member: {raw!r}")
        parts = tuple(raw.rstrip("/").split("/"))
        if (parts[0] != item.directory or any(part in {"", ".", ".."} or ":" in part for part in parts)):
            raise SetupError(f"unsafe archive member: {raw!r}")
        mode = info.external_attr >> 16
        kind = stat.S_IFMT(mode)
        if stat.S_ISLNK(mode) or kind not in {0, stat.S_IFREG, stat.S_IFDIR}:
            raise SetupError(f"non-regular archive member: {raw!r}")
        key = "/".join(parts).casefold()
        if key in seen:
            raise SetupError(f"duplicate archive member: {raw!r}")
        seen.add(key)
        normalized.append((info, parts))
    return normalized


def _extract_verified(path: Path, item: Archive, root: Path) -> Path:
    final = root / item.directory
    if final.exists():
        raise SetupError(f"provider directory already exists; refusing to overwrite: {final}")
    stage = root / f".stage-{item.directory}-{uuid.uuid4().hex}"
    stage.mkdir(exist_ok=False)
    try:
        with zipfile.ZipFile(path) as archive:
            members = _members(archive, item)
            required = sum(info.file_size for info, _ in members)
            if shutil.disk_usage(root).free < required:
                raise SetupError(f"insufficient free space to extract {item.name}")
            for info, parts in members:
                target = _io_path(stage.joinpath(*parts))
                if info.is_dir():
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with archive.open(info) as source, target.open("xb") as output:
                        shutil.copyfileobj(source, output, length=1024 * 1024)
        extracted = _io_path(stage / item.directory)
        expected = ("support/analyzeHeadless.bat", "Ghidra/application.properties") if item is GHIDRA else ("bin/java.exe",)
        if not all((extracted / relative).is_file() for relative in expected):
            raise SetupError(f"expected provider components missing after extraction: {item.name}")
        if not (stage / item.directory).resolve().is_relative_to(root.resolve()) or not final.resolve().is_relative_to(root.resolve()):
            raise SetupError("provider destination escaped the selected root")
        extracted.rename(_io_path(final))
        stage.rmdir()
        return final
    except Exception:
        # Preserve a partial stage for diagnosis; never remove a recursive tree implicitly.
        raise


def install_ghidra(root: str | Path | None = None, archives: str | Path | None = None) -> dict:
    if not windows_x64():
        raise SetupError("automatic installation is qualified only for Windows x64; use the manual route")
    destination = _root(root)
    destination.mkdir(parents=True, exist_ok=True)
    source_dir = Path(archives).expanduser().resolve(strict=True) if archives else None
    installed = []
    for item in ARCHIVES:
        target = destination / item.directory
        if target.exists():
            if not target.is_dir():
                raise SetupError(f"provider destination is not a directory: {target}")
            installed.append({"provider": item.directory, "status": "existing_directory_not_archive_attested"})
            continue
        source = _verified_archive(item, source_dir, destination)
        _extract_verified(source, item, destination)
        installed.append({"provider": item.directory, "status": "installed_from_verified_archive",
                          "archive": str(source), "sha256": item.sha256})
    try:
        qualified = probe(destination / GHIDRA.directory, destination / JDK.directory)
    except (GhidraError, OSError, ValueError) as exc:
        raise SetupError(f"installed components did not qualify: {exc}") from exc
    return {"schema_version": 1, "status": "components-qualified-not-target-tested",
            "root": str(destination), "actions": installed, "provider": qualified}


def doctor(root: str | Path | None = None) -> dict:
    destination = _root(root)
    result = {"schema_version": 1, "platform": platform.platform(), "python": sys.version.split()[0],
              "uv": shutil.which("uv"), "root": str(destination),
              "path_candidates": {name: shutil.which(name) for name in
                                  ("java", "ghidra", "jadx", "radare2", "gdb", "adb", "tshark", "binwalk", "frida")}}
    if (destination / GHIDRA.directory).is_dir() and (destination / JDK.directory).is_dir():
        try:
            result["ghidra"] = probe(destination / GHIDRA.directory, destination / JDK.directory)
        except (GhidraError, OSError, ValueError) as exc:
            result["ghidra"] = {"status": "present-but-unqualified", "error": str(exc)}
    else:
        result["ghidra"] = {"status": "not-installed-in-selected-root"}
    result["status"] = "inspection-only"
    return result
