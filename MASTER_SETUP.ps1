Write-Host ""
Write-Host "========================================="
Write-Host "        DARREL MASTER SETUP"
Write-Host "========================================="
Write-Host ""

Write-Host "[1/7] Checking Python..."

python --version

Write-Host ""
Write-Host "[2/7] Creating Virtual Environment..."

if (!(Test-Path ".venv")) {
    python -m venv .venv
}

Write-Host ""
Write-Host "[3/7] Activating Virtual Environment..."

& ".\.venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "[4/7] Upgrading pip..."

python -m pip install --upgrade pip

Write-Host ""
Write-Host "[5/7] Installing Python Packages..."

pip install -r requirements.txt

Write-Host ""
Write-Host "[6/7] Checking Ollama..."

ollama --version

Write-Host ""
Write-Host "[7/7] Checking Installed Models..."

ollama list

Write-Host ""
Write-Host "========================================="
Write-Host "SETUP COMPLETE"
Write-Host "========================================="
Write-Host ""
Write-Host "Next:"
Write-Host "python HEALTH_CHECK.py"
Write-Host ""