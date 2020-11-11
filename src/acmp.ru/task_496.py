fin  = open("input.txt")

n = int(fin.readline())
a = list(map(int, fin.readline().split()))
a.append(a[0])
a.insert(0, a[len(a) - 2])

max_q = 0

for i in range(1, n + 1):
    q = a[i - 1] + a[i] + a[i + 1]
    max_q = max(max_q, q)

print(max_q)

fin.close()