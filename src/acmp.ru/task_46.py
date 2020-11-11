fin  = open("input.txt")
 
n = int(fin.readline())
e = '2.7182818284590452353602875'

if n == 0:
	print(3)
elif n == 25:
	print(e)
else:
	d = int(e[n + 1])
	p = int(e[n + 2])

	if p >= 5:
		d += 1

	e = e[:n + 1] + str(d)
	print(e)

fin.close()