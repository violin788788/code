"""
from importlib import import_module
utils=import_module("0utils")
globals().update({n:getattr(utils,n) for n in dir(utils) if not n.startswith("_")})
if __name__=="__main__":
    print("Loaded 0utils.py")
"""

from pathlib import Path
import pyautogui,sys,os,time


book_name = "medici_money"
Path(book_name).mkdir(parents=True, exist_ok=True)
x, y = pyautogui.position()
print(f"X: {x} Y: {y}")
#sys.exit()
screen_width, screen_height = pyautogui.size()
clicks = 900
once = 0
for a in range(1,clicks+1):
    save_file = "page_"+str(a)+".png"
    path = os.path.join(book_name, save_file)
    #pyautogui.screenshot(path)  # Save the screenshot
    pyautogui.screenshot(
        path,
        region=(0, 0, screen_width // 2, screen_height)
    )    
    #pyautogui.press('pagedown')
    #time.sleep(2)
    #if once==0:
    pyautogui.click(x=653, y=550)
    time.sleep(1)
    #once=1
    print(a)

