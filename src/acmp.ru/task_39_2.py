fin = open('input.txt')
n = int(fin.readline())
c = list(map(int, fin.readline().split()))

sum = 0

for i in range(n):
    max_el = 0

    for j in range(i, n):
        if c[j] > max_el:
            max_el = c[j]

    sum += max_el

print(sum)

fin.close()