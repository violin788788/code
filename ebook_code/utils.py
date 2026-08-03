#from utils import *


import sys,os,math

def show(target_value):
    for key, value in list(locals().items()):
    #if target_value==key:
        print(key, "=", value)

    for key, value in list(globals().items()):
    #if target_value==key:
        #print(key, "=", value)
        print(key)


    """
    for name, val in globals().items():
        #if val == target_value:
        #print(f"{name}: {val}")
        print(name)
    """


def read_txt(file_path):
    #text = read_txt("file.txt")
    # Add encoding='utf-8' here:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content