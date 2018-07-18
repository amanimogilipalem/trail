"""64. Take employees info (id,name, age, adress, sal, height, weight)
	a. Take id, provide employee information for that id.
	b. find out average salary.
	c. find out which age, address taking the heighest salary
	d. find out every employee BMI value
	e. Finally find out the Organization overall BMI"""
import csv
def info(id):
    f= open("empinfo.csv", 'r', newline='')
    csvf = csv.reader(f)
    for row in csvf:
        if id in row:
            print("id:",row[0])
            print("name:",row[1],"\naddress:",row[3])
    f.close()
def avg_salary():
    n=0
    sal=0
    f = open("empinfo.csv", 'r', newline='')
    csvf = csv.reader(f)
    for row in csvf:
        n+=1
        sal+=int(row[4])
    return sal/n
def high_sal():
    pass
while(True):
    print("...menu...")
    print("1.empinfo 2.avg sal 3.highsal add 4.quit")
    ch=int(input("enter ur choice:"))
    if ch==1:
        id=input("enter emp id:")
        info(id)
    elif ch==2:
        print(avg_salary())
    elif ch==3:
        high_sal()
    elif ch==4:
        exit()
