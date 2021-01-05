class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * (len(obstacleGrid[0])) for i in range(len(obstacleGrid))]
        dp[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if (i + 1 == len(obstacleGrid)) and (j + 1 == len(obstacleGrid[i])):
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
                    continue
                if i + 1 == len(obstacleGrid) or j + 1 == len(obstacleGrid[i]):
                    continue
                if obstacleGrid[i + 1][j] == 0:
                    dp[i + 1][j] += dp[i][j]
                    
                    if i > 0:
                        dp[i + 1][j] += dp[i - 1][j]
                if obstacleGrid[i][j + 1] == 0:
                    dp[i][j + 1] += dp[i][j]
                    
                    if j > 0:
                        dp[i][j + 1] += dp[i][j - 1]
                        
        for row in dp:
            print(row)
            pass
        return dp[-1][-1]
    
"""
dynamic state: position
dynamic value function: number of unique paths to the bottom-right corner
dynamic initial states: top-left corner
dynamic transition functions: [i + 1][j] or [i][j + 1] if no obstacle
order of calculation: ?
answer to the original problem: f[m][n]
"""