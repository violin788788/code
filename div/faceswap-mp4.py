import os

# Set thread limits BEFORE importing cv2, insightface, or onnxruntime
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["ORT_NUM_THREADS"] = "1"

import time
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import cv2
import insightface
from insightface.app import FaceAnalysis

# 1. File Selection Dialogs
root = tk.Tk()
root.withdraw()
mp4_file = filedialog.askopenfilename(
    title="Select MP4 video",
    filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
)
replacement = filedialog.askopenfilename(
    title="Select replacement image",
    filetypes=[("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")]
)
root.destroy()

if not mp4_file:
    raise Exception("No MP4 selected.")
if not replacement:
    raise Exception("No replacement image selected.")

time_begin = time.time()

# 2. Initialize Face Analysis & Load Replacement Face
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)

source = cv2.imread(replacement)
if source is None:
    raise Exception("Could not read replacement image.")

source_faces = app.get(source)
if not source_faces:
    raise Exception("No face found in replacement image.")

# 3. Load Face Swapper Model
onnx_path = "inswapper_128.onnx"
print("ONNX path:", os.path.abspath(onnx_path))
if not os.path.exists(onnx_path):
    raise Exception("inswapper_128.onnx not found.")
print("ONNX size:", os.path.getsize(onnx_path), "bytes")

swapper = insightface.model_zoo.get_model(onnx_path, providers=["CPUExecutionProvider"])

# 4. Open Input Video & Configure Output Video
cap = cv2.VideoCapture(mp4_file)
if not cap.isOpened():
    raise Exception("Could not open input video.")

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("FPS:", fps)
print("Resolution:", width, "x", height)
print("Total frames:", total_frames)

# Frame range & skipping settings
start_frame = 0
end_frame = min(500, total_frames - 1)  # Prevents exceeding total frames
every_how_many_frames = 10

frames_to_convert = ((end_frame - start_frame) // every_how_many_frames) + 1
est_time_minutes = (frames_to_convert * 10) / 60

print("start_frame:", start_frame)
print("end_frame:", end_frame)
print("every_how_many_frames:", every_how_many_frames)
print("frames to convert:", frames_to_convert)
print("est_time_minutes:", round(est_time_minutes, 2))

# Safe output filename using Path.stem
out_file = f"{Path(replacement).stem}_{Path(mp4_file).name}"
print("out_file:", out_file)

# Scale output FPS so skipping frames plays back at real-time speed
out_fps = fps / every_how_many_frames
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(out_file, fourcc, out_fps, (width, height))

if not out.isOpened():
    raise Exception("Could not create output video.")

# 5. Main Processing Loop
frames_written = 0

for frame_number in range(total_frames):
    # Stop completely once we pass end_frame
    if frame_number > end_frame:
        break

    # Skip frames before start_frame or frames that don't match the step interval
    if frame_number < start_frame or (frame_number - start_frame) % every_how_many_frames != 0:
        cap.grab()  # Advances video pointer without full decoding
        continue

    start_time = datetime.now()
    ret, target = cap.read()
    if not ret:
        print("Could not read frame", frame_number)
        break

    target_faces = app.get(target)
    if target_faces:
        result = swapper.get(target, target_faces[0], source_faces[0], paste_back=True)
    else:
        result = target

    if result.shape[1] != width or result.shape[0] != height:
        result = cv2.resize(result, (width, height))

    out.write(result)
    frames_written += 1

    time_difference = (datetime.now() - start_time).total_seconds()
    frames_left = int((end_frame-frame_number)/every_how_many_frames)
    est_time_left = "estimted time left = "+str(int(frames_left*7/60))

    print(f"Range [{start_frame}-{end_frame}] | Frame {frame_number} | {time_difference:.2f}s to generate",est_time_left)

# 6. Cleanup & Summary
cap.release()
out.release()

print("")
print("Saved:", out_file)
print("Frames written:", frames_written)
time_end = time.time()
print("Time elapsed:", round(time_end - time_begin, 2), "seconds")
print("")
# os.startfile(out_file)