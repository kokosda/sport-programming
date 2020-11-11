fin  = open("input.txt")
fout = open("output.txt","w")

l, w, h = map(int, fin.readline().split())
s = l * h * 2 + w * h * 2
q = s // 16

if s % 16 > 0:
	q += 1

fout.write(str(q))

fin.close()
fout.close()