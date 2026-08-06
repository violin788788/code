#from utils import *
#from ..utils import *
import wave,epub2txt,platform,os 
from pathlib import Path
def main():
    #original_file = "rothschild_1798_1848.pdf"
    original_file = "grant.epub"

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
    os.startfile(txt_file)
    txt_to_mp3(txt_file)
    #convert txt file to mp3s
    #that's it!
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
    print(f"Successfully converted {epub_file} to {txt_file}!")
    return txt_file
def txt_to_mp3(txt_file):
    #txt_to_mp3(txt_file)
    import os
    import asyncio
    import edge_tts
    minutes_per_file = 60
    with open(txt_file,"r",encoding="utf-8") as f:
        text=f.read()
    words = text.split()
    #voice = PiperVoice.load("en_US-lessac-medium.onnx")
    #voice = PiperVoice.load("en_US-ryan-medium.onnx")
    voice = "en-US-AriaNeural"
    print("len(words)",len(words))
    words_per_file =minutes_per_file*150
    parts = int(len(words)/words_per_file)
    quit = 0
    count = 0
    while(quit<1):
        count = count+1
        begin = words_per_file*count
        end = words_per_file*(count+1)
        if end>len(words):
            quit=1
            end=len(words)
        chunk_text = text[begin:end]
        #output_file = txt_file.replace(".txt","_part"+str(count)+".wav")
        ending = "_part"+str(count)+".mp3"
        output_file = txt_file.replace(".txt",ending)
        print("generating ",output_file,"of",parts)
        async def run_tts():
            communicate = edge_tts.Communicate(chunk_text, voice)
            await communicate.save(output_file)
        asyncio.run(run_tts())

        #with wave.open(output_file, "wb") as wav_file:
        #    voice.synthesize_wav(text, wav_file)
        #print("Done - output.wav created")
    

        """
        with open(txt_file,"r",encoding="utf-8") as f:
            text=f.read()
        output_file=txt_file.replace(".txt",".mp3")
        async def generate():
            voice="en-US-AriaNeural"
            communicate=edge_tts.Communicate(text,voice)
            await communicate.save(output_file)
        asyncio.run(generate())
        print("generated",output_file)
        os.startfile(output_file)
    




def pdf_to_txt(pdf):
    from pypdf import PdfReader
    #pdf="file.pdf"
    reader=PdfReader(pdf)
    text=""
    count = 0
    for page in reader.pages:
        count=count+1
        print("getting text from",pdf,"page",str(count),"of",len(reader.pages))
        text+=page.extract_text()+"\n"
    print(text)
    output_file = pdf.replace(".pdf",".txt")
    with open(output_file,"w",encoding="utf-8") as f:
        f.write(text)
    print("generated",output_file)
""" 

"""
def tts_win7(txt_file):
    minutes_per_file = 60
    text = read_txt(txt_file)
    words = text.split()
    #voice = PiperVoice.load("en_US-lessac-medium.onnx")
    #voice = PiperVoice.load("en_US-ryan-medium.onnx")
    voice = "en-US-AriaNeural"
    print("len(words)",len(words))
    words_per_file =minutes_per_file*150
    quit = 0
    count = 0
    while(quit<1):
        count = count+1
        begin = words_per_file*count
        end = words_per_file*(count+1)
        if end>len(words):
            quit=1
            end=len(words)
        chunk_text = text[begin:end]
        #output_file = txt_file.replace(".txt","_part"+str(count)+".wav")
        ending = "_part"+str(count)+".mp3"
        output_file = txt_file.replace(".txt",ending)
        print("generating ",output_file)
        async def run_tts():
            communicate = edge_tts.Communicate(chunk_text, voice)
            await communicate.save(output_file)
        asyncio.run(run_tts())

        #with wave.open(output_file, "wb") as wav_file:
        #    voice.synthesize_wav(text, wav_file)
        #print("Done - output.wav created")

def tts_linux(txt_file):
    from piper import PiperVoice
    minutes_per_file = 60
    text = read_txt(txt_file)
    words = text.split()
    #voice = PiperVoice.load("en_US-lessac-medium.onnx")
    voice = PiperVoice.load("en_US-ryan-medium.onnx")
    print("len(words)",len(words))
    words_per_file =minutes_per_file*150
    quit = 0
    count = 0
    while(quit<1):
        count = count+1
        begin = words_per_file*count
        end = words_per_file*(count+1)
        if end>len(words):
            quit=1
            end=len(words)
        chunk_text = text[begin:end]
        print("txt_file",txt_file)
        #output_file = txt_file.replace(".txt","_part"+str(count)+".wav")
        ending = "_part"+str(count)+".mp3"
        output_file = str(txt_file).replace(".txt",ending)
        print("output_file ",output_file)
        with wave.open(output_file, "wb") as wav_file:
            voice.synthesize_wav(chunk_text, wav_file)
        #print("Done - output.wav created")

def txt_to_txt(txt_file):
    return txt_file

def epub_to_txt(epub_file):
    #epub_to_txt("french_revolution.epub")
    import epub2txt
    txt_file = epub_file.replace(".epub",".txt")
    text_content = epub2txt.epub2txt(epub_file)
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(text_content)
    print(f"Successfully converted {epub_file} to {txt_file}!")
    return txt_file
    
def pdf_to_txt(pdf_file):
    import fitz
    txt_file = pdf_file.replace(".pdf",".txt")
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    cleaned_text = "\n".join([line for line in text.splitlines() if line.strip()])
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)
    return txt_file
#def epub_to_txt():
#    blank = "blank"

"""
main()