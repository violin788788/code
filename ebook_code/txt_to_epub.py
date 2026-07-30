from ebooklib import epub
from pathlib import Path
import html
import zipfile
import shutil
txtfile="war_and_national_finance.txt"
title="War and National Finance"
author="brand"
coverfile="war_and_national_finance.png"
text=Path(txtfile).read_text(encoding="utf-8")
body="<p>"+html.escape(text).replace("\n\n","</p><p>").replace("\n","<br/>")+"</p>"
book=epub.EpubBook()
book.set_identifier(Path(txtfile).stem)
book.set_title(title)
book.set_language("en")
book.add_author(author)
cover=epub.EpubItem(uid="cover-image",file_name=coverfile,media_type="image/png",content=Path(coverfile).read_bytes())
cover.properties=["cover-image"]
book.add_item(cover)
cover_page=epub.EpubHtml(title="Cover",file_name="cover.xhtml")
cover_page.content=f'<html xmlns="http://www.w3.org/1999/xhtml"><body><img src="{coverfile}" alt="Cover"/></body></html>'
book.add_item(cover_page)
chapter=epub.EpubHtml(title=title,file_name="index.xhtml")
chapter.content=f'<html xmlns="http://www.w3.org/1999/xhtml"><body><h1>{html.escape(title)}</h1>{body}</body></html>'
book.add_item(chapter)
book.toc=(cover_page,chapter)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine=[cover_page,chapter]
outfile=Path(txtfile).with_suffix(".epub")
epub.write_epub(str(outfile),book)
tmp=outfile.with_suffix(".tmp.epub")
with zipfile.ZipFile(outfile,"r") as zin,zipfile.ZipFile(tmp,"w") as zout:
    for item in zin.infolist():
        data=zin.read(item.filename)
        if item.filename.endswith(".opf"):
            opf=data.decode("utf-8")
            opf=opf.replace(f'href="{coverfile}" media-type="image/png"',f'href="{coverfile}" media-type="image/png" properties="cover-image"')
            opf=opf.replace("<metadata>","<metadata><meta name=\"cover\" content=\"cover-image\"/>")
            data=opf.encode("utf-8")
        zout.writestr(item,data)
shutil.move(tmp,outfile)
print(f"Created {outfile}")