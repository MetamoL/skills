# Installs the skills in this repo for Claude Code and/or Codex.
# Safe to re-run (overwrites with the repo versions).
# NOTE: agent definitions under agents/ are NOT installed by this script on purpose.
# They use common names and could overwrite agents you already have. Review them
# and copy manually if you want them.
param(
    [ValidateSet('claude', 'codex', 'both')]
    [string]$Target = 'claude'
)

$ErrorActionPreference = 'Stop'

$userProfileDir = [Environment]::GetFolderPath('UserProfile')
$skillRoots = switch ($Target) {
    'claude' { @('.claude\skills') }
    'codex' { @('.agents\skills') }
    'both' { @('.claude\skills', '.agents\skills') }
}

foreach ($skillRoot in $skillRoots) {
    $dst = Join-Path $userProfileDir $skillRoot
    New-Item -ItemType Directory -Force -Path $dst | Out-Null
    Get-ChildItem -Path (Join-Path $PSScriptRoot 'skills') -Directory | ForEach-Object {
        $dest = Join-Path $dst $_.Name
        New-Item -ItemType Directory -Force -Path $dest | Out-Null
        Copy-Item -Path (Join-Path $_.FullName '*') -Destination $dest -Recurse -Force
        "installed skill: $($_.Name) -> $dst"
    }
}
"note: agents/ was not installed (optional parts; copy manually if needed)"
