"""16. Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
	Deside whether there is sufficient busses or not and give solution for how many extra busses required.  """
people=int(input("Total number of people:"))
busses=int(input("Total number of busses:"))
seats=int(input("Number of seats for bus:"))
diff=people-(busses*seats)
if diff>0:
    cnt=diff//seats
    if (diff/seats)>(diff//seats):
        cnt=cnt+1
    print(cnt,"more busses requires")
elif diff<0:
    print(-(diff),"seats are free")
elif diff==0:
    print("busses are sufficient")

#for identifing automatic build in jenkins
