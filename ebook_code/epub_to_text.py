

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



import zipfile
from bs4 import BeautifulSoup
epubfile="1776.epub"
output=epubfile.replace(".epub",".txt")
text=[]
with zipfile.ZipFile(epubfile,"r") as z:
    for name in z.namelist():
        if name.endswith((".html",".xhtml",".htm")):
            data=z.read(name).decode("utf-8")
            soup=BeautifulSoup(data,"html.parser")
            text.append(soup.get_text("\n",strip=True))
with open(output,"w",encoding="utf-8") as f:
    f.write("\n\n".join(text))
print(f"Created {output}")