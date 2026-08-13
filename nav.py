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

chrome_32_or_64_bit = 32
firefox_32_or_64_bit = 32
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

print("chrome_location",chrome_location)
print("firefox_location",firefox_location)
#sys.exit()

#chrome_path = os.path.join(os.path.splitdrive(os.getcwd())[0] + "\\", "Program Files (x86)", "Google", "Chrome", "Application", "chrome.exe")
#print ("chrome path = ",chrome_path)

import subprocess
url = "https://info34.pythonanywhere.com/"
seconds_wait_after_open_browser = 3
subprocess.Popen([
    r"B:\Program Files\Mozilla Firefox\firefox.exe",
    "--private-window",
    url
])
time.sleep(seconds_wait_after_open_browser)
pyautogui.hotkey("win", "left")
subprocess.Popen([
    r"B:\Program Files\Mozilla Firefox\firefox.exe",
    "--private-window",
    url
])
time.sleep(seconds_wait_after_open_browser)
pyautogui.hotkey("win", "right")
"""
url = "https://info34.pythonanywhere.com"
pyperclip.copy(url)
#subprocess.Popen([firefox_location, "--incognito"])
subprocess.Popen([firefox_location, "--private-window", url])

time.sleep(2)
pyautogui.hotkey("win", "right")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
#subprocess.Popen([firefox_location, "--incognito"])
subprocess.Popen([firefox_location, "--private-window", url])

time.sleep(2)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.hotkey("win", "left")

"""