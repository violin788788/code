import os
import pytesseract
from ebooklib import epub
from natsort import natsorted
os.environ["TESSDATA_PREFIX"] = r"B:\Program Files\Tesseract-OCR\tessdata"
pytesseract.pytesseract.tesseract_cmd = r"B:\Program Files\Tesseract-OCR\tesseract.exe"
jpgs_dir = "cheka"
files = natsorted(os.listdir(jpgs_dir))
book = epub.EpubBook()
book.set_identifier("ocr-book")
book.set_title("OCR Book")
book.set_language("en")
book.add_author("OCR")
chapters = []

for i, filename in enumerate(files):

#for i in range(0,5):
    #filename = files[i]
    print(i, filename)
    image = os.path.join(jpgs_dir, filename)
    text = pytesseract.image_to_string(image)
    #text = text.replace("\n"," ")
    chapter = epub.EpubHtml(
        title=f"Page {i+1}",
        file_name=f"page_{i+1}.xhtml",
        lang="en"
    )
    # Preserve line breaks
    html = "<html><body><pre>{}</pre></body></html>".format(
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )
    chapter.content = html
    book.add_item(chapter)
    chapters.append(chapter)
book.toc = tuple(chapters)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine = ["nav"] + chapters
out_file = "output.epub"
epub.write_epub(out_file, book)
print("Done!")