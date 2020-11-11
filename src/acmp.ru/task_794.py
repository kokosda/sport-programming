fin  = open("input.txt")

n, m, k = map(int, fin.readline().split())
r2 = (min(k - 1, m) + m // k) * n

print(r2)

fin.close()