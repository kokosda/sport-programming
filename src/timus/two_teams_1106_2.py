from collections import deque

# fin = open("input.txt")
n = int(input())
friends = [0]

for i in range(1, n + 1):
	friends.append([])

	for el in list(map(int, input().split())):
		if el != 0:
			friends[i].append(el)

team1 = set()
team2 = set()
i = 1
q = deque()

while i < n + 1:
	if i not in team1 and i not in team2:
		team1.add(i)

	for j in friends[i]:
		if j not in team1 and j not in team2:
			q.append(j)
			team2.add(j)
	
	while len(q) > 0:
		f = q.pop()
		team_f = team2 if f in team1 else team1

		for j in friends[f]:
			if j not in team1 and j not in team2:
				team_f.add(j)
				q.append(j)

	i += 1

# print(team1)
# print(team2)
if not team1 or not team2:
	print(0)
else:
	print(len(team1))
	print(' '.join([str(i) for i in team1]))

# fin.close()

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

4
2 0
1 4 0
4 0
2 3 0

I                 II
1				2
				4

"""