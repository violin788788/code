@echo off
cd /d "%~dp0"
copy /Y "..\new.py" "new.py"
echo new.py copied from directory code to current directory
echo .
python "new.py"
pause