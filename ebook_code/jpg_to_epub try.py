from ebooklib import epub
from pathlib import Path

img_dir = Path("pages")
#img_dir = "pages"
book = epub.EpubBook()

book.set_identifier("scan")
book.set_title("Scanned Book")
book.set_language("en")

css = """
html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}
img {
    width: 100%;
    height: auto;
    display: block;
}
"""

book.add_item(epub.EpubItem(
    uid="style",
    file_name="style.css",
    media_type="text/css",
    content=css
))

chapters = []

for i, img_path in enumerate(sorted(img_dir.glob("*.jpg"))):
    img_name = img_path.name
    img_data = img_path.read_bytes()

    c = epub.EpubHtml(
        title=f"Page {i+1}",
        file_name=f"page_{i+1}.xhtml",
        lang="en"
    )

    c.content = f"""
    <html>
    <head>
        <link rel="stylesheet" href="style.css"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>
    <body>
        <img src="{img_name}"/>
    </body>
    </html>
    """

    book.add_item(epub.EpubItem(
        uid=img_name,
        file_name=img_name,
        media_type="image/jpeg",
        content=img_data
    ))

    book.add_item(c)
    chapters.append(c)
    print(i)

book.toc = tuple(chapters)
book.spine = ["nav"] + chapters

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

epub.write_epub("output.epub", book)