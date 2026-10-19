# On-demand provider setup

RORE is usable without an installed analyzer for its skills, Evidence bundle and standard-library artifact CLI. Its MCP servers use the locked Python environment and require `uv`. `scripts/rore_setup.py` is a standard-library setup CLI for on-demand provider acquisition when the investigation needs that capability; it is never run automatically when the plugin loads.

The packaged `rore-providers` MCP is RORE's own transport over that same installer and Ghidra adapter. Its read-only `rore_provider_doctor` and `rore_provider_plan_ghidra` tools inspect the environment. For a selected native-code question, call `rore_provider_start_ghidra_analysis` with the exact source file and a **new** output directory. On Windows x64 its `auto_install` default provisions the pinned Ghidra/JDK pair if absent, then analyzes a copy. For setup alone, call `rore_provider_start_ghidra_install`. Both actions return a job ID promptly; poll `rore_provider_job_status` for the outcome and retained result path. If a host stops the background worker before it writes a final result, status reports `interrupted`; inspect retained logs/output and start a new job after checking the partial state. No provider is installed merely by loading the plugin or listing MCP tools. The existing `rore-evidence` MCP remains read-only.

## Windows x64: tested Ghidra + JDK route

Use Python 3.10 or newer. The default provider location is `%LOCALAPPDATA%\RORE\providers`; `--root` selects another user-writable directory. Run:

```text
python scripts/rore_setup.py doctor
python scripts/rore_setup.py plan-ghidra --root PROVIDER_ROOT
python scripts/rore_setup.py install-ghidra --root PROVIDER_ROOT
```

For an offline or already downloaded installation, supply `--archives DIRECTORY` to `plan-ghidra` and `install-ghidra`. The directory must contain the exact release ZIP names and bytes listed by `plan-ghidra`; mismatched files fail without overwrite. The Windows recipe pins the official Ghidra 12.1.4 PUBLIC ZIP and Eclipse Temurin JDK 25.0.4.1+1 x64 ZIP with their SHA-256 values. It downloads only when `install-ghidra` is invoked for a needed capability, validates sizes/hashes, rejects traversal/symlink/duplicate archive members, extracts into versioned directories, retains the ZIPs, and runs Java's version check. It needs roughly 1.3 GiB for extracted files plus archive storage. It makes no system-wide PATH, registry or JDK change and does not execute a reference target.

Use the returned `provider.install` and `provider.jdk` paths with [the Ghidra analysis CLI](GHIDRA_PROVIDER_ADAPTER.md). `components-qualified-not-target-tested` means setup succeeded, not that a particular file format, loader or decompilation result works. Run a representative real analysis and inspect the import identity, loader, mapping, logs and selected output before a strong finding.

The provider MCP's `rore_provider_ghidra_page` reads a retained run summary (`section=run`), program metadata, inventory pages, or a selected function's instruction/reference pages. `rore_provider_decompilation_page` returns bounded slices of a selected function's pseudocode. Both verify retained hashes; pagination never implies a capped inventory is complete. Full input copies, Ghidra project, raw export, logs and pseudocode remain in the output directory. These tools require an agent host that can run this plugin's MCP configuration and access the same local paths. Installation, analysis and decompilation are qualified provider operations, not independent proof of reference behavior.

Existing versioned directories are left untouched and reported as `existing_directory_not_archive_attested`; a component probe cannot prove how their whole distributions were acquired. A failed extraction leaves a `.stage-*` directory for diagnosis rather than deleting user files. Inspect and remove such a directory deliberately if no longer needed. The installer does not upgrade or overwrite an existing provider.

## Other providers and hosts

Linux/macOS and Windows architectures other than x64 use the manual route in `skills/rore-reconstruction/references/PROVIDER_PROVISIONING.md`. The agent selects a provider only after identifying the required capability and checking what is already available. It verifies the current official distribution, platform support, license, exact package/version, checksum or signature, privileges and side effects, then installs and tests only the needed capability. RORE supplies provider-neutral methods and inert candidate leads; it does not bundle Ghidra, JDK, REA, tool-master or a universal binary/tool installer.
