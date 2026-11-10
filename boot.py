import sys
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

import subprocess

# Define the URL
url = "https://info34.pythonanywhere.com"

# Windows command (uses 'start chrome' to locate the executable automatically)
subprocess.Popen(f'start chrome --incognito --new-window {url}', shell=True)
subprocess.Popen(f'start chrome --incognito --new-window {url}', shell=True)

# Mac command (uncomment if using macOS)
# subprocess.Popen(['open', '-na', 'Google Chrome', '--args', '--incognito', url])

# Linux command (uncomment if using Linux)
# subprocess.Popen(['google-chrome', '--incognito', url])
