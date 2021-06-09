n, k = map(int, input().split())
res = 0
comps = 1

while comps < k and comps < n:
	comps *= 2
	res += 1

if n > comps:
	res += (n - comps) // k

	if (n - comps) % k > 0:
		res += 1

print(res)


"""
n=5, k=5
c=8
res=3

1 -> 2 -> 4 -> 5

N=8, K=3
1 -> 2 -> 4 -> 7 -> 8
N-4 / k

4:100
k=3

(100-4)/3
"""