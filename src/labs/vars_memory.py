import sys
import ctypes

v = 10
print(id(v))
print(hex(id(v)))

sur = [2,1]
print(sys.getrefcount(sur))
print(sys.getrefcount(v))

print(ctypes.c_long.from_address(id(sur)).value)
print(ctypes.c_long.from_address(id(v)).value)