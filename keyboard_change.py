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



import ctypes
# Swedish (Sweden) keyboard layout
SWEDISH = 0x041D041D
user32 = ctypes.WinDLL("user32", use_last_error=True)
result = user32.ActivateKeyboardLayout(SWEDISH, 0)
if result == 0:
    raise ctypes.WinError(ctypes.get_last_error())
print("Keyboard layout changed to Swedish.")