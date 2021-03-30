class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = n * n
        
        for i in range(n):
            res += max(grid[i])
            
        for i in range(n):
            t = 0
            
            for j in range(n):
                if t < grid[j][i]:
                    t = grid[j][i]
                    
                if grid[i][j] is 0:
                    res -= 1
            
            res += t
            
        return res
    
"""
[
      |
      v
--> [1,2],
    [3,4]
]
front: 2,4
side: 3,4
"""