fin = open("input.txt")
n = fin.readline().strip()
prev_n = n
q = 0

while True:
    asc = int(''.join(sorted(prev_n)))
    desc = int(''.join(sorted(prev_n, reverse=True)))
    diff = desc - asc
    s = str(diff // 1000) + str(diff % 1000 // 100) + str(diff % 100 // 10) + str(diff % 10)

    if s == prev_n:
        break
    else:
        q += 1
        prev_n = s

print(prev_n)
print(q)

fin.close()