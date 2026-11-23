[CmdletBinding()]
param(
    [Parameter()]
    [string]$OutputDirectory = (Join-Path (Get-Location) 'codex-windows-diagnostics'),

    [Parameter()]
    [switch]$IncludeNetworkChecks
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

function Protect-Text {
    param([AllowNull()][object]$Value)

    if ($null -eq $Value) { return $null }
    $text = [string]$Value

    if (-not [string]::IsNullOrWhiteSpace($env:USERPROFILE)) {
        $text = $text -replace [regex]::Escape($env:USERPROFILE), '%USERPROFILE%'
    }
    if (-not [string]::IsNullOrWhiteSpace($env:USERNAME)) {
        $text = $text -replace [regex]::Escape($env:USERNAME), '<user>'
    }
    if (-not [string]::IsNullOrWhiteSpace($env:COMPUTERNAME)) {
        $text = $text -replace [regex]::Escape($env:COMPUTERNAME), '<computer>'
    }

    $text = [regex]::Replace($text, '(?i)(https?://)[^/@\s]+:[^/@\s]+@', '$1<redacted>@')
    $text = [regex]::Replace($text, '(?i)\b(api[_-]?key|access[_-]?token|auth[_-]?token|password|secret)\b\s*[:=]\s*["'']?[^,\s;"'']+', '$1=<redacted>')
    $text = [regex]::Replace($text, '(?i)\b(sk-[A-Za-z0-9_-]{12,}|gh[pousr]_[A-Za-z0-9_]{12,}|github_pat_[A-Za-z0-9_]{12,}|xox[baprs]-[A-Za-z0-9-]{12,})\b', '<redacted-token>')

    if ($text.Length -gt 16000) {
        $text = $text.Substring(0, 16000) + "`n<truncated>"
    }
    return $text
}

function Get-PathKind {
    param([AllowNull()][string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) { return 'unknown' }
    if ($Path -match '^\\\\(?:wsl\$|wsl\.localhost)\\') { return 'wsl-unc' }
    if ($Path -match '^/mnt/[a-z]/') { return 'wsl-mounted-windows-drive' }
    if ($Path -match '^/') { return 'linux' }
    if ($Path -match '^[A-Za-z]:\\') { return 'windows-drive' }
    if ($Path -match '^\\\\') { return 'unc' }
    return 'relative-or-other'
}

function Get-AdministratorState {
    try {
        $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
        $principal = New-Object Security.Principal.WindowsPrincipal($identity)
        return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
    }
    catch {
        return $null
    }
}

function Get-CommandSummary {
    param([Parameter(Mandatory = $true)][string]$Name)

    try {
        $commands = @(Get-Command $Name -All -ErrorAction SilentlyContinue)
        if ($commands.Count -eq 0) {
            return [pscustomobject]@{
                name = $Name
                found = $false
                count = 0
                resolutions = @()
            }
        }

        $resolutions = foreach ($command in ($commands | Select-Object -First 4)) {
            $sourcePath = $null
            if ($command.PSObject.Properties.Name -contains 'Path') { $sourcePath = $command.Path }
            if ([string]::IsNullOrWhiteSpace([string]$sourcePath) -and ($command.PSObject.Properties.Name -contains 'Source')) {
                $sourcePath = $command.Source
            }
            $version = $null
            if ($command.PSObject.Properties.Name -contains 'Version' -and $null -ne $command.Version) {
                $version = $command.Version.ToString()
            }

            [pscustomobject]@{
                command_type = [string]$command.CommandType
                source = Protect-Text $sourcePath
                version = $version
            }
        }

        return [pscustomobject]@{
            name = $Name
            found = $true
            count = $commands.Count
            resolutions = @($resolutions)
        }
    }
    catch {
        return [pscustomobject]@{
            name = $Name
            found = $false
            count = 0
            resolutions = @()
            error = Protect-Text $_.Exception.Message
        }
    }
}

function Invoke-LimitedProcess {
    param(
        [Parameter(Mandatory = $true)][string]$FilePath,
        [Parameter(Mandatory = $true)][string]$Arguments,
        [int]$TimeoutMilliseconds = 5000
    )

    try {
        $startInfo = New-Object System.Diagnostics.ProcessStartInfo
        $startInfo.FileName = $FilePath
        $startInfo.Arguments = $Arguments
        $startInfo.UseShellExecute = $false
        $startInfo.RedirectStandardOutput = $true
        $startInfo.RedirectStandardError = $true
        $startInfo.CreateNoWindow = $true

        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $startInfo
        [void]$process.Start()

        if (-not $process.WaitForExit($TimeoutMilliseconds)) {
            try { $process.Kill() } catch { }
            return [pscustomobject]@{ success = $false; timed_out = $true; exit_code = $null; output = $null }
        }

        $stdout = $process.StandardOutput.ReadToEnd()
        $stderr = $process.StandardError.ReadToEnd()
        $combined = ($stdout + "`n" + $stderr).Trim()
        return [pscustomobject]@{
            success = ($process.ExitCode -eq 0)
            timed_out = $false
            exit_code = $process.ExitCode
            output = Protect-Text $combined
        }
    }
    catch {
        return [pscustomobject]@{
            success = $false
            timed_out = $false
            exit_code = $null
            output = $null
            error = Protect-Text $_.Exception.Message
        }
    }
}

function Test-TcpEndpoint {
    param(
        [Parameter(Mandatory = $true)][string]$HostName,
        [int]$Port = 443,
        [int]$TimeoutMilliseconds = 3000
    )

    $client = New-Object System.Net.Sockets.TcpClient
    try {
        $async = $client.BeginConnect($HostName, $Port, $null, $null)
        $connected = $async.AsyncWaitHandle.WaitOne($TimeoutMilliseconds, $false)
        if ($connected) {
            $client.EndConnect($async)
        }
        return [pscustomobject]@{ host = $HostName; port = $Port; reachable = $connected }
    }
    catch {
        return [pscustomobject]@{ host = $HostName; port = $Port; reachable = $false; error = Protect-Text $_.Exception.Message }
    }
    finally {
        $client.Close()
    }
}

function Get-FileMetadata {
    param([AllowNull()][string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path) -or -not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return [pscustomobject]@{ exists = $false; path = Protect-Text $Path }
    }

    try {
        $file = Get-Item -LiteralPath $Path -ErrorAction Stop
        return [pscustomobject]@{
            exists = $true
            path = Protect-Text $file.FullName
            size_bytes = $file.Length
            last_write_utc = $file.LastWriteTimeUtc.ToString('o')
        }
    }
    catch {
        return [pscustomobject]@{ exists = $true; path = Protect-Text $Path; error = Protect-Text $_.Exception.Message }
    }
}

function Get-SafeSetupError {
    param([Parameter(Mandatory = $true)][string]$SandboxDirectory)

    $path = Join-Path $SandboxDirectory 'setup_error.json'
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        return [pscustomobject]@{ exists = $false }
    }

    try {
        $data = Get-Content -LiteralPath $path -Raw -ErrorAction Stop | ConvertFrom-Json -ErrorAction Stop
        $code = $null
        $message = $null
        if ($data.PSObject.Properties.Name -contains 'code') { $code = Protect-Text $data.code }
        if ($data.PSObject.Properties.Name -contains 'message') { $message = Protect-Text $data.message }
        return [pscustomobject]@{
            exists = $true
            code = $code
            message = $message
            metadata = Get-FileMetadata $path
        }
    }
    catch {
        return [pscustomobject]@{ exists = $true; metadata = Get-FileMetadata $path; error = Protect-Text $_.Exception.Message }
    }
}

function Get-SandboxSignatureSummary {
    param([Parameter(Mandatory = $true)][string]$SandboxDirectory)

    $signaturePatterns = [ordered]@{
        helper_launch_failed = 'orchestrator_helper_launch_failed|setup refresh failed to launch helper|helper not found'
        create_process_logon = 'CreateProcessWithLogonW failed'
        create_process_user = 'CreateProcessAsUserW failed'
        elevation_required = 'ERROR_ELEVATION_REQUIRED|os error 740|requires elevation|requested operation requires elevation'
        access_denied = 'Access is denied|os error 5|SetNamedSecurityInfoW failed:\s*5'
        canceled = 'os error 1223|ShellExecuteExW failed to launch setup helper:\s*1223'
        logon_credential = 'error 1326|failed:\s*1326|error 1385|failed:\s*1385|error 1909|failed:\s*1909'
        powershell_host = '8009001d|internal Windows PowerShell error|PowerShell host error'
        wrong_workdir = 'workdir.*(?:invalid|incorrect|wrong|failed)|(?:invalid|incorrect|wrong|failed).*workdir|working directory.*(?:invalid|incorrect|wrong|failed)|junction.*(?:failed|error)'
        network = 'network.*failed|proxy.*failed|firewall.*failed|DNS.*failed'
    }

    if (-not (Test-Path -LiteralPath $SandboxDirectory -PathType Container)) {
        return [pscustomobject]@{ directory_exists = $false; scanned_files = @(); signatures = @() }
    }

    try {
        $files = @(Get-ChildItem -LiteralPath $SandboxDirectory -File -Filter '*.log' -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 5)
        $totals = @{}
        foreach ($name in $signaturePatterns.Keys) { $totals[$name] = 0 }

        foreach ($file in $files) {
            try {
                $tail = @(Get-Content -LiteralPath $file.FullName -Tail 3000 -ErrorAction Stop)
                $text = $tail -join "`n"
                foreach ($name in $signaturePatterns.Keys) {
                    $totals[$name] += [regex]::Matches($text, $signaturePatterns[$name], [Text.RegularExpressions.RegexOptions]::IgnoreCase).Count
                }
            }
            catch { }
        }

        $signatures = foreach ($name in $signaturePatterns.Keys) {
            if ($totals[$name] -gt 0) {
                [pscustomobject]@{ name = $name; count = $totals[$name] }
            }
        }
        $fileMetadata = foreach ($file in $files) { Get-FileMetadata $file.FullName }

        return [pscustomobject]@{
            directory_exists = $true
            scanned_files = @($fileMetadata)
            signatures = @($signatures)
            note = 'Only signature counts from the last 3000 lines of up to five recent sandbox logs are included.'
        }
    }
    catch {
        return [pscustomobject]@{ directory_exists = $true; scanned_files = @(); signatures = @(); error = Protect-Text $_.Exception.Message }
    }
}

function Get-AppPackageSummary {
    try {
        if ($null -eq (Get-Command Get-AppxPackage -ErrorAction SilentlyContinue)) {
            return [pscustomobject]@{ available = $false; reason = 'Get-AppxPackage is unavailable.' }
        }
        $packages = @(Get-AppxPackage -Name 'OpenAI.Codex' -ErrorAction SilentlyContinue)
        if ($packages.Count -eq 0) {
            return [pscustomobject]@{ available = $true; found = $false }
        }
        $items = foreach ($package in $packages) {
            [pscustomobject]@{
                name = $package.Name
                version = $package.Version.ToString()
                architecture = [string]$package.Architecture
                install_location = Protect-Text $package.InstallLocation
            }
        }
        return [pscustomobject]@{ available = $true; found = $true; packages = @($items) }
    }
    catch {
        return [pscustomobject]@{ available = $true; found = $false; error = Protect-Text $_.Exception.Message }
    }
}

function Add-Finding {
    param(
        [Parameter(Mandatory = $true)][ref]$Collection,
        [Parameter(Mandatory = $true)][string]$Severity,
        [Parameter(Mandatory = $true)][string]$Id,
        [Parameter(Mandatory = $true)][string]$Evidence
    )

    $Collection.Value += [pscustomobject]@{ severity = $Severity; id = $Id; evidence = Protect-Text $Evidence }
}

# Refuse report collisions before any collection; a fresh task folder is required.
foreach ($reportName in @('codex-windows-diagnostics.json', 'codex-windows-diagnostics.md')) {
    if (Test-Path -LiteralPath (Join-Path $OutputDirectory $reportName)) { throw 'Diagnostic output already exists; choose a fresh directory.' }
}
$collectedAt = (Get-Date).ToUniversalTime().ToString('o')
$currentDirectory = (Get-Location).Path
$isWindowsProcess = ($env:OS -eq 'Windows_NT')

$osSummary = $null
try {
    $os = Get-CimInstance -ClassName Win32_OperatingSystem -ErrorAction Stop
    $osSummary = [pscustomobject]@{
        caption = $os.Caption
        version = $os.Version
        build_number = $os.BuildNumber
        architecture = $os.OSArchitecture
        last_boot_utc = $os.LastBootUpTime.ToUniversalTime().ToString('o')
    }
}
catch {
    $osSummary = [pscustomobject]@{
        caption = [Environment]::OSVersion.VersionString
        architecture = $env:PROCESSOR_ARCHITECTURE
        error = Protect-Text $_.Exception.Message
    }
}

$executionPolicies = @()
try {
    $executionPolicies = @(Get-ExecutionPolicy -List -ErrorAction Stop | ForEach-Object {
        [pscustomobject]@{ scope = [string]$_.Scope; policy = [string]$_.ExecutionPolicy }
    })
}
catch { }

$pathRaw = [Environment]::GetEnvironmentVariable('Path', 'Process')
$pathEntries = @()
if (-not [string]::IsNullOrWhiteSpace($pathRaw)) {
    $pathEntries = @($pathRaw.Split(';') | ForEach-Object { $_.Trim().Trim('"') } | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
}
$missingPathEntries = @($pathEntries | Where-Object { -not (Test-Path -LiteralPath $_ -ErrorAction SilentlyContinue) } | Select-Object -First 20 | ForEach-Object { Protect-Text $_ })
$duplicatePathEntries = @($pathEntries | Group-Object { $_.ToLowerInvariant() } | Where-Object { $_.Count -gt 1 } | Select-Object -First 20 | ForEach-Object { Protect-Text $_.Group[0] })

$toolNames = @('codex', 'pwsh', 'powershell', 'git', 'rg', 'node', 'npm', 'python', 'wsl')
$toolSummaries = @($toolNames | ForEach-Object { Get-CommandSummary $_ })

$codexHomeSource = 'default-user-profile'
$codexHome = $null
if (-not [string]::IsNullOrWhiteSpace($env:CODEX_HOME)) {
    $codexHomeSource = 'CODEX_HOME-environment-variable'
    $codexHome = $env:CODEX_HOME
}
elseif (-not [string]::IsNullOrWhiteSpace($env:USERPROFILE)) {
    $codexHome = Join-Path $env:USERPROFILE '.codex'
}

$configPath = $null
$sandboxDirectory = $null
if (-not [string]::IsNullOrWhiteSpace($codexHome)) {
    $configPath = Join-Path $codexHome 'config.toml'
    $sandboxDirectory = Join-Path $codexHome '.sandbox'
}

$setupError = if ($null -ne $sandboxDirectory) { Get-SafeSetupError $sandboxDirectory } else { [pscustomobject]@{ exists = $false } }
$sandboxSignatures = if ($null -ne $sandboxDirectory) { Get-SandboxSignatureSummary $sandboxDirectory } else { [pscustomobject]@{ directory_exists = $false; scanned_files = @(); signatures = @() } }

$wslCommand = $toolSummaries | Where-Object { $_.name -eq 'wsl' } | Select-Object -First 1
$wslSummary = [pscustomobject]@{
    command_found = ($null -ne $wslCommand -and $wslCommand.found)
    inherited_distro_variable = Protect-Text $env:WSL_DISTRO_NAME
    status = $null
    distributions = $null
}
if ($wslSummary.command_found) {
    $wslPath = $wslCommand.resolutions[0].source
    if (-not [string]::IsNullOrWhiteSpace($wslPath) -and $wslPath -notmatch '<redacted>') {
        $wslSummary.status = Invoke-LimitedProcess -FilePath $wslPath -Arguments '--status'
        $wslSummary.distributions = Invoke-LimitedProcess -FilePath $wslPath -Arguments '--list --verbose'
    }
}

$networkSummary = [pscustomobject]@{ included = $false; endpoints = @() }
if ($IncludeNetworkChecks) {
    $networkSummary = [pscustomobject]@{
        included = $true
        endpoints = @(
            Test-TcpEndpoint -HostName 'chatgpt.com' -Port 443
            Test-TcpEndpoint -HostName 'github.com' -Port 443
        )
    }
}

$findings = @()
if (-not $isWindowsProcess) {
    Add-Finding -Collection ([ref]$findings) -Severity 'warning' -Id 'not-native-windows-process' -Evidence 'The collector is not running in a process that reports Windows_NT.'
}
if ([string]::IsNullOrWhiteSpace($env:SystemRoot) -or [string]::IsNullOrWhiteSpace($env:windir)) {
    Add-Finding -Collection ([ref]$findings) -Severity 'high' -Id 'missing-windows-root-environment' -Evidence 'SystemRoot or windir is missing from the collector process.'
}
$codexCommand = $toolSummaries | Where-Object { $_.name -eq 'codex' } | Select-Object -First 1
if ($null -eq $codexCommand -or -not $codexCommand.found) {
    Add-Finding -Collection ([ref]$findings) -Severity 'medium' -Id 'codex-command-not-resolved' -Evidence 'The codex command does not resolve in this process PATH.'
}
if ($isWindowsProcess -and -not [string]::IsNullOrWhiteSpace($env:WSL_DISTRO_NAME)) {
    Add-Finding -Collection ([ref]$findings) -Severity 'medium' -Id 'wsl-marker-in-native-process' -Evidence 'A native Windows process inherited WSL_DISTRO_NAME, which can confuse environment selection.'
}
if ((Get-PathKind $currentDirectory) -eq 'wsl-unc' -and $isWindowsProcess) {
    Add-Finding -Collection ([ref]$findings) -Severity 'info' -Id 'native-process-on-wsl-unc-workspace' -Evidence 'A native Windows process is operating on a WSL UNC workspace.'
}
if ($missingPathEntries.Count -gt 0) {
    Add-Finding -Collection ([ref]$findings) -Severity 'info' -Id 'missing-path-entries' -Evidence ("Process PATH contains {0} non-existent entries in the first checked set." -f $missingPathEntries.Count)
}
if ($setupError.exists) {
    Add-Finding -Collection ([ref]$findings) -Severity 'high' -Id 'sandbox-setup-error-present' -Evidence ("Sandbox setup_error.json is present with code '{0}'." -f $setupError.code)
}
foreach ($signature in $sandboxSignatures.signatures) {
    $severity = 'medium'
    if ($signature.name -match 'helper|create_process|elevation|access_denied|logon') { $severity = 'high' }
    Add-Finding -Collection ([ref]$findings) -Severity $severity -Id ("sandbox-signature-{0}" -f $signature.name) -Evidence ("Found {0} matching event(s) in recent sandbox log tails." -f $signature.count)
}

$report = [ordered]@{
    schema_version = '1.0'
    collected_at_utc = $collectedAt
    collection_mode = if ($IncludeNetworkChecks) { 'read-only-with-explicit-network-checks' } else { 'read-only-offline' }
    privacy = [ordered]@{
        raw_config_read = $false
        sandbox_secrets_read = $false
        raw_logs_included = $false
        path_and_token_redaction = $true
    }
    system = [ordered]@{
        os = $osSummary
        process_architecture = $env:PROCESSOR_ARCHITECTURE
        culture = (Get-Culture).Name
        ui_culture = (Get-UICulture).Name
        is_administrator = Get-AdministratorState
    }
    shell = [ordered]@{
        host = $Host.Name
        powershell_version = $PSVersionTable.PSVersion.ToString()
        powershell_edition = if ($PSVersionTable.ContainsKey('PSEdition')) { $PSVersionTable.PSEdition } else { 'Desktop' }
        language_mode = [string]$ExecutionContext.SessionState.LanguageMode
        execution_policies = $executionPolicies
        system_root_present = -not [string]::IsNullOrWhiteSpace($env:SystemRoot)
        windir_present = -not [string]::IsNullOrWhiteSpace($env:windir)
    }
    workspace = [ordered]@{
        current_directory = Protect-Text $currentDirectory
        path_kind = Get-PathKind $currentDirectory
    }
    process_path = [ordered]@{
        entry_count = $pathEntries.Count
        missing_entries = $missingPathEntries
        duplicate_entries = $duplicatePathEntries
        full_path_included = $false
    }
    tools = $toolSummaries
    codex = [ordered]@{
        home_source = $codexHomeSource
        home = Protect-Text $codexHome
        home_exists = ($null -ne $codexHome -and (Test-Path -LiteralPath $codexHome -PathType Container))
        config = Get-FileMetadata $configPath
        app_package = Get-AppPackageSummary
        sandbox_directory = Protect-Text $sandboxDirectory
        setup_error = $setupError
        sandbox_log_scan = $sandboxSignatures
    }
    wsl = $wslSummary
    network = $networkSummary
    findings = $findings
}

New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null
$jsonPath = Join-Path $OutputDirectory 'codex-windows-diagnostics.json'
$markdownPath = Join-Path $OutputDirectory 'codex-windows-diagnostics.md'

$report | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $jsonPath -Encoding UTF8

$markdown = New-Object System.Collections.Generic.List[string]
$markdown.Add('# Codex Windows diagnostic summary')
$markdown.Add('')
$markdown.Add("- Collected (UTC): $collectedAt")
$markdown.Add("- Mode: $($report.collection_mode)")
$markdown.Add("- OS: $($osSummary.caption) $($osSummary.version) build $($osSummary.build_number)")
$markdown.Add("- PowerShell: $($PSVersionTable.PSVersion) ($($report.shell.powershell_edition))")
$markdown.Add("- Workspace kind: $($report.workspace.path_kind)")
$markdown.Add("- Workspace: $($report.workspace.current_directory)")
$markdown.Add('')
$markdown.Add('## Findings')
$markdown.Add('')
if ($findings.Count -eq 0) {
    $markdown.Add('- No known high-signal condition was detected. This does not prove the environment is healthy.')
}
else {
    foreach ($finding in $findings) {
        $markdown.Add("- [$($finding.severity)] $($finding.id): $($finding.evidence)")
    }
}
$markdown.Add('')
$markdown.Add('## Tool resolution')
$markdown.Add('')
foreach ($tool in $toolSummaries) {
    if ($tool.found) {
        $firstSource = $tool.resolutions[0].source
        $markdown.Add("- $($tool.name): found ($firstSource)")
    }
    else {
        $markdown.Add("- $($tool.name): not found")
    }
}
$markdown.Add('')
$markdown.Add('## Privacy notes')
$markdown.Add('')
$markdown.Add('- The collector did not read config.toml contents.')
$markdown.Add('- The collector did not read CODEX_HOME/.sandbox-secrets/.')
$markdown.Add('- The collector included sandbox-log signature counts, not raw log lines.')
$markdown.Add('- Review both files before sharing. If support requests sandbox.log, inspect it separately and never include .sandbox-secrets.')

$markdown | Set-Content -LiteralPath $markdownPath -Encoding UTF8

Write-Output "Diagnostic JSON: $jsonPath"
Write-Output "Diagnostic summary: $markdownPath"