#40. WAP to find union and intersection of lists.
def union(l1,l2):
    l=[]
    for i in l1:
        if i not in l:
            l.append(i)
    for i in l2:
        if i not in l:
            l.append(i)
    return l
def intersection(l1,l2):
    l=[]
    for i in l1:
        if (i in l2) and (i not in l):
            l.append(i)
    return l

l1=[1,3,5,7,6,7,'g','l',4]
l2=[0,7,'h','d','b',7,4,6]
print(union(l1,l2))
print(l1)
print(l2)
print(intersection(l1,l2))
