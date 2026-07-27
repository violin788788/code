import sys,os
#new_path = os.path.join(a,b,c)
#cwd = os.getcwd()


from pydub import AudioSegment
from datetime import datetime
AudioSegment.converter = r".\ffmpeg.exe"
AudioSegment.ffprobe = r".\ffprobe.exe"
song = "dmi.mp3"
audio_book_folder = "proudhon"
#narrate_file = "part_13.mp3"
start = datetime.now()
sound1 = AudioSegment.from_mp3(song)
start_file = 15
end_file = 20
for a in range(start_file,end_file):
    narrate_file = os.path.join(audio_book_folder,"part_"+str(a)+".mp3")
    print("starting to gen")
    print(song+" and "+narrate_file)
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
    output_file = narrate_file.replace(".mp3","_")+song
    mixed_sound.export(output_file, format="mp3")
    end = datetime.now()
    difference = end - start
    print("time to gen file = ", difference)
    os.startfile(os.getcwd())