
import sys,os
#new_file = os.path.join(a,b,c)
#cwd = os.getcwd()
#files = os.listdir(cwd)


cwd = os.getcwd()
files = os.listdir(cwd)

for a in range(0,len(files)):
    val = files[a]
    if "0" in val:
        new_name = val.replace("0","")

        os.rename(val,new_name)
