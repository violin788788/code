import os
import getpass

drive = str(os.getenv('SystemDrive'))
drive = drive+"\\"
user = getpass.getuser()  # This works on Windows, macOS, Linux
print(drive)
print(user)
save_directory = os.path.join(drive,"Users",user,"Downloads")
print(save_directory)
