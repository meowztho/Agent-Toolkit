# Agent Toolkit — Git upload package

This repository groups the current plugin sources and the manual agent workflow from the local workspace. Each plugin remains a standalone package; this repository is a distribution and development collection, not a runtime dependency between them.

## Contents

| Directory | Purpose |
| --- | --- |
| `plugins/core-first-governance/` | Core-First source repository; installable plugin is inside `core-first-governance/`. |
| `plugins/agent-project-compiler/` | APC source and JIT references. |
| `plugins/rore/` | RORE source, runtime, provider definitions, tests and attribution. |
| `plugins/agent-blueprint/` | Agent Blueprint plugin. |
| `plugins/runtime-debugger/` | Runtime Debugger plugin. |
| `plugins/gamedev-jit-skills/` | GameDev JIT plugin, extracted from its current package. |
| `plugins/codex-luna-orchestrator/` | Optional ChatGPT/CLI Luna orchestration plugin snapshot. |
| `workflow/agent-workflow/` | Manual role prompts and CHEATSHEET, including current workspace edits. |
| `knowledge/gamedev/` | Standalone GameDev handbook and system guidance. |

Read `COMPONENTS.md` for versions and source boundaries. `SOURCE_MANIFEST.json` records source revisions and file counts. `SHA256SUMS.txt` records file hashes. Follow each plugin's own README and license notices. No blanket license is asserted for the collection.

## Upload to a Git host

The extracted directory is already a Git repository on branch `main` with one initial snapshot commit. Create an empty repository on your Git host, then run from this directory:

```sh
git remote add origin <your-repository-url>
git push -u origin main
```

A `.bundle` sibling artifact can also be cloned or transported to another computer before pushing. Do not upload the source ZIP as a single file expecting the Git host to unpack it into a repository.

## Scope

Historical plugin ZIPs, RORE third-party source archives, analysis samples, local virtual environments, test runs and existing source-repository `.git` directories remain in the original workspace. The current tracked RORE source includes its provenance and license files. This upload package does not claim to vendor optional external analyzers.
