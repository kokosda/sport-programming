fin = open('input.txt')

h1, m1 = map(int, fin.readline().split())
h2, m2 = map(int, fin.readline().split())
 
r = 0
 
if h1 < h2:
    for i in range(h1, h2 + 1):
        r += i



    r = h2 - h1
    r += ((h1 + 1 + h2) / 2) * (h2 - h1) #5 6 7 8 9 10
elif h1 > h2:
    r = 24 - h1 + h2
    r1, r2, r3 = 0, 0, 0

    if h1 < 12:
        r1 = ((h1 + 1 + 12) / 2) * (12 - h1)

    r2 = ((1 + 12) / 2) * 12
    r3 = ((1 + h2) / 2) * h2
    r += r1 + r2 + r3
     
     
if m1 > 30:
    r -= 1
if m2 > 30:
    r -= 1
     
print(int(r))

fin.close()

#скил с формулой
#пишем, что просят, как проходит по времени