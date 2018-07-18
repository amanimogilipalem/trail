#35. l=[1,2,3] just make it as a string.

l=[1,2,3]
for i in range(len(l)):
    l[i]=str(l[i])
str=''.join(l)
print(str)