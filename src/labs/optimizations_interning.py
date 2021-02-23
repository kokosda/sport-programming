import sys
a = 10
b = 10

print(id(a), id(b))

a = 5000
b = 5000

print(id(a), id(b))

print(sys.version)

a = 'hello'
b = 'hello'

print(id(a), id(b))

a = 'hello world'
b = 'hello world'

print(id(a), id(b))
print(a is b)

def my_func(e):
    if e in [1,2,3]:
        pass

print(my_func.__code__.co_consts)

import string

print(string.ascii_letters)