class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * (len(obstacleGrid[0])) for i in range(len(obstacleGrid))]
        dp[0][0] = 1

        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][j] == 1:
                break
                
            dp[0][j] = 1
                
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
                
            for j in range(1, len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    continue
                    
                dp[i][j] = dp[i-1][j] + dp[i][j - 1]
                
        return dp[-1][-1]
    
"""
dynamic state: position
dynamic value function: number of unique paths to the bottom-right corner
dynamic initial states: top-left corner
dynamic transition functions: [i + 1][j] or [i][j + 1] if no obstacle
order of calculation: ?
answer to the original problem: f[m][n]
"""