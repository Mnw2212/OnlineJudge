def process(line):
    return sorted([int(i) for i in line.split()])

n = int(raw_input())         #This is for number of shows
results = []
for t in range(n):           #Do this "n" times
    num = int(raw_input())   #This is number of men/women

    men = process(raw_input())
    women = process(raw_input())
    print men
    print women

    p = sum(m*w for m, w in zip(men, women))
    results.append(p)
    print results

for item in results:
    print item
