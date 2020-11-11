fin  = open("input.txt")
 
n = int(fin.readline())
m = [list(map(int, fin.readline().split())) for i in range(n)]

for k in range(n):
	for i in range(n):
		for j in range(n):
			if i == j:
				continue
			else:
				m[i][j] = min(m[i][j], m[i][k] + m[k][j])

for i in range(n):
	print(*m[i])

fin.close()