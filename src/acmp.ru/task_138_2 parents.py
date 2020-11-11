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
parents = [[i] for i in range(n)]
updated = True

print(a)

while updated:
	updated = False

	for u, d in edges.items():
		for v in d:
			if a[u] != INFINITY and a[v] > a[u] + edges[u][v]:
				a[v] = a[u] + edges[u][v]

				if len(parents[v]) > 2:
					parents[v].clear()
					parents[v].append(v)

				for i in parents[u]:
					parents[v].append(i)

				updated = True

print(*a[1:])

for i in parents:
	print(*i)

fin.close()