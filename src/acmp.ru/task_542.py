fin  = open("input.txt")
fout = open("output.txt","w")

m = int(fin.readline())
m0 = m
s = ''

while m0 > 0:
	s += str(m0 % 2)
	m0 = m0 // 2

s0 = ''
for i in range(len(s) - 1, -1, -1):
	s0 += s[i]

r = 0
for i in range(len(s0)):
	r += int(s0[i]) * 2 ** i

fout.write(str(r))

fin.close()
fout.close()