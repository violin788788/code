#from utils import *
import sys,os
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)


def add_song(directory,song_file):
    #add_song("common_sense","dmitri.mp3"):
    import os
    import time
    import threading
    from pydub import AudioSegment
    #directory="common_sense"
    #song_file="dmitri.mp3"
    audio1=AudioSegment.from_mp3(song_file)
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
        combined.export(output_file,format="mp3")
        thread.join()
        print("saved",output_file,"length",len(combined)//1000,"seconds")
    os.startfile(directory)


add_song("common_sense","dmitri.mp3"):