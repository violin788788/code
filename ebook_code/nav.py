#from utils import *

import os,pyautogui,pyperclip
import subprocess,time


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

chrome_location = "B:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
firefox_location = "B:\\Program Files (x86)\\Mozilla Firefox\\private_browsing.exe"


#chrome_path = os.path.join(os.path.splitdrive(os.getcwd())[0] + "\\", "Program Files (x86)", "Google", "Chrome", "Application", "chrome.exe")
#print ("chrome path = ",chrome_path)

url = "https://info34.pythonanywhere.com"
pyperclip.copy(url)

subprocess.Popen([chrome_location, "--incognito"])
time.sleep(2)
pyautogui.hotkey("win", "right")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

subprocess.Popen([firefox_location, "--incognito"])
time.sleep(2)
pyautogui.hotkey("win", "left")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")


