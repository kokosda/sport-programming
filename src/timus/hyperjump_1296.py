#fin = open('input.txt')

m = int(input())
res = 0

if m > 0:
    moments = [0] * m
    i = 0

    while i < m:
        moments[i] = int(input())
        i += 1

    res = 0
    cur_sum = 0

    for i in range(m):
        cur_sum += moments[i]

        if cur_sum > res:
            res = cur_sum
        elif cur_sum < 0:
            cur_sum = 0

print(res)

#fin.close()

"""
31 -41 59 26 -53 58 97  -93 -23 84
0  -10 49 75  22 80 177  84  61 145

2
-10 5
-10 -5
"""