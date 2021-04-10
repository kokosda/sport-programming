class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        perm = [0] * (n + 1)
        dq = deque(range(0, n + 1))
        i = 0
        
        while i < n:
            if S[i] is 'D':
                perm[i] = dq.pop()
            else:
                perm[i] = dq.popleft()
                
            i += 1
            
        perm[-1] = dq.pop()
            
        return perm