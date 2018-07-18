#61. number of lines, words, characters
lines=0
words=0
char=0
with open('ex.py', 'r') as file:
    for row in file:
        lines+=1
        for c in row:
            char+=1
            if c==' ':
                words+=1
print(lines,words,char)
