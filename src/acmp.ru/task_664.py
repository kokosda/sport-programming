fin = open('input.txt')

k, m, n = map(int, fin.readline().split())

r = n // k

if n % k > 0:
	r += 1

r = r * 2 * m

if n > k and n % k > 0 and n % k <= k // 2:
	r -= m

print(r)

fin.close()