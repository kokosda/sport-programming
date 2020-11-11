fin = open('input.txt')
n = int(fin.readline())
c = list(map(int, fin.readline().split()))

max_c = []
max_el, max_el_i = 0, -1

while max_el_i != n - 1:
    if max_el_i == -1:
        max_el_i = 0

    for i in range(max_el_i, n):
        if c[i] > max_el:
            max_el = c[i]
            max_el_i = i

    c[max_el_i] = -1
    max_c.append([max_el, max_el_i])
    max_el = 0

sum, prev_idx = 0, 0

for i in range(len(max_c)):
    cost, idx = max_c[i][0], max_c[i][1]
    if i == 0:
        sum += cost * (idx - prev_idx + 1)
    else:
        sum += cost * (idx - prev_idx)
        
    prev_idx = idx

print(sum)

fin.close()