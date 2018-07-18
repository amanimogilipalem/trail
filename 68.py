"""68. Take Source and destination file paths from command line arguments and copy the sourcontent into destination.
    Make Sure that your program checking the below conditions.
     1.if the source file not there. Should ask the user to enter new source file or want to quit a program
     2.if the destination file already there in the specified path. Should warn the user want to proceed or want to enter new destination file name or want to quit
"""
import sys
def filecopy(dst,src):
    f = open(src, 'r')
    if f==False:
        print("source file not exist")
        exit()
    buff = f.read()
    f.close()
    f = open(dstpath, 'w')
    f.write(buff)
if len(sys.argv)!=3:
    print("error:python file.py source destination")
    exit()
srcpath=sys.argv[1]
dstpath=sys.argv[2]
filecopy(dstpath,srcpath)
