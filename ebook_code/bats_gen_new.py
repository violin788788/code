

def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)

import sys,os
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)


bat_base_code="""
@echo off
cd /d "%~dp0"
python "___"
pause
"""


for a,val in enumerate(files):
    if ".py" in val:
        print(val)
        code_to_paste = bat_base_code.replace("___",val)
        print(code_to_paste)
        bat_file = val.replace(".py",".bat")
        with open(bat_file, "w", encoding="utf-8") as f:
            f.write(code_to_paste)
