import ebooklib
from ebooklib import epub

# Load the epub file
book = epub.read_epub('output.epub')

# 1. Get standard metadata (e.g., Title, Language)
title = book.get_metadata('DC', 'title')
language = book.get_metadata('DC', 'language')
print(f"Title: {title}")
print(f"Language: {language}")

# 2. Get Table of Contents
toc = book.toc
for item in toc:
    print(f"TOC Item: {item.title}")

# 3. Get spine (reading order)
spine = book.spine
print(f"Spine order: {spine}")

# 4. Extract document items (HTML text, images, styles)
for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    print(f"Chapter/Document: {item.get_name()}")
