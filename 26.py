#26. findout nth occurance of given substring
str1=input("enter a string: ")
str2=input("enter a substring: ")
n=int(input("enter occurance num: "))
l=str1.split(str2)
if len(l)<n+1:
    print("substring not occured",n,"time")
else:
    index=(n-1)*len(str2)
    for i in range(n):
        index=index+len(l[i])
    print(index)