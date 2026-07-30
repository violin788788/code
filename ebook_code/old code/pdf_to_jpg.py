import fitz
import os
from PIL import Image
import io



import fitz,os,io
from PIL import Image

input_file = "cheka.pdf"

pdf=fitz.open(input_file)
os.makedirs("pages",exist_ok=True)

for i,page in enumerate(pdf):
    pix=page.get_pixmap(dpi=110)  # low DPI
    img=Image.open(io.BytesIO(pix.tobytes("png"))).convert("L")  # grayscale
    img.save(f"pages/page_{i+1:04}.jpg",format="JPEG",quality=65,optimize=True)
    print(i+1)


"""
pdf=fitz.open("cheka_cropped.pdf")
os.makedirs("pages",exist_ok=True)

for i,page in enumerate(pdf):
    pix=page.get_pixmap(dpi=150)  # LOWER DPI = smaller files
    img=Image.open(io.BytesIO(pix.tobytes("png"))).convert("L")  # grayscale
    img.save(f"pages/page_{i+1:03}.jpg",format="JPEG",quality=75,optimize=True)
    print(i+1)

    """