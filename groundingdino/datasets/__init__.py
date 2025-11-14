# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
"""
Dataset utilities for GroundingDINO.

This module provides transforms and data augmentation utilities for both
images and bounding boxes, useful for training and inference with GroundingDINO.
"""

from . import transforms

__all__ = ['transforms']
