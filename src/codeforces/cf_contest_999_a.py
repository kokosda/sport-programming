n, k = map(int, input().split())
a = list(map(int, input().split()))

i, j = 0, n - 1
count = 0

while i <= j and a[i] <= k:
	i += 1
	count += 1

i -= 1

while i != j and a[j] <= k:
	j -= 1
	count += 1

print(count)