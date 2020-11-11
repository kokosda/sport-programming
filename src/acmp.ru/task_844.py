from math import sqrt

fin  = open("input.txt")
 
a, b = map(int, fin.readline().split())
c = sqrt(a * b)

if c - int(c) == 0:
	print(int(c))
else:
	print(0)
 
fin.close()