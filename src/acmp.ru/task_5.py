fin  = open("input.txt")
fout = open("output.txt","w")

n = int(fin.readline())
a = list(map(int, fin.readline().split()))
a_3, a_4 = [], []
grade_4 = 0

for i in range(len(a)):
	if a[i] % 2 == 0:
		grade_4 += 1
		a_4.append(str(a[i]))
	else:
		a_3.append(str(a[i]))

fout.write(' '.join(a_3) + '\n')
fout.write(' '.join(a_4) + '\n')

if grade_4 >= (n - grade_4):
	fout.write('YES')
else:
	fout.write('NO')
 
fin.close()
fout.close()