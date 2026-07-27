from ebooklib import epub
import os,mimetypes
book=epub.EpubBook()
book.set_identifier("imgbook")
book_name = "cheka_cropped_2up"

book.set_title(book_name)
book.set_language("en")
pages=[]
imgs=sorted(f for f in os.listdir("pages") if f.lower().endswith(".jpg"))
for i,f in enumerate(imgs):
    path=os.path.join("pages",f)
    data=open(path,"rb").read()
    book.add_item(epub.EpubItem(uid=f,file_name="img/"+f,media_type=mimetypes.guess_type(f)[0],content=data))
    p=epub.EpubHtml(title=str(i),file_name=f"{i}.xhtml")
    p.content=f'<html><body style="margin:0"><img src="img/{f}" style="width:100%"/></body></html>'
    book.add_item(p)
    pages.append(p)
    print(i)
book.toc=tuple(pages)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine=["nav"]+pages
epub.write_epub(book_name+".epub",book)