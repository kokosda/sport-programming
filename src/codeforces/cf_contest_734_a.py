n = int(input())
a = input()

anton_wins, danik_wins = 0, 0

for i in range(n):
    if a[i] == 'A':
        anton_wins += 1
    else:
        danik_wins += 1

if anton_wins == danik_wins:
    print('Friendship')
elif anton_wins > danik_wins:
    print('Anton')
else:
    print('Danik')