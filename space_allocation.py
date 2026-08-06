import os
path=r"B:\Users\-\AppData\Local\Programs\Python\Python37\Lib\site-packages"
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