import os,sys
import shutil
from pathlib import Path
# Get the path of the current working directory
current_dir = Path.cwd()
# Move one directory up
parent_dir = current_dir.parent

original = os.path.join(parent_dir,"0new.py")
new = os.path.join(current_dir,"0new.py")

#full_path = os.path.join("user_data", "logs", "config.txt")
print( )
print(original)
print(new)

shutil.copy2(original, new)

#print(f"Current Directory: {current_dir}")
#print(f"Parent Directory: {parent_dir}")

sys.exit()


shutil.copy(item, destination)


# Loop through all items in the parent directory
for item in parent_dir.iterdir():
    # Only copy files to avoid infinite loops or recursively copying folders
    if item.is_file():
        destination = current_dir / item.name
        
        # Copy the file to the current directory
        shutil.copy2(item, destination)
        print(f"Copied: {item.name}")
