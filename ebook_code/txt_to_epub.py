

def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)

import sys,os
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)



from ebooklib import epub
from pathlib import Path
import html

text=Path("grant.txt").read_text(encoding="utf-8")
paragraphs=text.split("\n\n")
body="\n".join(f"<p>{html.escape(p).replace(chr(10),'<br/>')}</p>" for p in paragraphs if p.strip())
book=epub.EpubBook()
book.set_identifier("grant-book")
book.set_title("Grant")
book.set_language("en")
book.add_author("Unknown")
chapter=epub.EpubHtml(title="Grant",file_name="chapter1.xhtml")
chapter.content=f"<html><head><title>Grant</title></head><body><h1>Grant</h1>{body}</body></html>"
book.add_item(chapter)
book.toc=(chapter,)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine=["nav",chapter]
epub.write_epub("grant.epub",book)
print("Created grant.epub")