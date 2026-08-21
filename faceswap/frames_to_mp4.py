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



import cv2
import os
frames_dir = "hope"
output_video = frames_dir+"_generated.mp4"
fps = 30
frames = sorted([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])
first_frame = cv2.imread(os.path.join(frames_dir, frames[0]))
height, width = first_frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
for frame in frames:
    image = cv2.imread(os.path.join(frames_dir, frame))
    video.write(image)
    print(frame)
video.release()
print(f"Created {output_video} from {len(frames)} frames.")
os.startfile(output_video)