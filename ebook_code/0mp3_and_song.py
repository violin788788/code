
import os

from pydub import AudioSegment
AudioSegment.converter=r".\ffmpeg.exe"
AudioSegment.ffprobe=r".\ffprobe.exe"

audio1=AudioSegment.from_mp3("dmitri.mp3")-15
directory = "grant"
start_file = 6
end_file = 12

for a in range(start_file,end_file):
    print(directory,start_file,end_file)
    #print(a)
    part_file = os.path.join(directory,"part_"+str(a)+".mp3")
    audio2=AudioSegment.from_mp3(part_file)
    #mixed=audio1.overlay(audio2,loop=True)
    mixed=audio2.overlay(audio1,loop=True)
    output_file = os.path.join(directory,"grant_"+str(a)+".mp3")
    mixed.export(output_file,format="mp3")
    #print(a)




"""

import os,subprocess
from datetime import datetime
ffmpeg=r".\ffmpeg.exe"
song="dmitri.mp3"
audio_book_folder="grant"
start_file=6
end_file=12
for a in range(start_file,end_file+1):
    start_time=datetime.now()
    narrate_file=os.path.join(audio_book_folder,"part_"+str(a)+".mp3")
    output_file=narrate_file.replace("part","0"+audio_book_folder+"_part")
    print("generating")
    print(output_file)
    subprocess.run([ffmpeg,"-y","-i",narrate_file,"-stream_loop","-1","-i",song,"-filter_complex","[1:a]volume=0.18[bg];[0:a][bg]amix=inputs=2:duration=first","-c:a","libmp3lame","-q:a","2",output_file],check=True)
    end_time=datetime.now()
    print("time to gen file =",end_time-start_time)
os.startfile(os.getcwd())






import os,gc
from pydub import AudioSegment
from datetime import datetime
AudioSegment.converter=r".\ffmpeg.exe"
AudioSegment.ffprobe=r".\ffprobe.exe"
song="dmitri.mp3"
audio_book_folder="grant"
start_file=6
end_file=12
sound1=AudioSegment.from_mp3(song)
for a in range(start_file,end_file+1):
    start_time=datetime.now()
    narrate_file=os.path.join(audio_book_folder,"part_"+str(a)+".mp3")
    output_file=narrate_file.replace("part","0"+audio_book_folder+"_part")
    print("generating")
    print(output_file)
    sound2=AudioSegment.from_mp3(narrate_file)
    if len(sound1)>len(sound2):
        narration,bg_music=sound1,sound2
    else:
        narration,bg_music=sound2,sound1
    bg_music=bg_music-15
    mixed_sound=narration.overlay(bg_music,loop=True)
    mixed_sound.export(output_file,format="mp3")
    del sound2,narration,bg_music,mixed_sound
    gc.collect()
    end_time=datetime.now()
    print("time to gen file =",end_time-start_time)
os.startfile(os.getcwd())


import sys,os
#new_path = os.path.join(a,b,c)
#cwd = os.getcwd()
from pydub import AudioSegment
from datetime import datetime
AudioSegment.converter = r".\ffmpeg.exe"
AudioSegment.ffprobe = r".\ffprobe.exe"

song = "dmitri.mp3"
audio_book_folder = "grant"
start_file = 6
end_file = 12

#narrate_file = "part_13.mp3"
sound1 = AudioSegment.from_mp3(song)
for a in range(start_file,end_file+1):
    start_time = datetime.now()
    narrate_file = os.path.join(audio_book_folder,"part_"+str(a)+".mp3")
    output_file = narrate_file.replace("part","0"+audio_book_folder+"_part")

    #output_file = "0"+audio_book_folder+"_"+narrate_file.replace(".mp3","_")+song
    print("generating")
    print(output_file)
    #print(song+" and "+narrate_file)
    sound2 = AudioSegment.from_mp3(narrate_file)
    if len(sound1) > len(sound2):
        narration, bg_music = sound1, sound2
    else:
        narration, bg_music = sound2, sound1
    # Lower background music volume
    #bg_music = bg_music - 6
    #bg_music = bg_music - 12
    bg_music = bg_music - 15
    # Overlay with automatic looping (no huge repeated audio in memory)
    mixed_sound = narration.overlay(bg_music, loop=True)
    mixed_sound.export(output_file, format="mp3")
    end_time = datetime.now()
    time_difference = end_time - start_time
    print("time to gen file = ", time_difference)
    os.startfile(os.getcwd())

    """