import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils import *

stuff = read_txt("song.txt")
print(stuff)