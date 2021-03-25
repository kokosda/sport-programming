class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        MIN_GROUP_NUM = 3
        
        if len(s) < MIN_GROUP_NUM:
            return []
        
        res = []
        i = 1
        start = 0
        end = 1
        prev_ch = s[0]
        
        while i < len(s):
            if s[i] != prev_ch:
                if end - start + 1 >= MIN_GROUP_NUM:
                    res.append([start, end])
                    
                start = i
                prev_ch = s[i]
                
            end = i                
            i += 1
        else:
            if end - start + 1 >= MIN_GROUP_NUM:
                res.append([start, end])
                
        return res