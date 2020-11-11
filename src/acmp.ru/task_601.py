fin  = open("input.txt")
 
n, m = map(int, fin.readline().split())
a = {}
for i in range(m):
    u, v, c = map(int, fin.readline().split())

    if a.get(u) == None:
        a[u] = { c: v }
    else:
        a[u][c] = v

    if a.get(v) == None:
        a[v] = { c: u }
    else:
        a[v][c] = u

k = int(fin.readline())
path = list(map(int, fin.readline().split()))

u = 1

for color in path:
    if a[u].get(color) == None:
        u = 0
        break

    u = a[u][color]

if u == 0:
    print('INCORRECT')
else:
    print(u)
 
fin.close()