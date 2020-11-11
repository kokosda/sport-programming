def is_arrow(s, index_s, arrow):
	result = True
	i_s = index_s

	if i_s + len(arrow) - 1 > len(s):
		return False

	for i in range(len(arrow)):
		if s[i_s] == arrow[i]:
			i_s += 1
		else:
			result = False
			break
	
	return result

fin  = open("input.txt")
 
s = fin.readline().strip()
t = ''

arrow1 = '>>-->'
arrow2 = '<--<<'
arrows_count = 0

for i in range(len(s)):
	if is_arrow(s, i, arrow1) or is_arrow(s, i, arrow2):
		arrows_count += 1

print(arrows_count)

fin.close()