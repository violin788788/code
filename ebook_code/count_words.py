#from utils import *
import os
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

file_path = "jp_morgan.pdf"


from pathlib import Path
from pypdf import PdfReader
from ebooklib import epub
from bs4 import BeautifulSoup
import re
def count_words(text):
    words = re.findall(r"\b[\w'-]+\b", text)
    return len(words)
def count_pdf_words(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return count_words(text)
def count_epub_words(file_path):
    book = epub.read_epub(file_path)
    text = ""
    for item in book.get_items():
        if item.get_type() == 9:
            soup = BeautifulSoup(item.get_content(), "html.parser")
            text += soup.get_text(separator=" ") + "\n"
    return count_words(text)
def count_book_words(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    extension = file_path.suffix.lower()
    if extension == ".pdf":
        return count_pdf_words(file_path)
    elif extension == ".epub":
        return count_epub_words(file_path)
    else:
        raise ValueError("Only PDF and EPUB files are supported.")
word_count = count_book_words(file_path)
print(f"Word count: {word_count:,}")
