import os,time
from pathlib import Path
os.environ["OMP_NUM_THREADS"]="1"
os.environ["ORT_NUM_THREADS"]="1"
import cv2
import insightface
time_begin = time.time()
import cv2
import insightface
from insightface.app import FaceAnalysis
app=FaceAnalysis(name="buffalo_l",providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0)
#original photo

original_photo="lenin.png"
switch_with = "sanders.png"

target=cv2.imread(original_photo)
source=cv2.imread(switch_with)
#save_file = "result.png"
save_file = Path(original_photo).stem+"-"+switch_with
if source is None: raise Exception("source.jpg not found")
if target is None: raise Exception("target.jpg not found")
source_faces=app.get(source)
target_faces=app.get(target)
if not source_faces: raise Exception("No face found in source.jpg")
if not target_faces: raise Exception("No face found in target.jpg")
swapper=insightface.model_zoo.get_model("inswapper_128.onnx",providers=["CPUExecutionProvider"])
#swapper=insightface.model_zoo.get_model("inswapper_128.onnx",providers=["CPUExecutionProvider"],provider_options=[{"arena_extend_strategy":"kSameAsRequested"}])
result=swapper.get(target,target_faces[0],source_faces[0],paste_back=True)
#cv2.imwrite("result.jpg",result)
#print("Saved result.jpg")
cv2.imwrite(save_file,result)
print("Saved ",save_file)
time_end = time.time()
time_elapsed = time_end - time_begin
print("time_elapsed",time_elapsed)
os.startfile(save_file)