#from utils import *
#from ..utils import *
#from tts_add_song import *
import wave,epub2txt,platform,os 
from pathlib import Path
def main():
    #original_file = "rothschild_1798_1848.pdf"
    
    #original_file = "jp_morgan.epub"
    original_file = "french_revolution.epub"
    narrate_start_file = 10
    gen_narration = 1
    add_song_and_sound = 0
    song = "dmitri.mp3"
    plane_sound ="plane_sound.mp3"

    functions_to_run = []
    functions_to_run.append([".pdf",pdf_to_txt])
    functions_to_run.append([".epub",epub_to_txt])
    txt_file = original_file
    for a in range(0,len(functions_to_run)):
        check = functions_to_run[a][0]
        if check in original_file:
            run = functions_to_run[a][1]
            run(original_file)
            txt_file = original_file.replace(check,".txt")
            break
    directory = txt_file.replace(".txt","")
    #os.startfile(txt_file)
    if gen_narration==1:
        edge_tts_to_mp3(directory,txt_file,narrate_start_file)
    if add_song_and_sound==1:
        add_song_sound(directory,song,"plane_sound.mp3")
    #print("u done jack!")

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
    print(f"Successfully generated {txt_file} from {epub_file}!")
    return txt_file

def edge_tts_to_mp3(directory,txt_file,start):
    import os
    import asyncio
    import edge_tts
    from tqdm import tqdm
    minutes_per_file=60
    with open(txt_file,"r",encoding="utf-8") as f:
        text=f.read()
    words=text.split()
    voice="en-US-GuyNeural"
    print("len(words)",len(words))
    words_per_file=minutes_per_file*150
    parts=(len(words)+words_per_file-1)//words_per_file
    for count in range(start-1,parts):
        begin=words_per_file*count
        end=min(words_per_file*(count+1),len(words))
        print(f"part {count+1}: words {begin} to {end}")
        chunk_text=" ".join(words[begin:end])
        if not chunk_text.strip():
            break
        part_number=count+1
        output_file=txt_file.replace(".txt","_part"+str(part_number)+".mp3")
        output_file=os.path.join(directory,output_file)
        print(f"generating {output_file} of {parts}")
        async def run_tts():
            communicate=edge_tts.Communicate(chunk_text,voice)
            with open(output_file,"wb") as f:
                with tqdm(total=len(chunk_text),desc=f"Part {part_number}/{parts}",unit="char",unit_scale=True) as pbar:
                    last_length=0
                    async for chunk in communicate.stream():
                        if chunk["type"]=="audio":
                            f.write(chunk["data"])
                            pbar.update(len(chunk["data"]))
        asyncio.run(run_tts())
    print("done")


"""
def edge_tts_to_mp3(directory,txt_file,start):
    #edge_tts_to_mp3(directory,txt_file,8,20)
    import os
    import asyncio
    import edge_tts
    minutes_per_file=60
    with open(txt_file,"r",encoding="utf-8") as f:
        text=f.read()
    words=text.split()
    voice="en-US-GuyNeural"
    print("len(words)",len(words))
    words_per_file=minutes_per_file*150
    parts=(len(words)+words_per_file-1)//words_per_file
    count=0
    while count<parts:
        begin=words_per_file*count
        end=words_per_file*(count+1)
        if end>len(words):
            end=len(words)
        print("part",count+1,"words",begin,"to",end)
        chunk_text=" ".join(words[begin:end])
        if chunk_text.strip()=="":
            break  
        part_number = count+1
        output_file=txt_file.replace(".txt","_part"+str(part_number)+".mp3")
        output_file=os.path.join(directory,output_file)
        async def run_tts():
            communicate=edge_tts.Communicate(chunk_text,voice)
            await communicate.save(output_file)
        if part_number>=start: 
            print("generating",output_file,"of",parts)
            asyncio.run(run_tts())
        count+=1
    print("done")
"""

def add_song_sound(directory,song,plane):
    #add_song_sound(directory,song,plane)
    #add_song_sound("part_003.mp3","dmitri.mp3","plane_sound.mp3")

    import subprocess, os
    def get_duration(file_path):
        cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        try: return float(res.stdout.strip())
        except: return 0
    def mix_audio_fast(main_file, v1, overlay1, v2, overlay2, v3, output_file):
        dur = get_duration(main_file)
        cmd = ['ffmpeg', '-y', '-i', main_file, '-stream_loop', '-1', '-t', str(dur), '-i', overlay1, '-stream_loop', '-1', '-t', str(dur), '-i', overlay2, '-filter_complex', f'[0:a]volume={v1}[a0];[1:a]volume={v2}[a1];[2:a]volume={v3}[a2];[a0][a1][a2]amix=inputs=3:duration=first:dropout_transition=0', '-c:a', 'libmp3lame', '-q:a', '4', output_file]
        subprocess.run(cmd)
    folder, dmitri, plane = directory, song, plane
    for i in range(1, 100):
        main_part = os.path.join(folder, directory+f"_part{i}.mp3")
        out_part = os.path.join(folder, directory+f"_part{i}_mixed.mp3")
        if os.path.exists(main_part):
            print(f"\nProcessing part {i}...")
            mix_audio_fast(main_part, 1.0, dmitri, 0.1, plane, 0.5, out_part)
    input("\nAll done! Press Enter to exit...")




import os
import subprocess

main()



"""
voice = "en-US-AriaNeural"
voice="en-US-GuyNeural"
or:
voice="en-US-ChristopherNeural"
Other male voices:

voice="en-US-EricNeural"
voice="en-US-RogerNeural"
voice="en-US-SteffanNeural"
"""