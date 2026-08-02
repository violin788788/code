from utils import *
from gtts import gTTS


file = "french_revolution.txt"
len_portion = 55000


text = read_txt(file)
len_text = len(text)
print(len_text)
parts = math.ceil(len_text/len_portion)
print(parts)

tts = gTTS(text, lang="en")
for a in range(0,parts):
    portion = text[a*len_portion:(a+1)*len_portion]
    output_file = file.replace(".txt","")+"_part"+str(a+1)+".mp3"
    print(output_file)
    tts.save(output_file)
    #os.startfile(output_file)
