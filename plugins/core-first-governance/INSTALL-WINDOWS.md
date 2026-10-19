# Windows installation — Codex UI

This release targets the Codex UI / ChatGPT desktop plugin directory. No Codex CLI installation command is required.

## Install

From the extracted release directory:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\install-personal-windows.ps1
```

The installer copies the plugin source to:

```text
%USERPROFILE%\.codex\plugins\core-first-governance
```

and creates/updates the plugin entry in:

```text
%USERPROFILE%\.agents\plugins\marketplace.json
```

with source path:

```text
./.codex/plugins/core-first-governance
```

Then fully quit and restart the ChatGPT desktop app, open **Plugins Directory**, select the personal marketplace/source, install **Core-First Governance**, and start a **new Codex thread**.

v0.11.6 exposes the same five Skills and remains Skills-only. It preserves the complete v0.11.5 routing/architecture baseline and adds only freshness-sensitive oracle-liveness protection inside `observable-product-verification`. No model-specific rule, planning framework, approval framework, tracker, MCP server, or new Skill is added.

## Optional Authenticode signing

The distributed installer is unsigned because a valid publisher signature requires the publisher's private code-signing key.

If you own a suitable code-signing certificate in `Cert:\CurrentUser\My`:

```powershell
.\sign-installer.ps1 -Thumbprint <CERTIFICATE_THUMBPRINT>
```

Verify:

```powershell
Get-AuthenticodeSignature .\install-personal-windows.ps1 | Format-List
```
