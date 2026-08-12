import shutil

folder_path = r"B:\Program Files\kdenlive"

try:
    shutil.rmtree(folder_path)
    print("The folder is deleted.")
except OSError as e:
    print(f"Error: {e}")
