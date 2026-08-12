

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


chrome_32_or_64_bit = 32
firefox_32_or_64_bit = 32
drive = "B:"

match = []
match.append([32,"Program Files (x86)"])
match.append([64,"Program Files"])
chrome_program_files = ""
firefox_program_files = ""
for a in range(0,len(match)):
    if chrome_32_or_64_bit==match[a][0]:
        chrome_program_files = match[a][1]
    if firefox_32_or_64_bit==match[a][0]:
        firefox_program_files = match[a][1]
print("chrome_program_files",chrome_program_files)
print("firefox_program_files",firefox_program_files)
#chrome_location = "B:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
chrome_location = drive+"\\"+chrome_program_files+"\\Google\\Chrome\\Application\\chrome.exe"
firefox_location = drive+"\\"+firefox_program_files+"\\Mozilla Firefox\\private_browsing.exe"


github_repo=f"https://github.com/violin788788/{directory_name}"
python_anywhere_console = "https://www.pythonanywhere.com/user/info34/consoles/"
#if os.path.exists(chrome_path):
#subprocess.run([chrome_location,"--incognito",github_repo])
#subprocess.run([chrome_location,"--incognito",python_anywhere_console])
#subprocess.run([firefox_location,github_repo])
#subprocess.run([firefox_location,python_anywhere_console])

print("firefox_location",firefox_location)
sys.exit()

firefox_location = "B:\\Program Files\\Mozilla Firefox\\private_browsing.exe"

subprocess.Popen([firefox_location, "--private-window", python_anywhere_console])

print("")
print("")
print("don't forget to run python git-pull.py on python anywhere console")
print("")
print("")