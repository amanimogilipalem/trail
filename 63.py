"""63. Take three columns disease, symptoms, advice in a file and fill the details
	Ask the user to enter symptoms. Based on this symptoms Suggest the user to what disease it may be and few advices."""
sym=input("enter symptoms:")
with open('disease.csv', 'r') as file:
    for row in file:
        if sym in row:
            print(row.split(',')[0],":",row.split(',')[2])