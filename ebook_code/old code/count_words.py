
import fitz

def count_words_with_pymupdf(epub_path):
    doc = fitz.open(epub_path)
    total_words = 0

    for page in doc:
        print (page)
        text = page.get_text()
        total_words += len(text.split())

    return total_words

file_name = "cheka"

print(count_words_with_pymupdf(file_name+".epub"))



"""


import pymupdf

def count_words_with_pymupdf(epub_path):
    doc = pymupdf.open(epub_path)
    total_words = 0
    
    # Iterate through every page layout parsed from the ebook
    for page in doc:
        text = page.get_text()
        total_words += len(text.split())
        
    return total_words

# Example Usage:
print("Total words:", count_words_with_pymupdf("cheka.epub"))


"""