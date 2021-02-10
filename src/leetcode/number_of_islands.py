from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def mark_vertices(grid: List[List[str]], i: int, j: int, is_origin: bool):
            if grid[i][j] == '0':
                return

            if is_origin:
                grid[i][j] = '-1'

            if i + 1 < m and grid[i + 1][j] == '1':
                grid[i + 1][j] = '*'
                mark_vertices(grid, i + 1, j, False)

            if i > 0 and grid[i - 1][j] == '1':
                grid[i - 1][j] = '*'
                mark_vertices(grid, i - 1, j, False)

            if j + 1 < n and grid[i][j + 1] == '1':
                grid[i][j + 1] = '*'
                mark_vertices(grid, i, j + 1, False)

            if j > 0 and grid[i][j - 1] == '1':
                grid[i][j - 1] = '*'
                mark_vertices(grid, i, j - 1, False)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    continue

                mark_vertices(grid, i, j, True)
        
        res = 0

        for row in grid:
            res += row.count('-1')

        return res

fin = open('input.txt')
m, n = map(int, fin.readline().split(' '))
grid = [list(fin.readline().strip().split(',')) for i in range(m)]
fin.close()

s = Solution()
res = s.numIslands(grid)
print(res)