
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



import asyncio
import subprocess
from pathlib import Path
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import edge_tts

BOOK_NAME="french_revolution"
EPUB_FILE=BOOK_NAME+".epub"
OUTPUT_DIR=BOOK_NAME+"_audio"
VOICE="en-US-GuyNeural"
WORDS_PER_FILE=9000
SONG="dmitri.mp3"
FFMPEG=r".\ffmpeg.exe"
MUSIC_VOLUME=0.18

Path(OUTPUT_DIR).mkdir(exist_ok=True)

book=epub.read_epub(EPUB_FILE)
chapters=[]
for item in book.get_items():
    if item.get_type()==ITEM_DOCUMENT:
        soup=BeautifulSoup(item.get_content(),"html.parser")
        for tag in soup(["script","style"]):
            tag.decompose()
        text=soup.get_text(separator=" ",strip=True)
        if text:
            chapters.append(text)

full_text="\n\n".join(chapters)
if not full_text.strip():
    raise Exception("No text found in EPUB.")

words=full_text.split()
print(f"Total words: {len(words)}")
chunks=[" ".join(words[i:i+WORDS_PER_FILE]) for i in range(0,len(words),WORDS_PER_FILE)]
print(f"Generating {len(chunks)} MP3 files...")

async def make_mp3(text,filename):
    communicate=edge_tts.Communicate(text,VOICE)
    await communicate.save(filename)

def add_background_music(input_file,output_file):
    cmd=[
        FFMPEG,
        "-y",
        "-i",input_file,
        "-stream_loop","-1",
        "-i",SONG,
        "-filter_complex",f"[1:a]volume={MUSIC_VOLUME}[bg];[0:a][bg]amix=inputs=2:duration=first:dropout_transition=2",
        "-map_metadata","-1",
        "-c:a","libmp3lame",
        "-b:a","128k",
        output_file
    ]
    subprocess.run(cmd,check=True)

async def main():
    for i,chunk in enumerate(chunks,start=1):
        raw_file=f"{OUTPUT_DIR}/french_{i:03d}.mp3"
        final_file=f"{OUTPUT_DIR}/{BOOK_NAME}_{i:03d}.mp3"
        print(f"Creating {raw_file}...")
        await make_mp3(chunk,raw_file)
        print(f"Adding music...")
        add_background_music(raw_file,final_file)
        Path(raw_file).unlink()

asyncio.run(main())
print("Done!")