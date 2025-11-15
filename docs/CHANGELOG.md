# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2025.11.0] - 2025-11-XX

### Changed
- Updated version to 2025.11.0 for new release cycle
- Cleaned up version branches and tags

## [2025.2.1] - 2025-11-13

### Fixed
- **GitHub Actions build failures** - Fixed `CalledProcessError` during package build in CI/CD pipelines
  - Removed PyTorch from `build-system.requires` in pyproject.toml
  - Made PyTorch import optional in setup.py during build phase
  - Added `--no-isolation` flag to all build commands in GitHub Actions workflows
  - Package can now be built without PyTorch pre-installed (CUDA extensions compile during user installation)
- **Missing datasets module** - Added `groundingdino/datasets/__init__.py` to fix `ModuleNotFoundError` when importing `groundingdino.datasets` (#11)

### Changed
- Build system now gracefully handles missing PyTorch during package creation
- CUDA extensions are compiled during installation (when PyTorch is available) rather than during build
- Updated CI/CD workflows (ci.yml, build-wheels.yml, release.yml) to use non-isolated builds
- Added C++17 compiler standard for better compatibility and modern features
- Enhanced build messages with clear requirements and troubleshooting information

### Technical Details
- Build requirements reduced to: `setuptools>=68`, `wheel` only
- PyTorch remains a runtime dependency (installed automatically via pip)
- Backward compatible - no changes to user installation process
- Tests remain passing with relaxed CUDA extension checks

## [2025.2.0] - 2025-11-08

### Added
- Initial release of groundingdino-cu128 fork
- PyTorch 2.7+ and CUDA 12.8 support
- shadow_dino wrapper namespace for alternative imports
- Dual import support: `import groundingdino` and `import shadow_dino`
- Comprehensive test suite with 5 tests
- GitHub Actions CI/CD pipelines
- Code quality and security workflows
- Apache License 2.0 compliance

### Changed
- Upgraded from PyTorch 1.x to PyTorch 2.7+
- Fixed CUDA compilation for modern PyTorch API
- Updated deprecated PyTorch tensor methods (.type() → .scalar_type())
- Modernized build system with pyproject.toml
- Distribution name changed to groundingdino-cu128

### Fixed
- CUDA compilation errors with PyTorch 2.x
- AT_DISPATCH_FLOATING_TYPES compatibility issues
- Deprecated tensor.type().is_cuda() calls

### Technical Details
- Python support: 3.9, 3.10, 3.11, 3.12
- CUDA support: 12.6, 12.8
- PyTorch version: >=2.7.0, <2.8
- Build system: setuptools with pyproject.toml

### Attribution
This is a maintained fork of [GroundingDINO](https://github.com/IDEA-Research/GroundingDINO) by IDEA-Research.
Original authors and contributors are credited in the README.md (root directory).

---

## Template for Future Releases

### [Unreleased]

#### Added
- New features

#### Changed
- Changes in existing functionality

#### Deprecated
- Soon-to-be removed features

#### Removed
- Removed features

#### Fixed
- Bug fixes

#### Security
- Security vulnerability fixes

---

## Release Process

1. Update version in `pyproject.toml`
2. Update docs/CHANGELOG.md with release notes
3. Create git tag: `git tag -a v2025.2.0 -m "Release v2025.2.0"`
4. Push tag: `git push origin v2025.2.0`
5. GitHub Actions will automatically build and publish to PyPI
6. Create GitHub Release with changelog notes
