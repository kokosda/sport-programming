fin = open('input.txt')
n = int(fin.readline())
c = list(map(int, fin.readline().split()))

max_i = n - 1
sum = c[max_i]

for i in range(n - 2, -1, -1):
    if c[max_i] < c[i]:
        max_i = i
    sum += c[max_i]

print(sum)

fin.close()