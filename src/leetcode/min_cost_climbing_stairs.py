class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        INF = 10 ** 3
        dp = [INF] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        #if in this case is 90% faster than min.
        if dp[-2] < dp[-1]:
            return dp[-2]
        return dp[-1]
        #res = min(dp[-2], dp[-1])
        #return res
    
"""
[10,5,11,1,7,50]
dp: [INF,10,5,16,6,13,56]
"""