#5. take a string from the user and check contains only digits or not?
"""str=input("enter a string:")
for i in str:
    if i.isdigit()==False:
        print("alphanumeric")
        break
else:
    print("only digits")
"""
str=input("enter a string:")
for i in str:
    if not (i>='0' and i<='9'):
        print("alphanumeric")
        break
else:
    print("only digits")


#12. take a string from the user and check contains atleast one alphabets or not?
str=input("enter a string:")
for i in str:
    if (i>='A' and i<='Z')or(i>='a' and i<='z'):
        print("TRUE")
        break
else:
    print("FALSE")


#14. take a string from the user and check contains atleast one capital letter or not?
str=input("enter a string:")
for i in str:
    if (i>='A' and i<='Z'):
        print("TRUE")
        break
else:
    print("FALSE")

#15. take a string from the user and check contains atleast one small letter or not?
str=input("enter a string:")
for i in str:
    if (i>='a' and i<='z'):
        print("TRUE")
        break
else:
    print("FALSE")
