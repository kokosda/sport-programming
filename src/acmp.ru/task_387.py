fin  = open("input.txt")
n = int(fin.readline())
quantity = 0

for i in range(n):
	line = fin.readline().strip()

	for j in range(len(line)):
		if line[j] == '>':
			if line[0] == line[j + 1]:
				quantity += 1
			break

print(quantity)
fin.close()