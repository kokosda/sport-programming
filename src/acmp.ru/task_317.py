fin = open("input.txt")
x, y, z, w = map(int, fin.readline().split())

max_count = w // min(x, y, z) + 1
s = 0

for i in range(0, max_count):
    for j in range(0, max_count):
        k = (w - x * i - y * j) // z

        if k < 0:
            continue

        if (x * i + y * j + z * k) == w:
            s += 1

print(s)

fin.close()