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


import numpy as np
import sounddevice as sd
# Frequencies for a C harmonica
NOTES = {
    1: 261.63,
    -1: 293.66,
    2: 329.63,
    -2: 349.23,
    3: 392.00,
    -3: 440.00,
    4: 523.25,
    -4: 493.88,
    5: 659.25,
    -5: 587.33,
    6: 783.99,
    -6: 698.46,
    7: 880.00,
    -7: 987.77,
    8: 1046.50,
    -8: 1174.66,
    9: 1318.51,
    -9: 1396.91,
    10: 1567.98,
    -10: 1760.00
}
SAMPLE_RATE = 44100
NOTE_LENGTH = 0.25
def play_note(frequency,duration=NOTE_LENGTH):
    t = np.linspace(0,duration,int(SAMPLE_RATE*duration),False)
    wave = np.sin(2*np.pi*frequency*t)
    fade = int(SAMPLE_RATE*0.02)
    wave[:fade] *= np.linspace(0,1,fade)
    wave[-fade:] *= np.linspace(1,0,fade)
    #wave *= 0.4
    wave *= 1.5
    sd.play(wave,SAMPLE_RATE)
    sd.wait()
def play_song(filename):
    with open(filename,"r") as file:
        text = file.read()
    notes = [int(x) for x in text.split()]
    for note in notes:
        if note not in NOTES:
            print(f"Unknown note: {note}")
            continue
        print(f"Playing {note}")
        play_note(NOTES[note])
play_song("harmonica-song.txt")