#from utils import *
#from ..utils import *
#from tts_add_song import *
import wave,epub2txt,platform,os 
from pathlib import Path
def main():
    #original_file = "rothschild_1798_1848.pdf"
    
    original_file = "jp_morgan.epub"
    start_file = 0
    gen_narration = "no"
    add_song_and_sound = "yes"
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
    if gen_narration=="yes":
        edge_tts_to_mp3(directory,txt_file,start_file)
    if add_song_and_sound=="yes":
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


def add_song_sound(directory,song,plane):
    #add_song_sound(directory,song,plane)
    #add_song_sound("part_003.mp3","dmitri.mp3","plane_sound.mp3")
    from pydub import AudioSegment
    from tqdm import tqdm
    import math
    files = os.listdir(directory)
    for a,val in enumerate(files):
        narrate_file=os.path.join(directory,val)
        print(f"working on {narrate_file},{song},and {plane}!")
        tracks = [
            (narrate_file, 1.0),
            (song, 0.3),
            (plane, 1.0),
        ]
        audio_tracks = []
        for filename, volume in tracks:
            audio = AudioSegment.from_mp3(filename)
            if volume != 1.0:
                audio = audio.apply_gain(20 * math.log10(volume))
            audio_tracks.append(audio)
        target_length = max(len(audio) for audio in audio_tracks)
        def loop_to_length(audio, length):
            repeats = (length // len(audio)) + 1
            return (audio * repeats)[:length]
        audio_tracks = [loop_to_length(audio, target_length) for audio in audio_tracks]
        chunk_size = 1000
        mixed = AudioSegment.empty()
        out_file = tracks[0][0]+"_"+tracks[1][0]
        out_file = out_file.replace(".mp3","")+".mp3"
        out_file=os.path.join(directory,out_file)
        print("working on",out_file)
        for position in tqdm(range(0, target_length, chunk_size), desc="Mixing", unit="sec"):
            chunk = audio_tracks[0][position:position + chunk_size]
            for audio in audio_tracks[1:]:
                chunk = chunk.overlay(audio[position:position + chunk_size])
            mixed += chunk
        mixed.export(out_file, format="mp3")



    """
def add_song(directory,song_file):
    #main_file=os.path.abspath(song_file)
    for val in os.listdir(directory):
        if song_file in val:
            continue
        narrate_file=os.path.join(directory,val)
        output_file=narrate_file.replace(".mp3","_"+song_file)
        print("mixing",narrate_file)
        command=[
            "ffmpeg",
            "-y",
            "-i",narrate_file,
            "-stream_loop","-1",
            "-vn",
            "-i",song_file,
            "-filter_complex",
            "[0:a]volume=1.0[a0];[1:a]volume=0.2[a1];[a0][a1]amix=inputs=2:duration=first",
            "-c:a","libmp3lame",
            "-q:a","2",
            output_file
        ]
        subprocess.run(command)
        print("saved",output_file)
    os.startfile(directory)
    """



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