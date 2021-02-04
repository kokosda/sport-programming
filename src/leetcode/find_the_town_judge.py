class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        if not len(trust):
            return -1
        
        d = [0] * (N + 1)
        p = [0] * (N + 1)
        max_c, judge = 0, -1
        
        for pair in trust:
            i, j = pair
            d[j] += 1
            p[i] += 1
            
            if d[j] > max_c:
                max_c = d[j]
                judge = j
        
        if judge > -1 and d[judge] == (N - 1) and p[judge] == 0:
            return judge
        
        return -1
    
    def findJudgeMatrix(self, N: int, trust: List[List[int]]) -> int:
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
d = [0,0,0,0,N-1,0]
p = [0,0,0,0,0,0]
"""