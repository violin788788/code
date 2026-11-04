


"""
import os
uninstall_firefox = r"A:\Program Files (x86)\Mozilla Firefox\uninstall\helper.exe"
os.startfile(uninstall_firefox)
"""



"""


import subprocess

def uninstall_program(program_name):
    try:
        # Run the WMIC command to uninstall the program
        subprocess.run(['wmic', 'product', 'where', f'name="{program_name}"', 'call', 'uninstall'], check=True)
        print(f"{program_name} has been uninstalled.")
    except subprocess.CalledProcessError:
        print(f"Failed to uninstall {program_name}. Make sure it's installed.")

# Example usage
uninstall_program("Mozilla Firefox")


"""



"""

deletes and reinstalls firefox
and chrome so that when you
do a new reddit account then
it doesnt not let you log in


import os
import shutil

# Path to Firefox's user profile folder
firefox_profile_path = os.path.expanduser(r"~\AppData\Roaming\Mozilla\Firefox\Profiles")

# Remove all profiles
if os.path.exists(firefox_profile_path):
    shutil.rmtree(firefox_profile_path)

print("Firefox cache and cookies cleared.")



chrome_user_data_path = os.path.expanduser(r"~\AppData\Local\Google\Chrome\User Data")

# Remove Chrome's cache and cookies
if os.path.exists(chrome_user_data_path):
    shutil.rmtree(chrome_user_data_path)

print("Chrome cache and cookies cleared.")



import tempfile
import shutil

# Get temp directory path
temp_dir = tempfile.gettempdir()

# Clear files in temp directory
if os.path.exists(temp_dir):
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error removing file {file_path}: {e}")

print("Temporary files cleared.")




"""