fin  = open("input.txt")
fout = open("output.txt","w")

s = fin.readline().rstrip()
a = '123'

for i in range(len(s)):
	if s[i] == 'A':
		a = a[1] + a[0] + a[2]
	elif s[i] == 'B':
		a = a[0] + a[2] + a[1]
	else:
		a = a[2] + a[1] + a[0]

fout.write(str(a.find('1') + 1))

fin.close()
fout.close()