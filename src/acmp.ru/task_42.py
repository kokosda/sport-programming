fin  = open("input.txt")

n = int(fin.readline())

if n <= 3:
    print(n)
elif n % 3 == 0:
    print(pow(3, n // 3))
else:
    r = n % 3

    if r == 1:
        print(pow(3, (n // 3) - 1) * 4)
    else:
        print(pow(3, n // 3) * 2)

fin.close()