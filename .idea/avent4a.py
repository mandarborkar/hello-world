f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent4input.txt", "r")
mylist = f1.readlines()
#print (mylist)
numberofpassports=0
passport = []
newpassportcomingup=1
for i in range (0,len(mylist)):
    # print("passport = " + passport[numberofpassports])
    if newpassportcomingup==1 :
        passport.append(mylist[i])
        # print ("passport " + str(numberofpassports) + " = " + passport[numberofpassports])
    if mylist[i] == "\n" :
        newpassportcomingup=1
        numberofpassports += 1
    else:
        passport[numberofpassports]= passport[numberofpassports] + mylist[i]
        newpassportcomingup = 0
        # print ("passport " + str(numberofpassports) + " = " + passport[numberofpassports])

ValidPassportcount=0
for i in range (0,len(passport)):
    passport[i]=passport[i].replace("\n"," ")
    if passport[i].count("byr") != 0 and passport[i].count("iyr") != 0 and passport[i].count("eyr") != 0 and passport[i].count("hgt") != 0 and passport[i].count("hcl") != 0 and passport[i].count("ecl") != 0 and passport[i].count("pid") != 0  :
        passport[i] = passport[i] + " Valid"
        ValidPassportcount += 1
    else:
        passport[i] = passport[i] + " Invalid"
    print ("passport " + str(i) + " = " + passport[i])

print (str(numberofpassports))
print (str(ValidPassportcount))
''' 
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
'''