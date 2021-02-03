class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        if not len(trust):
            return -1
        
        m = [[0] * (N + 1) for _ in range(N + 1)]
        
        for pair in trust:
            i, j = pair
            m[i][j] = 1
            
        #for i in m:
         #   print(*i)
            
        judge = -1
        
        for i in range(1, len(m)):
            if max(m[i]) == 0:
                judge = i
                break
        
        for i in range(1, len(m)):
            if i == judge:
                continue
                
            if m[i][judge] != 1:
                judge = -1
                break
        
        return judge
    
"""

"""