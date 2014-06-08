def proc(v):
  x=len(v)
  l=[]
  for i in xrange(x):
    l.append(int(v[i]))
  return l

def ap(a,n,d):
    #sys.stdout.write(" ")
    #sys.stdout.write(a+((x-1)*d))
    print ' '.join([str(a+i*d) for ti in xrange(n)])



x=input()
while(x!=0):
  x-=1
  v=proc(raw_input().split())
  n=(2*v[2])/(v[0]+v[1])
  d=(v[1]-v[0])/(n-6)
  a=v[0]-(2*d)
  print n
  ap(a,n,d)
