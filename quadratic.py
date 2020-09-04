import math
a=input ('a = ')
b=input ('b = ')
c=input ('c = ')
if (a == 0):
	x=float(-c/b)
	print ("Solution for x is "+str(x))
elif (b*b)-(4*a*c) < 0 :
	print ("Complex solutions")
else:
	x1=(-1*b+(math.sqrt((b*b)-(4*a*c))))/2*a
	x2=(-1*b-(math.sqrt((b*b)-(4*a*c))))/2*a
	print (str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0")
	print ("Solution for x are "+str(x1)+" and "+str(x2))