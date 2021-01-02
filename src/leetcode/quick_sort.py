from typing import List
from random import randrange

def partition(a: List[int], l: int, r: int, xi: int, ij: List[int]):
    i, j = l, r
    
    while i <= j:
        while a[i] < a[xi]:
            i += 1
        while a[j] > a[xi]:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            print(a, f'part. l={l}, r={r}, x={xi}, i={i}, j={j}')
            i += 1
            j -= 1

    ij[0], ij[1] = i, j

def quick_sort(a: List[int], l: int, r: int):
    if l >= r:
        return

    i, j = 0, 0
    ij = [i, j]
    xi = randrange(l, r)
    print(xi, 'rand')
    partition(a, l, r, xi, ij)

    i, j = ij
    quick_sort(a, l, j)
    quick_sort(a, i, r)

a = [0,4,29,59,11,40,549,4,59,0,423]
print(a, 'source')
quick_sort(a, 0, len(a)-1)
print(a, 'result')