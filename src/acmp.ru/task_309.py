fin  = open("input.txt")

k = int(fin.readline())
n = 0

for i in range(k):
    j = i
    u = 0
    while j > 0:
        u = u * 10 + j % 10
        j = j // 10

    if i + u == k:
        n += 1

print(n)

fin.close()