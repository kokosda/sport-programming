fin  = open("input.txt")
fout = open("output.txt","w")

s, t = map(int, fin.readline().split())

if t > s:
	fout.write(str(t - s))
else:
	fout.write(str(12 - s + t))

fin.close()
fout.close()