import tkinter as tk
from tkinter import filedialog
import os
import time
import cv2
import insightface
root=tk.Tk()
root.withdraw()
mp4_file=filedialog.askopenfilename(title="Select MP4 video",filetypes=[("MP4 files","*.mp4"),("All files","*.*")])
replacement=filedialog.askopenfilename(title="Select replacement image",filetypes=[("Image files","*.png;*.jpg;*.jpeg"),("All files","*.*")])
root.destroy()
if not mp4_file:
    raise Exception("No MP4 selected.")
if not replacement:
    raise Exception("No replacement image selected.")
os.environ["OMP_NUM_THREADS"]="1"
os.environ["ORT_NUM_THREADS"]="1"
time_begin=time.time()
from insightface.app import FaceAnalysis
app=FaceAnalysis(name="buffalo_l",providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)
source=cv2.imread(replacement)
if source is None:
    raise Exception("Could not read replacement image.")
source_faces=app.get(source)
if not source_faces:
    raise Exception("No face found in replacement image.")
onnx_path="inswapper_128.onnx"
print("ONNX path:",os.path.abspath(onnx_path))
if not os.path.exists(onnx_path):
    raise Exception("inswapper_128.onnx not found.")
print("ONNX size:",os.path.getsize(onnx_path),"bytes")
swapper=insightface.model_zoo.get_model(onnx_path,providers=["CPUExecutionProvider"])
cap=cv2.VideoCapture(mp4_file)
if not cap.isOpened():
    raise Exception("Could not open input video.")
fps=cap.get(cv2.CAP_PROP_FPS)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("FPS:",fps)
print("Resolution:",width,"x",height)
print("Total frames:",total_frames)
out_file="output.mp4"
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter(out_file,fourcc,fps,(width,height))
if not out.isOpened():
    raise Exception("Could not create output video.")
start=0
end=100
for frame_number in range(total_frames):
    print("Doing frame",frame_number,"of",total_frames)
    ret,target=cap.read()
    if not ret:
        print("Could not read frame",frame_number)
        break
    if start<=frame_number<=end:
        target_faces=app.get(target)
        if target_faces:
            result=swapper.get(target,target_faces[0],source_faces[0],paste_back=True)
        else:
            result=target
    else:
        result=target
    if result.shape[1]!=width or result.shape[0]!=height:
        result=cv2.resize(result,(width,height))
    out.write(result)
cap.release()
out.release()
print("Saved:",out_file)
print("Frames processed:",frame_number+1)
time_end=time.time()
print("Time elapsed:",time_end-time_begin)
os.startfile(out_file)
