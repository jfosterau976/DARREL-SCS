$ErrorActionPreference = "Stop"

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$pythonExecutable = Join-Path $repositoryRoot ".venv\Scripts\python.exe"
$testModules = @(
    "tests.test_anthropic_provider"
    "tests.test_provider_failures"
    "tests.test_memory_contract"
    "tests.test_learned_relevance"
)

if (-not (Test-Path -LiteralPath $pythonExecutable -PathType Leaf)) {
    Write-Host "FAIL: DARREL Python interpreter was not found:" -ForegroundColor Red
    Write-Host $pythonExecutable
    exit 2
}

$previousBytecodeSetting = $env:PYTHONDONTWRITEBYTECODE
$previousMemoryFile = $env:SCS_MEMORY_FILE
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

Push-Location $repositoryRoot

try {
    Write-Host "Running isolated deterministic DARREL tests..."
    Write-Host ("Modules: {0}" -f ($testModules -join ", "))

    & $pythonExecutable -B -m unittest -v @testModules
    $testExitCode = $LASTEXITCODE
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

    Write-Host ""
    if ($testExitCode -eq 0) {
        Write-Host "PASS: All isolated DARREL tests passed." -ForegroundColor Green
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
