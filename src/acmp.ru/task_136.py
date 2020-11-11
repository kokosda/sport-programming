def floyd(m, n):
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if i == j:
					continue
				else:
					if m[i][k] != -1 and m[k][j] != -1:
						if m[i][j] == -1:
							m[i][j] = m[i][k] + m[k][j]
						elif m[i][j] != -1:
							m[i][j] = min(m[i][j], m[i][k] + m[k][j])
	return m
 
n = int(input())
m = [list(map(int, input().split())) for i in range(n)]

m = floyd(m, n)

max_mi = 0

for i in range(n):
	max_mi = max(max_mi, m[i])

print(max_mi)