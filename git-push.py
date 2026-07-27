

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
url=f"https://github.com/violin788788/{directory_name}"
chrome_path=r"A:\Program Files\Google\Chrome\Application\chrome.exe"
if os.path.exists(chrome_path):
    subprocess.run([chrome_path,"--incognito",url])
else:
    print(url)



"""
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
print(type(system_type))
print(system_type)
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
    subprocess.run(["git","push",repo_url,"main","--force"],check=True)
    print("GitHub is now an exact copy of this folder.")
except subprocess.CalledProcessError as e:
    print(f"Push failed: {e}")
    sys.exit(1)
if "Linux" in system_type:
    print("Linux detected - not opening Chrome.")
    sys.exit()
url=f"https://github.com/violin788788/{directory_name}"
chrome_path=r"A:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.run([chrome_path,"--incognito",url])

"""

"""

def show(what_to_show):
    #show(count)
    print(what_to_show)



import os,subprocess,sys,platform
from datetime import datetime
cwd=os.getcwd()
directory_name=os.path.basename(cwd)
print(directory_name)
print(cwd)
system_type=platform.system()
print(type(system_type))
print(system_type)
if "Linux" in system_type:
    print("do not open chrome")
timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
iden_last_pushed="git-push"
for f in os.listdir("."):
    if iden_last_pushed in f and f.endswith(".txt") and os.path.isfile(f):
        os.remove(f)
filename=f"{iden_last_pushed}-{timestamp}.txt"
with open(filename,"w") as f:
    f.write("Hello, this is the output.\n")
print(f"Created file: {filename}")
subprocess.run(["git","config","user.name","Your Name"],check=True)
subprocess.run(["git","config","user.email","you@example.com"],check=True)
subprocess.run(["git","add","-A"],check=True)
commit=subprocess.run(["git","commit","-m","update/create/delete files+folders"],capture_output=True,text=True)
if commit.returncode!=0:
    if "nothing to commit" in (commit.stdout+commit.stderr).lower():
        print("Nothing to commit.")
    else:
        print(commit.stdout)
        print(commit.stderr)
        sys.exit(1)
with open("token.txt","r") as file:
    token=file.read().strip()
repo_url=f"https://violin788788:{token}@github.com/violin788788/{directory_name}.git"
try:
    subprocess.run(["git","push",repo_url,"main","--force"],check=True)
    print("Force push to GitHub was successful!")
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
#os.startfile()

#sys.exit()

if "Linux" in system_type:
    print("do not open chrome")
    sys.exit()

url=r"https://github.com/violin788788/"+directory_name
chrome_path=r"A:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.run([chrome_path,"--incognito",url])

"""