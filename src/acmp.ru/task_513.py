from math import factorial
fin = open('input.txt')

n = int(fin.readline())
s = 0

for i in range(2, n + 1):
    s += factorial(n) / (factorial(n - i) * factorial(i))

print(int(s))

fin.close()