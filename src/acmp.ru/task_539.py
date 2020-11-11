from math import log2

fin  = open("input.txt")
fout = open("output.txt","w")

n = int(fin.readline())
log_n = log2(n)

if log_n - int(log_n) == 0:
    fout.write(str(int(log_n)))
elif n % 2 == 0:
    fout.write(str(int(n // 2)))
else:
    fout.write(str(n))

fin.close()
fout.close()