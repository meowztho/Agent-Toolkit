$ErrorActionPreference = 'Stop'

$PluginName = 'core-first-governance'
$Source = Join-Path $PSScriptRoot $PluginName
$PluginParent = Join-Path $HOME '.codex\plugins'
$Destination = Join-Path $PluginParent $PluginName
$MarketplacePath = Join-Path $HOME '.agents\plugins\marketplace.json'

if (-not (Test-Path (Join-Path $Source '.codex-plugin\plugin.json'))) {
    throw "Plugin source not found at $Source"
}

New-Item -ItemType Directory -Force -Path $PluginParent | Out-Null
if (Test-Path $Destination) {
    Remove-Item -Recurse -Force $Destination
}
Copy-Item -Recurse -Force $Source $Destination

$MarketplaceDir = Split-Path -Parent $MarketplacePath
New-Item -ItemType Directory -Force -Path $MarketplaceDir | Out-Null

if (Test-Path $MarketplacePath) {
    $Marketplace = Get-Content -Raw -Path $MarketplacePath | ConvertFrom-Json
    if ($null -eq $Marketplace.name -or [string]::IsNullOrWhiteSpace([string]$Marketplace.name)) {
        throw "Existing marketplace.json has no valid top-level name: $MarketplacePath"
    }
    if ($null -eq $Marketplace.plugins) {
        $Marketplace | Add-Member -NotePropertyName plugins -NotePropertyValue @()
    }
    if ($null -eq $Marketplace.interface) {
        $Marketplace | Add-Member -NotePropertyName interface -NotePropertyValue ([pscustomobject]@{ displayName = 'Personal' })
    }
} else {
    $Marketplace = [pscustomobject]@{
        name = 'personal'
        interface = [pscustomobject]@{ displayName = 'Personal' }
        plugins = @()
    }
}

$Entry = [pscustomobject]@{
    name = $PluginName
    source = [pscustomobject]@{
        source = 'local'
        path = "./.codex/plugins/$PluginName"
    }
    policy = [pscustomobject]@{
        installation = 'AVAILABLE'
        authentication = 'ON_INSTALL'
    }
    category = 'Productivity'
}

$OtherEntries = @($Marketplace.plugins | Where-Object { $_.name -ne $PluginName })
$Marketplace.plugins = @($OtherEntries + $Entry)
$json = $Marketplace | ConvertTo-Json -Depth 20
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($MarketplacePath, $json + [Environment]::NewLine, $utf8NoBom)

Write-Host "Plugin source installed: $Destination"
Write-Host "Marketplace updated:      $MarketplacePath"
Write-Host "Marketplace name:         $($Marketplace.name)"
Write-Host ""
Write-Host "Next steps (no Codex CLI required):"
Write-Host "  1. Fully quit and restart the ChatGPT desktop app."
Write-Host "  2. Open the Plugins Directory."
Write-Host "  3. Select marketplace/source: $($Marketplace.interface.displayName)."
Write-Host "  4. Find '$PluginName' and click Install."
Write-Host "  5. Start a NEW Codex thread for testing."
