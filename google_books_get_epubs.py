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

import pygetwindow as gw


def nav_to_window(window_iden):
  #nav_to_window("cmd")
  # Find all windows that contain "Play Books" in their title
  windows = gw.getWindowsWithTitle(window_iden)
  if windows:
      # Select the first matching window
      play_books_window = windows[0]
      # Unminimize if it's minimized, then bring to the front
      if play_books_window.isMinimized:
          play_books_window.restore()
      play_books_window.activate()
      print(f"Navigated to: {play_books_window.title}")
  else:
      print("No window with "+window_iden+" found.")

nav_to_window("Play Books")

pyautogui.hotkey("ctrl", "f")
time.sleep(0.5)
# Type 'read as epub'
pyautogui.write("export", interval=0.05)
time.sleep(1)
pyautogui.press("esc")
pyautogui.press("enter")
time.sleep(1)

pyautogui.hotkey("ctrl", "f")
time.sleep(0.5)
# Type 'read as epub'
pyautogui.write("export as", interval=0.05)
time.sleep(1)
pyautogui.press("esc")
pyautogui.press("enter")

nav_to_window("cmd")
time.sleep(3)

pyautogui.press("enter")

"""
import time
from pynput import mouse
import pyautogui

# Safety fail-safe: moving mouse to upper-left corner aborts PyAutoGUI
pyautogui.FAILSAFE = True
def execute_sequence():
  print("Left click detected. Waiting 2 seconds...")
  time.sleep(2)
  print("Performing actions...")
  # Down click (press and release down arrow key)
  pyautogui.press("down")
  # Enter
  pyautogui.press("enter")
  # Ctrl + F
  pyautogui.hotkey("ctrl", "f")
  time.sleep(0.5)
  # Type 'read as epub'
  pyautogui.write("export as", interval=0.05)
  # Esc, then Enter
  pyautogui.press("esc")
  pyautogui.press("enter")
  print("Sequence complete.")


def on_click(x, y, button, pressed):
  # Listen for the left mouse button being pressed down
  if button == mouse.Button.left and pressed:
    execute_sequence()


# Start the mouse listener
print("Listening for a left mouse click...")
with mouse.Listener(on_click=on_click) as listener:
  listener.join()


"""