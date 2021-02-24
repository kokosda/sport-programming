class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        INF = -2 ** 31
        max1, max2, max3 = None, None, None
        
        for _, v in enumerate(nums):
            if max1 is None or v > max1:
                max3 = max2
                max2 = max1
                max1 = v
            elif v != max1 and (max2 is None or v > max2):
                max3 = max2
                max2 = v
            elif v != max1 and v != max2 and (max3 is None or v > max3):
                max3 = v
                
        if max3 is None or max3 == max2 or max3 == max1:
            return max1
        
        return max3
                
"""
[2,2,3,1]
m1=3
m2=2
m3=2

[1,2,-2**31]
[1,2,2,1,2]
"""
        