

from PIL import Image
from pathlib import Path

src = Path("pages")
dst = Path("pages_600")
dst.mkdir(exist_ok=True)

TARGET_WIDTH = 600

for f in src.glob("*.jpg"):
    img = Image.open(f)
    w, h = img.size

    scale = TARGET_WIDTH / w
    new_h = round(h * scale)

    img = img.resize((TARGET_WIDTH, new_h), Image.Resampling.LANCZOS)
    img.save(dst / f.name, quality=95)    

    print(f)