import pygetwindow as gw
import pyautogui
import time,sys
time.sleep(1)
windows=gw.getAllTitles()
print(windows)
for a in range(0,len(windows)):
	print(windows[a])

sys.exit()


target=[w for w in windows if "compose" in w.lower()]
if target:
    win=gw.getWindowsWithTitle(target[0])[0]
    win.activate()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','f')
    time.sleep(0.5)
    pyautogui.write('compose',interval=0.05)
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.2)
    pyautogui.press('enter')