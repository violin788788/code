from gtts import gTTS
import os


def read_txt(file_path):
    # Add encoding='utf-8' here:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

    
text = read_txt("french_revolution.txt")
text = text[0:9000]

tts = gTTS(text, lang="en")
output_file = "output.mp3"
tts.save(output_file)
os.startfile(output_file)
