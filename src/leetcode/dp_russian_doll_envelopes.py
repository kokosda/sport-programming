class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not len(envelopes):
            return 0
        
        INF = -1
        envelopes.sort(key = lambda x: (x[0], x[1]))
        dp = [[INF, INF] for i in range(len(envelopes) + 1)]
        count = 0
        
        for i in range(len(envelopes)):
            j = count
                    
            if envelopes[i][0] > dp[j][0] and envelopes[i][1] > dp[j][1]:
                dp[j + 1] = envelopes[i]
                count += 1
            else:
                j -= 1

                while j >= 0:
                    if envelopes[i][0] > dp[j][0] and envelopes[i][1] > dp[j][1]:                        
                        if envelopes[i][1] < dp[j + 1][1]:
                            dp[j + 1] = envelopes[i]

                        break
                    j -= 1
        print(dp)
        return count
    
"""
[
    [1, 1]
    [1, 10]
    [2, 2]
    [2, 11]
    [3, 1]
    [3, 12]
]

[[1,1]]

max num of envelops
[
    (1, 8)
    (2, 3)
    (3, 5)
    (2, 9)
    (4, 6)
]
"""