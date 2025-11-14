# Contributing to groundingdino-cu128

Thank you for your interest in contributing to groundingdino-cu128! This document provides guidelines for contributing to this maintained fork.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Code Style](#code-style)
- [License](#license)

## Code of Conduct

This project follows a standard code of conduct. Be respectful, inclusive, and professional in all interactions.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/groundingdino-cu128.git
   cd groundingdino-cu128
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/ghostcipher1/groundingdino-cu128.git
   ```

## Development Setup

### Prerequisites

- Python 3.9 or higher
- CUDA 12.6+ (for GPU support)
- GCC/G++ compiler
- Git

### Create Development Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -e .  # Editable install

# Install development tools
pip install pytest pytest-cov black isort flake8 mypy
```

### Set CUDA Environment (if building with CUDA)

```bash
export CUDA_HOME=/usr/local/cuda-12.6
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
```

### Build CUDA Extensions

```bash
python setup.py build_ext --inplace
```

## Making Changes

### Branch Naming Convention

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation changes
- `refactor/description` - Code refactoring
- `test/description` - Test additions/changes

### Commit Messages

Follow conventional commit format:

```
type(scope): brief description

Longer description if needed

Fixes #issue-number
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Example:
```
feat(models): add support for custom backbone architectures

Implemented configurable backbone selection for GroundingDINO model.
Users can now specify alternative backbones via config.

Fixes #123
```

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_import_names.py -v

# Run with coverage
pytest tests/ --cov=groundingdino --cov=shadow_dino --cov-report=html
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use descriptive test names
- Include docstrings explaining what is being tested

Example:
```python
def test_model_forward_pass():
    """Test that the model can perform a forward pass with valid inputs."""
    model = build_model(config)
    output = model(input_tensor)
    assert output.shape == expected_shape
```

## Submitting Changes

### Before Submitting

1. **Sync with upstream**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests**:
   ```bash
   pytest tests/
   ```

3. **Check code style**:
   ```bash
   black groundingdino shadow_dino tests
   isort groundingdino shadow_dino tests
   flake8 groundingdino shadow_dino tests
   ```

4. **Update documentation** if needed

### Creating a Pull Request

1. Push your changes to your fork:
   ```bash
   git push origin your-branch-name
   ```

2. Go to GitHub and create a Pull Request

3. Fill out the PR template with:
   - Clear description of changes
   - Related issue numbers
   - Testing performed
   - Screenshots (if UI changes)

4. Wait for CI checks to pass

5. Respond to review feedback

### Pull Request Checklist

- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] PR description is clear and complete
- [ ] No merge conflicts with main branch

## Code Style

### Python Style

- **Formatter**: Black (line length 127)
- **Import sorting**: isort
- **Linter**: flake8
- **Type hints**: Use where beneficial

### Code Organization

- Keep functions small and focused
- Use descriptive variable names
- Add docstrings to public functions/classes
- Comment complex logic

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: int, param2: str) -> bool:
    """Brief description of function.

    Longer description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When input is invalid
    """
    pass
```

## Important Guidelines

### License Compliance

- This project is licensed under Apache License 2.0
- All contributions must be compatible with Apache 2.0
- Maintain attribution to the original GroundingDINO project

### What NOT to Include

- **No proprietary code** or code with incompatible licenses
- **No nightvyper references** - Use ghostcipher1
- **No large binary files** - Use Git LFS if absolutely necessary
- **No credentials** or sensitive information

### Code Review Process

1. Maintainer reviews your PR
2. CI/CD checks must pass
3. At least one approval required
4. Maintainer merges (do not merge your own PRs)

## Development Tips

### Debugging CUDA Issues

```bash
# Check CUDA version
nvcc --version

# Verify PyTorch CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Build with verbose output
python setup.py build_ext --inplace --verbose
```

### Common Issues

**Import errors**: Make sure you've installed in editable mode (`pip install -e .`)

**CUDA compilation errors**: Check CUDA_HOME environment variable

**Test failures**: Ensure PYTHONPATH includes project root


## Getting Help

- **Issues**: Open a GitHub issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check README.md (root directory) and existing docs

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- Release notes (for significant contributions)
- Project documentation (for major features)

Thank you for contributing to groundingdino-cu128! 🚀
