import sys
sys.path.insert(0, r"A:\Users\-\code")
from utils import *
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
#new_file = os.path.join(a,b,c)
drive = os.path.splitdrive(os.getcwd())[0]
cwd = os.getcwd()
files = os.listdir(cwd)

from pydub import AudioSegment
audio = AudioSegment.from_mp3("plane_sound.mp3")
# Repeat 20 times
looped = audio * 20
# Export as a new MP3
looped.export("plane_sound_new.mp3", format="mp3")