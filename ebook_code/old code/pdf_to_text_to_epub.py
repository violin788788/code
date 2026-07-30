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




import os
import pytesseract
from PIL import Image

os.environ["TESSDATA_PREFIX"] = r"B:\Program Files\Tesseract-OCR\tessdata"
pytesseract.pytesseract.tesseract_cmd = r"B:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("shib.png")
text = pytesseract.image_to_string(image)
print(text)