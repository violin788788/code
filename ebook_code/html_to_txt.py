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


html_file = "grant.html"
from bs4 import BeautifulSoup
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(separator="\n", strip=True)
output_txt = html_file.replace("html","txt")
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(text)
