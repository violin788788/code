import os,subprocess

#conemu_path = r"C:\Program Files\ConEmu\ConEmu64.exe"  # Change if your path is different
#cwd = os.getcwd()
#subprocess.run([conemu_path, "/dir", cwd])
# Path to your file
#file_path = r"mysite\templates\info34.html"


sublime_path = r"A:\Program Files\Sublime Text\sublime_text.exe"
path_info34=r"A:\Users\-\code\info34\mysite\templates\info34.html"

# Make sure the file exists
#if os.path.exists(file_path):
subprocess.run([sublime_path, path_info34])
#else:
#    print(f"File does not exist: {file_path}")


