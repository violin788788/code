import sys
sys.path.insert(0, r"A:\\Users\\-\\code")
from utils import *
from pathlib import Path
import wave,epub2txt,platform,os 
def main(original_file, gen_narration=0, add_song_and_sound=0, narrate_start_file=1, song="dmitri.mp3", plane_sound="plane_sound.mp3"):
    functions_to_run = []
    functions_to_run.append([".pdf", pdf_to_txt])
    functions_to_run.append([".epub", epub_to_txt])
    file_path = Path(original_file)
    suffix = file_path.suffix
    for a,val in enumerate(functions_to_run):
        if suffix in val[0]:
            val[1](original_file)
            break
    directory = original_file.replace(suffix,"")
    txt_file = original_file.replace(suffix,".txt")
    print("directory",directory)
    print("txt_file",txt_file)
    #sys.exit()

    if gen_narration == 1:
        edge_tts_to_mp3(directory, txt_file, narrate_start_file)
    if add_song_and_sound == 1:
        add_song_sound(directory, song, plane_sound)

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
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
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
    #folder, dmitri, plane = directory, song, plane
    files = os.listdir(directory)
    for a,val in enumerate(files):
    #for i in range(1, 100):
        part_number = a+1
        main_part = os.path.join(directory, directory+f"_part{part_number}.mp3")
        out_part = os.path.join(directory, directory+f"_part{part_number}_mixed.mp3")
        #if os.path.exists(main_part):
        print(f"\nProcessing part {part_number}...")
        mix_audio_fast(main_part, 1.0, song, 0.1, plane, 0.5, out_part)
    input("\nAll done! Press Enter to exit...")




import tkinter as tk
from tkinter import filedialog
from text_to_speech import main
def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("EPUB/PDF", "*.epub *.pdf")])
    file_label.config(text=selected_file)
def run():
    main(selected_file,int(generate_var.get()),int(song_var.get()),int(start_file.get()),song.get(),plane_sound.get())
selected_file=""
root=tk.Tk()
root.title("gen mp3 and add song to it")
root.geometry("500x400")
tk.Button(root,text="Select File",command=select_file).pack(pady=10)
file_label=tk.Label(root,text="No file selected")
file_label.pack()
generate_var=tk.IntVar()
song_var=tk.IntVar()
tk.Checkbutton(root,text="Generate Narration(if applicable?)",variable=generate_var).pack()
tk.Checkbutton(root,text="Add Song to Narration",variable=song_var).pack()
tk.Label(root,text="Narrate Start File").pack()
start_file=tk.Entry(root)
start_file.insert(0,"1")
start_file.pack()
tk.Label(root,text="Song").pack()
song=tk.Entry(root)
song.insert(0,"dmitri.mp3")
song.pack()
tk.Label(root,text="Plane Sound").pack()
plane_sound=tk.Entry(root)
plane_sound.insert(0,"plane_sound.mp3")
plane_sound.pack()
tk.Button(root,text="RUN",command=run).pack(pady=20)
root.mainloop()

