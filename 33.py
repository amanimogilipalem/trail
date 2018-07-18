#33. input: "google" print count of each character
def charcount(c):
    global word
    cnt=0
    for i in word:
        if i==c:
            cnt=cnt+1
    return cnt
word=input("enter a word: ")
char=[]
cnt=[]
for c in word:
    if c not in char:
        char.append(c)
        cnt.append(charcount(c))
for i,j in zip(char,cnt):
    print(i,":",j)