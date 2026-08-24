import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
mp4_file = filedialog.askopenfilename(title="Select MP4 video",filetypes=[("MP4 files","*.mp4"),("All files","*.*")])
replacement = filedialog.askopenfilename(title="replacement?",filetypes=[("All files","*.*")])
root.destroy()

import os,time
os.environ["OMP_NUM_THREADS"]="1"
os.environ["ORT_NUM_THREADS"]="1"
import cv2
import insightface
from tkinter import filedialog
time_begin=time.time()
from insightface.app import FaceAnalysis
app=FaceAnalysis(name="buffalo_l",providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)
cap=cv2.VideoCapture(mp4_file)
source=cv2.imread(replacement)
#out_file = mp4_file.replace(".mp4",replacement.replace(".","")+".mp4")

out_file = "output.mp4"
end = 0


if source is None: raise Exception("source.png not found")
source_faces=app.get(source)
if not source_faces: raise Exception("No face found in source.png")

import os

print("ONNX path:", os.path.abspath("inswapper_128.onnx"))
print("ONNX size:", os.path.getsize("inswapper_128.onnx"), "bytes")

swapper=insightface.model_zoo.get_model("inswapper_128.onnx",providers=["CPUExecutionProvider"])
if not cap.isOpened(): raise Exception("input.mp4 not found")
fps=cap.get(cv2.CAP_PROP_FPS)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter(out_file,fourcc,fps,(width,height))
frame_number=0
last_result=None
while True:
    ret,target=cap.read()
    if not ret: break
    if frame_number%3==0:
        target_faces=app.get(target)
        if target_faces:
            last_result=swapper.get(target,target_faces[0],source_faces[0],paste_back=True)
        else:
            last_result=target
    out.write(last_result)
    print("doing frame",frame_number,"of",end)
    frame_number+=1
    if frame_number==end:
        break
cap.release()
out.release()
print("Saved output.mp4")
time_end=time.time()
time_elapsed=time_end-time_begin
print("time_elapsed",time_elapsed)
#os.startfile(out_file)
