# Project Structure

This document describes the organization of the groundingdino-cu128 project.

## Directory Structure

```
groundingdino-cu128/
├── .github/              # GitHub configuration
│   ├── workflows/        # CI/CD workflows
│   ├── ISSUE_TEMPLATE/   # Issue templates
│   └── *.md              # GitHub documentation
├── demo/                 # Example scripts and notebooks
│   ├── *.py              # Python demo scripts
│   └── *.ipynb           # Jupyter notebooks
├── docs/                 # Project documentation
│   ├── CHANGELOG.md      # Version history
│   ├── CONTRIBUTING.md   # Contribution guidelines
│   ├── SECURITY.md       # Security policy
│   └── PROJECT_STRUCTURE.md  # This file
├── groundingdino/        # Main package (canonical import)
│   ├── config/           # Configuration files
│   ├── datasets/         # Dataset utilities
│   ├── models/           # Model implementations
│   │   └── GroundingDINO/
│   │       ├── backbone/ # Backbone architectures
│   │       ├── csrc/     # CUDA source code
│   │       └── *.py      # Model components
│   └── util/             # Utility modules
├── shadow_dino/          # Wrapper namespace (alternative import)
├── tests/                # Test suite
├── .editorconfig         # Editor configuration
├── .gitattributes        # Git attributes
├── .gitignore            # Git ignore rules
├── .dockerignore         # Docker ignore rules
├── Dockerfile            # Docker image definition
├── LICENSE               # Apache 2.0 license
├── NOTICE                # Attribution notice
├── pyproject.toml        # Python project configuration
├── README.md             # Main documentation
├── requirements.txt      # Python dependencies
├── constraints.txt       # Pinned dependency versions
└── setup.py              # Package setup script
```

## Key Directories

### `groundingdino/`
The main package directory containing the core implementation. This is the canonical import namespace.

- **`config/`**: Model configuration files
- **`datasets/`**: Dataset loading and transformation utilities
- **`models/`**: Model implementations including:
  - `GroundingDINO/`: Main model implementation
  - `backbone/`: Backbone architectures (Swin Transformer, etc.)
  - `csrc/`: CUDA extension source code
- **`util/`**: Utility functions for inference, visualization, etc.

### `shadow_dino/`
Alternative import namespace that re-exports all functionality from `groundingdino`. Provides the same API with additional metadata.

### `docs/`
All project documentation is centralized here:
- **CHANGELOG.md**: Version history and release notes
- **CONTRIBUTING.md**: Guidelines for contributors
- **SECURITY.md**: Security policy and vulnerability reporting
- **PROJECT_STRUCTURE.md**: This file

### `demo/`
Example scripts and notebooks demonstrating usage:
- Python scripts for inference and dataset creation
- Jupyter notebooks for interactive examples

### `tests/`
Test suite for the package:
- Import tests
- Functionality tests
- Integration tests

## Build Artifacts

The following directories and files are build artifacts and should not be committed:
- `build/` - Build output
- `dist/` - Distribution packages
- `*.egg-info/` - Package metadata
- `*.so` - Compiled extensions
- `*.o` - Object files
- `*.log` - Build logs

These are automatically ignored via `.gitignore`.

## Configuration Files

### `.editorconfig`
Defines coding style and formatting preferences for various file types.

### `.gitattributes`
Configures Git behavior for different file types, including line ending normalization.

### `.gitignore`
Specifies files and directories to ignore in version control.

### `pyproject.toml`
Modern Python project configuration including:
- Package metadata
- Dependencies
- Build system configuration
- Tool configurations

### `setup.py`
Legacy setup script for building C++/CUDA extensions. Most metadata is now in `pyproject.toml`.

## Documentation Files

- **README.md**: Main project documentation (root level for GitHub display)
- **docs/CHANGELOG.md**: Detailed version history
- **docs/CONTRIBUTING.md**: Contribution guidelines
- **docs/SECURITY.md**: Security policy
- **LICENSE**: Apache License 2.0
- **NOTICE**: Attribution and licensing notices

## Import Namespaces

The package supports two import namespaces:

1. **Canonical** (recommended):
   ```python
   import groundingdino
   from groundingdino.models import build_model
   ```

2. **Alternative**:
   ```python
   import shadow_dino
   from shadow_dino.models import build_model
   ```

Both namespaces provide identical functionality.

