class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.store = [None for i in range(self.size)]

    def add(self, key: int) -> None:
        h = self._get_hash(key)
        
        if self.store[h] is None:
            self.store[h] = deque()
            
        if self.contains(key):
            return
        
        self.store[h].append(key)

    def remove(self, key: int) -> None:
        h = self._get_hash(key)
        q = self.store[h]
        
        if q is None:
            return
        
        if not self._has_key(key, q):
            return
        
        #print(self.store, q, 'remove')
        
        i = q.index(key)
        q.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        h = self._get_hash(key)
        q = self.store[h]
        
        #print(self.store, q, 'contains')
        
        if q is None:
            return False

        return self._has_key(key, q)
        
    def _get_hash(self, key: int) -> int:
        res = 0
        
        for ch in str(key):
            res += ord(ch)
            
        return res % self.size
    
    def _has_key(self, key: int, q: deque) -> bool:        
        for v in q:
            if v == key:
                return True

        return False
    
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)