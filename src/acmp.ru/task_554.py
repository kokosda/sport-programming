fin  = open("input.txt")
n = int(fin.readline())
s = 1

for i in range(1, n + 1):
    s += i

print(s)

fin.close()