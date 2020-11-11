fin  = open("input.txt")

m, n, i, j, c = map(int, fin.readline().split())

if (m * n) % 2 == 0:
    print('equal')
else:
    c_i_1 = c
    c_1_1 = c

    if j % 2 == 0:
        c_i_1 = abs(c - 1)

    if i % 2 == 0:
        c_1_1 = abs(c_i_1 - 1)
    else:
        c_1_1 = c_i_1

    if c_1_1 == 0:
        print('black')
    else:
        print('white')

fin.close()