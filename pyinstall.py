import os,shutil,subprocess
from winshell import shortcut,desktop
APP_NAME="screenshot"
CURRENT_DRIVE=os.path.splitdrive(os.getcwd())[0]
INSTALL_DIR=os.path.join(CURRENT_DRIVE,r"\Program Files\screenshot")
PY_FILE="screenshot.pyw"
ICON_FILE="screenshot.ico"
print("Running PyInstaller to create onedir EXE")
subprocess.run(["pyinstaller","--onedir","--icon="+ICON_FILE,PY_FILE],check=True)
DIST_FOLDER=os.path.join("dist",os.path.splitext(PY_FILE)[0])
print(f"Copying onedir folder {DIST_FOLDER} to {INSTALL_DIR}")
if os.path.exists(INSTALL_DIR):
    shutil.rmtree(INSTALL_DIR)
shutil.copytree(DIST_FOLDER,INSTALL_DIR)
MAIN_EXE=os.path.join(INSTALL_DIR,os.path.splitext(PY_FILE)[0]+".exe")
SHORTCUT_PATH=os.path.join(desktop(),APP_NAME+".lnk")
print(f"Creating desktop shortcut at {SHORTCUT_PATH}")
with shortcut(SHORTCUT_PATH) as link:
    link.path=MAIN_EXE
    link.working_directory=INSTALL_DIR
    link.description=APP_NAME
print("Installation complete")
