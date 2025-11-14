# Test installation of groundingdino-cu128 v0.2.1 from PyPI
# Simple Ubuntu 22.04 container test

$ErrorActionPreference = "Stop"

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Testing groundingdino-cu128 v0.2.1 from PyPI" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check Docker
try {
    docker info | Out-Null
} catch {
    Write-Host "Error: Docker is not running." -ForegroundColor Red
    Write-Host "Please start Docker Desktop and try again." -ForegroundColor Yellow
    exit 1
}

Write-Host "Building test container..." -ForegroundColor Yellow
docker build -f Dockerfile.install-test -t groundingdino-install-test:v0.2.1 .

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host "Running installation test..." -ForegroundColor Green
    Write-Host "==========================================" -ForegroundColor Green
    Write-Host ""

    docker run --rm groundingdino-install-test:v0.2.1

    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✓ Installation test PASSED!" -ForegroundColor Green
    } else {
        Write-Host ""
        Write-Host "✗ Installation test FAILED!" -ForegroundColor Red
    }
} else {
    Write-Host ""
    Write-Host "Build failed!" -ForegroundColor Red
    exit 1
}
