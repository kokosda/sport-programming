fin  = open("input.txt")
fout = open("output.txt","w")

coord = fin.readline()

coords = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8
}

hor, ver = int(coord[1]), int(coords[coord[0]])

if hor % 2 == 0 and ver % 2 != 0 or hor % 2 != 0 and ver % 2 == 0:
    fout.write('WHITE')
else:
    fout.write('BLACK')

fin.close()
fout.close()