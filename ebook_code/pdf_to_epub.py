"""

from importlib import import_module
utils=import_module("0utils")
globals().update({n:getattr(utils,n) for n in dir(utils) if not n.startswith("_")})
if __name__=="__main__":
    print("Loaded 0utils.py")


"""


import fitz,os
from ebooklib import epub

"""
#name without .pdf
with open("0book_to_work_on.txt", "r", encoding="utf-8") as file:
    name = file.read()
    print(name)
"""
name = "war_and_national_finance"
author = "henry"

PDF_FILE=name+".pdf"
EPUB_FILE=name+".epub"
pdf=fitz.open(PDF_FILE)
book=epub.EpubBook()
book.set_identifier("pdf-to-epub")
book.set_title(name)
book.set_language("en")
book.add_author(author)
chapters=[]
for i,page in enumerate(pdf):
    text=page.get_text("text").strip()
    chapter=epub.EpubHtml(title=f"Page {i+1}",file_name=f"page_{i+1}.xhtml",lang="en")
    #chapter.content=f"<html><body><h2>Page {i+1}</h2><pre>{text}</pre></body></html>"
    chapter.content=f"<html><body><h2>Page {i+1}</h2><p>{text}</p></body></html>"
    book.add_item(chapter)
    chapters.append(chapter)
book.toc=tuple(chapters)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
css=epub.EpubItem(uid="style_nav",file_name="style/style.css",media_type="text/css",content="body{font-family:serif;margin:5%;}pre{white-space:pre-wrap;word-wrap:break-word;}")
book.add_item(css)
for chapter in chapters:
    chapter.add_item(css)
book.spine=["nav"]+chapters
epub.write_epub(EPUB_FILE,book)
print(f"Saved as {EPUB_FILE}")
os.startfile(EPUB_FILE)