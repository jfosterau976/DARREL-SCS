param(
    [ValidateSet("safe", "shadow", "all")]
    [string]$Suite = "safe"
)

$ErrorActionPreference = "Stop"

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$pythonExecutable = Join-Path $repositoryRoot ".venv\Scripts\python.exe"
$protectedMemory = Join-Path $repositoryRoot "scs_memory.json"
$safeTestModules = @(
    "tests.test_anthropic_provider"
    "tests.test_provider_failures"
    "tests.test_provider_telemetry"
    "tests.test_provider_diagnostics"
    "tests.test_telemetry_contract"
    "tests.test_memory_contract"
    "tests.test_learned_relevance"
    "tests.test_benchmark_result_contract"
)
$shadowTestModules = @(
    "tests.test_neural_routing_shadow"
    "tests.test_cognitive_budget_shadow"
)

switch ($Suite) {
    "safe" {
        $testModules = $safeTestModules
    }
    "shadow" {
        $testModules = $shadowTestModules
    }
    "all" {
        $testModules = $safeTestModules + $shadowTestModules
    }
}

if (-not (Test-Path -LiteralPath $pythonExecutable -PathType Leaf)) {
    Write-Host "FAIL: DARREL Python interpreter was not found:" -ForegroundColor Red
    Write-Host $pythonExecutable
    exit 2
}

function Get-ProtectedMemoryFingerprint {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return "absent"
    }

    $item = Get-Item -LiteralPath $Path
    $hash = (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash

    return ("{0}|{1}|{2}" -f @(
        $item.Length
        $item.LastWriteTimeUtc.Ticks
        $hash
    ))
}

$previousBytecodeSetting = $env:PYTHONDONTWRITEBYTECODE
$previousMemoryFile = $env:SCS_MEMORY_FILE

try {
    $protectedMemoryFingerprintBefore = Get-ProtectedMemoryFingerprint (
        $protectedMemory
    )
}
catch {
    Write-Host (
        "FAIL: Protected persistent memory could not be fingerprinted before testing."
    ) -ForegroundColor Red
    exit 3
}
$temporaryDirectory = Join-Path (
    [System.IO.Path]::GetTempPath()
) ("darrel-safe-tests-{0}" -f [guid]::NewGuid().ToString("N"))
$temporaryMemoryFile = Join-Path $temporaryDirectory "scs_memory.json"

[System.IO.Directory]::CreateDirectory($temporaryDirectory) | Out-Null
[System.IO.File]::WriteAllText($temporaryMemoryFile, "[]")

$env:PYTHONDONTWRITEBYTECODE = "1"
$env:SCS_MEMORY_FILE = $temporaryMemoryFile
$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
$testExitCode = 1
$memoryGuardPassed = $false

Push-Location $repositoryRoot

try {
    Write-Host "Running isolated deterministic DARREL tests..."
    Write-Host ("Suite: {0}" -f $Suite)
    Write-Host ("Modules: {0}" -f ($testModules -join ", "))

    $previousErrorPreference = $ErrorActionPreference

    try {
        $ErrorActionPreference = "Continue"
        $testOutput = & $pythonExecutable -B -m unittest -v @testModules 2>&1
        $testExitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorPreference
    }

    $testOutput | ForEach-Object {
        if ($_ -is [System.Management.Automation.ErrorRecord]) {
            Write-Host $_.Exception.Message
        }
        else {
            Write-Host ($_.ToString())
        }
    }
}
catch {
    Write-Host ("Test runner error: {0}" -f $_.Exception.Message) -ForegroundColor Red
    $testExitCode = 1
}
finally {
    $stopwatch.Stop()

    if ($null -eq $previousBytecodeSetting) {
        Remove-Item Env:PYTHONDONTWRITEBYTECODE -ErrorAction SilentlyContinue
    }
    else {
        $env:PYTHONDONTWRITEBYTECODE = $previousBytecodeSetting
    }

    if ($null -eq $previousMemoryFile) {
        Remove-Item Env:SCS_MEMORY_FILE -ErrorAction SilentlyContinue
    }
    else {
        $env:SCS_MEMORY_FILE = $previousMemoryFile
    }

    if (Test-Path -LiteralPath $temporaryDirectory) {
        Remove-Item -LiteralPath $temporaryDirectory -Recurse -Force
    }

    try {
        $protectedMemoryFingerprintAfter = Get-ProtectedMemoryFingerprint (
            $protectedMemory
        )
        $memoryGuardPassed = (
            $protectedMemoryFingerprintBefore -eq $protectedMemoryFingerprintAfter
        )

        if (-not $memoryGuardPassed) {
            $testExitCode = 3
        }
    }
    catch {
        Write-Host (
            "Protected memory fingerprint error: {0}" -f (
                $_.Exception.Message
            )
        ) -ForegroundColor Red
        $testExitCode = 3
    }

    Write-Host ""
    if ($memoryGuardPassed) {
        Write-Host (
            "PASS: Protected persistent memory fingerprint unchanged."
        ) -ForegroundColor Green
    }
    else {
        Write-Host (
            "FAIL: Protected persistent memory fingerprint changed or could not be verified."
        ) -ForegroundColor Red
    }

    if ($testExitCode -eq 0) {
        Write-Host ("PASS: DARREL {0} suite passed." -f $Suite) -ForegroundColor Green
    }
    else {
        Write-Host ("FAIL: DARREL tests exited with code {0}." -f $testExitCode) -ForegroundColor Red
    }

    Write-Host ("Elapsed: {0:N3} seconds" -f $stopwatch.Elapsed.TotalSeconds)
    Write-Host ""
    Write-Host "Git status --short:"
    & git status --short

    Pop-Location
}

exit $testExitCode
