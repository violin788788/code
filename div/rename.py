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


directory = "rac26"
how_many_iterations = 3
start_frame = 0


print("click any button to confirm data below is correct and continue")
print(directory,"= directory")
print(how_many_iterations,"= how_many_iterations")
print(start_frame,"= start_frame")
input()
directory_files = os.listdir(directory)
for a in range(0,len(directory_files)):
    print(directory_files[a])
print(directory_files)
frame_number = 0
Path(directory+"\\new").mkdir(exist_ok=True)
for a in range(0,how_many_iterations):
    for b,val in enumerate(directory_files):
        old_file = os.path.join(directory,val)
        frame_number = frame_number+1
        frame_number_string = str(frame_number)
        print("new frame",frame_number_string)
        how_many = len(frame_number_string)
        if how_many<6:
            for b in range(0,6-how_many):
                frame_number_string = "0"+frame_number_string
        new_file = os.path.join(directory,"new","frame_"+frame_number_string+".png")
        try:
            shutil.copy(old_file, new_file)
        except:
            print("error",new_file)
            continue
        #os.remove(old_file)
    #os.remove(old_file)
    
    
# Rename the file
#old_file.rename("new_name.txt")