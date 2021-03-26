class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        
        while end - start > 1:
            m = (start + end) // 2
            
            if nums[m] > target:
                end = m
            else:
                start = m
                
        return start if nums[start] == target else -1
    
"""
-1,0,3,5,9,12
8
s = 0 -> 2 -> 3 -> 3
e = 5 -> 5 -> 5 -> 4
s = 0 -> 3 -> 3
e = 5 -> 5 -> 4

"""