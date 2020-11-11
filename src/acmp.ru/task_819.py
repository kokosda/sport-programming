fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c = map(int, fin.readline().split())

s = a * b * 2 + a * c * 2 + b * c * 2
v = a * b * c

fout.write(str(s) + ' ' + str(v))

fin.close()
fout.close()