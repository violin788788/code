from ebooklib import epub
from pathlib import Path

img_dir = Path("pages_500")
book = epub.EpubBook()

book.set_title("Scan")
book.set_language("en")

chapters = []

for i, img_path in enumerate(sorted(img_dir.glob("*.jpg"))):
    print(i)
    img_name = img_path.name

    c = epub.EpubHtml(
        title=f"Page {i+1}",
        file_name=f"page_{i+1}.xhtml"
    )

    c.content = f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background: black;
        }}
        table {{
            width: 100%;
            height: 100%;
            border-collapse: collapse;
        }}
        td {{
            text-align: center;
            vertical-align: middle;
        }}
        img {{
            max-width: 100%;
            max-height: 100%;
        }}
    </style>
    </head>
    <body>
        <table>
            <tr>
                <td><img src="{img_name}"/></td>
            </tr>
        </table>
    </body>
    </html>
    """

    book.add_item(epub.EpubItem(
        uid=img_name,
        file_name=img_name,
        media_type="image/jpeg",
        content=img_path.read_bytes()
    ))

    book.add_item(c)
    chapters.append(c)

book.toc = tuple(chapters)
book.spine = ["nav"] + chapters
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

epub.write_epub("output.epub", book)