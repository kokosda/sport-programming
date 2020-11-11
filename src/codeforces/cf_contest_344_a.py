n = int(input())
prev_magnet, islands = input(), 1

for _ in range(n - 1):
    magnet = input()

    if prev_magnet[1] == magnet[0]:
        islands += 1

    prev_magnet = magnet

print(islands)