class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [0] * len(s)
        c_idx = deque()
        
        for i in range(len(s)):
            if s[i] == c:
                c_idx.append(i)
                
        cur_i = c_idx.popleft()
        prev_i = cur_i
        
        for i in range(len(s)):
            if cur_i < i:
                prev_i = cur_i
                
                if len(c_idx) > 0:
                    cur_i = c_idx.popleft()
                
            res[i] = min(abs(i - cur_i), abs(i - prev_i))
                    
        return res