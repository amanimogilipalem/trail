#32. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as sigle dimentiona list

l=[10,20,30,[40,50,60],70,[80,90,20]]
new=[]
temp=[]
for i in l:
    if type(i)==list:
        new.extend(i)
    else:
        new.append(i)

print(new)