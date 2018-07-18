#43. Remove duplicates from the list: a=[1,2,3,2,3,4,1,,3,4]
def removedups(l):
    temp=[]
    for i in l:
        if i not in temp:
            temp.append(i)
    return temp
l=[1,2,3,2,3,4,1,3,4]
print(removedups(l))