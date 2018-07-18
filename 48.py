#48. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
#  output = [[1, 2, 3], [5], [7, 8, 9, 10, 11, 12, 13], [20], [22, 23, 24, 25, 26, 27], [20, 21, 22], [4]]
l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
def subdiv(l):
    main=[]
    sub=[]
    #print(id(main),"...",id(sub))
    for i in l:
        if len(sub)!=0:
            if (i-sub[len(sub)-1])!=1:
                main.append(sub)
                sub=[]
        sub.append(i)
    main.append(sub)
    return main

print(subdiv(l))