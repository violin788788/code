from utils import *
#from piper import PiperVoice
import wave,epub2txt,platform
from pathlib import Path
def tts_win7():
    blank = "blank"
def tts_linux(txt_file):
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
        words = text[begin:end]
        #output_file = txt_file.replace(".txt","_part"+str(count)+".wav")
        output_file = txt_file.replace(".txt","_part"+str(count)+".mp3")
        print("generating ",output_file)
        with wave.open(output_file, "wb") as wav_file:
            voice.synthesize_wav(text, wav_file)
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
convert_to_txt = {}
convert_to_txt[".txt"] = ""
convert_to_txt[".epub"] = epub_to_txt
convert_to_txt[".pdf"] = pdf_to_txt
gen_function = {}
gen_function["Linux"] = tts_win7
gen_function["Windows"] = tts_linux

file_to_generate = "french_revolution.txt"

txt_file = ""
file_type = Path(file_to_generate).suffix
for key, value in convert_to_txt.items():
    if file_type == key:
        if callable(value):
            txt_file = value(file_to_generate)
system = platform.system()
print(system)
for key, value in gen_function.items():
    if system == key:
        if callable(value):
            value(txt_file)