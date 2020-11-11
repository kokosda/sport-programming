from math import sqrt

fin  = open("input.txt")
 
x1, y1, x2, y2 = map(int, fin.readline().split())

is_1_diff = x1 % 2 != 0 and y1 % 2 == 0 or x1 % 2 == 0 and y1 % 2 != 0
is_2_diff = x2 % 2 != 0 and y2 % 2 == 0 or x2 % 2 == 0 and y2 % 2 != 0

if is_1_diff and is_2_diff or (not is_1_diff and not is_2_diff):
	print('YES')
else:
	print('NO')
 
fin.close()