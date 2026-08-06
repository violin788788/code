#from utils import *
import sys,os
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)
import os
import subprocess



def add_song(directory,song_file):
    #main_file=os.path.abspath(song_file)
    for val in os.listdir(directory):
        if song_file in val:
            continue
        narrate_file=os.path.join(directory,val)
        output_file=narrate_file.replace(".mp3","_"+song_file)
        print("mixing",narrate_file)
        command=[
            "ffmpeg",
            "-y",
            "-i",narrate_file,
            "-stream_loop","-1",
            "-vn",
            "-i",song_file,
            "-filter_complex",
            "[0:a]volume=1.0[a0];[1:a]volume=0.2[a1];[a0][a1]amix=inputs=2:duration=first",
            "-c:a","libmp3lame",
            "-q:a","2",
            output_file
        ]
        subprocess.run(command)
        print("saved",output_file)
    os.startfile(directory)




#add_song("ten_days","dmitri.mp3")










"""
def add_song(directory,song_file):
    main_file=os.path.abspath(song_file)
    for val in os.listdir(directory):
        if song_file in val:
            continue
        narrate_file=os.path.join(directory,val)
        output_file=narrate_file.replace(".mp3","_"+song_file)
        print("mixing",narrate_file)
        command=[
            "ffmpeg",
            "-y",
            "-i",narrate_file,
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

