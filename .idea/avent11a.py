f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent11input.txt", "r")
waitingroom = f1.readlines()
print (len(waitingroom))
for i in range (0, len(waitingroom)):
    waitingroom[i] = waitingroom[i].replace('\n','')

print (waitingroom)