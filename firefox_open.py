import sys,pyperclip,time,pyautogui
sys.path.insert(0, r"A:\Users\-\code")
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

chrome_32_or_64_bit = 32
firefox_32_or_64_bit = 64
drive = "B:"

match = []
match.append([32,"Program Files (x86)"])
match.append([64,"Program Files"])
chrome_program_files = ""
firefox_program_files = ""
for a in range(0,len(match)):
    if chrome_32_or_64_bit==match[a][0]:
        chrome_program_files = match[a][1]
    if firefox_32_or_64_bit==match[a][0]:
        firefox_program_files = match[a][1]
print("chrome_program_files",chrome_program_files)
print("firefox_program_files",firefox_program_files)
#chrome_location = "B:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
chrome_location = drive+"\\"+chrome_program_files+"\\Google\\Chrome\\Application\\chrome.exe"
firefox_location = drive+"\\"+firefox_program_files+"\\Mozilla Firefox\\private_browsing.exe"

url = "https://info34.pythonanywhere.com"
#pyperclip.copy(url)
#subprocess.Popen([firefox_location, "--incognito"])
subprocess.Popen([firefox_location, "--private-window", url])
time.sleep(2)
pyperclip.copy(url)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("win", "left")
"""
time.sleep(2)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("win", "left")


import subprocess
url = "https://example.com"
firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
subprocess.Popen([firefox_path, "--private-window", url])
"""