fin  = open("input.txt")
fout = open("output.txt","w")

w, h, r = map(int, fin.readline().split())

if (min(w, h) / 2) >= r:
	fout.write('YES')
else:
	fout.write('NO')

fin.close()
fout.close()