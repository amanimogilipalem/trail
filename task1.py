import subprocess
from os.path import exists,join
from os import chdir

def exe_cmd(cmd):
    p= subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p.wait()
    print(str(output.decode('ascii')))

def search_file(filename, search_path):
    """Given a search path, find file
    """
    paths = search_path.split('/')
    for path in paths:
        if exists(join(path, filename)):
            return True
    return False

if not search_file("Python_adb","C:/Users/barrambelly/PycharmProjects/assignment"):
    exe_cmd("git clone https://github.com/mpigelati/Python_adb")
    chdir("C:/Users/barrambelly/PycharmProjects/assignment/Python_adb")
else:
    chdir("C:/Users/barrambelly/PycharmProjects/assignment/Python_adb")
    exe_cmd("git pull origin master --allow-unrelated-histories")

exe_cmd("git log>g_log.txt")
#exe_cmd("git push https://github.com/bhavani465/sample_rep.git master")