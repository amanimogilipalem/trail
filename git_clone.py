import subprocess
import os
import json
def log_dict():
    def command_exe(cmd):
        process=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
        out,error=process.communicate()
        process.wait()
        print(str(out.decode('ascii')))
    if (os.path.isdir("./Python_adb")):
        os.chdir("Python_adb")
        command_exe("git pull origin master --allow-unrelated-histories")
    else:
        command_exe("git clone https://github.com/mpigelati/Python_adb")
        os.chdir("Python_adb")
    command_exe("git log>log_msg.txt")
lst=[]
dict={}
with open("log_msg.txt","r")as fr:
    data=fr.readlines()
with open("git_log.json","w")as fw:
    for line in data:
        if "commit" in line and len(d)>0:
            lst.append(d)
            dict={}
        if "commit"in line:
            L=line
            d["commit"]=line.rstrip("\n")
        elif "Author:"in line:
            lst1=line.split("Author:")
            d["Author"]=lst1[1].rstrip("\n")
        elif "Date:" in line:
            lst1=line.split("Date:")
            d["Date"]=lst1[1].rstrip("\n")
        elif not line =="\n":
            d['message']=line.rstrip("\n")
    json.dump(lst,fw,indent=4,separators=(',',':'))
    fr.close()
    fw.close()
log_dict()


