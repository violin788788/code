import sys,os
#sys.path.insert(0, r"A:\Users\-\code")
#from utils import *
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
#new_file = os.path.join(a,b,c)
drive = os.path.splitdrive(os.getcwd())[0]
cwd = os.getcwd()
files = os.listdir(cwd)

import os, io, re, openpyxl, ebooklib, PIL.Image
from bs4 import BeautifulSoup
from ebooklib import epub
wb, files, row = openpyxl.Workbook(), os.listdir(os.path.dirname(os.path.abspath(__file__))), 2
ws = wb.active; ws.append(["Title", "Author", "Year", "Words (Thousands)", "Cover"])
for a in range(0, len(files)):
    if ".epub" in files[a]:
        print("working on", files[a]); b = epub.read_epub(files[a])
        t = b.get_metadata('DC', 'title')[0] if b.get_metadata('DC', 'title') else files[a]
        au = b.get_metadata('DC', 'creator')[0] if b.get_metadata('DC', 'creator') else "Unknown"
        d = b.get_metadata('DC', 'date')[0] if b.get_metadata('DC', 'date') else "Unknown"
        yr = re.search(r'\b\d{4}\b', str(d)).group(0) if re.search(r'\b\d{4}\b', str(d)) else "Unknown"
        w = sum(len(re.findall(r'\b\w+\b', BeautifulSoup(i.get_content(), 'html.parser').get_text())) for i in b.get_items() if i.get_type() == ebooklib.ITEM_DOCUMENT)
        cov = b.get_item_with_id('cover-image')
        ws.cell(row=row, column=1, value=str(t)), ws.cell(row=row, column=2, value=str(au)), ws.cell(row=row, column=3, value=str(yr)), ws.cell(row=row, column=4, value=round(w / 1000, 2)), ws.row_dimensions[row].__setattr__('height', 80)
        if cov: img = PIL.Image.open(io.BytesIO(cov.get_content())); img.thumbnail((100, 100)); out = io.BytesIO(); img.save(out, format="PNG"); out.seek(0); xl_img = openpyxl.drawing.image.Image(out); xl_img.anchor = f"E{row}"; ws.add_image(xl_img)
        row += 1
wb.save("books_manifest.xlsx")
