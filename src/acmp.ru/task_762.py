fin  = open("input.txt")
n = int(fin.readline())

count = 1
remainder = n % 3

while n > 3:
    n //= 3

    if remainder > 0:
        n += 1

    remainder = n % 3
    count += 1

print(count)

fin.close()0