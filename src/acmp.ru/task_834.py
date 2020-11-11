from math import sqrt, degrees, pi, asin

fin  = open("input.txt")
fout = open("output.txt","w")

xk, yk = map(float, fin.readline().split())
xc, yc, rc = map(float, fin.readline().split())

s_both_triangles, s = 0, 0
c = sqrt(abs(xc - xk) ** 2 + abs(yk - yc) ** 2)

if c > rc:
	a = sqrt(c ** 2 - rc ** 2)
	s_both_triangles = a * rc
	alpha = degrees(asin(a / c))
	s_sect = ((360 - 2 * alpha) / 360) * pi * (rc ** 2)
	s = s_both_triangles + s_sect
else:
	s = pi * (rc ** 2)

fout.write(str(s))

fin.close()
fout.close()