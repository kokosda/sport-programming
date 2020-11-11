fin  = open("input.txt")
fout = open("output.txt","w")
 
x, y, z = map(int, fin.readline().split())
p = (x + y + z) / 2
r = p * (p - x) * (p - y) * (p - z)

if r > 0:
    fout.write('YES')
else:
    fout.write('NO')
 
fin.close()
fout.close()