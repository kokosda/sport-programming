class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(i) for i in grid]
        dp[0][0] = grid[0][0]
        
        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):
                if i == j == 0:
                    continue
                if i == 0:
                    if j > 0:
                        dp[i][j] = dp[i][j-1] + grid[i][j]
                        
                if i > 0:
                    if j == 0:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                        
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        for i in dp:
            print(i)
            
        return dp[-1][-1]
"""
dynamic state: number
dynamic value func: min path
dynamic initial states: dp[0][0] = [top][left]
dynamic transition funcs: 
    1) dp[i][j] = dp[i-1][j] if i > 0
    2) dp[i][j] = dp[i][j-1 if j > 0
    3) dp[i][j] = min(dp[i-1][j], dp[i][j-1])
order of calculation: 0..n, 0..m
answer to the original problem: dp[n][m]
"""