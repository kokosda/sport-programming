v = int(input())
pairs = [list(map(int, input().split())) for i in range(v)]
m = [[0] * v for i in range(v)]
k = int(input())
v1, v2 = [int(i) - 1 for i in input().split()]

for i in range(v):
	for j in range(0, i):
		m[i][j] = abs(pair[i][0] - pair[j][0]) + abs(pair[i][1] - pair[j][1])
		m[j][i] = m[i][j]

queue = [v1]
used = [False] * v
used[v1] = True

if m[v1][v2] <= k:
	print(1)
else:
	min_count = 0

	while queue:
		vx = queue.pop()
