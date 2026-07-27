from ebooklib import epub
import os, mimetypes

book = epub.EpubBook()
book_name = "cheka_cropped_2up"

book.set_identifier("imgbook")
book.set_title(book_name)
book.set_language("en")

pages = []
imgs = sorted(f for f in os.listdir("pages") if f.lower().endswith(".jpg"))

for i, f in enumerate(imgs):
    path = os.path.join("pages", f)
    data = open(path, "rb").read()

    media_type = mimetypes.guess_type(f)[0] or "image/jpeg"

    img_name = f"img_{i}.jpg"

    book.add_item(epub.EpubItem(
        uid=img_name,
        file_name="images/" + img_name,
        media_type=media_type,
        content=data
    ))

    p = epub.EpubHtml(title=str(i), file_name=f"page_{i}.xhtml")

    p.content = f"""
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style>
@page {{
    margin: 0;
}}
html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background: black;
}}
img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
}}
</style>
</head>
<body>
<img src="images/{img_name}"/>
</body>
</html>
"""

    book.add_item(p)
    pages.append(p)

book.toc = pages
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

book.spine = ["nav"] + pages

epub.write_epub(book_name + ".epub", book)