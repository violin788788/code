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

import ebooklib
from ebooklib import epub
from RealtimeTTS import TextToAudioStream, SystemEngine

# Load epub and extract text paragraphs...
# Feed text into a live audio stream for playback:
engine = SystemEngine()
stream = TextToAudioStream(engine)
stream.feed("Your extracted book text goes here...")
stream.play_async()