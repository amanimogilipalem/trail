#4. take a number from the user and check whether it is prime?
n=int(input("enter a number:"))
for i in range(2,n):
    if n%i==0:
        print("not prime number")
        break
else:
    print("prime number")
