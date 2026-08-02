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
from pydub import AudioSegment
# Load the two MP3 files

directory = "ten_days"

song_file = "dmitri.mp3"
sound1 = AudioSegment.from_mp3(song_file)

get_parts = os.listdir(directory)
for a,val in enumerate(get_parts):
    print(directory,val)
    try:
        part_file = os.path.join(directory,val)
    except:
        continue
    sound2 = AudioSegment.from_mp3(part_file)

    combined = song + part
# Export the result to a new MP3 file
    output_file = os.path.join(directory,directory+val)
    combined.export(output_file, format="mp3")
