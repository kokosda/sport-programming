n = int(input())
a = input().strip()
b = input().strip()

c = 0

for i in range(n):
	if a[i] == b[i]:
		continue

	a0 = int(a[i])
	b0 = int(b[i])

	c += min(abs(a0 - b0), 10 - max(a0, b0) + min(a0, b0))

print(c)