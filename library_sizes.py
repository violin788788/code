from utils import *
def show(value):
    #show(epub_file)
    for name, val in globals().items():
        if val is value:
            print(f"{name} = {value}")
            return
    print(value)
#new_file = os.path.join(a,b,c)
drive = os.path.splitdrive(os.getcwd())[0]
cwd = os.getcwd()
files = os.listdir(cwd)


path=r"B:\Users\-\AppData\Local\Programs\Python\Python38\Lib\site-packages"
sizes=[]
for d in os.listdir(path):
    print("getting size of ",d)
    p=os.path.join(path,d)
    if os.path.isdir(p):
        t=0
        for r,_,f in os.walk(p):
            for x in f:
                try:t+=os.path.getsize(os.path.join(r,x))
                except:pass
        sizes.append((t,d))
#sizes.sort(reverse=True)
sizes.sort()
for s,d in sizes:
    print(f"{s/1024/1024:8.2f} MB  {d}")