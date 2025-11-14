# coding=utf-8
# Copyright 2022 The IDEA Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------------------------
# Modified from
# https://github.com/fundamentalvision/Deformable-DETR/blob/main/models/ops/setup.py
# https://github.com/facebookresearch/detectron2/blob/main/setup.py
# https://github.com/open-mmlab/mmdetection/blob/master/setup.py
# https://github.com/Oneflow-Inc/libai/blob/main/setup.py
# ------------------------------------------------------------------------------------------------

import glob
import os
import subprocess

from setuptools import find_packages, setup

try:
    import torch
    from torch.utils.cpp_extension import CUDA_HOME, CppExtension, CUDAExtension
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    CUDA_HOME = None
    CppExtension = None
    CUDAExtension = None

# groundingdino version info
version = "0.2.1"
package_name = "groundingdino-cu128"
cwd = os.path.dirname(os.path.abspath(__file__))


sha = "Unknown"
try:
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=cwd).decode("ascii").strip()
except Exception:
    pass


def write_version_file():
    version_path = os.path.join(cwd, "groundingdino", "version.py")
    with open(version_path, "w") as f:
        f.write(f"__version__ = '{version}'\n")
        # f.write(f"git_version = {repr(sha)}\n")


requirements = ["torch", "torchvision"]

# Only check torch version if torch is available
if TORCH_AVAILABLE:
    torch_ver = [int(x) for x in torch.__version__.split(".")[:2]]
else:
    torch_ver = None


def get_extensions():
    # If torch is not available, skip building extensions
    # Extensions will be built when torch is installed
    if not TORCH_AVAILABLE:
        print("\n" + "="*70)
        print("PyTorch not found. Skipping C++ extension compilation.")
        print("Extensions will be compiled on first import if CUDA is available.")
        print("="*70 + "\n")
        return []

    this_dir = os.path.dirname(os.path.abspath(__file__))
    extensions_dir = os.path.join(this_dir, "groundingdino", "models", "GroundingDINO", "csrc")

    main_source = os.path.join(extensions_dir, "vision.cpp")
    sources = glob.glob(os.path.join(extensions_dir, "**", "*.cpp"))
    source_cuda = glob.glob(os.path.join(extensions_dir, "**", "*.cu")) + glob.glob(
        os.path.join(extensions_dir, "*.cu")
    )

    sources = [main_source] + sources

    extension = CppExtension

    # C++17 compiler flags for better compatibility and modern features
    extra_compile_args = {"cxx": ["-std=c++17"]}
    define_macros = []

    if torch.cuda.is_available() and CUDA_HOME is not None:
        print("\n" + "="*70)
        print("Compiling with CUDA support")
        print(f"CUDA_HOME: {CUDA_HOME}")
        print("Using C++17 standard")
        print("="*70 + "\n")
        extension = CUDAExtension
        sources += source_cuda
        define_macros += [("WITH_CUDA", None)]
        extra_compile_args["nvcc"] = [
            "-std=c++17",  # C++17 support for CUDA compiler
            "-DCUDA_HAS_FP16=1",
            "-D__CUDA_NO_HALF_OPERATORS__",
            "-D__CUDA_NO_HALF_CONVERSIONS__",
            "-D__CUDA_NO_HALF2_OPERATORS__",
        ]
    else:
        print("\n" + "="*70)
        print("CUDA not available - building in CPU-only mode")
        if not torch.cuda.is_available():
            print("Reason: PyTorch CUDA not detected")
        if CUDA_HOME is None:
            print("Reason: CUDA_HOME not set")
        print("\nTo enable CUDA support, ensure:")
        print("  - CUDA Toolkit 12.6 or 12.8 is installed")
        print("  - PyTorch with CUDA support is installed")
        print("  - C++17 compatible compiler is available:")
        print("    * Windows: Visual Studio 2019+ with C++ build tools")
        print("    * Linux: GCC 7+ or Clang 5+")
        print("    * macOS: Xcode Command Line Tools")
        print("="*70 + "\n")
        define_macros += [("WITH_HIP", None)]
        extra_compile_args["nvcc"] = []
        return []

    sources = [os.path.join(extensions_dir, s) for s in sources]
    include_dirs = [extensions_dir]

    ext_modules = [
        extension(
            "groundingdino._C",
            sources,
            include_dirs=include_dirs,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
        )
    ]

    return ext_modules


def parse_requirements(fname="requirements.txt", with_version=True):
    """Parse the package dependencies listed in a requirements file but strips
    specific versioning information.

    Args:
        fname (str): path to requirements file
        with_version (bool, default=False): if True include version specs

    Returns:
        List[str]: list of requirements items

    CommandLine:
        python -c "import setup; print(setup.parse_requirements())"
    """
    import re
    import sys
    from os.path import exists

    require_fpath = fname

    def parse_line(line):
        """Parse information from a line in a requirements text file."""
        if line.startswith("-r "):
            # Allow specifying requirements in other files
            target = line.split(" ")[1]
            for info in parse_require_file(target):
                yield info
        else:
            info = {"line": line}
            if line.startswith("-e "):
                info["package"] = line.split("#egg=")[1]
            elif "@git+" in line:
                info["package"] = line
            else:
                # Remove versioning from the package
                pat = "(" + "|".join([">=", "==", ">"]) + ")"
                parts = re.split(pat, line, maxsplit=1)
                parts = [p.strip() for p in parts]

                info["package"] = parts[0]
                if len(parts) > 1:
                    op, rest = parts[1:]
                    if ";" in rest:
                        # Handle platform specific dependencies
                        # http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-platform-specific-dependencies
                        version, platform_deps = map(str.strip, rest.split(";"))
                        info["platform_deps"] = platform_deps
                    else:
                        version = rest  # NOQA
                    info["version"] = (op, version)
            yield info

    def parse_require_file(fpath):
        with open(fpath, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    for info in parse_line(line):
                        yield info

    def gen_packages_items():
        if exists(require_fpath):
            for info in parse_require_file(require_fpath):
                parts = [info["package"]]
                if with_version and "version" in info:
                    parts.extend(info["version"])
                if not sys.version.startswith("3.4"):
                    # apparently package_deps are broken in 3.4
                    platform_deps = info.get("platform_deps")
                    if platform_deps is not None:
                        parts.append(";" + platform_deps)
                item = "".join(parts)
                yield item

    packages = list(gen_packages_items())
    return packages


if __name__ == "__main__":
    print(f"Building wheel {package_name}-{version}")

    write_version_file()

    # Note: Most metadata is now in pyproject.toml
    # This setup.py only handles the C++ extension compilation
    ext_modules = get_extensions()

    # Only use BuildExtension if torch is available and we have extensions
    if TORCH_AVAILABLE and ext_modules:
        setup(
            ext_modules=ext_modules,
            cmdclass={"build_ext": torch.utils.cpp_extension.BuildExtension},
        )
    else:
        setup()
