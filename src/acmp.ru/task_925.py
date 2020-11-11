fin  = open("input.txt")
 
maxmin = int(fin.readline())
n, a, b, c = map(int, fin.readline().split())
r = 0
 
if maxmin == 2:
	r = min(a, b, c)
else:
	a0 = n - a
	b0 = n - b
	c0 = n - c
	r = max(0, n - (a0 + b0 + c0))
 
print(r)
 
fin.close()