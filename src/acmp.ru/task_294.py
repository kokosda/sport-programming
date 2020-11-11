fin  = open("input.txt")

k1, l1, m1 = map(int, fin.readline().split())
k2, l2, m2 = map(int, fin.readline().split())

sb = k1 - k1 * l1 / 100
sg = k2 - k2 * l2 / 100
s_min = min(sb, sg)
s = (k1 - s_min) * m1 + (k2 - s_min) * m2

print(int(s))

fin.close()