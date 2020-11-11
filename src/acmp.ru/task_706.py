fin  = open("input.txt")
r, x, y = map(int, fin.readline().split())

if r == 0:
    print(abs(x))
else:
    r1 = abs(r - y)
    coef = r1 / r
    ox1 = abs(x) / (1 + coef)

    print(ox1)

fin.close()