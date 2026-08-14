#from utils import *
import sys,os,math,subprocess
import sys,pyperclip,time,pyautogui
"""
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
"""
def read_txt(file_path):
    #read_txt("song.txt")
    #text = read_txt("file.txt")
    # Add encoding='utf-8' here:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
    #A:\Users\-\code\utils.py

def open_browser_to_url(browser, bits,wait_time,url):
    #open_browser_to_url("firefox", 64,2,"www.pythonanywhere.com")
    drive = "B:"
    if bits == 32:
        program_files = "Program Files (x86)"
    elif bits == 64:
        program_files = "Program Files"
    else:
        print("Invalid bit size. Choose 32 or 64.")
        return
    browser = browser.lower()
    if "chrome" in browser:
        chrome_location = f"{drive}\\{program_files}\\Google\\Chrome\\Application\\chrome.exe"
        print(f"Launching Chrome from: {chrome_location}")
        os.startfile(chrome_location)
    elif "firefox" in browser:
        firefox_location = f"{drive}\\{program_files}\\Mozilla Firefox\\private_browsing.exe"
        print(f"Launching Firefox from: {firefox_location}")
        os.startfile(firefox_location)
    else:
        print(f"Browser '{browser}' not recognized.")
    pyperclip.copy(url)
    time.sleep(wait_time)
    pyautogui.hotkey("alt", "d")    
    pyautogui.hotkey("ctrl", "v")  
    pyautogui.press('enter')   