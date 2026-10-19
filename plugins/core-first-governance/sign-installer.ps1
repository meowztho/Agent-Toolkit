param(
    [Parameter(Mandatory = $true)]
    [string]$Thumbprint
)

$ErrorActionPreference = 'Stop'
$Target = Join-Path $PSScriptRoot 'install-personal-windows.ps1'

if (-not (Test-Path $Target)) {
    throw "Installer not found: $Target"
}

$NormalizedThumbprint = ($Thumbprint -replace '\\s', '').ToUpperInvariant()
$Certificate = Get-ChildItem -Path 'Cert:\\CurrentUser\\My' |
    Where-Object { $_.Thumbprint -eq $NormalizedThumbprint } |
    Select-Object -First 1

if ($null -eq $Certificate) {
    throw "Certificate not found in Cert:\\CurrentUser\\My: $Thumbprint"
}
if (-not $Certificate.HasPrivateKey) {
    throw "Certificate has no private key: $Thumbprint"
}

$Signature = Set-AuthenticodeSignature -FilePath $Target -Certificate $Certificate -HashAlgorithm SHA256
if ($null -eq $Signature.SignerCertificate -or $Signature.SignerCertificate.Thumbprint -ne $Certificate.Thumbprint) {
    throw "Authenticode signing did not attach the requested certificate. Status: $($Signature.Status)"
}

Write-Host "Signed:      $Target"
Write-Host "Thumbprint:  $($Certificate.Thumbprint)"
Write-Host "Status:      $($Signature.Status)"
