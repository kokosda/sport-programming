fin  = open("input.txt")

n = int(fin.readline())
a = [list(map(int, fin.readline().split())) for i in range(n)]
fin.readline()
colors = list(map(int, fin.readline().split()))

edges = []

for i in range(n):
    for j in range(i):
        if a[i][j] == 1:
            edges.append([i, j])

bad_bridges = 0

for edge in edges:
    if colors[edge[0]] != colors[edge[1]]:
        bad_bridges += 1

print(bad_bridges)

fin.close()