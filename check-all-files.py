

"""
		if "A:" in text:
			print("A: - "+val)
		if "0code" in text:
			print("0code"+val)
"""

import sys,os

files = os.listdir()
print(files)

for a in range(0,len(files)):
	file = files[a]
	if ".py" in file:
		#print(file)
		with open(file,'r') as check:
			text=check.read()
			if "A:" in text:
				print("A: - "+str(file))
			if "0code" in text:
				print("0code - "+str(file))
			

"""
for val in enumerate(files):
#for val in range(0,len(files)):
	if ".py" in val:
	    with open(val, 'r') as file:
	        text = file.read()
		#text = #read file
		print(text)

		"""