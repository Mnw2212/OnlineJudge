n=input()

def process(string):
	x=string.split()
	new=[int(x[i]) for i in range(2)]
	return new
	
if __name__=="__main__":
	for i in range(n):
		ass=process(raw_input())
		base=ass[0]
		ans=ass[0]
		index=ass[1]
		for j in range(2,index+1):
			ans=ans*base%10
		print ans
