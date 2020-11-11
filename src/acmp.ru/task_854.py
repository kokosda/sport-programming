fin  = open("input.txt")
fout = open("output.txt","w")
 
tr, tc = map(int, fin.readline().split())
mode = fin.readline().split()[0]
 
if mode == 'heat':
    fout.write(str(max(tr, tc)))
elif mode == 'freeze':
    fout.write(str(min(tr, tc)))
elif mode == 'auto':
    fout.write(str(tc))
else:
    fout.write(str(tr))
 
fin.close()
fout.close()