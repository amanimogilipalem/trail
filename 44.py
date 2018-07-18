#44. l=['1','2','3'] get the sum of the list
def listsum(l):
    sum=0
    for i in l:
        sum=sum+int(i)
    return sum

l=['1','3','5','2']
print("sum of list:",listsum(l))