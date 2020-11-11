fin  = open("input.txt")
fout = open("output.txt","w")

n = int(fin.readline())

seasons = {
	12: 'Winter',
	1: 'Winter',
	2: 'Winter',
	3: 'Spring',
	4: 'Spring',
	5: 'Spring',
	6: 'Summer',
	7: 'Summer',
	8: 'Summer',
	9: 'Autumn',
	10: 'Autumn',
	11: 'Autumn'
}

value = seasons.get(n)

if value == None:
	fout.write('Error')
else:
	fout.write(value)

fin.close()
fout.close()