import os
import json
from os.path import exists,join

def git_log():
    d={}
    l=[]
    fw=open("json_log.json","w")
    fr=open("g_log.txt","r")
    for line in fr.readlines():
        if "commit" in line and len(d)>1:
            l.append(d)
            d={}
        if "commit" in line:
            s=line
            d["commit"]=line.rstrip('\n')
        elif "Author:" in line:
            l1=line.split("Author:")
            d["Author:"]=l1[1].rstrip('\n')
        elif "Date:" in line:
            l1=line.split("Date:")
            d["Date"]=l1[1].rstrip('\n')
        elif not line=='\n':
            d["msg"]=line.rstrip('\n')
    json.dump(l,fw,indent=4,separators=(',',':'))
    fw.close()
    fr.close()

def exe_cmd(cmd):
    os.system(cmd)
def search_file(filename,search_path):
    paths=search_path.split('/')
    for path in paths:
        if exists(join(path,filename)):
            return True
    return False

if not search_file("trail","/home/amani/linux"):
    exe_cmd("git clone https://github.com/amanimogilipalem/trail")
    os.chdir("/home/amani/linux/trail")
else:
    os.chdir("/home/amani/linux/trail")
    exe_cmd("git pull origin master")
exe_cmd("git log>g_log.txt")

exe_cmd("git add -A")
exe_cmd("git commit -m ...gitlogfile...")
exe_cmd("git push -u https://github.com/amanimogilipalem/trail.git")
git_log()
