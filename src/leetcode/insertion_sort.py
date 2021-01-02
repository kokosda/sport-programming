from typing import List

def insertion_sort(a: List[int]) -> List[int]:
    for i in range(len(a)):
        j = i

        while j > 0 and a[j] < a[j-1]:
            print(a, f'j={j}, a[j]={a[j]}, a[j-1]={a[j-1]}')
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

        i += 1

    return a

a = [0,59,4,5,2,5,32,6]
print('before', a)
result = insertion_sort([0,59,4,5,2,5,32,6])
print('after', result)