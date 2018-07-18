#30. Take actuual string, soucrce string, destination string. replce first nth occurances of soucestring with destination string of actual string
astr=input("enter a string: ")
sstr=input("enter source string: ")
dstr=input("enter dest string: ")
n=int(input("enter number of occurances to repalce: "))
l=astr.split(sstr)
l1=[]
l2=[]
for i in range(n+1):
    l1.append(l[i])
for i in range(n+1,len(l)):
    l2.append(l[i])
astr=dstr.join(l1)+sstr+sstr.join(l2)
print(astr)