
import sys
sys.path.insert(0, r"A:\\Users\\-\\code")
from utils import *
from pathlib import Path

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
open_browser_to_url("firefox", 64,5,"https://info34.pythonanywhere.com/")
pyautogui.hotkey("win","left")    
open_browser_to_url("firefox", 64,3,"https://info34.pythonanywhere.com/")
pyautogui.hotkey("win","right")    
time.sleep(2)
pyautogui.hotkey("ctrl","f")
paste_text("browse")   
click_buttons(["esc","tab","enter"])
time.sleep(5)

google_username = "oak234345"
google_password = "cats2534"
paste_text(google_username)
pyautogui.press('enter')   
time.sleep(5)
paste_text(google_password)
pyautogui.press('pagedown') 

facebook_username = "violin788788@proton.me"
facebook_password = "Viovio3#"
pyautogui.press('tab')   
paste_text(facebook_username)
pyautogui.press('tab')  
paste_text(facebook_password) 
pyautogui.press('enter')
pyautogui.press('pagedown') 



navigate_to_window("Google Accounts")

pyautogui.write("oak234345") 
click_buttons(["enter"]) 

pyperclip.copy("oak234345")
pyautogui.hotkey("ctrl", "v")  
click_buttons(["enter"]) 