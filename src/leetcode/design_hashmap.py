class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.store = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_code = self._get_hash_code(key)
        
        if self.store[hash_code] is None:
            self.store[hash_code] = deque()
            
        dq = self.store[hash_code]
        
        if dq:
            el = self._find_in_deque(dq, key)
            
            if el:
                el[1] = value
                return

        dq.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_code = self._get_hash_code(key)
        
        if self.store[hash_code] is None:
            return -1
            
        dq = self.store[hash_code]        
        el = self._find_in_deque(dq, key)
        
        if el is None:
            return -1
        return el[1]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_code = self._get_hash_code(key)
        
        if self.store[hash_code] is None:
            return
        
        dq = self.store[hash_code]        
        el = self._find_in_deque(dq, key)
        
        if el:
            dq.remove(el)
    
    def _get_hash_code(self, key: int) -> int:
        res = 0
        for ch in str(key):
            res += ord(ch)
        res = res % self.size
        return res
        
    def _find_in_deque(self, dq: deque, key: int) -> List[int]:
        for el in dq:
            if el[0] == key:
                return el
            
        return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)