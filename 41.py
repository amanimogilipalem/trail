#41. input: fun(5) output: [1,2,3,4,3,2,1]
def fun(n):
    l=[]
    for i in range(1,n):
        l.append(i)
    for i in range(n-2,0,-1):
        l.append(i)
    return l

print(fun(5))