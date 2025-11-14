# CI/CD Setup Documentation

## Overview

This repository is equipped with a comprehensive CI/CD pipeline using GitHub Actions. This document explains the workflows, their purpose, and how to use them.

## Table of Contents

- [Workflows](#workflows)
- [Secrets Configuration](#secrets-configuration)
- [Release Process](#release-process)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## Workflows

### 1. CI - Test Suite (`.github/workflows/ci.yml`)

**Trigger:** Push to `main`/`develop`, Pull Requests

**Purpose:** Runs comprehensive tests on every code change

**Jobs:**
- **test**: Runs tests on Python 3.9, 3.10, 3.11, 3.12
  - Linting with flake8
  - Import tests
  - Full test suite with coverage
  - Coverage upload to Codecov

- **build-cpu**: Builds CPU-only source distribution
  - Validates the package can be built
  - Uploads artifacts for verification

- **check-package**: Validates package metadata
  - Runs twine check
  - Verifies pyproject.toml configuration
  - Ensures no nightvyper references

**Status Badge:**
```markdown
[![CI](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/ci.yml/badge.svg)](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/ci.yml)
```

### 2. Build CUDA Wheels (`.github/workflows/build-wheels.yml`)

**Trigger:**
- Tags matching `v*`
- Manual dispatch

**Purpose:** Builds CUDA-enabled wheels for distribution

**Jobs:**
- **build-cuda-wheels**: Matrix build
  - Python versions: 3.9, 3.10, 3.11, 3.12
  - CUDA versions: 12.6.2, 12.8.0
  - Uses NVIDIA CUDA Docker containers
  - Compiles CUDA extensions
  - Uploads wheel artifacts

- **test-wheels**: Tests wheel installation
  - Downloads built wheels
  - Verifies import works
  - Validates dual namespace imports

**Manual Trigger:**
```bash
# Via GitHub UI: Actions → Build CUDA Wheels → Run workflow
# Or via gh CLI:
gh workflow run build-wheels.yml
```

### 3. Release to PyPI (`.github/workflows/release.yml`)

**Trigger:**
- GitHub Release published
- Manual dispatch (for Test PyPI)

**Purpose:** Publishes package to PyPI

**Jobs:**
- **build-and-publish**:
  - Verifies version matches tag
  - Builds source distribution
  - Publishes to Test PyPI (manual) or PyPI (release)
  - Creates release summary

- **verify-installation**:
  - Waits for PyPI to update
  - Installs from PyPI
  - Verifies dual imports work

**Publishing Options:**
1. **Test PyPI** (manual): For testing before production
2. **Production PyPI** (automatic): On GitHub Release

### 4. Code Quality (`.github/workflows/code-quality.yml`)

**Trigger:** Push to `main`/`develop`, Pull Requests

**Purpose:** Enforces code quality standards

**Jobs:**
- **lint**: Style and format checks
  - Black (code formatting)
  - isort (import sorting)
  - flake8 (linting)
  - pylint (static analysis)

- **security**: Security scanning
  - Bandit (security issues)
  - Safety (dependency vulnerabilities)

- **dependency-review**: PR dependency analysis
  - Checks for vulnerable dependencies in PRs

- **validate-metadata**: Package compliance
  - Validates pyproject.toml
  - Checks for forbidden references
  - Verifies license compliance
  - Ensures required files exist

**Status Badge:**
```markdown
[![Code Quality](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/code-quality.yml/badge.svg)](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/code-quality.yml)
```

### 5. Dependabot (`.github/dependabot.yml`)

**Trigger:** Automatic, weekly

**Purpose:** Keeps dependencies updated

**Updates:**
- GitHub Actions versions
- Python package dependencies
- Excludes major PyTorch updates (version-locked)

## Secrets Configuration

### Required Secrets

Configure these in: `Settings → Secrets and variables → Actions`

#### For PyPI Publishing

**Option 1: Trusted Publishing (Recommended)**
1. Go to [PyPI](https://pypi.org/) → Account Settings → Publishing
2. Add trusted publisher:
   - Owner: `ghostcipher1`
   - Repository: `groundingdino-cu128`
   - Workflow: `release.yml`
   - Environment: (leave empty)

**Option 2: API Token**
1. Generate token at PyPI → Account Settings → API tokens
2. Add as secret: `PYPI_API_TOKEN`
3. Update workflow to use token instead of trusted publishing

#### For Test PyPI (Optional)

1. Create account at [Test PyPI](https://test.pypi.org/)
2. Generate API token
3. Add as secret: `TEST_PYPI_API_TOKEN`

#### For Codecov (Optional)

1. Sign up at [Codecov](https://codecov.io/)
2. Add repository
3. Copy token and add as secret: `CODECOV_TOKEN`

### Environment Variables

No environment variables required - all configuration is in `pyproject.toml`

## Release Process

### Standard Release

1. **Update Version**
   ```bash
   # Edit pyproject.toml
   version = "0.3.0"
   ```

2. **Update Changelog**
   ```bash
   # Edit docs/CHANGELOG.md
   ## [0.3.0] - 2025-XX-XX
   ### Added
   - New features...
   ```

3. **Commit Changes**
   ```bash
   git add pyproject.toml docs/CHANGELOG.md
   git commit -m "chore: bump version to 0.3.0"
   git push origin main
   ```

4. **Create Tag**
   ```bash
   git tag -a v0.3.0 -m "Release v0.3.0"
   git push origin v0.3.0
   ```

5. **Create GitHub Release**
   - Go to: Releases → Draft a new release
   - Choose tag: `v0.3.0`
   - Title: `v0.3.0`
   - Description: Copy from docs/CHANGELOG.md
   - Click "Publish release"

6. **Automated Steps**
   - CI runs tests ✓
   - Wheels build ✓
   - Package publishes to PyPI ✓
   - Installation verified ✓

### Pre-release Testing

Test on Test PyPI first:

```bash
# Manually trigger release workflow
gh workflow run release.yml -f test_pypi=true
```

Then install and test:

```bash
pip install --index-url https://test.pypi.org/simple/ groundingdino-cu128
```

### Hotfix Release

For urgent fixes:

1. Create branch from tag:
   ```bash
   git checkout -b hotfix/0.2.1 v0.2.0
   ```

2. Make fix and commit

3. Update version to `0.2.1`

4. Tag and release:
   ```bash
   git tag -a v0.2.1 -m "Hotfix: ..."
   git push origin v0.2.1
   ```

## Troubleshooting

### CI Failures

**Lint Errors**
```bash
# Fix locally before pushing
black groundingdino shadow_dino tests
isort groundingdino shadow_dino tests
flake8 groundingdino shadow_dino tests
```

**Test Failures**
```bash
# Run tests locally
pytest tests/ -v
export PYTHONPATH=$(pwd):$PYTHONPATH
pytest tests/test_import_names.py -v
```

**Build Failures**
```bash
# Test build locally
pip install build
python -m build --sdist
```

### Workflow Debugging

**View Logs**
- Go to: Actions → Select workflow run → View logs

**Re-run Failed Jobs**
- Actions → Failed run → Re-run failed jobs

**Enable Debug Logging**
Add secrets:
- `ACTIONS_RUNNER_DEBUG`: `true`
- `ACTIONS_STEP_DEBUG`: `true`

### PyPI Publishing Issues

**Version Already Exists**
- Increment version number
- PyPI doesn't allow re-uploading same version

**Authentication Failed**
- Verify trusted publisher setup
- Or check API token is correct

**Package Rejected**
```bash
# Validate locally first
pip install twine
python -m build
twine check dist/*
```

## Best Practices

### Before Pushing

```bash
# Run full local checks
black groundingdino shadow_dino tests
isort groundingdino shadow_dino tests
flake8 groundingdino shadow_dino tests
pytest tests/ -v
```

### Pull Request Workflow

1. Create feature branch
2. Make changes
3. Run local tests
4. Push and create PR
5. Wait for CI to pass
6. Address review comments
7. Merge after approval

### Security

- Never commit secrets
- Review dependency updates from Dependabot
- Monitor security advisories
- Keep CUDA toolkit updated

### Performance

- Workflows use caching for dependencies
- Matrix builds run in parallel
- Artifacts expire after 7-30 days

## Monitoring

### Check Workflow Status

```bash
# List recent workflow runs
gh run list

# View specific run
gh run view <run-id>

# Watch current run
gh run watch
```

### Badges

Add to README.md:

```markdown
[![CI](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/ci.yml/badge.svg)](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/ci.yml)
[![Code Quality](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/code-quality.yml/badge.svg)](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/code-quality.yml)
```

## Support

- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Contributing**: See docs/CONTRIBUTING.md

---

Last updated: 2025-11-08
