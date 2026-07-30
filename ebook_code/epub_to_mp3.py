
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)

# pip install ebooklib beautifulsoup4 edge-tts
import asyncio
from pathlib import Path
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import edge_tts
# ---------------- SETTINGS ----------------
BOOK_NAME = "robert"          # without .epub
EPUB_FILE = BOOK_NAME + ".epub"
OUTPUT_DIR = BOOK_NAME + "_audio"
VOICE = "en-US-GuyNeural"
WORDS_PER_FILE = 9000
Path(OUTPUT_DIR).mkdir(exist_ok=True)
# ---------------- EXTRACT TEXT ----------------
book = epub.read_epub(EPUB_FILE)
chapters = []
for item in book.get_items():
    if item.get_type() == ITEM_DOCUMENT:
        soup = BeautifulSoup(item.get_content(), "html.parser")
        # Remove scripts/styles
        for tag in soup(["script", "style"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        if text:
            chapters.append(text)
full_text = "\n\n".join(chapters)
if not full_text.strip():
    raise Exception("No text found in EPUB.")
# ---------------- SPLIT INTO 9000-WORD CHUNKS ----------------
words = full_text.split()
print(f"Total words: {len(words)}")
chunks = [
    " ".join(words[i:i + WORDS_PER_FILE])
    for i in range(0, len(words), WORDS_PER_FILE)
]
print(f"Generating {len(chunks)} MP3 files...")
# ---------------- GENERATE MP3S ----------------
async def make_mp3(text, filename):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)
async def main():
    for i, chunk in enumerate(chunks, start=1):
        filename = f"{OUTPUT_DIR}/part_{i:03d}.mp3"
        print(f"Creating {filename}...")
        await make_mp3(chunk, filename)
asyncio.run(main())
print("Done!")




"""
# pip install ebooklib beautifulsoup4 edge-tts
import asyncio,sys
from pathlib import Path
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import edge_tts,os
#name without .pdf
#BOOK_NAME="lenin_socialism_and_war"
BOOK_NAME = "robert"
EPUB_FILE=BOOK_NAME+".epub"
OUTPUT_DIR=BOOK_NAME
Path(OUTPUT_DIR).mkdir(exist_ok=True)
VOICE="en-US-GuyNeural"
CHARS_PER_FILE=55000
book=epub.read_epub(EPUB_FILE)
text=" ".join(BeautifulSoup(i.get_content(),"html.parser").get_text(" ",strip=True) for i in book.get_items() if i.get_type()==ITEM_DOCUMENT)
len_text = len(text)
show(CHARS_PER_FILE)
show(len_text)
show(int(chars/CHARS_PER_FILE))
show(EPUB_FILE)
quit = 0
start = 0
part = 0
while(quit<1):
    part = part+1
    end = start+CHARS_PER_FILE
    if end>len(text):
        quit=1
    to_write = text[start:end]
    mp3_file = os.path.join(OUTPUT_DIR,"part_"+str(part)+".mp3") 
    show(mp3_file)
    async def make_mp3():
        await edge_tts.Communicate(to_write, "en-US-GuyNeural").save(mp3_file)
    asyncio.run(make_mp3())
    
    start = end


sys.exit()
"""