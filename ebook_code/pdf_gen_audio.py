"""
from importlib import import_module
utils=import_module("0utils")
globals().update({n:getattr(utils,n) for n in dir(utils) if not n.startswith("_")})
if __name__=="__main__":
    print("Loaded 0utils.py")


"""


import pytesseract

#pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"


import os
import fitz
#import pytesseract
from PIL import Image
from gtts import gTTS

pdf_file="cheka_cropped.pdf"
doc=fitz.open(pdf_file)
output_dir=os.path.splitext(pdf_file)[0]
os.makedirs(output_dir,exist_ok=True)
for i,page in enumerate(doc):
    pix=page.get_pixmap(dpi=300)
    img=Image.frombytes("RGB",(pix.width,pix.height),pix.samples)
    text=pytesseract.image_to_string(img).strip()
    if not text:
        print(f"Skipping page {i+1} (no text found by OCR)")
        continue
    filename=os.path.join(output_dir,f"{i+1:04d}.mp3")
    print(f"Generating {filename}")
    gTTS(text=text,lang="en").save(filename)
print("Done.")