from ebooklib import epub
from pathlib import Path
import html

txtfile="war_and_national_finance.txt"
title=txtfile.replace(".txt","")
author="brand"

text=Path(txtfile).read_text(encoding="utf-8")
body="<p>"+html.escape(text).replace("\n\n","</p><p>").replace("\n","<br/>")+"</p>"
book=epub.EpubBook()
book.set_identifier(Path(txtfile).stem)
book.set_title(title)
book.set_language("en")
book.add_author(author)
chapter=epub.EpubHtml(title=title,file_name="index.xhtml")
chapter.content=f"<html><body><h1>{html.escape(title)}</h1>{body}</body></html>"
book.add_item(chapter)
book.toc=(chapter,)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine=["nav",chapter]
outfile=Path(txtfile).with_suffix(".epub")
epub.write_epub(str(outfile),book)
print(f"Created {outfile}")