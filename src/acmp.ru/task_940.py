fin  = open("input.txt")
fout = open("output.txt","w")

k_s, s = fin.readline().split()
k = int(k_s)

s = s[:k-1] + s[k:]

fout.write(s)

fin.close()
fout.close()