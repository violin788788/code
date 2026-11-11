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

from moviepy.editor import VideoFileClip

# 1. Load the target MP4 file
file = "des.mp4"
clip = VideoFileClip(file)
# 2. Rotate the video clockwise by degrees (e.g., 90, 180, 270)
# Use negative numbers for counter-clockwise rotation (e.g., -90)
rotated_clip = clip.rotate(90)
# 3. Export the newly rotated video (audio is automatically preserved)
file_rotated = file.replace(".mp4","_rotated.mp4")
rotated_clip.write_videofile(file_rotated)
# 4. Close the clips to release system resources
clip.close()
rotated_clip.close()
os.startfile(file_rotated)
