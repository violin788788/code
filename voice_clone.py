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


from TTS.api import TTS
tts=TTS("tts_models/multilingual/multi-dataset/your_tts")
tts.tts_to_file(
    text="Hello, this is a voice cloning test.",
    speaker_wav="myvoice.wav",
    language="en",
    file_path="output.wav"
)