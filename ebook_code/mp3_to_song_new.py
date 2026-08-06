

import os
import time
import threading
from pydub import AudioSegment
directory="common_sense"
song_file="dmitri.mp3"
audio1=AudioSegment.from_mp3(song_file)
def progress():
    start=time.time()
    while running:
        print("exporting...","time:",int(time.time()-start),"seconds")
        time.sleep(1)
for val in os.listdir(directory):
    if song_file in val:
        continue
    part_file=os.path.join(directory,val)
    audio2=AudioSegment.from_mp3(part_file)
    if len(audio1)>len(audio2):
        loops=(len(audio1)//len(audio2))+1
        audio2=(audio2*loops)[:len(audio1)]
    elif len(audio2)>len(audio1):
        loops=(len(audio2)//len(audio1))+1
        audio1=(audio1*loops)[:len(audio2)]
    combined=audio1.overlay(audio2)
    output_file=part_file.replace(".mp3","_"+song_file)
    print("creating",output_file)
    running=True
    thread=threading.Thread(target=progress)
    thread.start()
    combined.export(output_file,format="mp3")
    running=False
    thread.join()
    print("saved",output_file,"length",len(combined)//1000,"seconds")
os.startfile(directory)



"""
import os
from pydub import AudioSegment
directory="common_sense"
song_file="dmitri.mp3"
audio1=AudioSegment.from_mp3(song_file)
for val in os.listdir(directory):
    #print(val)
    if song_file in val:
        continue
    part_file=os.path.join(directory,val)
    #print("mixing",val)
    audio2=AudioSegment.from_mp3(part_file)
    if len(audio1)>len(audio2):
        loops=(len(audio1)//len(audio2))+1
        audio2=(audio2*loops)[:len(audio1)]
    elif len(audio2)>len(audio1):
        loops=(len(audio2)//len(audio1))+1
        audio1=(audio1*loops)[:len(audio2)]
    combined=audio1.overlay(audio2)
    output_file = part_file.replace(".mp3","_"+song_file)
    print("creating",output_file)
    combined.export(output_file,format="mp3")
    print("saved",output_file,"length",len(combined)//1000,"seconds")
os.startfile(directory)


"""