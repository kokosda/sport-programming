fin  = open("input.txt")

n = int(fin.readline())
m = [list(map(int, fin.readline().split())) for i in range(n)]
parents = []

for i in range(n):
	parents.append([])

	for j in range(n):
		parents[i].append([])
		parents[i][j] = i+1

for k in range(n):
	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			else:
				if m[i][j] > (m[i][k] + m[k][j]):
					m[i][j] = m[i][k] + m[k][j]
					parents[i][j] = parents[k][j]

for i in range(n):
	print(*parents[i])

fin.close()