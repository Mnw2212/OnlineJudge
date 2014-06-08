def palin():
  n=input()
  r=True
  while(r):
    n=n+1
    x=str(n)
    y=x[::-1]
    r=(x!=y)
  print n

x=input()
for i in range(x):
  palin()
