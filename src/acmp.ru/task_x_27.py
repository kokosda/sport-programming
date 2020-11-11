def get_coords(column, y1, y2):
    return 0

fin  = open("input.txt")

w, h = map(int, fin.readline().split())
n = int(fin.readline())
coords = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, fin.readline().split())
    coords.append(x1, y1, x2, y2)

for i in range(w):
    get_coords(i, coords)


fin.close()

#func(column, y1, y2):
#???? - вопрос что
#get(column, row) - достаёт результат виртуального массива.