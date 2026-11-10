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

def shutdown_windows():
    """Initiates an immediate shutdown on a Windows system."""
    # /s - Shuts down the computer.
    # /t 0 - Sets the time-out period to 0 seconds (immediate).
    try:
        print("Initiating system shutdown...")
        subprocess.call(["shutdown", "/s", "/t", "0"])
    except Exception as e:
        print(f"Failed to execute shutdown command: {e}")

if __name__ == '__main__':
    # Ensure all your work is saved before running this script
    shutdown_windows()
