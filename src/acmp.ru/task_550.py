fin  = open("input.txt")
fout = open("output.txt","w")

def isLeapYear(year):
	if year % 400 == 0:
		return True
	if year % 4 == 0 and year % 100 != 0:
		return True
	return False

y = int(fin.readline())
r = '13/09/' + str(y).zfill(4)

if isLeapYear(y):
	r = '12/09/' + str(y).zfill(4)

fout.write(r)

fin.close()
fout.close()