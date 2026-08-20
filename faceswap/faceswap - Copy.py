import cv2
import dlib
import numpy as np
SOURCE="source.jpg"
TARGET="target.jpg"
OUTPUT="result.jpg"
LANDMARK_MODEL="shape_predictor_68_face_landmarks.dat"
source=cv2.imread(SOURCE)
target=cv2.imread(TARGET)
if source is None: raise Exception("Could not load source.jpg")
if target is None: raise Exception("Could not load target.jpg")
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor(LANDMARK_MODEL)
def get_landmarks(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=detector(gray)
    if len(faces)==0: raise Exception("No face found")
    face=max(faces,key=lambda r:r.width()*r.height())
    shape=predictor(gray,face)
    return np.array([(shape.part(i).x,shape.part(i).y) for i in range(68)],dtype=np.float32)
src_points=get_landmarks(source)
dst_points=get_landmarks(target)
indices=[36,45,30,48,54]
M,_=cv2.estimateAffinePartial2D(src_points[indices],dst_points[indices])
if M is None: raise Exception("Could not calculate face transformation")
height,width=target.shape[:2]
warped=cv2.warpAffine(source,M,(width,height),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REFLECT_101)
src_points_h=np.hstack([src_points,np.ones((68,1))])
warped_points=src_points_h.dot(M.T)
hull=cv2.convexHull(warped_points.astype(np.int32))
mask=np.zeros((height,width),dtype=np.uint8)
cv2.fillConvexPoly(mask,hull,255)
mask=cv2.GaussianBlur(mask,(15,15),10)
x,y,w,h=cv2.boundingRect(hull)
center=(x+w//2,y+h//2)
result=cv2.seamlessClone(warped,target,mask,center,cv2.NORMAL_CLONE)
cv2.imwrite(OUTPUT,result)
print("Face swap complete!")
print("Saved:",OUTPUT)