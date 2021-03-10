x = True
y = False
c = x and y
d = x or y

print(c, d)

x = 1
y = 0
c = x and y
d = x or y

print(c, d)

x = 20
y = 0
z = 10
c = x and y
d = x or y
e = y or x
f = y or z or x

print(c, d, e, f)