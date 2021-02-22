class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()
        
        for i, ch in enumerate(s):
            if od.get(ch) is None:
                od[ch] = i
            else:
                od[ch] = -1
                
        for k, v in od.items():
            if v != -1:
                return od[k]
        
        return -1
