import cv2
import numpy as np
import pyautogui
import time
import keyboard
def select_region(image):
    r = cv2.selectROI("Select Region", image, fromCenter=False, showCrosshair=True)
    cv2.destroyAllWindows()
    return r
screen_width, screen_height = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
out = cv2.VideoWriter('screen_record.mp4', fourcc, fps, (screen_width, screen_height))
start_time = time.time()
while True:
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)
    if keyboard.is_pressed('space'):  # Stop recording when Ctrl+E is pressed
        print("Recording stopped by user.")
        break
out.release()
cap = cv2.VideoCapture('screen_record.mp4')
ret, frame = cap.read()
if ret:
    # Resize the image to fit the screen automatically
    frame = cv2.resize(frame, (screen_width, screen_height))
    region = select_region(frame)  # Let the user select a region with no need to move
    x, y, w, h = region
    out_cropped = cv2.VideoWriter('screen_record_cropped.mp4', fourcc, fps, (w, h))
    while ret:
        ret, frame = cap.read()
        if not ret:
            break
        cropped_frame = frame[y:y+h, x:x+w]
        out_cropped.write(cropped_frame)
    out_cropped.release()
cap.release()
cv2.destroyAllWindows()
