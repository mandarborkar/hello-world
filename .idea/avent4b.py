#from aocd import get_data
#mylist = get_data(day=4)

f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent4input.txt", "r")
mypassporstring = f1.read()
passport = mypassporstring.split("\n\n")

def HasRequiredPassportInformation (singlepassport):
    # print (passportdetails)
    passportattribute = singlepassport.split (" ")
    # print (passportattribute)
    passportattributename = []
    for i in range (0,len(passportattribute)) :
        passportattributename.append (passportattribute[i].split (":")[0])

    RequiredPassportInformation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for requireddetails in RequiredPassportInformation:
        if requireddetails not in passportattributename :
            return 'Invalid'
    return 'Valid'

# cleaning up new lines and multiple spaces for each of the passports
validpassportcount = 0
for i in range (0,len(passport)):
    passport[i] = passport[i].replace ("\n"," ").strip ()
    passportstatus = HasRequiredPassportInformation (passport[i])
    passport[i] = passport[i] + " " + passportstatus
    if passportstatus == 'Valid':
        validpassportcount +=1
    print (passport[i])
#print (passport)
print ('Valid passports = ' + str(validpassportcount))
'''
mylist = mypassporstring.split("\n\n")
numberofpassports=0
passport = []
newpassportcomingup=True
for i in range (0,len(mylist)):
    if newpassportcomingup :
        passport.append(mylist[i])
    if mylist[i] != "\n" :
        passport[numberofpassports] = passport[numberofpassports] + mylist[i]
        newpassportcomingup = False
    else:
        newpassportcomingup=True
        numberofpassports += 1


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
print (passport[0])
'''
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