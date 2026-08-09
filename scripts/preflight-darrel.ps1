$ErrorActionPreference = "Stop"

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$pythonExecutable = Join-Path $repositoryRoot ".venv\Scripts\python.exe"
$safeTestRunner = Join-Path $PSScriptRoot "test-darrel-safe.ps1"
$memoryImplementation = Join-Path $repositoryRoot "core\cognitive_memory.py"
$memoryContractTests = Join-Path $repositoryRoot "tests\test_memory_contract.py"
$protectedMemory = Join-Path $repositoryRoot "scs_memory.json"

$failures = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

function Write-Pass {
    param([string]$Message)
    Write-Host ("PASS: {0}" -f $Message) -ForegroundColor Green
}

function Write-Failure {
    param([string]$Message)
    $failures.Add($Message)
    Write-Host ("FAIL: {0}" -f $Message) -ForegroundColor Red
}

function Write-Warning {
    param([string]$Message)
    $warnings.Add($Message)
    Write-Host ("WARN: {0}" -f $Message) -ForegroundColor Yellow
}

function Test-RequiredFile {
    param(
        [string]$Path,
        [string]$Description
    )

    if (Test-Path -LiteralPath $Path -PathType Leaf) {
        Write-Pass ("{0}: {1}" -f $Description, $Path)
        return $true
    }

    Write-Failure ("{0} not found: {1}" -f $Description, $Path)
    return $false
}

Write-Host "DARREL development preflight"
Write-Host ("Repository: {0}" -f $repositoryRoot)
Write-Host ""

$insideWorkTree = & git -C $repositoryRoot rev-parse --is-inside-work-tree 2>$null
if ($LASTEXITCODE -eq 0 -and $insideWorkTree -eq "true") {
    Write-Pass "Git repository detected"
}
else {
    Write-Failure "Git repository could not be verified"
}

$pythonAvailable = Test-RequiredFile $pythonExecutable "Repository Python"
$runnerAvailable = Test-RequiredFile $safeTestRunner "Safe test runner"
$memoryAvailable = Test-RequiredFile $memoryImplementation "Memory implementation"
$memoryTestsAvailable = Test-RequiredFile $memoryContractTests "Memory contract tests"

if (Test-Path -LiteralPath $protectedMemory -PathType Leaf) {
    Write-Pass "Protected persistent memory is present and was not opened"
}
else {
    Write-Warning ("Protected persistent memory was not found: {0}" -f $protectedMemory)
}

if ($pythonAvailable) {
    $previousBytecodeSetting = $env:PYTHONDONTWRITEBYTECODE

    try {
        $env:PYTHONDONTWRITEBYTECODE = "1"
        $pythonVersion = & $pythonExecutable -B --version 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Pass ("Interpreter executable: {0}" -f $pythonVersion)
        }
        else {
            Write-Failure ("Interpreter exited with code {0}" -f $LASTEXITCODE)
        }
    }
    catch {
        Write-Failure ("Interpreter could not be executed: {0}" -f $_.Exception.Message)
    }
    finally {
        if ($null -eq $previousBytecodeSetting) {
            Remove-Item Env:PYTHONDONTWRITEBYTECODE -ErrorAction SilentlyContinue
        }
        else {
            $env:PYTHONDONTWRITEBYTECODE = $previousBytecodeSetting
        }
    }
}

if ($memoryAvailable) {
    $memorySource = Get-Content -LiteralPath $memoryImplementation -Raw -Encoding UTF8

    if ($memorySource -match 'os\.getenv\("SCS_MEMORY_FILE"\)') {
        Write-Pass "Memory implementation supports SCS_MEMORY_FILE isolation"
    }
    else {
        Write-Failure "Memory implementation does not expose SCS_MEMORY_FILE isolation"
    }
}

if ($memoryTestsAvailable) {
    $memoryTestSource = Get-Content -LiteralPath $memoryContractTests -Raw -Encoding UTF8

    if ($memoryTestSource -match 'test_environment_override_isolates_persistent_memory' -and $memoryTestSource -match 'SCS_MEMORY_FILE') {
        Write-Pass "Memory isolation regression test is present"
    }
    else {
        Write-Failure "Memory isolation regression test is missing"
    }
}

if ($runnerAvailable) {
    $runnerSource = Get-Content -LiteralPath $safeTestRunner -Raw -Encoding UTF8
    $runnerChecks = @(
        $runnerSource -match 'PYTHONDONTWRITEBYTECODE'
        $runnerSource -match 'SCS_MEMORY_FILE'
        $runnerSource -match '&\s+\$pythonExecutable\s+-B\s+-m\s+unittest'
    )

    if ($runnerChecks -notcontains $false) {
        Write-Pass "Safe runner preserves bytecode and memory-isolation safeguards"
    }
    else {
        Write-Failure "Safe runner safeguards are incomplete"
    }
}

if ($insideWorkTree -eq "true") {
    $branch = (& git -C $repositoryRoot branch --show-current).Trim()
    $commit = (& git -C $repositoryRoot rev-parse --short HEAD).Trim()
    $status = @(& git -C $repositoryRoot status --short)
    $staged = @(& git -C $repositoryRoot diff --cached --name-only)

    if ([string]::IsNullOrWhiteSpace($branch)) {
        Write-Warning "Git is in a detached HEAD state"
    }
    else {
        Write-Pass ("Git branch: {0}" -f $branch)
    }

    Write-Pass ("Git commit: {0}" -f $commit)

    if ($staged.Count -gt 0) {
        Write-Warning ("Git has {0} staged path(s)" -f $staged.Count)
    }
    else {
        Write-Pass "Git staging area is empty"
    }

    if ($status.Count -gt 0) {
        Write-Warning ("Git worktree has {0} existing change(s); preserve them" -f $status.Count)
    }
    else {
        Write-Pass "Git worktree is clean"
    }
}

Write-Host ""
Write-Host ("Warnings: {0}" -f $warnings.Count)
Write-Host ("Failures: {0}" -f $failures.Count)

if ($failures.Count -gt 0) {
    Write-Host "NOT READY: DARREL development preflight failed." -ForegroundColor Red
    exit 1
}

Write-Host "READY: DARREL development preflight passed." -ForegroundColor Green
exit 0
