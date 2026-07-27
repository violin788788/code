import os
import subprocess
def add_path_from_txt(txt_file):
    try:
        with open(txt_file, 'r') as file:
            directory_to_add = file.read().strip()
        current_path = os.environ.get('PATH', '')
        if directory_to_add not in current_path:
            new_path = current_path + os.pathsep + directory_to_add
            os.environ['PATH'] = new_path
            subprocess.run(['setx', 'PATH', new_path], shell=True)
            print(f"Successfully added {directory_to_add} to PATH.")
        else:
            print(f"{directory_to_add} is already in the PATH.")
    except Exception as e:
        print(f"Error: {e}")
txt_file = "path_path_to_add.txt"
add_path_from_txt(txt_file)
