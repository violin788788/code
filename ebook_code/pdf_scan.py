from pypdf import PdfReader


from pypdf import PdfReader
import sys

#inspect("lenin.pdf")

def inspect(pdf_path):
    r = PdfReader(pdf_path)

    print("FILE:", pdf_path)
    print("Encrypted:", r.is_encrypted)
    print("Pages:", len(r.pages))
    print("PDF Version:", r.pdf_header)

    #sys.exit()

    for i, page in enumerate(r.pages):
        print("\n--- PAGE", i+1, "---")

        mb = page.mediabox
        print("Size:", float(mb.width), "x", float(mb.height))

        # rotation
        print("Rotation:", page.get("/Rotate"))

        # resources (images/fonts/etc)
        res = page.get("/Resources", {})
        xobj = res.get("/XObject", {})
        print("XObjects:", len(xobj))

        if xobj:
            for k in xobj:
                try:
                    obj = xobj[k]
                    print("  -", k, obj.get("/Subtype"))
                except:
                    pass



inspect("lenin.pdf")

#inspect("output.pdf")

"""

reader = PdfReader("output.pdf")

for i, page in enumerate(reader.pages):
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    print(f"Page {i+1}: {w} x {h}")

    """