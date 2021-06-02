#fin = open('input.txt')

m = int(input())
res = 0

if m > 0:
    moments = [0] * m
    i = 0

    while i < m:
        moments[i] = int(input())
        i += 1

    max_sum_idx = 0
    max_sum = 0
    cur_sum = moments[0]
    sums = [0] * m

    for i in range(1, m):
        cur_sum += moments[i]
        sums[i] = cur_sum

        if cur_sum > max_sum:
            max_sum_idx = i
            max_sum = cur_sum

    res = max_sum

    for i in range(max_sum_idx):
        max_sum -= sums[i]

        if max_sum > res:
            res = max_sum

print(res)

#fin.close()

"""
31 -41 59 26 -53 58 97  -93 -23 84
0  -10 49 75  22 80 177  84  61 145
"""