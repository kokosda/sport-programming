fin  = open("input.txt")
fout = open("output.txt","w")

n = int(fin.readline())
a = [int(i) for i in fin.readline().split()]

for i in range(n - 1, -1, -1):
	fout.write(str(a[i]) + ' ')

fin.close()
fout.close()