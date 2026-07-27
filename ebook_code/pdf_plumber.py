import pdfplumber

with pdfplumber.open("output.pdf") as pdf:
    # Inspect the first page
    page = pdf.pages[0]
    
    # Extract characters with bounding boxes (x0, top, x1, bottom)
    for char in page.chars[:50]:
        print(f"Char: {char['text']} | X: {char['x0']:.1f} | Y: {char['top']:.1f}")