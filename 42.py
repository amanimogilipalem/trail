#42.input fun('abc') output: [[],][a],[b],[c],[a,b],[b,c],[c,a],[a,b,c]]
def fun(str):
    l=[[]]
    for i in str:
        l.append(list(i))
    return l
print(fun('abc'))