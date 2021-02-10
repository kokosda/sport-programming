class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        cur_price = prices[0]
        delta = max(0, prices[1] - cur_price)
        
        for i in range(1, len(prices)):
            if prices[i] < cur_price:
                cur_price = prices[i]
            else:
                delta = max(delta, prices[i] - cur_price)
        
        return delta
    
    def maxProfitBrute(self, prices: List[int]) -> int:
        max_profit = 0
        
        for i in range(len(prices)):
            i_profit = 0
            
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > 0:
                    i_profit = max(i_profit, prices[j] - prices[i])
                    
            max_profit = max(max_profit, i_profit)
            
        return max_profit
    
"""
[7,1,5,3,6,4]
1(4)
1(5)
"""