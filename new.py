from utils import *
from pathlib import Path
name=input("Enter the name of the new script (without .py): ").strip()
if not name:
    print("No name entered.")
    input("Press Enter to exit...")
    raise SystemExit
if name.lower().endswith(".py"):
    name=name[:-3]
if name.lower().endswith(".bat"):
    name=name[:-4]
py_text='''from utils import *
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

'''
bat_text=f'''@echo off
cd /d "%~dp0"
python "{name}.py"
pause
'''
Path(f"{name}.py").write_text(py_text,encoding="utf-8")
Path(f"{name}.bat").write_text(bat_text,encoding="utf-8")
print(f"Created {name}.py")
print(f"Created {name}.bat")
os.startfile(name+".py")