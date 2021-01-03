from typing import List

class MaxHeap:
    def __init__(self, a: List[int]):
        self.__a = a[:]
        self.__len = len(a)
        self.__size = len(a)
        self.__build(self.__a)

    def sort(self) -> List[int]:
        a = [None] * self.__size
        
        for i in range(self.__len - 1, 0, -1):
            self.print()
            self.__swap(self.__a, 0, i)
            self.__size -= 1
            self.__heapify(self.__a, 0)

        self.print()
        return a
    
    def __build(self, a: List[int]):
        for i in range(self.__len // 2, -1, -1):
            self.__heapify(a, i)

    def __heapify(self, a: List[int], i: int):
        l = self.__left(a, i)
        r = self.__right(a, i)
        largest = i

        if l < self.__size and a[l] > a[i]:
            largest = l

        if r < self.__size and a[r] > a[largest]:
            largest = r

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
max_heap = MaxHeap(a)
res = max_heap.sort()
print(res)