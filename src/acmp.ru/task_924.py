fin  = open("input.txt")
 
n = 4
a = [fin.readline().strip() for i in range(n)]
is_beautiful = True

for i in range(n - 1):
	for j in range(n - 1):
		if a[i][j] == a[i + 1][j] and a[i][j] == a[i][j + 1] and a[i][j + 1] == a[i + 1][j + 1]:
			is_beautiful = False
			break

if is_beautiful:
	print('Yes')
else:
	print('No')
 
fin.close()