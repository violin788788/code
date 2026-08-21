import os,time
os.environ["OMP_NUM_THREADS"]="1"
os.environ["ORT_NUM_THREADS"]="1"
import cv2
import insightface
time_begin=time.time()
from insightface.app import FaceAnalysis
app=FaceAnalysis(name="buffalo_l",providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)


mp4_file = "input.mp4"



cap=cv2.VideoCapture("input.mp4")
source=cv2.imread("hope.png")
out_file = "output.mp4"
end = 100

if source is None: raise Exception("source.png not found")
source_faces=app.get(source)
if not source_faces: raise Exception("No face found in source.png")
swapper=insightface.model_zoo.get_model("inswapper_128.onnx",providers=["CPUExecutionProvider"])
if not cap.isOpened(): raise Exception("input.mp4 not found")
fps=cap.get(cv2.CAP_PROP_FPS)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter(out_file,fourcc,fps,(width,height))
frame_number=0
last_result=None
end = 100
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
os.startfile(out_file)
