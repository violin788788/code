import PyInstaller.__main__
import shutil, os,sys,subprocess

#file_without_py = "git-status"
file = "screenshot"

#onefile_or_onedir = "onedir"
onefile_or_onedir = "onefile"
cmd_line = "yes"  #"yes" or "no"
#pyinstaller --onefile --windowed screenshot_tool.py

windowed=""
if cmd_line=="no":
    windowed = " --windowed" 

file_with_extension = ""
if "." not in file:
    extension = ".pyw"
    file_with_extension = file+extension



#if ".py" not in file_without_py:
#    file_with_py=file_without_py+".py"


cwd = os.getcwd()
ico_name = file+".ico"
ico_directory = os.path.join(cwd,"icos")
ico = os.path.join(ico_directory,ico_name)
#command = "pyinstaller --"+onefile_or_onedir+" --icon="+ico+" "+file_with_py
command = "pyinstaller --"+onefile_or_onedir+windowed+" --icon="+ico+" "+file_with_extension
print(command)

os.system(command)
cwd = os.getcwd()
drive = os.path.splitdrive(os.getcwd())[0]+"\\"
exe_file = file+".exe"
cwd = os.getcwd()

code_directory = cwd
print(code_directory)

src=os.path.join(code_directory,"dist",exe_file)
dst = os.path.join(drive, "Program Files", exe_file)
shutil.copy2(src, dst)
subprocess.run(["explorer", "dist"])
#subprocess.run(["explorer", "dist"])
#print(save_directory)

#os.startfile("dist")
#os.startfile(os.path.join(drive, "Program Files"))