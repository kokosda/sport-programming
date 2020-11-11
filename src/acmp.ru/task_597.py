fin  = open("input.txt")
fout = open("output.txt","w")

r1, r2, r3 = map(int, fin.readline().split())

if r1 >= (r2 + r3):
	fout.write('YES')
else:
	fout.write('NO')


fin.close()
fout.close()