inputarray = [8, 7, 4, 3, 9, 6]
print ("My input array = ")
print (inputarray)
for i in range(len(inputarray)):
    for j in range(len(inputarray)):
        if inputarray[i]<inputarray[j]:
            larger=inputarray[i]
            inputarray[i]=inputarray[j]
            inputarray[j]=larger
print ("My output array = ")
print (inputarray)