#34. Convert n dimentional list to single dimentiona list.

l=[10,20,30,[40,[45,50],60],70,[80,[81,82,83,[84,85,[86,87],88,89]],90,20]]
new=[]
temp=[]
def multilist(l):
    global new
    for i in l:
        if type(i)==list:
            multilist(i)
        else:
            new.append(i)
multilist(l)
print(new)