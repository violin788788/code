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
drive = os.path.splitdrive(os.getcwd())[0]
cwd = os.getcwd()
files = os.listdir(cwd)
import cv2
import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
mp4 = filedialog.askopenfilename(title="Select MP4 video",filetypes=[("MP4 files","*.mp4"),("All files","*.*")])
root.destroy()
if not mp4:
    print("No video selected.")
    sys.exit()
output_dir = os.path.splitext(mp4)[0]
os.makedirs(output_dir, exist_ok=True)
cap = cv2.VideoCapture(mp4)
frame_number = 0
while True:
    success, frame = cap.read()
    if not success:
        break
    filename = os.path.join(output_dir, f"frame_{frame_number:06d}.jpg")
    cv2.imwrite(filename, frame)
    frame_number += 1
    print("frame_number", frame_number)
cap.release()
print(f"Saved {frame_number} frames to {output_dir}/")
