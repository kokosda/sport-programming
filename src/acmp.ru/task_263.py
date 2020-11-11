fin  = open("input.txt")
fout = open("output.txt","w")

n, i, j = map(int, fin.readline().split())

r1 = abs(i - j) - 1
r2 = n - max(i, j) + min(i, j) - 1

fout.write(str(min(r1, r2)))

fin.close()
fout.close()