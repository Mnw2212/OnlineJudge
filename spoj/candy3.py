n = input()
for i in range(n):
  c=[]
  raw_input()
  x=input()
  for j in range(x):
    c.append(int(raw_input()))
  t=sum(c)
  if t%n==0:
    print "YES"
  else:
    print "NO"
