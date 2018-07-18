#9. take a string from the user and check contains only  small letters or not?
str=input("enter a string:")
for i in str:
    if not (i>='a' and i<='z'):
        print("FALSE: contains upper letters")
        break

else:
    print("TRUE: only lower letters")
