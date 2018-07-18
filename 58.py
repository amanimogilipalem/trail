#58. WAP to remove n occurances of specified element from a list
l=[1,2,4,6,9,7,8,4,2,4,7]
def Remove(d,n):
    for i in l:
        if i==d and n!=0:
            l.remove(i)
            n=n-1

d=int(input("enter ele to delete:"))
n=int(input("enter n :"))
Remove(d,n)
print(l)