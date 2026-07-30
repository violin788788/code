import sys,os
#new_path = os.path.join(a,b,c)
#cwd = os.getcwd()
from pydub import AudioSegment
from datetime import datetime
AudioSegment.converter = r".\ffmpeg.exe"
AudioSegment.ffprobe = r".\ffprobe.exe"

song = "dmi.mp3"
audio_book_folder = "volodarsky"
start_file = 18
end_file = 22

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