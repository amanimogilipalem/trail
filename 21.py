#21. Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.
age=int(input("enter age: "))
if age<=1:
    print("baby")
elif age<3:
    print("toddler")
elif age<13:
    print("child")
elif age<19:
    print("teenager")
elif age<60:
    print("adult")
else:
    print("old")