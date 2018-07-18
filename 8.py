#8. take a string from the user and check contains only  capiatl letters or not?
str=input("enter a string:")
for i in str:
    if not (i>='A' and i<='Z'):
        print("FALSE: contains lower letters")
        break

else:
    print("TRUE: only upper letters")
