#11. take a string from the user and check contains atleast one digit or not?
str=input("enter a string:")
for i in str:
    if (i>='0' and i<='9'):
        print("TRUE")
        break
else:
    print("FALSE")
#example program
