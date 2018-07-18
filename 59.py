#59. copy 1 file content in to another file(Take the source and destination file path from the user)
def filecopy(dst,src):
    f = open(src, 'r')
    buff = f.read()
    f.close()
    f = open(dstpath, 'w')
    f.write(buff)

srcpath=input("enter path of source file:")
dstpath=input("enter dest path")
filecopy(dstpath,srcpath)
