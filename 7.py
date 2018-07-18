#7. take a string from the user and check contains only  special chars or not?
str=input("enter a string:")
for i in str:
    if ((i>='A' and i<='Z') or (i>='a' and i<='z') or (i>='0' and i<='9')):
        print("alphanumeric")
        break

else:
    print("only special chars")
