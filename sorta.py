def findlargest (inputarray):
    largest=0
    for j in range(len(inputarray)):
        if inputarray[j-1] < inputarray[j]:
            largest=j
    return largest
inputarray = [1, 2, 3, 4, 5, 6]
print ("My input array = ")
print (inputarray)
outputarray = []
for i in range(len(inputarray)):
    largest=findlargest(inputarray)
    outputarray.append(inputarray[largest])
    inputarray[largest]=0
print ("My output array = ")
print (outputarray)
# upload latest