import subprocess
import sys

def run(cmd):
    print("\nRunning:", cmd)
    subprocess.check_call(cmd)

# Upgrade install tools first
run([
    sys.executable, "-m", "pip",
    "install", "--upgrade",
    "pip", "setuptools", "wheel"
])

# Install PyTorch 1.7.1 from the old PyTorch wheel repository
run([
    sys.executable, "-m", "pip",
    "install",
    "torch==1.7.1",
    "-f",
    "https://download.pytorch.org/whl/torch_stable.html"
])

# Install matching torchvision
run([
    sys.executable, "-m", "pip",
    "install",
    "torchvision==0.8.2",
    "-f",
    "https://download.pytorch.org/whl/torch_stable.html"
])

# Test installation
print("\nTesting PyTorch...")
import torch
import torchvision

print("Torch:", torch.__version__)
print("Torchvision:", torchvision.__version__)

print("\nPyTorch installation OK")