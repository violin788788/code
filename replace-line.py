# Python script to replace double newlines with single newlines

def replace_newlines(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Replace double newlines with single newline
    content = content.replace('\n\n', '\n')
    with open(file_path, 'w') as file:
        file.write(content)

        
# Replace 'your_file.html' with your actual file name
replace_newlines('screenshot.py')
