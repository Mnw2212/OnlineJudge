import math
x=input()
for i in range(x):
  n=raw_input()
  l=n.split()
  a=1/float(l[0])
  b=1/float(l[1])
  c=1/float(l[2])
  d=(a*b)+(b*c)+(c*a)
  print 1/(a+b+c+(2*math.sqrt(d)))
