file_path = "example.txt"
text = """

click enter to replace all \n\n with just \n
for file

"""

print(text+file_path)
# Read the file
with open(file_path, "r", encoding="utf-8") as f:
  text = f.read()

# Replace double newlines with single newlines
new_text = text.replace("\n\n", "\n")

# Save the changes back to the file
with open(file_path, "w", encoding="utf-8") as f:
  f.write(new_text)
