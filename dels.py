import re
import os
input_file="dels.txt"
output_file="dels22.txt"
email_pattern=r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
with open(input_file,"r",encoding="utf-8") as file:
    text=file.read()
emails=re.findall(email_pattern,text)
emails=list(set(emails))
with open(output_file,"w",encoding="utf-8") as file:
    for email in emails:
        file.write(email+"\n")
print(f"Found {len(emails)} email(s). Saved to {output_file}.")
os.startfile(output_file)