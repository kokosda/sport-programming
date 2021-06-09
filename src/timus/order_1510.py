n = int(input())
i = 0
cur_k = -1
count_k = 0

while i < n:
    k = int(input())

    if cur_k == k:
        count_k += 1
    else:
        if count_k is 0:
            cur_k = k
            count_k = 1
        else:
            count_k -= 1

    i += 1

print(cur_k)

"""
3
3
2
2
2
3
3
3
"""