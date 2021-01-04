from typing import List

def relax(f: List[int], x: int, b: int):
    f[x] = min(f[x], b)

def calc(x: int, f: List[int]) -> int:
    if f[x] != -1:
        return f[x]
    if x == 1:
        f[x] = 0
        return f[x]

    f[x] = calc(x - 1, f)

    if x - 7 >= 1:
        relax(f, x, calc(x - 7, f))
    if x % 2 == 0:
        relax(f, x, calc(x // 2, f))
    if x % 3 == 0:
        relax(f, x, calc(x // 3, f))

    f[x] += 1
    return f[x]

n = int(input())
f = [-1] * (n + 1)
calc(n, f)

print(f)