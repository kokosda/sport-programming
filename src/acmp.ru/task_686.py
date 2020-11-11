fin = open("input.txt")

n = int(fin.readline())
a = list(map(int, fin.readline().split()))

a.sort()
b = [0] * n

for i in range(n):
    if i % 2 == 0:
        b[i // 2] = a[i]
    else:
        b[n - i // 2 - 1] = a[i]

print(*b)

fin.close()