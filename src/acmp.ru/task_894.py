from math import pi, sqrt

fin  = open("input.txt")

s, r1 = map(float, fin.readline().split())

r2 = sqrt((pi * r1 ** 2 - s) / pi)

print(r2)

fin.close()