import os,time
os.environ["OMP_NUM_THREADS"]="1"
os.environ["ORT_NUM_THREADS"]="1"
import cv2
import insightface
time_begin=time.time()
from insightface.app import FaceAnalysis
app=FaceAnalysis(name="buffalo_l",providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)
source=cv2.imread("source.png")
if source is None: raise Exception("source.png not found")
source_faces=app.get(source)
if not source_faces: raise Exception("No face found in source.png")
swapper=insightface.model_zoo.get_model("inswapper_128.onnx",providers=["CPUExecutionProvider"])
cap=cv2.VideoCapture("input.mp4")
if not cap.isOpened(): raise Exception("input.mp4 not found")
fps=cap.get(cv2.CAP_PROP_FPS)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter("output.mp4",fourcc,fps,(width,height))
frame_number=0
last_result=None
counter = 0
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
    print("doing frame",frame_number)
    frame_number+=1
    if frame_number==20:
        break
cap.release()
out.release()
print("Saved output.mp4")
time_end=time.time()
time_elapsed=time_end-time_begin
print("time_elapsed",time_elapsed)
