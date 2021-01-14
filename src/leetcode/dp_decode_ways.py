class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0':
            return 0
        if len(s) == 1:
            return 1
            
        dp = [0] * (len(s) + 1)
        
        for i in range(len(s) - 1, 0, -1):
            pair_i = s[i - 1]
            pair_j = s[i]
            
            if pair_i == '0':
                dp[i] = dp[i + 1]
            if pair_i > '0' and pair_i <= '2':
                if pair_j == '0':
                    dp[i] = 1 + dp[i + 1]
                else:
                    dp[i] = 3 + dp[i + 1]
            else:
                dp[i] = 2 + dp[i + 1]
                
        print(dp)
        return dp[0]
    
"""
dynamic state: letter A-Z
dynamic value: number of ways
initial state: dp[n]
transition:
    1) 0 - only 10, 20; impossible if self only
    2) pair [i,j] - if i > 2 then only 1 option: 2 letters
    3) pair [i,j] - if i > 0 and i <= 2 then 2 options possible: A/B [1/2] and [0-9] or [10-26]
order funcs: 0..n
answer: dp[0]

A-1
...
L-12
...
Z-26
12

"1720101" - 17, 20, 10, 1
"1720101" - 1, 7, 20, 10, 1
"""