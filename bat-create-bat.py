def create_bat_from_txt(txt_file):
    try:
        with open(txt_file, 'r') as file:
            python_script = file.read().strip()
        if ".py" not in python_script:
            python_script = python_script+".py"
        bat_file=python_script.replace(".py",".bat")
        with open(bat_file, 'w') as bat:
            bat.write(f'@echo off\n')
            bat.write(f'python {python_script}\n')
            bat.write(f'pause\n')
        print(f"Batch file '{bat_file}' created successfully to run {python_script}")
    except Exception as e:
        print(f"Error: {e}")

txt_file = "bat-file-to-make-bat-of.txt"


create_bat_from_txt(txt_file)
