def bubble_sort(a):
	for _ in range(len(a)):
		for j in range(1, len(a)):
			if a[j - 1] > a[j]:
				a[j - 1], a[j] = a[j], a[j - 1]

fin = open('input.txt')
 
n, s = map(int, fin.readline().split())
a = list(map(int, fin.readline().split()))
 
result, s0 = 0, 0
 
bubble_sort(a)
 
for i in range(n):
    if s0 + a[i] <= s:
        result += 1
        s0 += a[i]
    else:
        break
     
print(result)
 
fin.close()