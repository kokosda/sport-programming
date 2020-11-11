fin  = open("input.txt")
fout = open("output.txt","w")

x, y, z = map(int, fin.readline().split())

if z <= (x + y):
    fout.write(str(x + y - z))
else:
    fout.write('Impossible')

fin.close()
fout.close()