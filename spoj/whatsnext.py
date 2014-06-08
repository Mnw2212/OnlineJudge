#problem code ACPC10A
import sys

def process(string):
  num=[]
  x=string.split()
  for i in range(3):
    num.append(int(x[i]))

  return num

while(True):
  x=raw_input()
  num = process(x)
  zero=[0,0,0]
  con = (set(num)==set(zero))
  if(con==True):
    break
  else:
    if ((num[0]-num[1])==(num[1]-num[2])):
      ap = num[1]-num[0]
      v = num[2]+ap
      print "AP",
      print v
    else:
      gp = num[2]/num[1]
      v = num[2]*gp
      print "GP",
      print v
