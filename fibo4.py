x=1
y=1
z=0
i=1
print ("fibo["+str(i)+"]="+str(x))
i=2
print ("fibo["+str(i)+"]="+str(y))
for i in range(3):
    z=x+y
    x=y
    y=z
    print ("fibo["+str(i+2)+"]="+str(z))