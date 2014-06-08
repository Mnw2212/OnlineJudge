import math
def Prime(x):
	n=int(x)
	val=0
	factors=[]
	d = 2
	while n>1:
		while n%d==0:
			factors.append(d)
			n/=d
		d=d+1
	return factors

while(True):
	y=input()
	print Prime(y)