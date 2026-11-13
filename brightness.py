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

import screen_brightness_control as sbc

# Get the current brightness level (returns a percentage or list of percentages)
current_brightness = sbc.get_brightness()
print(f"Current screen brightness is: {current_brightness}%")

brightness = int(input("what level of brightness do you want?(i.e. 30 for 30%, 70 for 70%..)= "))
sbc.set_brightness(brightness)

"""

# 1. Get the current brightness of all connected displays
current_brightness = sbc.get_brightness()
print(f"Current brightness: {current_brightness}%")

# 2. Set the brightness to 75% for all displays
sbc.set_brightness(75)
print("Brightness set to 75%")

# 3. Target a specific monitor (e.g., the primary display)
sbc.set_brightness(50, display=0)

# 4. Smoothly fade the brightness to 30%
sbc.fade_brightness(30)

"""