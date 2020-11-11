fin  = open("input.txt")
fout = open("output.txt","w")
 
n = int(fin.readline())
a = list(map(int, fin.readline().split()))
m = int(fin.readline())

for k in range(m):
	i, j = map(int, fin.readline().split())

	fout.write(' '.join([str(p) for p in a[i - 1:j]]) + '\n')
 
fin.close()
fout.close()