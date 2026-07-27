
import os,pyautogui,pyperclip
import subprocess,time

chrome_path = os.path.join(os.path.splitdrive(os.getcwd())[0] + "\\", "Program Files (x86)", "Google", "Chrome", "Application", "chrome.exe")
print ("chrome path = ",chrome_path)

url = "https://info34.pythonanywhere.com"
pyperclip.copy(url)

subprocess.Popen([chrome_path, "--incognito"])
time.sleep(2)
pyautogui.hotkey("win", "right")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

subprocess.Popen([chrome_path, "--incognito"])
time.sleep(2)
pyautogui.hotkey("win", "left")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
