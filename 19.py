#19. Play a number guessing game (User enters a guess, you print YES or Higher or Lower)
import random
num=random.randint(1,20)
print(num)
while(True):
    i=int(input("enter a number between 1 to 20: "))
    if i>num:
        print("Higher")
    elif i<num:
        print("Lower")
    else:
        print("YES")
        break