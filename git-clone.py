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
import sys
repo_url = "https://github.com/corentinj/real-time-voice-cloning"
#try:

repo_name = repo_url.split("/")[-1]
print(repo_name)
print(f"Cloning {repo_url}...\n")
subprocess.run(["git", "clone", "--progress", repo_url],check=True)
print("\nRepository cloned successfully!")
subprocess.run(["cd", repo_name],check=True)

subprocess.run(["pip install -r requirements.txt"],check=True)



"""


except subprocess.CalledProcessError as e:
    print(f"\nGit clone failed with exit code {e.returncode}")
    sys.exit(e.returncode)
except FileNotFoundError:
    print("Error: 'git' was not found. Make sure Git is installed and available in your PATH.")
    sys.exit(1)
"""