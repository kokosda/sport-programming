fin  = open("input.txt")
fout = open("output.txt","w")

n, m, y, x = map(int, fin.readline().split())

if (y - 1) % 2 == 0:
	fout.write(str((y - 1) * m + x - 1))
else:
	fout.write(str((y - 1) * m + m - x))

fin.close()
fout.close()