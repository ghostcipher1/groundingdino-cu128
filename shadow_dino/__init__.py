"""
Shadow DINO - Wrapper namespace for groundingdino-cu128

This package provides an alternative import namespace for the groundingdino package.
Both import methods are supported:

    import groundingdino  # canonical, original package name
    import shadow_dino    # wrapper namespace

The shadow_dino namespace re-exports all public APIs from groundingdino while
providing additional metadata and future extensibility for product integration.

Note: Both namespaces reference the same underlying implementation. The CUDA
extension (_C) is loaded through groundingdino._C regardless of which import
you use.
"""

__version__ = "0.2.0"

# Re-export everything from groundingdino
from groundingdino import *  # noqa: F401, F403

# Explicitly re-export commonly used modules for better IDE support
from groundingdino import models  # noqa: F401
from groundingdino import util  # noqa: F401
from groundingdino import datasets  # noqa: F401

# Provide access to the CUDA extension through this namespace
try:
    from groundingdino import _C  # noqa: F401
    __cuda_available__ = True
except ImportError:
    __cuda_available__ = False

__all__ = [
    'models',
    'util',
    'datasets',
    '__version__',
    '__cuda_available__',
]
