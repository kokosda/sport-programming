n = int(input())
a = []

for i in range(n):
	if i == 0:
		a.append([1] * n)
		continue

	a.append([0] * n)
	a[i][0] = 1

	for j in range(n):
		a[i][j] = a[i - 1][j] + a[i][j - 1]

print(a[n - 1][n - 1])