fin  = open("input.txt")
n, m, k = map(int, fin.readline().split())
x = m
moves = 0

while True:
    x -= n
    moves += 1

    if x <= 0:
        break

    x += k

    if x > 0 and k >= n:
        moves = -1
        break

if moves == -1:
    print('NO')
else:
    print(moves)

fin.close()