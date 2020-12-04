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
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
'''