class Solution:
    def divisorGame(self, N: int) -> bool:
        if N < 2:
            return False
        
        dp = [False] + [False] * N
        dp[2] = True
        
        for i in range(3, N + 1):
            dp[i] = not dp[i - 1]
            
        return dp[-1]

    def divisorGameEasy(self, N: int) -> bool:
        if N % 2 == 0:
            return True
        else:
            return False
    
"""
1. 0 < x < N and N % x == 0
2. N: N - x
dp: [0..N]
dp[0]: 
"""