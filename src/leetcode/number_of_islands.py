from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(grid, i, j, is_one):
            if grid[i][j] == '1':
                if is_one:
                    grid[i][j] = '*'
                else:
                    is_one = True
            else:
                is_one = False
                
            if i + 1 < m:
                dfs(grid, i + 1, j, is_one)
                
            if j + 1 < n:
                dfs(grid, i, j + 1, is_one)

            if i + 1 < m and j + 1 < n:
                is_one_0 = grid[i + 1][j] == '*' or grid[i][j + 1] == '*'
                dfs(grid, i + 1, j + 1, is_one_0)
            
        dfs(grid, 0, 0, False)
        
        res = 0

        for row in grid:
            res += row.count('1')

        return res

fin = open('input.txt')
m, n = map(int, fin.readline().split(' '))
grid = [list(fin.readline().strip().split(',')) for i in range(m)]
fin.close()

s = Solution()
res = s.numIslands(grid)
print(res)