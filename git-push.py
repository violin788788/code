

import os
import subprocess
import sys
import platform
from datetime import datetime
cwd=os.getcwd()
directory_name=os.path.basename(cwd)
print(directory_name)
print(cwd)
system_type=platform.system()
print(system_type)
subprocess.run(["git","rm","-r","--cached","--ignore-unmatch","*.pdf","*.epub","*.mp3","*.exe"],capture_output=True,text=True)
subprocess.run(["git","add","-A"],check=True)
timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
commit=subprocess.run(["git","commit","-m",f"sync {timestamp}"],capture_output=True,text=True)
if commit.returncode!=0:
    output=(commit.stdout+commit.stderr).lower()
    if "nothing to commit" in output:
        print("Nothing to commit. Local and GitHub are already identical.")
    else:
        print(commit.stdout)
        print(commit.stderr)
        sys.exit(1)
with open("token.txt","r") as file:
    token=file.read().strip()
repo_url=f"https://violin788788:{token}@github.com/violin788788/{directory_name}.git"
try:
    subprocess.run(["git","push","-u",repo_url,"main","--force"],check=True)
    print("GitHub is now an exact copy of this folder.")
except subprocess.CalledProcessError as e:
    print(f"Push failed: {e}")
    sys.exit(1)
if system_type=="Linux":
    print("Linux detected - not opening Chrome.")
    sys.exit()
chrome_path=r"A:\Program Files\Google\Chrome\Application\chrome.exe"
github_repo=f"https://github.com/violin788788/{directory_name}"
python_anywhere_console = "https://www.pythonanywhere.com/user/info34/consoles/"
#if os.path.exists(chrome_path):
subprocess.run([chrome_path,"--incognito",github_repo])
subprocess.run([chrome_path,"--incognito",python_anywhere_console])
print("")
print("don't forget to run python git-pull.py on python anywhere console")
print("")

#https://www.pythonanywhere.com/user/info34/consoles/

#else:
#    print(url)

