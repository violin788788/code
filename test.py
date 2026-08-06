from utils import *
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)


import subprocess

repo_url = "https://github.com/yl4579/StyleTTS2.git"
repo_name = repo_url.split("/")[-1]
repo_name = repo_name.replace(".git","")
print(repo_name)
subprocess.run(["cd", repo_name],check=True)
subprocess.run(["pip install -r requirements.txt"],check=True)
