

def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)

import sys,os
#new_file = os.path.join(a,b,c)
cwd = os.getcwd()
files = os.listdir(cwd)

