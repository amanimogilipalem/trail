#20. Take two numbers from the user a,b check whether a is divisible by b or not?
a=int(input("enter a number a= "))
b=int(input("enter a number b= "))
if b==0:
    print("b shoud not be 0")
elif a%b==0:
    print(a, "is divisible by",b)
else:
    print(a, "is not divisible by", b)