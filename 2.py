#2. write a program to chek given substring is there in actual string or not? (search should be case insensitive)
str="hello GOOD morning"
str2=input("enter substring to search:")
print(str.casefold().find(str2.casefold()))

