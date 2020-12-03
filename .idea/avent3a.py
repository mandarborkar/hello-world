f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent3input.txt", "r")
mylist = f1.readlines()

rowcount=len(mylist)
columncount=len(mylist[0])
duplicatecount=int(columncount/rowcount)*3
for i in range (0,len(mylist)):
    mylist[i] = mylist[i].replace("\n","")
    for j in range (0,duplicatecount-1):
        mylist[i] += mylist[i]
print (mylist)
addtotree = 0
for i in range (0,len(mylist)-1):
    print (mylist[i+1][i*3])
    if mylist[i+1][i*3] == "#":
        addtotree += 1
        print (i)

print (addtotree)