class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A) is 1:
            return 0
        
        min_a = min(A)
        max_a = max(A)
        
        t = min_a + 2 * K
        
        if max_a - t > 0:
            return max_a - t
        
        return 0
    
"""
[-2,3,6]
3

B:[3,3,3]
B:[1,3,3]

[1,7,31]
10
B:[3,3,4]

[1]
0
[0,10]
2
[1,3,6]
3
[1,5,31,500]
10
"""