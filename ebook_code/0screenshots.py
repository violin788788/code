from pynput import mouse
import pyautogui
import time
import os,sys

clicks = []

print("Do 3 clicks:")
print("1st = top-left of capture area")
print("2nd = bottom-right of capture area")
#print("3rd = next-page button")

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        clicks.append((x, y))
        print(f"Captured click {len(clicks)} at: ({x}, {y})")

        if len(clicks) == 2:
            return False  # stop listener

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

# unpack clicks
top_left = clicks[0]
bottom_right = clicks[1]
#next_button = clicks[2]

print(clicks)
print(clicks[0])
print(clicks[0][0]+clicks[1][0])
print(clicks[1])
#sys.exit()

# user inputs
pages = int(input("\nHow many pages to capture? "))
folder = input("Enter folder name to save screenshots: ")

os.makedirs(folder, exist_ok=True)

# calculate region
x1, y1 = top_left
x2, y2 = bottom_right

width = x2 - x1
height = y2 - y1

print("\nStarting capture in 3 seconds...")
time.sleep(3)


mid_x = (clicks[0][0]+clicks[1][0]) // 2
mid_y = (clicks[0][1]+clicks[1][1]) // 2

# Move the mouse and left-click at the center point
pyautogui.click(x=mid_x, y=mid_y)


for i in range(pages):
    # screenshot region
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    
    file_path = os.path.join(folder, f"page_{i+1}.png")
    screenshot.save(file_path)

    print(f"Saved {file_path}")

    # click next page (skip after last page)
    if i != pages - 1:
        #pyautogui.click(next_button)
        pyautogui.press('pagedown')
        #pyautogui.press('right')
        time.sleep(1)

print("\nDone.")