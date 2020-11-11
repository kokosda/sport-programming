fin  = open("input.txt")
fout = open("output.txt","w")
 
w, h = map(int, fin.readline().split())
a, b = [], []

for i in range(h * 2):
	if i < h:
		a.append(fin.readline())
	else:
		b.append(fin.readline())

ops = fin.readline()
o = {
	"00": ops[0],
	"01": ops[1],
	"10": ops[2],
	"11": ops[3]
}
r = []

for i in range(h):
	r.append('')

	for j in range(w):
		r[i] += o[a[i][j]+b[i][j]]

	fout.write(r[i] + '\n')
 
fin.close()
fout.close()