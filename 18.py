#18. Determine the factors of a number entered  by the user
d=int(input("enter a number: "))
print("factors of",d,"are:")
for i in range(1,d+1):
    if d%i==0:
        print(i)