#45. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists

def sum(l1,l2):
    l3=[i+j for i,j in zip(l1,l2)]
    return l3

l1=[1,2,3,4]
l2=[5,6,7,8]
print(sum(l1,l2))