import os
import subprocess

conemu_path = r"C:\Program Files\ConEmu\ConEmu64.exe"  # Change if your path is different

#conemu_path = r"A:\Program Files\ConEmu\ConEmu64.exe"  # Change if your path is different

#A:\Program Files\ConEmu

cwd = os.getcwd()
subprocess.run([conemu_path, "/dir", cwd])
