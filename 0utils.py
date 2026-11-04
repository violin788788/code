import sys,os,time

#cwd = cwd()
def cwd():
	cwd = os.getcwd(cwd)
	return cwd

#drive = drive()
def drive():	
	cwd = os.getcwd(cwd)
	drive = drive(cwd)
	return drive

#folder = folder()
def folder():
	cwd = os.getcwd(cwd)
	os.basepath(cwd)

#files = files()
def files():
	files = os.listdir()
	return files

