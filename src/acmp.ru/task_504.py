fin  = open("input.txt")
fout = open("output.txt","w")

k = int(fin.readline())

w = 'GCV'
o = []
o.append(w)

for i in range(1, 4):
	w = w[0] + w[2] + w[1]
	o.append(w)
	w = w[1] + w[0] + w[2]
	o.append(w)

r = o[(k * 2) % (len(o) - 1)]

fout.write(r)

fin.close()
fout.close()