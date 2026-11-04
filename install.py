from utils import *
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


packages_to_install = "matplotlib"

#subprocess.run(["demo_toolbox.lnk"],check=True)

try:
    subprocess.run(["cmd", "/c", "start", "", "demo_toolbox.lnk"], check=True)
except:
    print("meow")



"""
import subprocess
import sys
import re
FILE="demo_toolbox.lnk"
while True:
    result=subprocess.run([sys.executable,FILE],capture_output=True,text=True)
    if result.returncode==0:
        print(result.stdout)
        break
    error=result.stderr+result.stdout
    print(error)
    match=re.search(r"No module named '([^']+)'",error)
    if match:
        package=match.group(1)
        fixes={"cv2":"opencv-python","PIL":"Pillow","sklearn":"scikit-learn"}
        package=fixes.get(package,package)
        subprocess.run([sys.executable,"-m","pip","install",package])
        continue
    break


packages_to_install = "matplotlib"

subprocess.run(["pip", "install", packages_to_install],check=True)
"""