n = int(input())
a = list(map(int, input().split()))

current_el, current_el_i, move = 0, 0, 0

while move < n - 1:
    if move % 2 == 0:
        for i in range(n):
            if a[i] != -1 and current_el < a[i]:
                current_el = a[i]
                current_el_i = i
    else:
        for i in range(n):
            if a[i] != -1 and current_el > a[i]:
                current_el = a[i]
                current_el_i = i

    a[current_el_i] = -1
    move += 1

for i in range(n):
    if a[i] != -1:
        print(a[i])
        break