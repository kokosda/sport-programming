fin  = open("input.txt")
fout = open("output.txt", "w")

a, b, c, t = map(int, fin.readline().split())
s = min(a, t) * b + (t - min(a, t)) * c

fout.write(str(s))

fin.close()
fout.close()