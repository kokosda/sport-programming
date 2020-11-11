fin  = open("input.txt")
size = 3
a = [''] * size

for i in range(size):
	a[i] = fin.readline().strip()

symbol = ''

for i in range(0, size):
	if a[i][0] == a[i][1] and a[i][1] == a[i][2]:
		symbol = a[i][0]
		break

if (symbol == ''):
	for j in range(0, size):
		if a[0][j] == a[1][j] and a[1][j] == a[2][j]:
			symbol = a[0][j]
			break

if (symbol == ''):
	if a[0][0] == a[1][1] and a[1][1] == a[2][2]:
		symbol = a[0][0]
	elif a[2][0] == a[1][1] and a[1][1] == a[0][2]:
		symbol = a[2][0]

if symbol == '':
	print('Draw')
elif symbol == 'X':
	print('Win')
else:
	print('Lose')


fin.close()