fin  = open("input.txt")
tutors_count = int(fin.readline())
max_start, min_end = 1, 31
is_feasible = True

for i in range(tutors_count):
	start, end = map(int, fin.readline().split())

	if start <= min_end and end >= max_start:
		max_start = max(max_start, start)
		min_end = min(min_end, end)
	else:
		is_feasible = False
		break

if is_feasible and tutors_count > 0:
	print('YES')
else:
	print('NO')

fin.close()