#!/bin/bash
# Test installation of groundingdino-cu128 v0.2.1 from PyPI
# Simple Ubuntu 22.04 container test

set -e

echo "=========================================="
echo "Testing groundingdino-cu128 v0.2.1 from PyPI"
echo "=========================================="
echo ""

# Check Docker
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running."
    echo "Please start Docker and try again."
    exit 1
fi

echo "Building test container..."
docker build -f Dockerfile.install-test -t groundingdino-install-test:v0.2.1 .

echo ""
echo "=========================================="
echo "Running installation test..."
echo "=========================================="
echo ""

docker run --rm groundingdino-install-test:v0.2.1

echo ""
echo "✓ Installation test PASSED!"
