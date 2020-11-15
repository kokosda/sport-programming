n = int(input())
s, d = map(int, input().split())
min_d = s

for i in range(n - 1):
	s, d = map(int, input().split())

	while s <= min_d:
		s += d

	min_d += s - min_d

print(min_d)