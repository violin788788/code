import os,pytesseract
from PIL import Image
from ebooklib import epub
#pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd=r"B:\Program Files\Tesseract-OCR"

image_folder="battle_of_britain"
book=epub.EpubBook()
book.set_identifier(image_folder)
book.set_title(image_folder)
book.set_language("en")
spine=["nav"]
toc=[]
images=sorted(f for f in os.listdir(image_folder) if f.lower().endswith((".png",".jpg",".jpeg",".bmp",".tif",".tiff",".webp")))
for i,f in enumerate(images,1):
    text=pytesseract.image_to_string(Image.open(os.path.join(image_folder,f)),lang="eng").strip()
    if not text:
        text="[No text detected]"
    chapter=epub.EpubHtml(title=f"Page {i}",file_name=f"page{i}.xhtml",lang="en")
    chapter.content=f"<h2>Page {i}</h2><pre>{text}</pre>"
    book.add_item(chapter)
    toc.append(chapter)
    spine.append(chapter)
book.toc=tuple(toc)
book.spine=spine
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
epub.write_epub(image_folder+".epub",book,{})
print("Done:",image_folder+".epub")