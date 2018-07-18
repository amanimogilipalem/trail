#39. find the start position of the largest block of repeated characters in a given string
str=input("enter a string:")
def repblock(str):
    pos=-1
    pre=0
    cur=-1
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i]==str[j]:
                t=i
                cur=1
                for i,j in zip(range(i+1,len(str)),range(j+1,len(str))):
                    if str[i]!=str[j] or i==len(str) or j==len(str):
                        break
                    cur=cur+1
                if cur>pre:
                    pre=cur
                    pos=t
    return pos

print(repblock(str))