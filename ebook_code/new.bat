@echo off
cd /d "%~dp0"
copy /Y "..\new.py" "new.py"
python "new.py"
pause