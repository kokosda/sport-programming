class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0        
        
        buy_i = 0 if prices[1] > prices[0] else -1
        sum_res = 0
        i = 1
        
        while (i + 1) < len(prices):
            if buy_i == -1:
                if  prices[i - 1] >= prices[i] and prices[i + 1] > prices[i]:
                    buy_i = i            
            else:
                if prices[i] > prices[buy_i] and prices[i + 1] < prices[i]:
                    sum_res += prices[i] - prices[buy_i]
                    buy_i = -1
                
            i += 1
            
        if buy_i != -1 and prices[-1] > prices[buy_i]:
            sum_res += prices[-1] - prices[buy_i]
            
        return sum_res
    
"""
[7,1,5,3,6,4]
prev: 1-6
now: 1-5, 3-6

dp[1,5]

[7,1,5,6,4,14]
dp[1(5),7(7)]

prices: [7,1,5,6,4,14]
buy_i = -1
sum_res = 0
i = 1

i: 1
    7 > 1 and 5 > 1 -> buy_i: 1
i: 2
    5 > 1 and 6 > 5 -> continue
i: 3
    6 > 1 and 4 < 6 ->
        sum_res: 5
        buy_i: -1
i: 4
    6 > 4 and 14 > 4
        buy_i: 4
i: 5

[2,2,5]
[2]
[2,0]
[0,5]
[7,6,4,3,1]
[1,2,3,4,5]
[7,1,5,6,4,14]
[7,1,5,3,6,4]
"""