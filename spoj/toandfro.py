import sys


def final(string,n):
	newstr=[]
	for i in range(len(string)):
		if i%2==0:
			newstr.append(string[i])
		else:
			newstr.append(string[i][::-1])
	for i in range(n):
		for j in range(len(newstr)):
			sys.stdout.write(newstr[j][i])
	sys.stdout.write("\n")


if __name__ == "__main__":
	n=1
	while(True):
		n=input()
		if(n==0):
			break
		else:
			text = raw_input()
			string = [text[i:i+n] for i in range(0, len(text), n)]
			final(string,n)
