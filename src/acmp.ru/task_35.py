fin  = open("input.txt")
fout = open("output.txt","w")

k = int(fin.readline())

for i in range(k):
    n, m = map(int, fin.readline().split())
    d = 19 * m + (n + 239) * (n + 366) / 2
    fout.write(str(int(d)) + '\n')

fin.close()
fout.close()