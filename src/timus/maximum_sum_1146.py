fin = open('input.txt')
n = int(fin.readline())
m = [list(map(int, fin.readline().split())) for i in range(n)]

print(m)

fin.close()

"""
 0 -2 -7  0 |  0 -2 -9  0
 9  2 -6  2 |  9 11  5  7
-4  1 -4  1 | -4 -3 -7 -6
-1  8  0 -2 | -1  7  7  5

 0 -2 -7  0 |  0 -2 -9  0
 9  2 -6  2 |  9  9 -4 -2
-4  1 -4  1 |  5  6 -7 -6
-1  8  0 -2 | -1  7  7  5

ROWS:
0 -2 -7  0
0 max

9  2 -6  2
9 2 max

-4  1 -4  1
1 max

-1  8  0 -2
8 max


COLS:
0 9 -4 -1
9 max

-2 2 1 8
2, 1, 8 max

-7 -6 -4 0
0 max

0 2 1 -2
2 1 max








 m:  0 -2 -7  0 9  2 -6  2 -4  1 -4  1 -1  8  0 -2
 s1: 0 -2 -9 -9 0  2 -4 -2 -6 -5 -9 -8 -9 -1 -1 -3
 s2: 0  0  0  0 9 11  5  7  3  4  0  1  0  8  8  6
"""