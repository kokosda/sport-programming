fin = open("input.txt")
n, m = map(int, fin.readline().split())
a = [fin.readline() for i in range(n)]
positions_count = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            if i > 0 and i < n - 1:
                if a[i + 1][j] == '.':
                    positions_count += 1
            if i == n - 1:

fin.close()