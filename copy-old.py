import os,shutil,sys,ctypes
def is_admin(): return ctypes.windll.shell32.IsUserAnAdmin()!=0
if not is_admin(): ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable," ".join(sys.argv),None,1); sys.exit()
def resource_path(p): return os.path.join(sys._MEIPASS,p) if hasattr(sys,"_MEIPASS") else os.path.join(os.path.abspath("."),p)
src=resource_path("dist\\screenshot")
drive=os.path.splitdrive(sys.executable)[0] or "C:"
dst=os.path.join(drive,r"Program Files\screenshot")
os.makedirs(dst,exist_ok=True)
for i in os.listdir(src):
    s=os.path.join(src,i)
    d=os.path.join(dst,i)
    #shutil.copytree(s,d,dirs_exist_ok=True) if os.path.isdir(s) else shutil.copy2(s,d)
