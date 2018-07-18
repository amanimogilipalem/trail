#6. take a string from the user and check contains only  alphabets or not?
str=input("enter a string:")
for i in str:
    if not ((i>='A' and i<='Z') or (i>='a' and i<='z')):
        print("alphanumeric")
        break
else:
    print("only alphabets")
