from pathlib import Path
import pyautogui,sys,os,time
from PIL import Image

folder = Path("medici_money")

pages = []

files = os.listdir(folder)
files = sorted(files, key=lambda f: int(f.split("_")[1].split(".")[0]))


pages = []

for a in range(len(files)):
    img = Image.open(folder / files[a]).convert("RGB")
    pages.append(img)
    print(files[a])

    """
for a in range(0, len(files)):  # 1 through 700
    img = Image.open(folder / files[a]).convert("RGB")
    pages.append(img)
    print (a),
	"""


pages[0].save(
    folder / "medici_money.pdf",
    save_all=True,
    append_images=pages[1:]
)

os.startfile(folder)