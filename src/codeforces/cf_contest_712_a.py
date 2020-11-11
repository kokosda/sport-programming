n = int(input())
a = list(map(int, input().split()))

b = []

for i in range(n - 2, -1, -1):
    bi = a[i + 1] + a[i]
    b.append(bi)

b.reverse()
b.append(a[n - 1])

print(' '.join([str(i) for i in b]))
