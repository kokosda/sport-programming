fin  = open("input.txt")
k = int(fin.readline())
max_clients = 73 + 72

if k > max_clients:
	print('NO')
else:
	service_time = (k - 1) * 5
	formatted_time = str(service_time // 60) + ' ' + str(service_time % 60)
	print(formatted_time)

fin.close()