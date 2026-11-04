#from utils import *
import os
from pathlib import Path
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

file_to_count = "jp_morgan.pdf"


def pdf_to_txt(pdf):
    import fitz
    doc=fitz.open(pdf)
    print("pages:",len(doc))
    text=""
    for i,page in enumerate(doc):
        print("getting page",i+1,"of",len(doc))
        text+=page.get_text()+"\n"
    output_file=pdf.replace(".pdf",".txt")
    with open(output_file,"w",encoding="utf-8") as f:
        f.write(text)
    print("generated",output_file)
def epub_to_txt(epub_file):
    #epub_to_txt("french_revolution.epub")
    import epub2txt
    txt_file = epub_file.replace(".epub",".txt")
    text_content = epub2txt.epub2txt(epub_file)
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(text_content)
    print(f"Successfully converted {epub_file} to {txt_file}!")
    return txt_file


def read_txt(file_path):
    #read_txt("song.txt")
    #text = read_txt("file.txt")
    # Add encoding='utf-8' here:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content



if ".pdf" in file_to_count:
    pdf_to_txt(file_to_count)
if ".epub" in file_to_count:
    epub_to_txt(file_to_count)
get = file_to_count
get = Path(file_to_count).with_suffix(".txt")
text = read_txt(get)
number_of_spaces = text.count(" ")
number_of_new_lines = text.count("\n")
words = number_of_spaces+number_of_new_lines
print("words = ",words)