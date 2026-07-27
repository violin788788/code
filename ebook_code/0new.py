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
py_text='''

import sys,os

new_path = os.path.join(a,b,c)
cwd = os.getcwd()

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
input("Press Enter to exit...")