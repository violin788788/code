def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
import sys,os
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)

from pypdf import PdfReader

def pdf_to_txt(pdf_path, txt_path):
    # Load the PDF file
    reader = PdfReader(pdf_path)
    
    # Open the text file in write mode with UTF-8 encoding
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        # Loop through every page in the PDF
        for i, page in enumerate(reader.pages):
            print(i,len(reader.pages))
            text = page.extract_text()
            if text:
                txt_file.write(f"--- Page {i+1} ---\n")
                txt_file.write(text)
                txt_file.write("\n\n")

# Run the conversion
file_without_pdf_or_txt = "direkte"
pdf_to_txt(file_without_pdf_or_txt+".pdf",file_without_pdf_or_txt+".txt")
