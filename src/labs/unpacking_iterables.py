a, b = 'ef'
print(a, b)

a, *b = [1, 2, 3]
print(a, b)

a, *b = [1]
print(a, b)

d = { 'key1': 1, 'key2': 2}
print(type({**d}))