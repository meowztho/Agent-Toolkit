# Inert provider seeds from tool-master

Use this only after `CAPABILITY_FIRST_TOOLING.md` identifies an unresolved capability. The audited `tool-master.zip` snapshot contains 22 YAML catalog files with 90 standalone entries and 184 overlays, plus Python-defined tools. The entries below are **leads**; this file contains no install or run recipes. Confirm the actual build, host, exact format, output, authorization and side effects before use. The source catalog mixes static inspection, target execution, network capture, mutating utilities and security workflows; its tags and example commands alone are not a RORE capability proof.

| Evidence need | Candidate leads from the supplied catalog | Boundary and effect to verify |
| --- | --- | --- |
| Native headers, symbols, strings, bytes | binutils, Ghidra, radare2 | File format, architecture, parser result and file/virtual mapping; static import can create analysis files. `file` is a separate utility, not supplied by binutils. |
| Native runtime causality | GDB, Frida | Starts or attaches to a process; record baseline, debugger/hook effects, live module/build and restoration. |
| Android package/code/resources | Jadx, Androguard, apktool | Decompiled source is derived; distinguish manifest/resources/dex/sidecars. apktool can also rebuild, which writes a new artifact. |
| Mobile runtime/state | adb, Frida, Objection, MobSF | Device/emulator identity and permissions, process hooks, network/service effects and cleanup; static scans do not prove exercised behavior. |
| Packets and protocol flow | Wireshark/tshark | Offline pcap reading differs from privileged live capture; keep raw packets, capture scope and decoder version. |
| Offline memory image | Volatility 3, bulk_extractor | Image provenance and OS/profile fit; extracted strings/features are candidates, not complete process semantics. |
| Firmware/nested resources | Binwalk, Foremost, bulk_extractor | Extraction writes many child files; keep parent ranges, nested lineage, unsupported members and output limits. |
| Asset metadata | ExifTool | Read mode can inspect metadata; write/strip modes alter the file. Metadata presence does not prove runtime use. |
| Suspected hidden image data | zsteg and similar steganography readers | Use only for a material asset hypothesis; output is a candidate decode until format and reference use are corroborated. |

Do not absorb the full security catalog, installer, interactive menu or prebuilt attack pipelines into RORE. Tool candidates remain inert; no example command is an authorization grant. If the exact tool is unavailable, seek another provider for the same evidence boundary. Store any selected provider's real identity, settings, output and limitations in the investigation Evidence record.
