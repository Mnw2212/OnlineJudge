
if __name__=="__main__":
  n=input()
  while(n!=-1):
    total=0
    candy=[]
    for i in range(n):
      x=input()
      candy.append(x)

    total=sum(candy)
    avg=(total/n)

    if avg*n!=total:
      val=-1
      print val

    else:
      pos_shift=0
      for i in range(0,n):
        if candy[i]<avg:
          pos_shift+=avg-candy[i]
      print pos_shift
    n=input()
