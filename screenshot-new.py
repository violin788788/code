import tkinter as tk
from tkinter.simpledialog import askstring
from PIL import ImageGrab
import os,subprocess,sys
import getpass


filename = input("name of screenshot = ")


# --- 1. Create single root ---
root = tk.Tk()
root.withdraw()  # hide for input dialog
# --- 2. Get filename from popup ---
#filename = askstring("classified documents", "Enter screenshot name and then click enter to drag and drop it")
if not filename:
    root.destroy()
    exit()  # exit if user cancels
# --- 3. Prepare fullscreen screenshot overlay ---
root.deiconify()  # show root
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.3)
root.configure(bg="black")

canvas = tk.Canvas(root, cursor="cross")
canvas.pack(fill=tk.BOTH, expand=True)
start_x = start_y = rect = None

def on_mouse_down(event):
    global start_x, start_y, rect
    start_x, start_y = event.x, event.y
    rect = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red")
def on_mouse_drag(event):
    canvas.coords(rect, start_x, start_y, event.x, event.y)
def on_mouse_up(event):
    x1 = min(start_x, event.x)
    y1 = min(start_y, event.y)
    x2 = max(start_x, event.x)
    y2 = max(start_y, event.y)
    root.destroy()  # close GUI
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    cwd = os.getcwd()
    #cwd.replace("") replade basepath with..Downloads?
    cwd = os.getcwd()

    drive = str(os.getenv('SystemDrive'))
    drive = drive+"\\"
    user = getpass.getuser()  # This works on Windows, macOS, Linux
    print(drive)
    print(user)
    save_directory = os.path.join(drive,"Users",user,"Downloads")
    print(save_directory)

    save_file = os.path.join(save_directory, filename+".png")
    print("save_file",save_file)
    img.save(save_file)
    #os.startfile(save_directory)  # open folder
    subprocess.run(["explorer", save_directory])
    print(save_directory)

canvas.bind("<ButtonPress-1>", on_mouse_down)
canvas.bind("<B1-Motion>", on_mouse_drag)
canvas.bind("<ButtonRelease-1>", on_mouse_up)
root.mainloop()
       