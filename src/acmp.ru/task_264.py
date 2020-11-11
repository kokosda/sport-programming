fin  = open("input.txt")

n = int(fin.readline())
a = list(map(int, fin.readline().split()))
t, t0 = 0, 0

for i in range(n):
    if a[i] > 0:
        t0 += 1
        t = max(t, t0)
    else:
        t0 = 0

print(t)

fin.close()