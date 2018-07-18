#38. l=['a','A','b','B','d','D','c','C']  sort the list properly

l=['a','A','b','B','d','D','c','C']
def listsort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l

print(listsort(l))