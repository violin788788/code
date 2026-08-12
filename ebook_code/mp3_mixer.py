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
from tqdm import tqdm
import math
tracks = [
    ("part_003.mp3", 1.0),
    ("dmitri.mp3", 0.3),
    ("plane_sound.mp3", 0.3),
]
audio_tracks = []
for filename, volume in tracks:
    audio = AudioSegment.from_mp3(filename)
    if volume != 1.0:
        audio = audio.apply_gain(20 * math.log10(volume))
    audio_tracks.append(audio)
target_length = max(len(audio) for audio in audio_tracks)
def loop_to_length(audio, length):
    repeats = (length // len(audio)) + 1
    return (audio * repeats)[:length]
audio_tracks = [loop_to_length(audio, target_length) for audio in audio_tracks]
chunk_size = 1000
mixed = AudioSegment.empty()
for position in tqdm(range(0, target_length, chunk_size), desc="Mixing", unit="sec"):
    chunk = audio_tracks[0][position:position + chunk_size]
    for audio in audio_tracks[1:]:
        chunk = chunk.overlay(audio[position:position + chunk_size])
    mixed += chunk
out_file = tracks[0][0]+"_"+tracks[1][0]
out_file = out_file.replace(".mp3","")+".mp3"
print(out_file)
mixed.export(out_file, format="mp3")
