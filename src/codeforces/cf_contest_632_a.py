n, p = map(int, input().split())
commands = []

for i in range(n):
    commands.append(input())

commands.reverse()

apples = 1
total = p // 2

for i in range(1, n):
    if commands[i] == 'halfplus':
        apples = apples * 2 + 1
        total += (apples / 2) * p
    else:
        total += apples * p
        apples *= 2

print(int(total))