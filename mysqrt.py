import math

def mysqrt(x):
    y=math.sqrt(x)
    y=math.floor(y)
    for i in range(y,1,-1):
        z = x % (i*i)
        if z==0:
            return i
    return y

inputx=int(48)
mainsquare=int(mysqrt(inputx))
remaingfactor=int(inputx/(mainsquare*mainsquare))
print ("sqrt("+str(inputx)+ ") = "+str(mainsquare)+"√"+str(remaingfactor))