#25. findout third occurance of given substring
str1=input("enter a string: ")
str2=input("enter a substring: ")
l=str1.split(str2)
if len(l)<4:
    print("substring not occured third time")
else:
    index=2*len(str2)+len(l[0])+len(l[1])+len(l[2])
    print(index)