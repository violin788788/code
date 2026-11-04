import os
import shutil

def copy_all_files(src_dir, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)

        if os.path.isdir(src_path):
            #shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            shutil.copytree(src_path, dst_path)
        elif os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
        print (item)

cwd = os.getcwd()
directories = os.path.splitdrive(cwd)
drive = val[0]

src = cwd+r"\dist\screenshot"
dst = drive+r"\Program Files\screenshot"

copy_all_files(src, dst)


"""
import os,subprocess,sys
folder="dist\\screenshot"
script="copy_files.py"
cmd=f'pyinstaller --onefile --add-data "{folder};{folder}" {script}'
subprocess.run(cmd,shell=True)
"""
