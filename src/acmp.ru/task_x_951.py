fin  = open("input.txt")

n, m = map(int, fin.readline().split())
s = list(map(int, fin.readline().split()))
k = s[0]
field = [False] * n
 
for i in range(n):
    field[i] = [False] * m
    for j in range(m):
        field[i][j] = False

i = 1
o = [[]] * 2
 
while i < 2 * k:
    y, x = s[i], s[i + 1]
    field[y - 1][x - 1] = True
    o[0].append(str(y - 1) + '_' + str(x - 1))
    i += 2
     
is_infected = True
quants = 0

while is_infected:
    is_infected = False
    o[1] = []

    for ij_s in o[0]:
        i, j = map(int, ij_s.split('_'))

        if i > 0 and field[i - 1][j] == 0:
            field[i - 1][j] = True
            o[1].append(str(i - 1) + '_'  + str(j))
            is_infected = True

        if i < n - 1 and field[i + 1][j] == 0:
            field[i + 1][j] = True
            o[1].append(str(i + 1) + '_' + str(j))
            is_infected = True

        if j > 0 and field[i][j - 1] == 0:
            field[i][j - 1] = True
            o[1].append(str(i) + '_' + str(j - 1))
            is_infected = True

        if j < m - 1 and field[i][j + 1] == 0:
            field[i][j + 1] = True
            o[1].append(str(i) + '_' + str(j + 1))
            is_infected = True

    o[0] = o[1]
     
    if is_infected:
        quants += 1

print(quants)

fin.close()
#поиск в ширину(!)
#bytearray -- развлечение (можно байты отдельно изменять)