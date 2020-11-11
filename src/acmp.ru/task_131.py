fin  = open("input.txt")
fout = open("output.txt","w")
 
n = int(fin.readline())
v0, i0 = -1, -1

for i in range(n):
	v, s = map(int, fin.readline().split())
	
	if s == 1 and v0 < v:
		v0 = v
		i0 = i + 1

fout.write(str(i0))
 
fin.close()
fout.close()