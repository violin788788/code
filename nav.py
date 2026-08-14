from utils import *
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
#new_file = os.path.join(a,b,c)
drive = os.path.splitdrive(os.getcwd())[0]
cwd = os.getcwd()
files = os.listdir(cwd)
import os,pyautogui,pyperclip
import subprocess,time

open_browser_to_url("firefox", 64,2,"https://info34.pythonanywhere.com/")
pyautogui.hotkey("win","left")    
open_browser_to_url("firefox", 64,2,"https://info34.pythonanywhere.com/")
pyautogui.hotkey("win","right")    
