#[2]
#0-0
#0-1
#0-2
#1-1
#1-2
#2-2
#12
#0sum(n + 1) + 1sum(n) + 2sum(n - 1)
fin  = open("input.txt")
fout = open("output.txt","w")
 
n = int(fin.readline())
s = 0

for i in range(n + 1):
	a1 = i
	an = n
	s += ((a1 + an) / 2) * (n - i + 1) + i * (n - i + 1)

fout.write(str(int(s)))
 
fin.close()
fout.close()