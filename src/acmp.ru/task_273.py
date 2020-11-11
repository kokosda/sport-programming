fin = open("input.txt")

n = fin.readline().strip()
a = set()

for i in range(len(n)):
    if n[i] == '0':
        continue

    for j in range(i + 1, len(n)):
        for k in range(j + 1, len(n)):
            a.add(n[i] + n[j] + n[k])

print(len(a))

fin.close()