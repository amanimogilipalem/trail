import subprocess
import os
import time
def exe_cmd(cmd):
    os.system(cmd)
exe_cmd("git add -A")
exe_cmd("git commit -m ..noo...")
exe_cmd("git clone https://github.com/mpigelati/Python_adb")
time.sleep(3)
exe_cmd("cd C:/Users/barrambelly/PycharmProjects/assignment/Python_adb")
#time.sleep(3)
#exe_cmd("git log>C:/Users/barrambelly/PycharmProjects/assignment/Python_adb/g_log.txt")
buff=subprocess.check_output("git log")
print(buff)