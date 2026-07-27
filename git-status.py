import subprocess
import os
cwd=os.getcwd()
repos=["info34","info34\\vote34","info34\\earnings",""]
commands=["git status"]
print("")
print("")
for repo in repos:
    check=os.path.join(cwd,repo)
    print("--------------------------------------------")
    #print("--- Running in",check,"---")
    print("Running in",check)
    for command in commands:
        subprocess.run(command,shell=True,cwd=check)

    #print("--------------------------------------------")
    
