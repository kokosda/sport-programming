class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        last_idx = n - 1
        
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                
                if v is 0:
                    continue
                    
                area = self._get_area(v)
                
                if i > 0:
                    area -= min(v, grid[i - 1][j])
                if j > 0:
                    area -= min(v, grid[i][j - 1])
                if i < last_idx:
                    area -= min(v, grid[i + 1][j])
                if j < last_idx:
                    area -= min(v, grid[i][j + 1])

                res += area
                
        return res
    
    def _get_area(self, v: int) -> int:
        res = v * 6 - (v - 1) * 2
        return res
"""
2: 2+2+2+2+1+1

[1,2]
[3,4]

S[1]=1*6=6
S[2]=2*6-2
S[3]=3*6-2-2

[[1,0],[0,2]]
[[1,1,1],[1,0,1],[1,1,1]]
[[2]]
[[1,2],[3,4]]
[[2,2,2],[2,1,2],[2,2,2]]
"""