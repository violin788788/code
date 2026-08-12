import tkinter as tk
from tkinter import filedialog
from text_to_speech import main
def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("EPUB/PDF", "*.epub *.pdf")])
    file_label.config(text=selected_file)
def run():
    main(selected_file,int(generate_var.get()),int(song_var.get()),int(start_file.get()),song.get(),plane_sound.get())
selected_file=""
root=tk.Tk()
root.title("Narration Tool")
root.geometry("500x400")
tk.Button(root,text="Select File",command=select_file).pack(pady=10)
file_label=tk.Label(root,text="No file selected")
file_label.pack()
generate_var=tk.IntVar()
song_var=tk.IntVar()
tk.Checkbutton(root,text="Generate Narration",variable=generate_var).pack()
tk.Checkbutton(root,text="Add Song to Narration",variable=song_var).pack()
tk.Label(root,text="Narrate Start File").pack()
start_file=tk.Entry(root)
start_file.insert(0,"4")
start_file.pack()
tk.Label(root,text="Song").pack()
song=tk.Entry(root)
song.insert(0,"dmitri.mp3")
song.pack()
tk.Label(root,text="Plane Sound").pack()
plane_sound=tk.Entry(root)
plane_sound.insert(0,"plane_sound.mp3")
plane_sound.pack()
tk.Button(root,text="RUN",command=run).pack(pady=20)
root.mainloop()