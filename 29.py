#29. names  ="emp1,emp2,emp3,emp4" iterate through the employee names.
names=input("enter names: ")
list=names.split(",")
for name in list:
    print(name)