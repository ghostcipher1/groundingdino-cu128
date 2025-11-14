# Docker Testing for groundingdino-cu128 v0.2.1

This repository includes two Docker-based testing approaches to validate the v0.2.1 release.

## Test 1: Installation Test (Quick - 5 minutes)

Tests that v0.2.1 can be installed from PyPI on a clean Ubuntu 22.04 system.

### What it tests:
- ✅ Package can be installed via pip
- ✅ Both `groundingdino` and `shadow_dino` imports work
- ✅ Version is correct (0.2.1)
- ✅ Datasets module fix (Issue #11) is included
- ✅ All basic imports succeed

### How to run:

**Windows:**
```powershell
.\test-install.ps1
```

**Linux/macOS:**
```bash
chmod +x test-install.sh
./test-install.sh
```

**Manual:**
```bash
docker build -f Dockerfile.install-test -t groundingdino-install-test:v0.2.1 .
docker run --rm groundingdino-install-test:v0.2.1
```

### Expected output:
```
==========================================
groundingdino-cu128 v0.2.1 Installation Test
==========================================

Python: Python 3.10.12
pip: pip 24.0

Package version: 0.2.1
shadow_dino version: 0.2.1
CUDA available: False

Testing imports...
✓ All imports successful

✓ Installation test passed!
```

---

## Test 2: Full Build Test (Comprehensive - 30+ minutes)

Tests building the package from source with C++17 compilation and CUDA extensions.

### What it tests:
- ✅ C++17 compiler support (GCC 11)
- ✅ Build system configuration (pyproject.toml)
- ✅ PyTorch 2.7+ with CUDA 12.8 installation
- ✅ Package builds with `--no-isolation` flag
- ✅ CUDA extensions compile correctly
- ✅ Wheel installation works
- ✅ Complete test suite passes
- ✅ C++ extension (_C module) is available

### How to run:

**Windows:**
```powershell
.\test-build.ps1
```

**Linux/macOS:**
```bash
chmod +x test-build.sh
./test-build.sh
```

**Manual:**
```bash
docker build -f Dockerfile.test -t groundingdino-cu128-test:v0.2.1 .
docker run --rm --gpus all groundingdino-cu128-test:v0.2.1
```

### Expected output:
See [TESTING.md](TESTING.md) for detailed expected output.

---

## Test 3: Local Verification (No Docker)

For quick checks without Docker.

### How to run:

```bash
python verify-build-local.py
```

### What it checks:
- Python version (3.9+)
- C++17 compiler availability
- PyTorch installation
- Build dependencies (setuptools, wheel, build)
- pyproject.toml configuration
- datasets/__init__.py exists
- Attempts source distribution build

---

## File Overview

| File | Purpose |
|------|---------|
| `Dockerfile.install-test` | Quick PyPI installation test (Ubuntu 22.04) |
| `Dockerfile.test` | Full build test with CUDA and C++17 |
| `docker-compose.test.yml` | Docker Compose for GPU-enabled testing |
| `test-install.sh/ps1` | Scripts to run installation test |
| `test-build.sh/ps1` | Scripts to run full build test |
| `verify-build-local.py` | Local verification without Docker |
| `TESTING.md` | Comprehensive testing documentation |

---

## Quick Comparison

| Feature | Installation Test | Build Test | Local Verification |
|---------|------------------|------------|-------------------|
| **Time** | ~5 minutes | ~30 minutes | ~2 minutes |
| **Requires Docker** | Yes | Yes | No |
| **Requires GPU** | No | Optional | No |
| **Tests C++ compilation** | No | Yes | Checks only |
| **Tests PyPI package** | Yes | No | No |
| **Tests from source** | No | Yes | Yes |
| **Best for** | Quick validation | Full validation | Pre-commit checks |

---

## Troubleshooting

### Docker not running
```
Error: Docker is not running.
```

**Solution:** Start Docker Desktop

### Docker daemon connection error
```
ERROR: error during connect: ... dockerDesktopLinuxEngine
```

**Solution:**
1. Open Docker Desktop
2. Wait for it to fully start
3. Verify with: `docker info`

### CUDA not available in container
```
CUDA available: False
```

**Note:** This is expected for installation test (no GPU required). For build test with GPU support, ensure:
1. NVIDIA drivers installed
2. NVIDIA Docker runtime installed
3. Use `--gpus all` flag

### Build fails in local environment

**Solution:** Use Docker tests instead - they provide isolated, reproducible environments with all dependencies pre-installed.

---

## CI/CD Integration

These Docker tests mirror the GitHub Actions workflows:

- **Installation Test** → Validates PyPI package quality
- **Build Test** → Matches `build-wheels.yml` workflow
- **Local Verification** → Pre-commit validation

Running these locally before pushing ensures CI/CD will pass.

---

## Next Steps After Testing

1. ✅ Run installation test to verify PyPI package
2. ✅ (Optional) Run build test for comprehensive validation
3. ✅ Create pull request
4. ✅ Wait for GitHub Actions to pass
5. ✅ Merge to main
6. ✅ Create release tag v0.2.1
7. ✅ Verify automatic PyPI publication

---

## Questions?

- Installation issues: Check [TESTING.md](TESTING.md)
- Build configuration: See [pyproject.toml](pyproject.toml)
- Release notes: See [CHANGELOG.md](CHANGELOG.md)
- Issue #11 fix: See `groundingdino/datasets/__init__.py`
