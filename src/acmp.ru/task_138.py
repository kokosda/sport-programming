def floyd(m, n):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if i == j:
					m[i][j] = 0
					continue
				else:
					if m[i][k] != 30000 and m[k][j] != 30000:
						if m[i][j] == 30000:
							m[i][j] = m[i][k] + m[k][j]
						elif m[i][j] != 30000:
							m[i][j] = min(m[i][j], m[i][k] + m[k][j])
	return m
 
fin = open('input.txt')
n, m = map(int, fin.readline().split())

a = [[30000] * n for i in range(n)]

for i in range(m):
	u, v, w = map(int, fin.readline().split())
	a[u - 1][v - 1] = min(a[u - 1][v - 1], w)

a[0][0] = 0
a = floyd(a, n)
print(*a[0])

fin.close()