import sys, os
#new_file = os.path.join(a,b,c)
#cwd = os.getcwd()
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
def count_epub_words_by_page(epub_path, start_page, end_page, words_per_page=300):
    book = epub.read_epub(epub_path)
    full_text = []
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), "html.parser")
        full_text.append(soup.get_text())
    combined_text = "".join(full_text)
    words = combined_text.split()
    start_idx = (start_page - 1) * words_per_page
    end_idx = end_page * words_per_page
    target_words = words[start_idx:end_idx]
    print("book =", epub_path)
    print("start_page =", start_page)
    print("end_page =", end_page)
    print("target_words =", len(target_words))
    #return len(target_words)
print(count_epub_words_by_page("volodarsky.epub", start_page=1, end_page=500))
print(count_epub_words_by_page("volodarsky.epub", start_page=1, end_page=450))
print(count_epub_words_by_page("volodarsky.epub", start_page=1, end_page=50))
