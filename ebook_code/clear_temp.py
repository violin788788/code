
import sys,os
#new_file = os.path.join(a,b,c)
#cwd = os.getcwd()


import os
import tempfile
def clear_large_temp_files(size_limit_mb=100):
    temp_dir=tempfile.gettempdir()
    size_limit=size_limit_mb*1024*1024
    print(f"Checking temp folder: {temp_dir}")
    deleted=0
    for root,dirs,files in os.walk(temp_dir):
        for file in files:
            try:
                path=os.path.join(root,file)
                size=os.path.getsize(path)
                if size>size_limit:
                    os.remove(path)
                    deleted+=1
                    print(f"Deleted: {path} ({size/1024/1024:.1f} MB)")
            except (PermissionError,FileNotFoundError):
                pass
    print(f"Cleanup complete. Removed {deleted} large temp files.")
clear_large_temp_files(100)