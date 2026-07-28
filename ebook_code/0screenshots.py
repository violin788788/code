import sys,os
#new_file = os.path.join(a,b,c)
#cwd = os.getcwd()
import pyautogui
import time
import os
# ==========================
# Settings
# ==========================
# Screenshot region (left, top, width, height)
# Replace these values with your own.
SCREENSHOT_REGION = (100, 100, 1200, 1600)
# Coordinates to click for "Next Page"
# Replace these with your own.
NEXT_BUTTON = (1800, 900)
# Number of pages
NUM_PAGES = 300
# Time to wait after clicking next page
PAGE_LOAD_DELAY = 0.8
# Folder to save screenshots
OUTPUT_FOLDER = "ww2_book_screenshots"
# ==========================
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
print("Starting in 5 seconds...")
print("Switch to your ebook window.")
time.sleep(5)
for i in range(1, NUM_PAGES + 1):
    filename = os.path.join(OUTPUT_FOLDER, f"page_{i:03}.png")
    # Take screenshot
    screenshot = pyautogui.screenshot(region=SCREENSHOT_REGION)
    screenshot.save(filename)
    print(f"Saved {filename}")
    # Go to next page
    pyautogui.click(*NEXT_BUTTON)
    # Wait for page to load
    time.sleep(PAGE_LOAD_DELAY)
print("Done!")