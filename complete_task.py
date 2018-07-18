import os
import subprocess
import json

def execute_shell_command(cmd):
    pipe = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out,error)
    pipe.wait()


def git_clone(repo_url):
    cmd = 'git clone ' + repo_url
    execute_shell_command(cmd)


def git_pull():
    cmd='git pull origin master'
    execute_shell_command(cmd)

s1 ="https://github.com/mpigelati/Python_adb"


if os.path.isdir("Python_adb"):
    print("file exists")
    os.chdir("Python_adb")
    git_pull()
else:
    print("does not exist")
    git_clone(s1)
    os.chdir("Python_adb")

s="git log >test.txt"
execute_shell_command(s)

l1=[]
l2=[]
d={}
jp=open("js1.json","w")
f=open("test.txt","r")
for line in f.readlines():
    if "commit" in line and len(d)!=0:
        l2.append(d)
        d={}

    if "commit" in line:
        l1=line.split()
        d[l1[0]]=l1[1]
    elif "Date" in line:
        l1=line.split('Date:')
        d["Date"]=l1[1][:-1]
    elif "Author" in line:
        l1=line.split('Author:')
        d["Author"]=l1[1][:-1]
    elif not line=='\n':
            d["msg"]=line[:-1]
json.dump(l2, jp, indent=4, separators=(',',':'))
jp.close()

