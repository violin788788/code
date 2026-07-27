import tkinter as tk
from tkinter import messagebox
import os
def run_code():
    input_file=code_input.get("1.0",tk.END).strip()
    if ".py" not in input_file:
        input_file = input_file+".py"
    #redo this to cwd..driver..etc..
    cwd = os.getcwd()
    code_directory = cwd
    file_to_run = os.path.join(code_directory,input_file)
    cmd = "python "+file_to_run
    print(cmd)
    os.system(cmd)
    #os.system(f"python \"{filename}\"")
root=tk.Tk()
root.title("Python Runner")
root.geometry("400x200")
tk.Label(root,text="Run what in Python?",font=("Arial",14)).pack(pady=10)
code_input=tk.Text(root,width=40,height=3,font=("Consolas",12))
code_input.pack(padx=10,pady=10)
run_button=tk.Button(root,text="Run",font=("Arial",12),command=run_code)
run_button.pack(pady=10)
root.mainloop()
