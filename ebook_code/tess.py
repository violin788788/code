import os
import pytesseract
from PIL import Image

os.environ["TESSDATA_PREFIX"] = r"B:\Program Files\Tesseract-OCR\tessdata"
pytesseract.pytesseract.tesseract_cmd = r"B:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("shib.png")
text = pytesseract.image_to_string(image)
print(text)