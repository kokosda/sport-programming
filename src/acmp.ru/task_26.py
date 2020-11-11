from math import sqrt
fin  = open("input.txt")

x0, y0, r0 = map(int, fin.readline().split())
x1, y1, r1 = map(int, fin.readline().split())

l = sqrt(abs(x0 - x1) ** 2 + abs(y0 - y1) ** 2)

if l <= (r0 + r1):
    max_r = max(r0, r1)
    min_r = min(r0, r1)

    if max_r > l:
        if (l + min_r) >= max_r:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')
else:
    print('NO')

fin.close()