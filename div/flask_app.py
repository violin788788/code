import os,platform
import time
import uuid
import threading
os.environ["OMP_NUM_THREADS"]="1"
os.environ["ORT_NUM_THREADS"]="1"
import cv2
import insightface
from flask import Flask,render_template,request,redirect,url_for,send_file
from insightface.app import FaceAnalysis
app=Flask(__name__)
UPLOAD_FOLDER="uploads"
OUTPUT_FOLDER="outputs"
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
os.makedirs(OUTPUT_FOLDER,exist_ok=True)
app.config["MAX_CONTENT_LENGTH"]=2*1024*1024*1024
print("Loading FaceAnalysis...")
face_app=FaceAnalysis(name="buffalo_l",providers=["CPUExecutionProvider"])
face_app.prepare(ctx_id=0)
print("Loading inswapper...")
swapper=insightface.model_zoo.get_model("inswapper_128.onnx",providers=["CPUExecutionProvider"])
print("Models loaded.")
jobs={}
def process_video(job_id,mp4_file,replacement_file,output_file):
    cap=None
    out=None
    try:
        jobs[job_id]["status"]="Loading replacement image..."
        jobs[job_id]["progress"]=0
        source=cv2.imread(replacement_file)
        if source is None:
            raise Exception("Could not read replacement image.")
        source_faces=face_app.get(source)
        if not source_faces:
            raise Exception("No face found in replacement image.")
        jobs[job_id]["status"]="Opening video..."
        cap=cv2.VideoCapture(mp4_file)
        if not cap.isOpened():
            raise Exception("Could not open input video.")
        fps=cap.get(cv2.CAP_PROP_FPS)
        width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fourcc=cv2.VideoWriter_fourcc(*"mp4v")
        out=cv2.VideoWriter(output_file,fourcc,fps,(width,height))
        frame_number=0
        last_result=None
        start_time=time.time()
        while True:
            ret,target=cap.read()
            if not ret:
                break
            if frame_number%3==0:
                jobs[job_id]["status"]=f"Processing frame {frame_number:,} of {total_frames:,}"
                target_faces=face_app.get(target)
                if target_faces:
                    last_result=swapper.get(target,target_faces[0],source_faces[0],paste_back=True)
                else:
                    last_result=target
            if last_result is None:
                last_result=target
            out.write(last_result)
            frame_number+=1
            if total_frames>0:
                jobs[job_id]["progress"]=min(int((frame_number/total_frames)*100),100)
        cap.release()
        out.release()
        elapsed=time.time()-start_time
        jobs[job_id]["progress"]=100
        jobs[job_id]["status"]=f"Finished in {elapsed:.1f} seconds."
        jobs[job_id]["finished"]=True
        jobs[job_id]["output"]=output_file
        print(f"Job {job_id} finished.")
    except Exception as e:
        print("ERROR:",e)
        if cap is not None:
            cap.release()
        if out is not None:
            out.release()
        jobs[job_id]["status"]=str(e)
        jobs[job_id]["error"]=True
        jobs[job_id]["finished"]=True
@app.route("/")
def index():
    return render_template("index.html",job=None)
@app.route("/process",methods=["POST"])
def process():
    video=request.files.get("video")
    replacement=request.files.get("replacement")
    if not video or not replacement:
        return "Please select both files.",400
    job_id=str(uuid.uuid4())
    video_path=os.path.join(UPLOAD_FOLDER,job_id+"_video.mp4")
    replacement_path=os.path.join(UPLOAD_FOLDER,job_id+"_replacement.png")
    output_path=os.path.join(OUTPUT_FOLDER,job_id+"_output.mp4")
    video.save(video_path)
    replacement.save(replacement_path)
    jobs[job_id]={"status":"Starting...","progress":0,"finished":False,"error":False}
    thread=threading.Thread(target=process_video,args=(job_id,video_path,replacement_path,output_path))
    thread.start()
    return redirect(url_for("status",job_id=job_id))
@app.route("/status/<job_id>")
def status(job_id):
    if job_id not in jobs:
        return "Job not found.",404
    job=jobs[job_id]
    if job["finished"]:
        if job.get("error"):
            return render_template("index.html",job=job,error=True)
        return render_template("index.html",job=job,finished=True,job_id=job_id)
    return render_template("index.html",job=job,processing=True,job_id=job_id)
@app.route("/download/<job_id>")
def download(job_id):
    if job_id not in jobs:
        return "Job not found.",404
    job=jobs[job_id]
    if not job.get("finished") or job.get("error"):
        return "Output is not ready.",400
    return send_file(job["output"],as_attachment=True,download_name="output.mp4")
if __name__=="__main__":
    print("Face Swap Web App")
    print("Open http://127.0.0.1:5000")


    current_os = platform.system()
    print(current_os)
    if "Windows" in current_os:
        os.startfile("http://127.0.0.1:5000")


    app.run(host="127.0.0.1",port=5000,debug=False,threaded=True)
