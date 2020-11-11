fin  = open("input.txt")
fout = open("output.txt","w")

n = int(fin.readline())
d, t1, t2, i = 0, 0, 1, 0

while i < n:
    d = t1 + t2
    t1, t2 = d, t1
    i += 1

fout.write(str(d))

fin.close()
fout.close()