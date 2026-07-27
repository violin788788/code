

from ebooklib import epub
import os,mimetypes

book=epub.EpubBook()
book_name="cheka_cropped_2up"

book.set_identifier("imgbook")
book.set_title(book_name)
book.set_language("en")

book.add_metadata("meta","rendition:layout","pre-paginated")
book.add_metadata("meta","viewport","width=device-width,height=device-height")

pages=[]
imgs=sorted(f for f in os.listdir("pages") if f.lower().endswith(".jpg"))

for i,f in enumerate(imgs):
    path=os.path.join("pages",f)
    data=open(path,"rb").read()

    book.add_item(epub.EpubItem(
        uid=f,
        file_name="img/"+f,
        media_type=mimetypes.guess_type(f)[0],
        content=data
    ))

    p=epub.EpubHtml(title=str(i),file_name=f"{i}.xhtml")
    p.content=f"""
<html>
<head>
<meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0"/>
<style>
html,body{{margin:0;padding:0;width:100%;height:100%;background:black;}}
img{{width:100vw;height:100vh;object-fit:contain;display:block;margin:0;}}
</style>
</head>
<body>
<img src="img/{f}"/>
</body>
</html>
"""
    book.add_item(p)
    pages.append(p)
    print(i)

book.toc=tuple(pages)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine=["nav"]+pages

epub.write_epub(book_name+".epub",book)