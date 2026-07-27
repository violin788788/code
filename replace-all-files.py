"""
import os
for filename in os.listdir('.'):
    if '_' in filename:
        os.rename(filename, filename.replace('_', '-'))
        print(f'Renamed: {filename} -> {filename.replace("_", "-")}')
"""


import os
for filename in os.listdir('.'):
    if filename.endswith('.bat'):
        with open(filename,'r',encoding='utf-8') as f:
            content=f.read()
        content=content.replace('_','-')
        with open(filename,'w',encoding='utf-8') as f:
            f.write(content)
        print(f'Updated: {filename}')
