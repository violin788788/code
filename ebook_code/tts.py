from utils import *
from piper import PiperVoice
import wave


txt_file = "french_revolution.txt"
minutes_per_file = 60


text = read_txt(txt_file)
words = text.split()
voice = PiperVoice.load("en_US-lessac-medium.onnx")
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
    output_file = txt_file.replace(".txt","_part"+str(count)+".wav")
    print("generating ",output_file)
    with wave.open(output_file, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
    #print("Done - output.wav created")



sys.exit()


with wave.open("output.wav", "wb") as wav_file:
    voice.synthesize_wav(text, wav_file)
print("Done - output.wav created")


"""
import pyttsx4,sys
engine = pyttsx4.init()


voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print("Voice", i)
    print("Name:", voice.name)
    print("ID:", voice.id)
    print()

#sys.exit()

#engine.setProperty('voice', 'english')

engine.setProperty('voice', 'english-us')


text_to_speak = "Welcome to your offline text to speech file on PythonAnywhere."
output_file = 'output.mp3'
engine.save_to_file(text_to_speak, output_file)
engine.runAndWait()
print(f"Success! Offline audio saved as {output_file}")
"""