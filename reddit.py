import os,sys,shutil
uninstall_firefox = r"A:\Program Files (x86)\Mozilla Firefox\uninstall\helper.exe"
try:
	os.startfile(uninstall_firefox)
except:
    print("does not exist")
    print("directory",uninstall_firefox)

input("click this after u uninstall chrome..so that all the remaining dirs can be uninstalled")    

app_data = r"A:\Users\-\AppData"
lis = os.listdir(app_data)
for folder in lis:
    specific_mozilla = os.path.join(app_data, folder,"Mozilla")  # Corrected: using os.path.join()
    specific_google = os.path.join(app_data, folder,"Google")  # Corrected: using os.path.join()
    #print("specific_mozilla",specific_mozilla)
    #print("specific_google",specific_google)
    #continue
    #remove dir
    try:
        shutil.rmtree(specific_mozilla)
    except:
        print("didn't work deleting",specific_mozilla)

    try:
        shutil.rmtree(specific_google)
    except:
        print("didn't work deleting",specific_google)


#delete remaining google directory in program files 86

#A:\Program Files (x86)\Google

dir_google_32 = r"A:\Program Files (x86)\Google"
dir_google_64 = r"A:\Program Files\Google"
try:
    shutil.rmtree(dir_google_32)
    shutil.rmtree(dir_google_64)
    print("deleted dir_google_32",dir_google_32)
    print("deleted dir_google_64",dir_google_64)

except:
    print("doesn't exist dir_google_32",dir_google_32)
    print("doesn't exist dir_google_64",dir_google_64)

print("")
print("ok..all cookies firefox and chrome..")
print("should be abolished..")
print("should be good to reinstall..")

print("or..all dirs and cookies..")
