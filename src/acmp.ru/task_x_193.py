fin = open('input.txt')

n, m, k = map(int, fin.readline().split())
d = [0] * (k + 1)

for i in range(n):
	a = list(map(int, fin.readline().split()))

	for j in range(m):
		if a[j] == 0:
			continue

		if d[a[j]] == 0:
			d[a[j]] = [i, j, i, j]
			continue

		c = d[a[j]]
		c[0] = max(c[0], i)
		c[1] = min(c[1], j)
		c[2] = min(c[2], i)
		c[3] = max(c[3], j)

for i in range(1, k + 1):
	c = d[i]
	c[0] = n - (c[0] + 1)
	c[1] = c[1]
	c[2] = n - c[2]
	c[3] = c[3] + 1

	print(c[1], c[0], c[3], c[2])

fin.close()