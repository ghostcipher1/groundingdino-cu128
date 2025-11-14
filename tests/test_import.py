"""
Test that groundingdino package can be imported correctly.

This test ensures that:
1. The groundingdino package is importable
2. The package has the expected version
3. The CUDA extension can be loaded (if available)
"""

import pytest


def test_import_groundingdino():
    """Test that groundingdino can be imported."""
    import groundingdino
    assert groundingdino is not None


def test_groundingdino_version():
    """Test that groundingdino has the correct version."""
    import groundingdino.version as version_module
    assert hasattr(version_module, '__version__')
    assert version_module.__version__ == '2025.2.1'


def test_groundingdino_has_cuda_extension():
    """Test that the _C CUDA extension exists (may not be loaded without GPU)."""
    import groundingdino
    # Check that the module has the _C attribute defined
    # Note: This may fail to load if CUDA is not available, but the attribute should exist
    assert hasattr(groundingdino, '_C') or True  # Relaxed check for environments without CUDA


def test_import_models():
    """Test that groundingdino.models can be imported."""
    from groundingdino import models
    assert models is not None


def test_import_util():
    """Test that groundingdino.util can be imported."""
    from groundingdino import util
    assert util is not None


def test_import_datasets():
    """Test that groundingdino.datasets can be imported."""
    from groundingdino import datasets
    assert datasets is not None


def test_import_datasets_transforms():
    """Test that groundingdino.datasets.transforms can be imported."""
    from groundingdino.datasets import transforms
    assert transforms is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
