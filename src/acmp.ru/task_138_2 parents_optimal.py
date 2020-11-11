fin = open('input.txt')
n, m = map(int, fin.readline().split())
n += 1
edges = {}

for i in range(n):
	edges[i] = {}

for i in range(m):
	u, v, w = map(int, fin.readline().split())
	
	if edges[u].get(v) == None:
		edges[u][v] = w
	else:
		edges[u][v] = min(edges[u][v], w)

INFINITY = 30000
a = [INFINITY] * n
a[0], a[1] = 0, 0
parents = [-1 for i in range(n)]
parents[1] = 1
updated = True

print(a)

while updated:
	updated = False

	for u, d in edges.items():
		for v in d:
			if a[u] != INFINITY and a[v] > a[u] + edges[u][v]:
				a[v] = a[u] + edges[u][v]

				parents[v] = u
				updated = True

print(*a[1:])

for i in parents:
	print(i)

fin.close()