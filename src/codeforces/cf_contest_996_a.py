n = int(input().strip())
a = [1, 5, 10, 20, 100]
i = len(a) - 1
r = 0

while i >= 0 and n != 0:
	r += n // a[i]
	n = n % a[i]
	i -= 1

print(r)