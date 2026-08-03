from utils import *
from piper import PiperVoice
import wave,epub2txt

def epub_to_txt():
    blank = "blank"

def pdf_to_txt():
    blank = "blank"

#def epub_to_txt():
#    blank = "blank"



file_to_generate = "french_revolution.txt"

if ".txt" in file_to_generate:
    #convert from .txt
    blank = "blank"
if ".epub" in file_to_generate:
    import epub2txt
    # Define file paths
    epub_file = "sample.epub"
    txt_file = "output.txt"
    # Extract text content from the EPUB file
    # The library supports both local paths and web URLs
    text_content = epub2txt.epub2txt(epub_file)
    # Save the plain text to a file using UTF-8 encoding
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(text_content)
    print(f"Successfully converted {epub_file} to {txt_file}!")

    #convert to .txt and gen?
    blank = "blank"
if ".pdf" in file_to_generate:
    import fitz
    doc = fitz.open("sample.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    cleaned_text = "\n".join([line for line in text.splitlines() if line.strip()])
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    #convert to .txt and gen?
    blank = "blank"
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



sys.exit()