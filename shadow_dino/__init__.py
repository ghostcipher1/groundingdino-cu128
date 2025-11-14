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

__version__ = "2025.2.1"

# Re-export everything from groundingdino
from groundingdino import *  # noqa: F401, F403

# Explicitly re-export commonly used modules for better IDE support
try:
    from groundingdino import models  # noqa: F401
except ImportError:
    pass

try:
    from groundingdino import util  # noqa: F401
except ImportError:
    pass

try:
    from groundingdino import datasets  # noqa: F401
except ImportError:
    pass

# Provide access to the CUDA extension through this namespace
try:
    from groundingdino import _C  # noqa: F401
    __cuda_available__ = True
except ImportError:
    __cuda_available__ = False

# Build __all__ dynamically based on what's available
__all__ = ['__version__', '__cuda_available__']
if 'models' in dir():
    __all__.append('models')
if 'util' in dir():
    __all__.append('util')
if 'datasets' in dir():
    __all__.append('datasets')
