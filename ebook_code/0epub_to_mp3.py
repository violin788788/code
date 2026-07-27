def show(what_to_show):
    #show(count)
    print(what_to_show)
# pip install ebooklib beautifulsoup4 edge-tts
import asyncio,sys
from pathlib import Path
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import edge_tts,os

#name without .pdf
with open("0book_to_work_on.txt", "r", encoding="utf-8") as file:
    BOOK_NAME = file.read()
    print(BOOK_NAME)
#BOOK_NAME="lenin_socialism_and_war"
EPUB_FILE=BOOK_NAME+".epub"

OUTPUT_DIR=BOOK_NAME
Path(OUTPUT_DIR).mkdir(exist_ok=True)
VOICE="en-US-GuyNeural"
CHARS_PER_FILE=55000
book=epub.read_epub(EPUB_FILE)
text=" ".join(BeautifulSoup(i.get_content(),"html.parser").get_text(" ",strip=True) for i in book.get_items() if i.get_type()==ITEM_DOCUMENT)
chars = len(text)
show(CHARS_PER_FILE)
show(chars)
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


pages=[]
current_page=1
for item in book.get_items():
    if item.get_type()==ITEM_DOCUMENT:
        soup=BeautifulSoup(item.get_content(),"html.parser")
        text=soup.get_text(separator=" ",strip=True)
        if text:
            pages.append((current_page,text))
            current_page+=1
chunks=[]
current_words=[]
start_page=1
for page_num,text in pages:
    words=text.split()
    if len(current_words)+len(words)>WORDS_PER_FILE and current_words:
        chunks.append((start_page,page_num-1," ".join(current_words)))
        current_words=[]
        start_page=page_num
    current_words.extend(words)
if current_words:
    chunks.append((start_page,pages[-1][0]," ".join(current_words)))
print(f"Total audio parts: {len(chunks)}")
Path(OUTPUT_DIR).mkdir(exist_ok=True)
print (EPUB_FILE)
async def generate():
    total=len(chunks)
    for i,(start,end,text) in enumerate(chunks,1):
        filename=Path(OUTPUT_DIR)/f"part_{i:03}_{start}_{end}.mp3"
        print(f"Generating {i}/{total}: {filename.name} ({len(text.split())} words)")
        await edge_tts.Communicate(text,VOICE).save(str(filename))
asyncio.run(generate())
print(f"Done! Generated {len(chunks)} MP3 files in '{OUTPUT_DIR}'.")