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

import tkinter as tk
import cv2
import numpy as np
import mss
import time
root=tk.Tk()
root.attributes("-fullscreen",True)
root.attributes("-alpha",0.3)
root.configure(bg="black")
canvas=tk.Canvas(root,bg="black",cursor="cross")
canvas.pack(fill="both",expand=True)
start_x=start_y=0
rect=None
def mouse_down(event):
    global start_x,start_y,rect
    start_x=event.x
    start_y=event.y
    rect=canvas.create_rectangle(start_x,start_y,start_x,start_y,outline="red",width=3)
def mouse_drag(event):
    canvas.coords(rect,start_x,start_y,event.x,event.y)
def mouse_up(event):
    global x1,y1,x2,y2
    x1=min(start_x,event.x)
    y1=min(start_y,event.y)
    x2=max(start_x,event.x)
    y2=max(start_y,event.y)
    root.destroy()
canvas.bind("<ButtonPress-1>",mouse_down)
canvas.bind("<B1-Motion>",mouse_drag)
canvas.bind("<ButtonRelease-1>",mouse_up)
root.mainloop()
width=x2-x1
height=y2-y1
if width<10 or height<10:
    print("Selection too small.")
    exit()
sct=mss.mss()
monitor={"left":x1,"top":y1,"width":width,"height":height}
#fps=20
fps=30
out_file = "record.mp4"
out=cv2.VideoWriter(out_file,cv2.VideoWriter_fourcc(*"mp4v"),fps,(width,height))
print("Recording selected area. Press Ctrl+C to stop.")
try:
    while True:
        frame=np.array(sct.grab(monitor))
        frame=cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
        out.write(frame)
        time.sleep(1/fps)
except KeyboardInterrupt:
    pass
finally:
    out.release()
    print("Saved as screen_recording.mp4")
os.startfile(out_file)