import subprocess
import os
cwd=os.getcwd()
folders=["info34","info34\\vote34","info34\\earnings",""]
commands=["git status"]
file_name = "git-push.bat"
for folder in folders:
    print("--------------------------------------------")
    check=os.path.join(cwd,folder)
    print("--- Running in",check,"---")
    push_to_run = os.path.join(cwd,folder,file_name)
    print(push_to_run)
    os.startfile(push_to_run)

    #for command in commands:
    #    subprocess.run(command,shell=True,cwd=check)
