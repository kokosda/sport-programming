fin = open("input.txt")
n = int(fin.readline())
a = list(map(int, fin.readline().split()))
s = 0
prev_amount = 3

for i in range(n):
    if a[i] == 1:
        s += prev_amount
        prev_amount += 1
    else:
        prev_amount = max(3, prev_amount - 3)

print(s)

fin.close()