class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique_nums = set(nums)
        return [i + 1 for i in range(len(nums)) if (i + 1) not in unique_nums]
    
    def findDisappearedNumbers_negating_elements(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        
        for i, v in enumerate(nums):
            val = abs(v)
            
            if nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]
                
        for i, v in enumerate(nums):
            if v > 0:
                res.append(i + 1)                
        
        return res
    
    def findDisappearedNumbers_swapping_elements(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        
        while i < len(nums):
            val = nums[i]
            val_i = val - 1
            
            if val_i == i or nums[val_i] == val:
                i += 1
            else:
                nums[i], nums[val_i] = nums[val_i], val
                
        for i, v in enumerate(nums):
            if i + 1 != v:
                res.append(i + 1)
        
        return res
    
"""
[2,3,4,5,6,7,8,1]
[4,3,2,7,8,2,3,1]
[2,2]
[2,1,3]
[3,3,1]
[1]

[2,3,4,5,6,7,8,1] - nums | nums[i] == ordered[nums[i]]
[4,3,2,7,8,2,3,1]
[1,2,3,4,0,0,7,8] - zero[nums[i]] = nums[i]

[-4,-3,-2,-7,8,2,-3,-1] = nums[nums[i] - 1] = nums[i]
написать несколько версий
как вариант подумать решение через set (в одну строчку)

start: [4,3,2,7,8,2,3,1]
1: [7,3,2,4,8,2,3,1]
2: [3,3,2,4,8,2,7,1]
3: [2,3,3,4,8,2,7,1]
4: [3,2,3,4,8,2,7,1]
5: [3,2,3,4,1,2,7,8]
6: [1,2,3,4,3,2,7,8]

0: [4,3,2,7,8,2,3,1]
1: [4,3,-2,-7,8,2,3,1]
"""