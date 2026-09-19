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

from pathlib import Path
import shutil
directory = "rename"
directory_files = os.listdir(directory)
for a in range(0,len(directory_files)):
    print(directory_files[a])
print(directory_files)
for a,val in enumerate(directory_files):
    print(a)
    old_file = os.path.join(directory,val)
    frame_number = str(a+100)
    how_many = len(frame_number)
    if how_many<6:
        for b in range(0,6-how_many):
            frame_number = "0"+frame_number
    new_file = os.path.join(directory,"frame_"+frame_number+".png")
    shutil.copy(old_file, new_file)
    os.remove(old_file)
    
    
    
# Rename the file
#old_file.rename("new_name.txt")