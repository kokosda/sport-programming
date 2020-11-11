n = int(input())
min1, max1 = map(int, input().split())
min2, max2 = map(int, input().split())
min3, max3 = map(int, input().split())

sum = min1 + min2 + min3
diplomas = [min1, min2, min3]

max1_t, max2_t, max3_t = max1, max2, max3

while diplomas[0] < max1 and sum < n:
    max1_t -= 1
    diplomas[0] += 1
    sum += 1

while diplomas[1] < max2 and sum < n:
    max2_t -= 1
    diplomas[1] += 1
    sum += 1

while diplomas[2] < max3 and sum < n:
    max3_t -= 1
    diplomas[2] += 1
    sum += 1

print(' '.join([str(i) for i in diplomas]))