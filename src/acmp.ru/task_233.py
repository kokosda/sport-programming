fin  = open("input.txt")
fout = open("output.txt","w")

s = fin.readline()

if s.count('0') == 0:
	fout.write('YES')
else:
	fout.write('NO')

fin.close()
fout.close()