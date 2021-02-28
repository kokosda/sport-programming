class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        coord_x, coord_y = self._get_coords(grid)
        
        if coord_x == -1 or coord_y == -1:
            return 0
        
        res = 0
        row_last, col_last = len(grid) - 1, len(grid[0]) - 1
        
        def dfs(x: int, y: int) -> int:
            if grid[x][y] == 0 or grid[x][y] == -1:
                return 0
            
            grid[x][y] = -1
            p = 4
            
            if x > 0 and grid[x - 1][y] != 0:
                p += -1 + dfs(x - 1, y)
            if y > 0 and grid[x][y - 1] != 0:
                p += -1 + dfs(x, y - 1)
            if x < row_last and grid[x + 1][y] != 0:
                p += -1 + dfs(x + 1, y)
            if y < col_last and grid[x][y + 1] != 0:
                p += -1 + dfs(x, y + 1)
                
            return p
        
        res = dfs(coord_x, coord_y)
        return res
    
    def _get_coords(self, grid: List[List[int]]) -> tuple[int, int]:
        for i, row in enumerate(grid):
            for j, mark in enumerate(row):
                if mark == 1:
                    return (i, j)
                    
        return (-1, -1)