num = input()

for i in xrange(num):
  ans=0
  n=input()
  men=raw_input().split()
  women=raw_input().split()
  for j in range(n):
    ans+=int(men[j])*int(women[j])
  print ans
