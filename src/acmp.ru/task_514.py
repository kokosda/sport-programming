	fin = open("input.txt")
	k = int(fin.readline())
	sum = k
	i = 0

	while sum > i:
		i += 1
		sum -= i

	print(i)

	fin.close()