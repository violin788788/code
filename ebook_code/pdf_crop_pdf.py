import fitz,os,sys  # PyMuPDF
open_file = "cheka_cropped.pdf"
doc = fitz.open(open_file)
for i, page in enumerate(doc):
    rect = page.rect
    print(f"Page {i + 1}:")
    print(f"  Width:  {rect.width}")
    print(f"  Height: {rect.height}")
    print(f"  Full rect: {rect}")
    print(i)
#sys.exit()
doc = fitz.open(open_file)
for page in doc:
    width = page.rect.width
    height = page.rect.height
    # Remove 20% from top and bottom
    y0 = height * .1
    y1 = height * .99
    x0 = width * 0.01
    x1 = width * 0.99
    # Remove 5% from left and right
    #x0 = width * 0.05
    #x1 = width * 0.95
    crop = fitz.Rect(x0, y0, x1, y1)
    page.set_cropbox(crop)
out_file = "cheka_final.pdf"
doc.save(out_file)
os.startfile(out_file)
