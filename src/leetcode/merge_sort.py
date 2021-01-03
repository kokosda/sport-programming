from typing import List

def merge_sort(a: List[int], l: int, r: int, buff: List[int]):
    if r - l <= 1:
        return

    m = (l + r) // 2

    merge_sort(a, l, m, buff)
    merge_sort(a, m, r, buff)
    merge(a, l, m, r, buff)

def merge(a: List[int], l: int, m: int, r: int, buff: List[int]):
    print(l, m, r, buff, 'before')
    i = l

    while i <= m:
        if buff[i] > buff[m]:
            buff[i], buff[m] = buff[m], buff[i]

        i += 1

    i = r

    print(l, m, r, buff, 'mid')

    while i >= m:
        if buff[i] < buff[m]:
            buff[m], buff[i] = buff[i], buff[m]

        i -= 1

    print(l, m, r, buff, 'after')


a = [0,4,29,59,11,40,549,4,59,0,423]
result = a[:]
print(a, 'source')
merge_sort(a, 0, len(a)-1, result)
print(result, 'result')