import os
a=''
b=''
print ('Erasing output file')
if os.path.exists('output.csv'):
	os.remove('output.csv')
f2=open('output.csv','a')
print ('Reading input file......')
with open('input.csv') as f1:
	x=f1.readlines()
for y in x:
	a=a+y
print (a)
a=a.replace('\r',';').replace('\n','')
print (a)
f2.write(a)
print ('Writing output file....')
f2.close()
print ('Closing output file....')


