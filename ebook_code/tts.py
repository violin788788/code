from utils import *
#from piper import PiperVoice
import wave,epub2txt,platform
def tts_win7():
    blank = "blank"
def tts_linux():
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
def epub_to_txt(epub_file):
    #epub_to_txt("french_revolution.epub")
    import epub2txt
    txt_file = epub_file.replace(".epub",".txt")
    text_content = epub2txt.epub2txt(epub_file)
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(text_content)
    print(f"Successfully converted {epub_file} to {txt_file}!")
def pdf_to_txt(pdf_file):
    import fitz
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    cleaned_text = "\n".join([line for line in text.splitlines() if line.strip()])
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)

#def epub_to_txt():
#    blank = "blank"
convert_to_txt = {}
# Add a key called "name" with the value "Alice"
convert_to_txt[".txt"] = ""
convert_to_txt[".epub"] = epub_to_txt
convert_to_txt[".pdf"] = pdf_to_txt

print(convert_to_txt)


file_to_generate = "french_revolution.txt"

for key, value in convert_to_txt.items():
    print(f"{key}: {value}")
    if key in file_to_generate:
        print(key)
        action_dict[key]()

sys.exit()

if ".txt" not in file_to_generate:
    convert = convert
system = platform.system()
print(system)
if system=="Linux":
    tts_linux()
if system=="Windows":
    tts_win7()



"""
file_to_generate = "french_revolution.txt"

if ".txt" not in file_to_generate:




if ".pdf" in file_to_generate:




sys.exit()
"""