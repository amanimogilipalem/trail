#56. WAP to do all stack operations using lists
l=[]
def push(d):
    l.append(d)
def pop():
    if len(l):
        r=l[len(l)-1]
        l.pop()
        return r
    print("stack is empty")
def display():
    for i in l:
        print(i)

while(True):
    print("1.push 2.pop 3.display 4.peak 5.quit")
    ch=input("enter ur choice:")
    if ch=='1':
        d=input("enter element to push:")
        push(d)
    elif ch=='2':
        print(pop(),"deleted")
    elif ch=='3':
        display()
    elif ch=='4':
        print("top:",l[len(l)-1])
    else:
        exit()
