fin  = open("input.txt")
 
n, m = map(int, fin.readline().split())
laps_min_time, racer_min_time = 10 ** 9, ''

for i in range(n):
	name = fin.readline().rstrip()
	laps = list(map(int, fin.readline().split()))
	laps_time_current = 0

	for lap in laps:
		laps_time_current += lap

	if laps_min_time > laps_time_current:
		laps_min_time = laps_time_current
		racer_min_time = name

print(racer_min_time)

fin.close()