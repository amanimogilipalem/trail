#24. Write a program to findout biggest number in the given numbers.
max=0
a=input("enter numbers: ")
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
    if a[i]>max:
        max=a[i]
print("biggest number is: ",max)