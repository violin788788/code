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



import wave
from piper.voice import PiperVoice

# Path to your downloaded ONNX model and config file
model_path = "en_US-lessac-medium.onnx"
config_path = "en_US-lessac-medium.onnx.json"

# Load the voice model
voice = PiperVoice.load(model_path, config_path)

# Text you want to convert to speech
text = "Hello! This is a local text to speech test using Piper."

# Open a wave file to save the output audio
with wave.open("output.wav", "wb") as wav_file:
    voice.synthesize(text, wav_file)

print("Audio saved to output.wav")