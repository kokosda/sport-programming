import queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.size = 0
        self.top_el = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.size += 1
        self.top_el = x        
        self.push_in_queues(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.size:
            res = self.q1.get()
            self.size -= 1

            if self.size:
                el = self.q1.get()
                self.push_in_queues(el)
                self.top_el = el
            else:
                self.top_el = None
            return res
        
        return None

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_el

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0
        
    def push_in_queues(self, x: int):
        while not self.q1.empty():
            el = self.q1.get()
            self.q2.put(el)
            
        self.q1.put(x)
            
        while not self.q2.empty():
            el = self.q2.get()
            self.q1.put(el)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
[2,1,6,3,7,3]
2
q1: [2]
q2: []

1
q1: [1,2]
q2: []

6
q1: [6,2,1]
q2: []
"""
