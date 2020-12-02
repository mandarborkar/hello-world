import math
def isdivisible (inputx,inputy):
    if (inputx%inputy == 0 ):
        return True;
    else:
        return False;

# upload latest
a=int(input("a = "))
c=int(math.sqrt(a))
b=[]
for i in range (1,c,1):
    b.append(i)
print ("divisibility list", b)
print (str(len(b)))
for i in range (2,len(b),1):
    if b[i] != 0 :
        for j in range (2*b[i],len(b),b[i]):
            b[j]=0
            print (str(j)+"revised divisibility list", b)
if isdivisible(a, 2):
    print("Is Even")
    exit()
for i in range (3,c,2):
    print ("checking disvibility with "+str(i))
    if isdivisible(a,i):
        print("Is Divisible")
        exit()
print("Is prime")