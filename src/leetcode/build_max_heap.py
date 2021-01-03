from typing import List

class MaxHeap:
    def __init__(self, a: List[int]):
        self.__a = a[:]
        self.__size = len(a)
        self.__build(self.__a)
    
    def __build(self, a: List[int]):
        for i in range(self.__size // 2, -1, -1):
            self.__heapify(a, i)

    def __heapify(self, a: List[int], i: int) -> List[int]:
        l = self.__left(a, i)
        r = self.__right(a, i)
        largest = -1

        if l < self.__size and a[l] > a[i]:
            largest = l
        else:
            largest = i

        if r < self.__size and a[r] > a[largest]:
            largest = r

        print(a, i, l, r)

        if largest != i:
            self.__swap(a, i, largest)
            self.__heapify(a, largest)

    def __parent(self, a, i):
        return i // 2

    def __left(self, a, i):
        return 2 * i

    def __right(self, a, i):
        return 2 * i + 1

    def __swap(self, a: List[int], i: int, j: int):
        a[i], a[j] = a[j], a[i]

    def print(self):
        print(self.__a)


a = [3,1,6,5,2,4]
maxHeap = MaxHeap(a)
maxHeap.print()