import subprocess,time,shutil,os,pyautogui
URL="https://info34.pythonanywhere.com/"
def find_chrome():
    paths=[r"A:\Program Files\Google\Chrome\Application\chrome.exe",r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    for p in paths:
        if os.path.exists(p):
            return p
    c=shutil.which("chrome")
    if c:
        return c
    raise FileNotFoundError("Google Chrome not found.")
chrome=find_chrome()
subprocess.Popen([chrome,"--incognito","--new-window",URL])
time.sleep(1)
pyautogui.hotkey("winleft","left")
time.sleep(1)
subprocess.Popen([chrome,"--incognito","--new-window",URL])
time.sleep(1)
pyautogui.hotkey("winleft","right")
time.sleep(1)
print("Done.")