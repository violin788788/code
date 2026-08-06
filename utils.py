#from utils import *
import sys,os,math,subprocess
"""
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
"""
def read_txt(file_path):
    #text = read_txt("file.txt")
    # Add encoding='utf-8' here:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content