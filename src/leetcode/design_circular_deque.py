class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.__size = 0
        self.__capacity = k
        self.__container = [None] * self.__capacity * 2
        self.__front_ind = self.__capacity
        self.__back_ind = self.__capacity

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        if self.__container[self.__front_ind]:
            self.__front_ind -= 1
        
        self.__container[self.__front_ind] = value
        self.__size += 1
        print(self.__container, self.__front_ind, 'fi')
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        if self.__container[self.__back_ind]:
            self.__back_ind += 1
        
        self.__container[self.__back_ind] = value
        self.__size += 1
        print(self.__container, self.__back_ind, 'bi')
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.__container[self.__front_ind] = None
        self.__size -= 1
        
        if not self.isEmpty():
            self.__front_ind += 1
        
        self.__update_indices()
        print(self.__container, self.__front_ind, 'fi')
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.__container[self.__back_ind] = None
        self.__back_ind -= 1
        self.__size -= 1
        self.__update_indices()
        print(self.__container, self.__back_ind, 'bi')
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        
        return self.__container[self.__front_ind]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        
        return self.__container[self.__back_ind]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.__size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.__size == self.__capacity
    
    def __update_indices(self):
        if self.__back_ind != self.__front_ind:
            return
        
        #self.__back_ind = self.__capacity
        #self.__front_ind = self.__capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()