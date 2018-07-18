#37. l=['a','A','b','B','d','D','c','C'] WAP to find out case insensitive count and case insensitive search for an element.
from string import ascii_letters
def charcount(c):
    global word
    cnt=0
    for i in word:
        p=ascii_letters.find(c)
        if p>26:
            if i==ascii_letters[p] or i== ascii_letters[p - 26]:
                cnt=cnt+1
        else:
            if i==ascii_letters[p] or i== ascii_letters[p + 26]:
                cnt=cnt+1
    return cnt
def charsearch(c):
    global word
    for i in range(len(word)):
        p = ascii_letters.find(c)
        if p>26:
            if word[i]==ascii_letters[p] or word[i]== ascii_letters[p - 26]:
                return i
        else:
            if word[i]==ascii_letters[p] or word[i]== ascii_letters[p + 26]:
                return i
    else:
        return -1

word =input("enter a string: ")
c=input("enter a char: ")
if charsearch(c) != -1:
    print("found at:",charsearch(c))
    print("count:",charcount(c))
else:
    print("not found")