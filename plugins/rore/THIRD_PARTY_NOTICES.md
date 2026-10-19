# Third-party notices

RORE v0.15.0 adapts the optional PNG difference helper from MIT-licensed CoreReplica v0.4.0 (`corereplica-verify/scripts/imgdiff.py`), copyright (c) 2026 CoreReplica contributors. Its purpose and output are limited to locating candidate changes between reference captures; see `SOURCE_PROVENANCE.md` and `LICENSE-COREREPLICA`.

RORE evolves from CoreReplica and incorporates/adapts selected methodology and historical helper-code lineage from `Jakeschincariol/replica-skill`, copyright (c) 2026 Jake Schincariol, under the MIT License reproduced in `LICENSE-UPSTREAM`.

RORE also adapts selected reverse-engineering methodology from `zhaoxuya520/reverse-skill`, copyright (c) 2026 zhaoxuya520, under the MIT License reproduced in `LICENSE-REVERSE-SKILL`.

RORE v0.4.0 uses these sources for reverse-engineering methodology only; downstream clone/product ownership and offensive attack-chain goals are not part of RORE. See `SOURCE_PROVENANCE.md` for the detailed admission boundary.

RORE v0.4.3 also reviews the user-supplied MIT-licensed `tool-master.zip` (`Z4nzu/hackingtool`, copyright (c) 2020 Mr.Z4nzu) for tool-discovery methodology. No code, executable catalog entry or installer is incorporated; see `SOURCE_PROVENANCE.md`.

RORE v0.5.0 adapts selected reverse-engineering methodology from the user-supplied MIT-licensed `rea-main.zip` (`morluto/rea`, copyright (c) 2026 morluto). No REA code, executable runtime, tool catalog or bundled third-party engine is incorporated. The source license is reproduced in `LICENSE-REA`; see `SOURCE_PROVENANCE.md` for the admitted method and exclusion boundary.

RORE v0.8.0 reviewed the user-supplied Ghidra `12.3 DEV` source snapshot, whose root is Apache-2.0 licensed and which contains a separate GPL subtree. RORE incorporates no Ghidra code or executable; a conditional provider method is independently written from the reviewed documentation. See `SOURCE_PROVENANCE.md`.

RORE v0.9.0 adds its own optional adapter for a separately installed Ghidra distribution and compatible JDK. Neither external binary is bundled. Provider installation and distribution retain their own upstream licenses; see `SOURCE_PROVENANCE.md` and `docs/GHIDRA_PROVIDER_ADAPTER.md`.

RORE v0.10.0 adds a user-invoked installer for pinned official Ghidra and Eclipse Temurin release ZIPs on Windows x64. It downloads them only on request; their binaries and licenses remain external to this plugin ZIP. See `docs/PROVIDER_SETUP.md`.
