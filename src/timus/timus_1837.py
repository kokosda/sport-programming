n = int(input())
d = {}
levels = {}
root = 'Isenbaev'

for i in range(n):
	a, b, c = input().split()

	if d.get(a) == None:
		d[a] = set()

	d[a].add(b)
	d[a].add(c)

	if d.get(b) == None:
		d[b] = set()

	d[b].add(a)
	d[b].add(c)
	
	if d.get(c) == None:
		d[c] = set()

	d[c].add(a)
	d[c].add(b)

if d.get(root) != None:
	levels[root] = 0

	current_dude = root
	queue = [current_dude]
	current = 0

	while current < len(queue) and current < 50:
		current_dude = queue[current]

		for i in d[current_dude]:
			if levels.get(i) != None:
				continue

			levels[i] = levels[current_dude] + 1
			queue.append(i)

		current += 1

for i in sorted(d.keys()):
	if levels.get(i) != None:
		print(i, levels[i])
	else:
		print(i, 'undefined')