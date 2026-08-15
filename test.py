import sys
sys.path.insert(0, r"A:\\Users\\-\\code")
from utils import *
from pathlib import Path


navigate_to_window("Google Accounts")


"""
import win32gui
import win32con

def get_windows():
    windows = []
    def enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_handler, None)
    return windows


def navigate_to_window(window_contains):
    #navigate_to_window("Google Accounts")
    windows = []
    def enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_handler, None)
    for hwnd, title in windows:
        if window_contains in title:
            print(f"\nSwitching to: {title} (Handle: {hwnd})")
            # Restore window if minimized
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            # Bring to foreground
            win32gui.SetForegroundWindow(hwnd)
            break
            """