fin  = open("input.txt")

n = int(fin.readline())
child1 = int(fin.readline())
child2 = int(fin.readline())

while child1 != child2:
	if child1 > child2:
		if child1 % 2 == 0:
			child1 //= 2
		else:
			child1 = (child1 - 1) // 2
	
	if child2 > child1:
		if child2 % 2 == 0:
			child2 //= 2
		else:
			child2 = (child2 - 1) // 2

print(child1)

fin.close()