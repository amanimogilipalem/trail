#57. WAP to do all queue operations using lists
from collections import deque
q=deque([])
def enq(d):
    q.append(d)
def deq():
    if len(q):
        r=q[0]
        q.popleft()
        return r
    print("queue is empty")
def display():
    for i in q:
        print(i)

while(True):
    print("1.push 2.pop 3.display 4.peak 5.quit")
    ch=input("enter ur choice:")
    if ch=='1':
        d=input("enter element to push:")
        enq(d)
    elif ch=='2':
        print(deq(),"deleted")
    elif ch=='3':
        display()
    elif ch=='4':
        print("top:",q[len(q)-1])
    else:
        exit()
