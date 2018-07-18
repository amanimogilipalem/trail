import os
import subprocess

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
s1=" https://github.com/mpigelati/Python_adb"

#file="Python_adb"
#my_file = "/Users/machalla/Documents"
if os.path.isdir("Python_adb"):
    print("file exists")
    git_pull()
else:
    print("does not exist")
    git_clone(s1)


"""def log(s):
    pipe = subprocess.Popen(s, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    print(out, error)
    pipe.wait()
s="git log >log.txt"
log(s)
"""
