"""
Tests to verify that both import paths work correctly.

This test suite ensures:
1. The canonical groundingdino import works
2. The wrapper shadow_dino import works
3. Both namespaces reference the same underlying modules
4. The CUDA extension is accessible through both namespaces
"""

import pytest


def test_import_groundingdino():
    """Test that groundingdino can be imported."""
    import groundingdino

    # Verify core modules can be imported
    from groundingdino import models
    from groundingdino import util

    assert models is not None, "models module not found"
    assert util is not None, "util module not found"


def test_import_shadow_dino():
    """Test that shadow_dino wrapper can be imported."""
    import shadow_dino

    # Should re-export version
    assert hasattr(shadow_dino, "__version__"), "shadow_dino missing __version__"
    assert shadow_dino.__version__ == "2025.2.1"

    # Should have cuda availability flag
    assert hasattr(shadow_dino, "__cuda_available__"), "shadow_dino missing __cuda_available__"

    # Should re-export core modules
    assert hasattr(shadow_dino, "models"), "shadow_dino missing models"
    assert hasattr(shadow_dino, "util"), "shadow_dino missing util"


def test_shadow_dino_models_import():
    """Test that models can be accessed through shadow_dino."""
    import shadow_dino

    # Verify we can access models through the wrapper
    assert hasattr(shadow_dino, "models"), "shadow_dino missing models"
    assert shadow_dino.models is not None


def test_both_namespaces_reference_same_modules():
    """Test that both namespaces reference the same underlying implementation."""
    import groundingdino
    import shadow_dino

    # Both should reference the same models module
    assert shadow_dino.models is groundingdino.models

    # Both should reference the same util module
    assert shadow_dino.util is groundingdino.util

    # Both should reference the same CUDA extension if available
    if hasattr(shadow_dino, "_C") and hasattr(groundingdino, "_C"):
        assert shadow_dino._C is groundingdino._C


def test_cuda_extension_loadable():
    """Test that the CUDA extension can be loaded."""
    try:
        import groundingdino._C as cuda_ext
        # If we get here, the extension loaded successfully
        assert cuda_ext is not None
    except ImportError as e:
        pytest.skip(f"CUDA extension not available: {e}")


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"])
