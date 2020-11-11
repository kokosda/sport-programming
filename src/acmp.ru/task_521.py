fin  = open("input.txt")
fout = open("output.txt","w")

p, k = map(int, fin.readline().split())
a = [0] * (k - p + 1)

for i in range(len(a)):
	a[i] = p + i

i = 0
updated = True
steps = 0

while updated:
	i = 0
	updated = False

	while i < len(a):
		if a[i] == 2:
			i += 1
			continue

		if a[i] % 2 == 0:
			a[i] = a[i] // 2
		else:
			a[i] = a[i] * 3 + 1

		i += 1
		updated = True
		steps += 1

fout.write(str(steps))

fin.close()
fout.close()