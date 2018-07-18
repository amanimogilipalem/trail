"""60. Show the below menu to the user:
     1. Add a row
     2. modify a row
     3. delete a row
     Go with one unique field in the file. And maintain that unique constraint in all file modifiction operations
     Use .CSV file for this program
"""
import csv
def add_row():
    f=open(file,'a',newline='')
    csvf=csv.writer(f)
    csvf.writerow(input("enter data:").split())
    f.close()
def modify_row(row):
    buff=[]
    f = open(file, 'r', newline='')
    csvf = csv.reader(f)
    for r in csvf:
        row=row-1
        if row==0:
            r=input("enter new data:").split()
        buff.append(r)
    f.close()
    #print(buff)
    f = open(file, 'w', newline='')
    csvf = csv.writer(f)
    for r in buff:
        csvf.writerow(r)
    f.close()
def delete_row(row):
    buff = []
    f = open(file, 'r', newline='')
    csvf = csv.reader(f)
    for r in csvf:
        row = row - 1
        if row == 0:
            continue
        buff.append(r)
    f.close()
    f = open(file, 'w', newline='')
    csvf = csv.writer(f)
    for r in buff:
        csvf.writerow(r)
    f.close()
file=input("enter file name:")
print("...menu...")
print("1. Add a row\n2. modify a row\n3. delete a row")
ch =int(input("enter ur choice:"))
if ch==1:
    add_row()
elif ch==2:
    row=int(input("enter row no:"))
    modify_row(row)
elif ch==3:
    row = int(input("enter row no:"))
    delete_row(row)