def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
import sys,os

def read_txt(file_path):
    # Add encoding='utf-8' here:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content