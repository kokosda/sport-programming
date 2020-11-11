fin = open('input.txt')

n, k = map(int, fin.readline().split())
m = [list(map(int, fin.readline().split())) for i in range(n)]

while k > 0:
	for i in range(n // 2):
		for j in range(1, n - 1):
			if i == j or (n - i - 1) == j:
				continue

			m[i][j], m[j][n-i-1], m[n-i-1][n-j-1], m[n-j-1][i] = m[n-j-1][i], m[i][j], m[j][n-i-1], m[n-i-1][n-j-1]

	k -= 1

for i in range(n):
	print(*m[i])

fin.close()