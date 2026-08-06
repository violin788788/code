#from utils import *
import sys,os
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)
import os
import subprocess

import os
import subprocess
def add_song(directory,song_file):
    main_file=os.path.abspath(song_file)
    for val in os.listdir(directory):
        if song_file in val:
            continue
        part_file=os.path.join(directory,val)
        output_file=part_file.replace(".mp3","_"+song_file)
        print("mixing",part_file)
        command=[
            "ffmpeg",
            "-y",
            "-i",part_file,
            "-stream_loop","-1",
            "-vn",
            "-i",main_file,
            "-filter_complex",
            "[0:a][1:a]amix=inputs=2:duration=first",
            "-c:a","libmp3lame",
            "-q:a","2",
            output_file
        ]
        subprocess.run(command)
        print("saved",output_file)
    os.startfile(directory)


    
add_song("ten_days","dmitri.mp3")



"""
def add_song(directory,song_file):
    import os
    import subprocess
    for val in os.listdir(directory):
        if song_file in val:
            continue
        if not val.lower().endswith(".mp3"):
            continue
        part_file=os.path.join(directory,val)
        output_file=part_file.replace(".mp3","_"+song_file)
        print("mixing",part_file)
        cmd=[
            "ffmpeg",
            "-i",song_file,
            "-stream_loop","-1",
            "-i",part_file,
            "-filter_complex",
            "[1:a]aloop=loop=-1:size=2e+09[a1];[0:a][a1]amix=inputs=2:duration=longest",
            "-y",
            output_file
        ]
        subprocess.run(cmd)
        print("saved",output_file)
    os.startfile(directory)
add_song("common_sense","dmitri.mp3")



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
        print("getting",part_file)
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
        print("saved",output_file,"length",len(combined)//1000,"seconds")
    os.startfile(directory)


add_song("ten_days","dmitri.mp3")

"""