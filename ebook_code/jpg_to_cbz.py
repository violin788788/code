import zipfile
from pathlib import Path

img_dir = Path("pages")
out_file = "book.cbz"

images = sorted(
    list(img_dir.glob("*.jpg")) +
    list(img_dir.glob("*.jpeg")) +
    list(img_dir.glob("*.png"))
)

with zipfile.ZipFile(out_file, "w", zipfile.ZIP_DEFLATED) as z:
    for img in images:
        print()
        z.write(img, arcname=img.name)