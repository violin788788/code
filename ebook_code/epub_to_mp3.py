
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



BOOK_NAME = "french_revolution"          # without .epub
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


