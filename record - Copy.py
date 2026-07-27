import cv2,mss,numpy as np,subprocess,time,os
from pynput import keyboard

name=input("Save name (no extension): ")
print("Press Enter after you put name in")
print("Click Space to end recording")
stop=False
def on_press(key):
    global stop
    if key==keyboard.Key.space: stop=True
keyboard.Listener(on_press=on_press).start()

ix=iy=fx=fy=-1
drag=False
def mouse(event,x,y,flags,param):
    global ix,iy,fx,fy,drag
    if event==cv2.EVENT_LBUTTONDOWN: ix,iy=x,y; drag=True
    elif event==cv2.EVENT_MOUSEMOVE and drag: fx,fy=x,y
    elif event==cv2.EVENT_LBUTTONUP: fx,fy=x,y; drag=False

sct=mss.mss()
mon=sct.monitors[1]
screenshot=sct.grab(mon)
frame=np.array(screenshot)
frame=cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
cv2.namedWindow("Select Area",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Select Area",mouse)
while fx==-1 or drag:
    show=frame.copy()
    if ix!=-1 and fx!=-1: cv2.rectangle(show,(ix,iy),(fx,fy),(255,0,0),2)
    cv2.imshow("Select Area",show)
    cv2.waitKey(1)
cv2.destroyAllWindows()

x,y=min(ix,fx),min(iy,fy)
w,h=abs(fx-ix),abs(fy-iy)
region={"left":x,"top":y,"width":w,"height":h}
save_directory=os.path.join(os.path.expanduser("~"),"Downloads")
os.makedirs(save_directory,exist_ok=True)
out_file=os.path.join(save_directory,name+".mp4")

FPS=30
ffmpeg_cmd=[
    "ffmpeg",
    "-y",
    "-f","rawvideo","-pix_fmt","bgr24","-s",f"{w}x{h}","-r",str(FPS),"-i","-",
    "-f","dshow","-i","audio=Stereo Mix (Realtek(R) Audio)",
    "-c:v","libx264","-preset","fast","-crf","23",
    "-c:a","aac","-b:a","192k",
    out_file
]

proc=subprocess.Popen(ffmpeg_cmd,stdin=subprocess.PIPE)
frame_time=1/FPS
next_time=time.time()
while not stop:
    img=np.array(sct.grab(region))[:,:,:3]
    proc.stdin.write(img.tobytes())
    next_time+=frame_time
    sleep=next_time-time.time()
    if sleep>0: time.sleep(sleep)

proc.stdin.close()
proc.wait()
os.startfile(save_directory)
