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


from deep_translator import GoogleTranslator
translator=GoogleTranslator(source="de",target="en")
with open("direkte.txt","r",encoding="utf-8") as f:
    text=f.read()
part=1
files=[]
while text:
    chunk=text[:4900]
    text=text[4900:]
    translated=translator.translate(chunk)
    filename=f"direkte_english_part{part}.txt"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(translated)
    files.append(filename)
    print(f"Translated part {part}")
    part+=1
with open("direkte_english.txt","w",encoding="utf-8") as output:
    for filename in files:
        with open(filename,"r",encoding="utf-8") as f:
            output.write(f.read())
print(f"Done. Created {len(files)} parts and combined them into direkte_english.txt")


"""
from deep_translator import GoogleTranslator
translator=GoogleTranslator(source="de",target="en")
with open("direkte.txt","r",encoding="utf-8") as f:
    text=f.read()
part=1
while text:
    chunk=text[:4900]
    text=text[4900:]
    translated=translator.translate(chunk)
    with open(f"direkte_part{part}.txt","w",encoding="utf-8") as f:
        f.write(translated)
    print(f"Translated part {part}")
    part+=1
print(f"Created {part-1} translated parts.")
"""