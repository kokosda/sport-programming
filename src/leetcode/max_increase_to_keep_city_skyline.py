class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        max_rows = [0] * n
        max_cols = [0] * m
        
        for i in range(n):
            max_rows[i] = max(grid[i])
            
        for i in range(m):
            for j in range(n):
                max_cols[i] = max(max_cols[i], grid[j][i])
                
        for i in range(n):
            for j in range(m):
                res += min(max_rows[i], max_cols[j]) - grid[i][j]
        
        return res