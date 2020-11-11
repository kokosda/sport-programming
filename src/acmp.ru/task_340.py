def are_equal(box1, box2):
	result = True

	for i in range(len(box1)):
		if box1[i] == box2[i]:
			continue
		result = False

	return result

def is_first_box_more_than_second(box1, box2):
	result = True	
	
	for i in range(len(box1)):
		if box1[i] >= box2[i]:
			continue
		result = False

	return result

fin  = open("input.txt")

box1 = list(map(int, fin.readline().split()))
box2 = list(map(int, fin.readline().split()))

box1.sort()
box2.sort()

if are_equal(box1, box2):
	print('Boxes are equal')
elif is_first_box_more_than_second(box1, box2):
	print('The first box is larger than the second one')
elif is_first_box_more_than_second(box2, box1):
	print('The first box is smaller than the second one')
else:
	print('Boxes are incomparable')

fin.close()