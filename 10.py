#10. Show the below menu to the user until and until user select quit and display corresponding os message
'''
Menu:
1. windows
2. Linux
3. Mac
4. quit
'''
while(True):
    print("Menu:\n","1.windows\n","2.Linux\n","3.Mac\n","4.quit")
    i=int(input("enter ur choice:"))
    if i==1:
        print("welcome to windows")
    elif i==2:
        print("welcome to linux")
    elif i==3:
        print("welcome to mac")
    elif i==4:
        exit(0)
    else:
        print("invalid choice")
