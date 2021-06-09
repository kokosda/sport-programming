fin = open("input.txt")
n = int(fin.readline())
friends = []
team1 = set()
team2 = set()

for i in range(1, n + 1):
	if i not in team1 and i not in team2:
		team1.add(i)

	i_friends = list(map(int, fin.readline().split()))
	print(i_friends)
	j = 0

	while i_friends[j] != 0:
		if i_friends[j] not in team2 and i_friends[j] not in team1:
			team2.add(i_friends[j])

		j += 1

res = len(team1)
print(res)

if res > 0:
	print(' '.join([str(i) for i in team1]))

fin.close()

"""
team1: 1
team2: 2, 3

1: 2,3
2: 3,1
3: 1,2,4,5
4: 3
5: 3
6: 7
7: 6

I                 II
1,4,5,6			  2,3,7

"""