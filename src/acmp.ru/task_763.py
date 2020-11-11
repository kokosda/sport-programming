fin  = open("input.txt")

i, j = map(int, fin.readline().split())

if i == 1 and j == 1:
    print(0)
elif i == j:
    print(2)
else:
    print(1)

fin.close()