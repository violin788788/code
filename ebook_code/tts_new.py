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

from pathlib import Path
import subprocess
txtfile="french_revolution.txt"
basename="french_revolution"
words_per_part=9000
model="en_US-lessac-medium.onnx"
text=Path(txtfile).read_text(encoding="utf-8")
words=text.split()
parts=[words[i:i+words_per_part] for i in range(0,len(words),words_per_part)]
print("Total words:",len(words))
print("Total parts:",len(parts))
for i,part in enumerate(parts,1):
    print("Starting part",i,flush=True)
    text_part=" ".join(part)
    wavfile=f"{basename}_part_{i}.wav"
    mp3file=f"{basename}_part_{i}.mp3"
    subprocess.run(["piper","--model",model,"--output_file",wavfile],input=text_part.encode("utf-8"))
    subprocess.run(["ffmpeg","-y","-i",wavfile,mp3file])
    Path(wavfile).unlink()
    print("Created",mp3file,flush=True)
print("Done")


"""
!!! worked  !!!

from pathlib import Path
import subprocess
txtfile="french_revolution.txt"
basename="french_revolution"
words_per_part=9000
model="en_US-lessac-medium.onnx"
text=Path(txtfile).read_text(encoding="utf-8")
words=text.split()
parts=[words[i:i+words_per_part] for i in range(0,len(words),words_per_part)]
for i,part in enumerate(parts,1):
    print("working on part",str(i))
    part_text=" ".join(part)
    wavfile=f"{basename}_part_{i}.wav"
    mp3file=f"{basename}_part_{i}.mp3"
    subprocess.run(["piper","--model",model,"--output_file",wavfile],input=part_text.encode("utf-8"))
    if Path(wavfile).exists():
        subprocess.run(["ffmpeg","-y","-i",wavfile,mp3file])
        Path(wavfile).unlink()
        print(f"Created {mp3file}")
    else:
        print(f"Failed part {i}")

"""