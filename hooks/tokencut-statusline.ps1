$claudeDir = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $HOME ".claude" }
$flag = Join-Path $claudeDir ".tokencut-active"

if (Test-Path $flag) {
    $mode = (Get-Content $flag -ErrorAction SilentlyContinue | Select-Object -First 1).Trim().ToLower()
    if ([string]::IsNullOrWhiteSpace($mode) -or $mode -eq "auto") {
        Write-Output "[TOKENCUT]"
    } else {
        Write-Output "[TOKENCUT:$($mode.ToUpper())]"
    }
}
