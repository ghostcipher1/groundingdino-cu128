# Grounding DINO - CUDA 12.8 Edition

> **Maintained Fork** - Upgraded for PyTorch 2.7 + CUDA 12.8

[![CI](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/ci.yml/badge.svg)](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/ci.yml)
[![Code Quality](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/code-quality.yml/badge.svg)](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/code-quality.yml)
[![Docker](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/ghostcipher1/groundingdino-cu128/actions/workflows/docker-publish.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/badge/PyPI-groundingdino--cu128-blue.svg)](https://pypi.org/project/groundingdino-cu128/)
[![Docker](https://img.shields.io/badge/Docker-GHCR-blue.svg)](https://github.com/ghostcipher1/groundingdino-cu128/pkgs/container/groundingdino-cu128)
![Branch Protection](https://img.shields.io/badge/branch--protection-enabled-brightgreen?style=flat&logo=github)

---

### 🛡️ Branch Protection Policy

The `main` branch of **GroundingDINO-CU128** is fully protected to maintain build integrity and code quality.

| Rule | Description |
|------|--------------|
| ✅ **Pull Requests Required** | All commits must go through a PR — direct pushes to `main` are blocked. |
| ✅ **Signed Commits** | Every commit must be verified (GPG / SSH signature required). |
| ✅ **1 Approval Minimum** | Each PR requires at least one review approval before merge. |
| ✅ **Status Checks Required** | PRs must pass all required workflows:<br>• `CI – Test Suite / tests`<br>• `Code Quality / ruff`<br>• `Code Quality / mypy` |
| 🔄 **Up-to-Date with `main`** | Branches must be rebased or merged with the latest `main` before merging. |
| 🧱 **No Force Push / No Deletion** | The `main` branch cannot be force-pushed or deleted. |

**Merge methods enabled:** Merge, Squash, and Rebase  
**Administrator enforcement:** Active (rules apply equally to maintainers)

---

🧩 _Maintainers use feature branches for all development and release PRs are automatically verified through GitHub Actions CI before merging._

---

**Original Project** |  [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/IDEA-Research/GroundingDINO)
[![arXiv](https://img.shields.io/badge/arXiv-2303.05499-b31b1b.svg)](https://arxiv.org/abs/2303.05499)
[![YouTube](https://badges.aleen42.com/src/youtube.svg)](https://youtu.be/wxWDt5UiwY8)

Grounding DINO Demos |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/zero-shot-object-detection-with-grounding-dino.ipynb)
[![YouTube](https://badges.aleen42.com/src/youtube.svg)](https://youtu.be/cMa77r3YrDk)
[![HuggingFace space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/ShilongLiu/Grounding_DINO_demo)
[![YouTube](https://badges.aleen42.com/src/youtube.svg)](https://youtu.be/C4NqaRBz_Kw)

Extensions | [Grounding DINO with Stable Diffusion](demo/image_editing_with_groundingdino_stablediffusion.ipynb);
[Grounding DINO with Segment Anything](https://github.com/IDEA-Research/Grounded-Segment-Anything)



[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/grounding-dino-marrying-dino-with-grounded/zero-shot-object-detection-on-mscoco)](https://paperswithcode.com/sota/zero-shot-object-detection-on-mscoco?p=grounding-dino-marrying-dino-with-grounded) \
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/grounding-dino-marrying-dino-with-grounded/zero-shot-object-detection-on-odinw)](https://paperswithcode.com/sota/zero-shot-object-detection-on-odinw?p=grounding-dino-marrying-dino-with-grounded) \
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/grounding-dino-marrying-dino-with-grounded/object-detection-on-coco-minival)](https://paperswithcode.com/sota/object-detection-on-coco-minival?p=grounding-dino-marrying-dino-with-grounded) \
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/grounding-dino-marrying-dino-with-grounded/object-detection-on-coco)](https://paperswithcode.com/sota/object-detection-on-coco?p=grounding-dino-marrying-dino-with-grounded)



Official PyTorch implementation of [Grounding DINO](https://arxiv.org/abs/2303.05499), a stronger open-set object detector. Code is available now!


## Highlight

- **Open-Set Detection.** Detect **everything** with language!
- **High Performancce.** COCO zero-shot **52.5 AP** (training without COCO data!). COCO fine-tune **63.0 AP**.
- **Flexible.** Collaboration with Stable Diffusion for Image Editting.

## News
- **`2023/04/06`**: We build a new demo by marrying GroundingDINO with [Segment-Anything](https://github.com/facebookresearch/segment-anything) named [Grounded-Segment-Anything](https://github.com/IDEA-Research/Grounded-Segment-Anything) aims to support segmentation in GroundingDINO.
- **`2023/03/28`**: A YouTube [video](https://youtu.be/cMa77r3YrDk) about Grounding DINO and basic object detection prompt engineering. [[SkalskiP](https://github.com/SkalskiP)]
- **`2023/03/28`**: Add a [demo](https://huggingface.co/spaces/ShilongLiu/Grounding_DINO_demo) on Hugging Face Space!
- **`2023/03/27`**: Support CPU-only mode. Now the model can run on machines without GPUs.
- **`2023/03/25`**: A [demo](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/zero-shot-object-detection-with-grounding-dino.ipynb) for Grounding DINO is available at Colab. [[SkalskiP](https://github.com/SkalskiP)]
- **`2023/03/22`**: Code is available Now!

<details open>
<summary><font size="4">
Description
</font></summary>
<img src=".asset/hero_figure.png" alt="ODinW" width="100%">
</details>

---

## Why This Fork?

This is a maintained fork of the original GroundingDINO project, modernized for current GPU infrastructure:

- **Modern Toolchain**: PyTorch 2.7 + CUDA 12.8 support
- **No API Breaking Changes**: Package folder remains `groundingdino`, all existing code works unchanged
- **Distribution Name**: Published as `groundingdino-cu128` on PyPI for clear version identification
- **Maintained**: Regular updates and bug fixes for compatibility with latest dependencies

### Why the New Distribution Name?

The distribution name `groundingdino-cu128` serves several purposes:

1. **Version Clarity**: Clearly identifies this as a CUDA 12.8-compatible build
2. **Parallel Installation**: Allows coexistence with other GroundingDINO versions if needed
3. **Maintained Fork**: Distinguishes this actively maintained fork from the original repository
4. **No Code Changes Required**: Despite the new distribution name, all imports remain `import groundingdino`

The optional `shadow_dino` wrapper namespace provides:
- A distinctive brand for product integration
- Additional metadata and version information
- Future extensibility while maintaining full backward compatibility

## Installation

> **⚠️ IMPORTANT: CUDA Toolkit Required**
>
> This package requires the **NVIDIA CUDA Toolkit** to be installed on your system **BEFORE** installation.
> The package includes CUDA extensions that must be compiled during `pip install`.
>
> **Install CUDA Toolkit first:**
> - CUDA 12.6 or 12.8: https://developer.nvidia.com/cuda-downloads
> - Set `CUDA_HOME` environment variable (e.g., `export CUDA_HOME=/usr/local/cuda`)
> - Verify: `nvcc --version`
>
> **Without CUDA toolkit installed, the installation will fail.**

### From PyPI (Recommended)

```bash
# After installing CUDA toolkit:
pip install groundingdino-cu128
```

### From Source

If you have a CUDA environment, please make sure the environment variable `CUDA_HOME` is set. It will be compiled under CPU-only mode if no CUDA available.

```bash
git clone https://github.com/ghostcipher1/groundingdino-cu128.git
cd groundingdino-cu128
pip install -e .
```

### Optional Extras

The package supports several optional dependency groups for different use cases:

```bash
# Development tools (linting, testing, formatting)
pip install groundingdino-cu128[dev]

# ONNX export and runtime support
pip install groundingdino-cu128[onnx]

# All extras at once
pip install groundingdino-cu128[dev,onnx]
```

**Note:** TensorRT (`trt`) and Jetson (`jetson`) extras are placeholders for future support. These require external SDKs to be installed separately.

### Reproducible Environments

For reproducible environments with pinned dependency versions, use the included `constraints.txt`:

```bash
# Install with strict version pins
pip install -c constraints.txt groundingdino-cu128

# Install with extras and constraints
pip install -c constraints.txt groundingdino-cu128[dev]

# For development from source
git clone https://github.com/ghostcipher1/groundingdino-cu128.git
cd groundingdino-cu128
pip install -c constraints.txt -e .[dev]
```

The `constraints.txt` file pins specific versions of dependencies that have been tested together, ensuring consistent behavior across different environments.

### Requirements

- **NVIDIA CUDA Toolkit 12.6 or 12.8** (required before installation)
- Python >= 3.9
- PyTorch >= 2.7.0, < 2.8
- CUDA-capable GPU (for GPU acceleration)

## Docker

For users who prefer a pre-configured environment without manually installing CUDA toolkit and dependencies, we provide ready-to-run Docker images with everything pre-installed.

### Quick Start with Docker

```bash
# Pull the latest image from GitHub Container Registry
docker pull ghcr.io/ghostcipher1/groundingdino-cu128:latest

# Run with GPU support
docker run --gpus all -it --rm ghcr.io/ghostcipher1/groundingdino-cu128:latest

# Run a quick test
docker run --gpus all --rm ghcr.io/ghostcipher1/groundingdino-cu128:latest python -c "
import groundingdino
import shadow_dino
print(f'✓ GroundingDINO version: {shadow_dino.__version__}')
print(f'✓ CUDA available: {shadow_dino.__cuda_available__}')
"
```

### Docker Image Details

The Docker image includes:
- **Base**: NVIDIA CUDA 12.8.0 runtime on Ubuntu 22.04
- **Python**: 3.10
- **PyTorch**: 2.7.1 with CUDA 12.8 support
- **GroundingDINO**: Pre-installed with all dependencies
- **Size**: Multi-stage build optimized for smaller runtime image

### Available Tags

- `latest` - Latest stable release
- `edge` - Latest build from main branch
- `v0.2.0` - Specific version tags
- `main-<sha>` - Commit-specific builds

### Building Locally

```bash
# Build the image
docker build -t groundingdino-cu128:local .

# Test the build
docker run --gpus all --rm groundingdino-cu128:local python -c "import groundingdino; print('OK')"
```

### Docker Requirements

- **NVIDIA Docker Runtime** (`nvidia-docker2` or Docker with `--gpus` support)
- **NVIDIA GPU** with compatible drivers
- See [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/) for setup

## Usage

### Import Options

This package supports two import namespaces:

**1. Canonical Import (recommended for compatibility)**
```python
import groundingdino
from groundingdino.models import build_model
from groundingdino.util.slconfig import SLConfig
from groundingdino.util.utils import clean_state_dict

# Your existing GroundingDINO code works without modification
```

**2. Wrapper Namespace (alternative)**
```python
import shadow_dino
from shadow_dino.models import build_model
from shadow_dino.util.slconfig import SLConfig
from shadow_dino.util.utils import clean_state_dict

# Same functionality through the shadow_dino namespace
```

Both import methods work identically and reference the same underlying implementation. The `shadow_dino` namespace is provided as an optional wrapper for product integration while maintaining full backward compatibility with the canonical `groundingdino` import.

The package directory remains `groundingdino` to ensure full backward compatibility with existing code.

## Demo

```bash
CUDA_VISIBLE_DEVICES=6 python demo/inference_on_a_image.py \
  -c /path/to/config \
  -p /path/to/checkpoint \
  -i .asset/cats.png \
  -o "outputs/0" \
  -t "cat ear." \
  [--cpu-only] # open it for cpu mode
```
See the `demo/inference_on_a_image.py` for more details.

**Web UI**

We also provide a demo code to integrate Grounding DINO with Gradio Web UI. See the file `demo/gradio_app.py` for more details.

## Checkpoints

<!-- insert a table -->
<table>
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>backbone</th>
      <th>Data</th>
      <th>box AP on COCO</th>
      <th>Checkpoint</th>
      <th>Config</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>GroundingDINO-T</td>
      <td>Swin-T</td>
      <td>O365,GoldG,Cap4M</td>
      <td>48.4 (zero-shot) / 57.2 (fine-tune)</td>
      <td><a href="https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth">Github link</a> | <a href="https://huggingface.co/ShilongLiu/GroundingDINO/resolve/main/groundingdino_swint_ogc.pth">HF link</a></td>
      <td><a href="https://github.com/IDEA-Research/GroundingDINO/blob/main/groundingdino/config/GroundingDINO_SwinT_OGC.py">link</a></td>
    </tr>
  </tbody>
</table>

## Results

<details open>
<summary><font size="4">
COCO Object Detection Results
</font></summary>
<img src=".asset/COCO.png" alt="COCO" width="100%">
</details>

<details open>
<summary><font size="4">
ODinW Object Detection Results
</font></summary>
<img src=".asset/ODinW.png" alt="ODinW" width="100%">
</details>

<details open>
<summary><font size="4">
Marrying Grounding DINO with <a href="https://github.com/Stability-AI/StableDiffusion">Stable Diffusion</a> for Image Editing
</font></summary>
See our example: demo/image_editing_with_groundingdino_stablediffusion.ipynb .
<img src=".asset/GD_SD.png" alt="GD_SD" width="100%">
</details>


<details open>
<summary><font size="4">
Marrying Grounding DINO with <a href="https://github.com/gligen/GLIGEN">GLIGEN</a> for more Detailed Image Editing
</font></summary>
<img src=".asset/GD_GLIGEN.png" alt="GD_GLIGEN" width="100%">
</details>

## Model

Includes: a text backbone, an image backbone, a feature enhancer, a language-guided query selection, and a cross-modality decoder.

![arch](.asset/arch.png)


## Acknowledgement

Our model is related to [DINO](https://github.com/IDEA-Research/DINO) and [GLIP](https://github.com/microsoft/GLIP). Thanks for their great work!

We also thank great previous work including DETR, Deformable DETR, SMCA, Conditional DETR, Anchor DETR, Dynamic DETR, DAB-DETR, DN-DETR, etc. More related work are available at [Awesome Detection Transformer](https://github.com/IDEACVR/awesome-detection-transformer). A new toolbox [detrex](https://github.com/IDEA-Research/detrex) is available as well.

Thanks [Stable Diffusion](https://github.com/Stability-AI/StableDiffusion) and [GLIGEN](https://github.com/gligen/GLIGEN) for their awesome models.


## Citation

If you find our work helpful for your research, please consider citing the following BibTeX entry.   

```bibtex
@inproceedings{ShilongLiu2023GroundingDM,
  title={Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection},
  author={Shilong Liu and Zhaoyang Zeng and Tianhe Ren and Feng Li and Hao Zhang and Jie Yang and Chunyuan Li and Jianwei Yang and Hang Su and Jun Zhu and Lei Zhang},
  year={2023}
}
```




