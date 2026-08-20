import sys
sys.path.insert(0, r"A:\\Users\\-\\code")
from utils import *
from pathlib import Path

import onnxruntime as ort

print(ort.get_available_providers())