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

from utils import *
from piper import PiperVoice
import wave


txt_file = "french_revolution.txt"
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