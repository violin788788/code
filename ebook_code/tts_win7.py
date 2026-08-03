from utils import *
import sys,os
import asyncio, edge_tts
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)

txt_file = "french_revolution.txt"

#def tts_linux(txt_file):
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
    words = text[begin:end]
    #output_file = txt_file.replace(".txt","_part"+str(count)+".wav")
    output_file = txt_file.replace(".txt","_part"+str(count)+".mp3")
    print("generating ",output_file)
    async def run_tts():
        communicate = edge_tts.Communicate(words, voice)
        await communicate.save(output_file)
    asyncio.run(run_tts())

    #with wave.open(output_file, "wb") as wav_file:
    #    voice.synthesize_wav(text, wav_file)
    #print("Done - output.wav created")
