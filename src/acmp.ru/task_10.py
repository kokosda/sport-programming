fin  = open("input.txt")

a, b, c, d = map(int, fin.readline().split())

coef_min = -100
coef_max = 100
roots = set()

for i in range(coef_min, coef_max + 1):
    r = a * i ** 3 + b * i ** 2 + c * i + d

    if r == 0:
        roots.add(i)

print(*sorted(roots))

fin.close()